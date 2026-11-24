#!/usr/bin/env python3
"""evidence_check_core.py — deterministic core of the /evidence-check skill.

Captures the skill's marker-audit contract as CODE (the regression net that did not
exist), per docs/DECISION-canonical-ownership.md action #4 and the migration boundary
in docs/evidence-check-feature-map.md:

  KEEP  (this file decides):  <!-- evidence: EV-### --> marker bookkeeping with
        file/line locations, typo suggestions for unknown IDs, pending-review
        warnings, restricted-citation surfacing (adjudication stays with the LLM
        layer), unused-approved-evidence surfacing, marker-denominated coverage.
  MIGRATE (delegated to warrant_ledger, never re-implemented here): claim-sentence
        extraction, citation admissibility + content-overlap floor, semantic
        candidates, gate, WBOM.

The warrant engine is an optional sibling repo. If it cannot be imported, this
script degrades gracefully to marker-audit only and says so in the output.

Usage:
  python scripts/evidence_check_core.py <draft.md> [<draft2.md> ...] <ledger.json>
  python scripts/evidence_check_core.py ... --json          # machine-readable output
  python scripts/evidence_check_core.py ... --no-warrant    # skip the engine call
  python scripts/evidence_check_core.py ... --warrant-src <path-to-warrant-ledger/src>
  python scripts/evidence_check_core.py --selftest          # deterministic, offline

Warrant location knob (first match wins):
  --warrant-src flag > FPA_WARRANT_SRC env var > default sibling path.

Exit: 0 = report produced (or selftest passed); findings do NOT set the exit code
(this is a reporter, not a gate — FPA's export gates live in the pre-submit scripts).
2 = bad invocation / unreadable input. 1 = selftest failure.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

# Windows consoles default to cp1252, which can't print the check glyphs.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

SCHEMA_VERSION = "evidence-check-core.v1"

DEFAULT_WARRANT_SRC = r"C:\Users\wbal9\CODEX projects\edgerunner-warrant\warrant-ledger\src"

MARKER_RE = re.compile(r"<!--\s*evidence:\s*([^>]*?)\s*-->", re.IGNORECASE)
EV_ID_RE = re.compile(r"EV-\d{3,}", re.IGNORECASE)
# Callout sidebar (tools/md_to_docx.py): `:::callout TITLE` ... `:::` with an optional
# `evidence: EV-###` key line before the body. The box IS a proof point, so its key
# line is audited exactly like an inline marker (2026-09-04).
CALLOUT_OPEN_RE = re.compile(r"^\s*:::\s*callout\b\s*(.*)$")
CALLOUT_CLOSE_RE = re.compile(r"^\s*:::\s*$")
CALLOUT_EVIDENCE_RE = re.compile(r"^\s*evidence\s*:\s*(.+?)\s*$", re.IGNORECASE)
UNSUPPORTED_TOKEN = "CLAIM-UNSUPPORTED"

KNOWN_STATUSES = ("approved", "retired", "restricted", "pending_review")
CANONICAL_CONFIDENCE = ("low", "medium", "high")


# ────────────────────────────────────────────────────────────────
# Ledger index (FPA schema, read-only)
# ────────────────────────────────────────────────────────────────

def build_ledger_index(payload: dict) -> dict:
    """Index the FPA-schema ledger by approval_status. Never mutates the payload."""
    index = {
        "entries": {},
        "approved": set(),
        "retired": set(),
        "restricted": set(),
        "pending_review": set(),
        "other": set(),
    }
    for item in payload.get("items", []):
        if not isinstance(item, dict):
            continue
        entry_id = str(item.get("id", "")).strip().upper()
        if not entry_id:
            continue
        index["entries"][entry_id] = item
        status = str(item.get("approval_status", "")).strip().lower()
        bucket = status if status in KNOWN_STATUSES else "other"
        index[bucket].add(entry_id)
    return index


def ledger_counts(index: dict) -> dict:
    return {
        "approved": len(index["approved"]),
        "retired": len(index["retired"]),
        "restricted": len(index["restricted"]),
        "pending_review": len(index["pending_review"]),
        "other": len(index["other"]),
        "total": len(index["entries"]),
    }


# ────────────────────────────────────────────────────────────────
# Marker parsing
# ────────────────────────────────────────────────────────────────

def parse_markers(text: str, filename: str) -> list[dict]:
    """Extract every <!-- evidence: ... --> marker with file/line/sentence context,
    plus the `evidence:` key line of every :::callout block (context = the box title)."""
    markers = []
    callout_title = None          # not None while inside a :::callout block
    callout_keys_open = False     # key lines are only recognised before the first body line
    for lineno, line in enumerate(text.splitlines(), start=1):
        om = CALLOUT_OPEN_RE.match(line)
        if om:
            callout_title, callout_keys_open = om.group(1).strip(), True
            continue
        if callout_title is not None:
            if CALLOUT_CLOSE_RE.match(line):
                callout_title, callout_keys_open = None, False
                continue
            if callout_keys_open:
                em = CALLOUT_EVIDENCE_RE.match(line)
                if em:
                    body = em.group(1)
                    markers.append({
                        "file": filename,
                        "line": lineno,
                        "ids": [m.group(0).upper() for m in EV_ID_RE.finditer(body)],
                        "unsupported_marker": UNSUPPORTED_TOKEN in body.upper(),
                        "sentence": f"callout: {callout_title}",
                    })
                    continue
                if line.strip() and not re.match(r"^\s*align\s*:", line, re.IGNORECASE):
                    callout_keys_open = False
        for match in MARKER_RE.finditer(line):
            body = match.group(1)
            ids = [m.group(0).upper() for m in EV_ID_RE.finditer(body)]
            unsupported = UNSUPPORTED_TOKEN in body.upper()
            prefix = line[: match.start()].strip()
            # Last sentence fragment before the marker, for human context.
            sentence = re.split(r"(?<=[.!?])\s+", prefix)[-1].strip() if prefix else ""
            markers.append({
                "file": filename,
                "line": lineno,
                "ids": ids,
                "unsupported_marker": unsupported,
                "sentence": sentence,
            })
    return markers


# ────────────────────────────────────────────────────────────────
# Typo suggestion (Levenshtein over known ledger IDs)
# ────────────────────────────────────────────────────────────────

def _levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        cur = [i]
        for j, cb in enumerate(b, start=1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def suggest_id(unknown_id: str, index: dict, max_distance: int = 2) -> str:
    """Nearest known ledger ID within max_distance edits; approved IDs win ties.
    Returns "" when nothing is close enough or the minimum is ambiguous."""
    best: list[tuple[int, int, str]] = []  # (distance, approved_rank, id)
    for known in index["entries"]:
        d = _levenshtein(unknown_id, known)
        if d <= max_distance:
            best.append((d, 0 if known in index["approved"] else 1, known))
    if not best:
        return ""
    best.sort()
    if len(best) > 1 and best[0][:2] == best[1][:2]:
        return ""  # ambiguous — don't guess
    return best[0][2]


# ────────────────────────────────────────────────────────────────
# Marker audit (the FPA skill's Step 2–5 contract, deterministically)
# ────────────────────────────────────────────────────────────────

def audit_markers(markers: list[dict], index: dict) -> dict:
    findings = {
        "unsupported_claims": [],
        "unknown_ids": [],
        "retired_ids": [],
        "restricted_ids": [],
        "pending_ids": [],
        "unused_approved": [],
    }
    cited: set[str] = set()
    supported = 0
    unsupported = 0

    for marker in markers:
        ids = marker["ids"]
        cited.update(ids)
        problem_only = bool(ids)  # true until we see an approved/pending id
        for entry_id in ids:
            entry = index["entries"].get(entry_id)
            if entry_id in index["approved"]:
                problem_only = False
            elif entry_id in index["pending_review"] or entry_id in index["other"]:
                problem_only = False
                findings["pending_ids"].append({
                    "file": marker["file"], "line": marker["line"], "id": entry_id,
                    "summary": (entry or {}).get("summary", ""),
                })
            elif entry_id in index["retired"]:
                findings["retired_ids"].append({
                    "file": marker["file"], "line": marker["line"], "id": entry_id,
                    "summary": (entry or {}).get("summary", ""),
                })
            elif entry_id in index["restricted"]:
                problem_only = False  # restricted is a surfacing, not an unsupported bucket
                findings["restricted_ids"].append({
                    "file": marker["file"], "line": marker["line"], "id": entry_id,
                    "restrictions": (entry or {}).get("restrictions", ""),
                    "summary": (entry or {}).get("summary", ""),
                })
            else:
                findings["unknown_ids"].append({
                    "file": marker["file"], "line": marker["line"], "id": entry_id,
                    "suggestion": suggest_id(entry_id, index),
                })

        if marker["unsupported_marker"]:
            unsupported += 1
            findings["unsupported_claims"].append({
                "file": marker["file"], "line": marker["line"],
                "sentence": marker["sentence"],
            })
        elif any(i in index["approved"] for i in ids):
            supported += 1
        elif ids and problem_only:
            # every cited id was retired or unknown — the skill's "unsupported" rule
            unsupported += 1

    findings["unused_approved"] = sorted(index["approved"] - cited)
    total = len(markers)
    coverage = round(supported / total * 100, 1) if total else 0.0
    return {
        "markers": {
            "total": total,
            "supported": supported,
            "unsupported": unsupported,
            "coverage_pct": coverage,
        },
        "findings": findings,
    }


# ────────────────────────────────────────────────────────────────
# Warrant integration (MIGRATE/BOTH features — delegated, never re-implemented)
# ────────────────────────────────────────────────────────────────

def adapt_ledger_for_warrant(payload: dict) -> tuple[dict, list[str]]:
    """FPA schema → canonical warrant shape, IN MEMORY only (the real ledger file
    is never modified). Per DECISION action #2: source_file/source_anchor →
    evidence_refs; proof_strength 'highest' clamped to 'high'; out-of-range
    values warned, not silently accepted."""
    warnings: list[str] = []
    items = []
    for item in payload.get("items", []):
        if not isinstance(item, dict):
            continue
        adapted = dict(item)
        entry_id = str(item.get("id", "")).strip().upper()
        strength = str(item.get("proof_strength", "")).strip().lower()
        if strength == "highest":
            adapted["proof_strength"] = "high"
            warnings.append(f"{entry_id}: proof_strength 'highest' clamped to 'high'")
        elif strength and strength not in CANONICAL_CONFIDENCE:
            warnings.append(f"{entry_id}: proof_strength '{strength}' outside low/medium/high")
        if not adapted.get("evidence_refs"):
            src = str(item.get("source_file", "")).strip()
            anchor = str(item.get("source_anchor", "")).strip()
            if src:
                adapted["evidence_refs"] = [f"{src}#{anchor}" if anchor else src]
        items.append(adapted)
    return {"items": items}, warnings


def inline_markers(text: str) -> str:
    """Rewrite FPA's HTML-comment markers into inline citations warrant can see.
    Warrant's sentence splitter would otherwise orphan a trailing
    '... scale. <!-- evidence: EV-101 -->' into a separate fragment, detaching
    the citation from its sentence."""
    # Trailing marker: move the ids inside the sentence, before the punctuation.
    text = re.sub(
        r"([.!?;])\s*<!--\s*evidence:\s*([^>]*?)\s*-->",
        r" (\2)\1",
        text,
        flags=re.IGNORECASE,
    )
    # Mid-sentence markers: just de-comment them.
    return MARKER_RE.sub(r"(\1)", text)


def resolve_warrant_src(cli_value: str | None) -> str:
    return cli_value or os.environ.get("FPA_WARRANT_SRC") or DEFAULT_WARRANT_SRC


def run_warrant(draft_texts: list[str], ledger_payload: dict, warrant_src: str) -> dict:
    """Call the canonical engine. Returns a dict that always has 'available'."""
    src = Path(warrant_src)
    if not (src / "warrant_ledger" / "__init__.py").is_file():
        return {
            "available": False,
            "reason": f"warrant engine not found at {src} — falling back to marker-audit only",
        }
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))
    try:
        from warrant_ledger import Ledger, Policy, gate, to_wbom, verify  # noqa: PLC0415
        import warrant_ledger  # noqa: PLC0415
    except Exception as exc:  # pragma: no cover — import failure is environment-specific
        return {
            "available": False,
            "reason": f"warrant engine import failed ({exc}) — falling back to marker-audit only",
        }

    canonical, adapter_warnings = adapt_ledger_for_warrant(ledger_payload)
    ledger = Ledger.from_payload(canonical)
    answer = "\n\n".join(inline_markers(t) for t in draft_texts)
    verdict = verify(answer, ledger)  # citation-only: deterministic, no embedder
    decision = gate(verdict, Policy())
    wbom = to_wbom(verdict, decision)
    return {
        "available": True,
        "engine_version": getattr(warrant_ledger, "__version__", "unknown"),
        "engine_src": str(src),
        "adapter_warnings": adapter_warnings,
        "verdicts": [
            {
                "text": c.text,
                "status": c.status,
                "method": c.method,
                "entry_id": c.entry_id,
                "match_score": c.match_score,
                "cited_ids": list(c.cited_ids),
            }
            for c in verdict.claims
        ],
        "summary": {
            "claims_total": verdict.total,
            "supported_cited": verdict.supported,
            "candidates_unconfirmed": verdict.candidates,
            "unverified": verdict.unverified,
            "issues": verdict.issues,
            "grounding_rate": round(verdict.grounding_rate, 4),
        },
        "gate": {"decision": decision.decision, "reasons": list(decision.reasons)},
        "wbom": wbom,
    }


# ────────────────────────────────────────────────────────────────
# Pipeline
# ────────────────────────────────────────────────────────────────

def run_check(draft_paths: list[Path], ledger_path: Path,
              warrant_src: str, use_warrant: bool = True) -> dict:
    payload = json.loads(ledger_path.read_text(encoding="utf-8"))
    index = build_ledger_index(payload)

    markers: list[dict] = []
    texts: list[str] = []
    for p in draft_paths:
        text = p.read_text(encoding="utf-8")
        texts.append(text)
        markers.extend(parse_markers(text, p.name))

    audit = audit_markers(markers, index)
    if use_warrant:
        warrant = run_warrant(texts, payload, warrant_src)
    else:
        warrant = {"available": False, "reason": "warrant call disabled (--no-warrant)"}

    return {
        "schema_version": SCHEMA_VERSION,
        "ledger": {"path": str(ledger_path), "counts": ledger_counts(index)},
        "drafts": [str(p) for p in draft_paths],
        "markers": audit["markers"],
        "findings": audit["findings"],
        "warrant": warrant,
    }


def render_human(result: dict) -> str:
    m = result["markers"]
    f = result["findings"]
    lines = [
        "Evidence check (deterministic core)",
        f"  Ledger: {result['ledger']['path']} {result['ledger']['counts']}",
        f"  Markers: {m['total']} total | {m['supported']} supported | "
        f"{m['unsupported']} unsupported | coverage {m['coverage_pct']}%",
    ]
    for key, label in (
        ("unsupported_claims", "CLAIM-UNSUPPORTED"),
        ("unknown_ids", "Unknown/typo IDs"),
        ("retired_ids", "Retired IDs cited"),
        ("restricted_ids", "Restricted IDs cited (adjudicate vs proposal type)"),
        ("pending_ids", "Pending-review IDs cited"),
    ):
        if f[key]:
            lines.append(f"  {label}:")
            for row in f[key]:
                loc = f"{row.get('file')}:{row.get('line')}"
                extra = row.get("suggestion") or row.get("sentence") or row.get("id", "")
                hint = f" (suggest {row['suggestion']}?)" if row.get("suggestion") else ""
                lines.append(f"    - {loc} {row.get('id', extra)}{hint}")
    if f["unused_approved"]:
        lines.append(f"  Unused approved evidence: {', '.join(f['unused_approved'])}")
    w = result["warrant"]
    if w.get("available"):
        lines.append(
            f"  Warrant engine v{w['engine_version']}: gate={w['gate']['decision']} "
            f"({'; '.join(w['gate']['reasons']) or 'clean'}) | "
            f"claims={w['summary']['claims_total']} supported={w['summary']['supported_cited']} "
            f"candidates={w['summary']['candidates_unconfirmed']} issues={w['summary']['issues']} | "
            f"grounding_rate={w['summary']['grounding_rate']}"
        )
        for warning in w.get("adapter_warnings", []):
            lines.append(f"    adapter: {warning}")
    else:
        lines.append(f"  Warrant: UNAVAILABLE — {w.get('reason', 'unknown')}")
    return "\n".join(lines)


# ────────────────────────────────────────────────────────────────
# Selftest — deterministic, offline, no fixtures needed
# ────────────────────────────────────────────────────────────────

def selftest() -> int:
    failures: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            failures.append(name)

    ledger = {"items": [
        {"id": "EV-001", "approval_status": "approved", "proof_strength": "highest",
         "summary": "alpha capability validated", "source_file": "a.md", "source_anchor": "§A"},
        {"id": "EV-002", "approval_status": "retired", "summary": "old thing"},
        {"id": "EV-003", "approval_status": "restricted", "restrictions": "gov only",
         "summary": "quiet thing"},
        {"id": "EV-004", "approval_status": "pending_review", "summary": "new thing"},
        {"id": "EV-005", "approval_status": "approved", "proof_strength": "colossal",
         "summary": "unused approved thing"},
    ]}
    index = build_ledger_index(ledger)
    check("counts", ledger_counts(index) == {
        "approved": 2, "retired": 1, "restricted": 1, "pending_review": 1,
        "other": 0, "total": 5})

    draft = (
        "# Heading\n\n"
        "Alpha capability validated in the field. <!-- evidence: EV-001 -->\n"
        "Something bold and new. <!-- evidence: EV-101 -->\n"
        "We rest on the old thing. <!-- evidence: EV-002 -->\n"
        "The quiet thing helps. <!-- evidence: EV-003 -->\n"
        "Fastest in the world. <!-- evidence: CLAIM-UNSUPPORTED -->\n"
        "New thing incoming. <!-- evidence: EV-004 -->\n"
        "Mixed cite survives on the approved leg. <!-- evidence: EV-001, EV-002 -->\n"
        ":::callout Proof at Site X\n"
        "evidence: EV-001\n"
        "Body of the box; evidence: EV-999 here is prose, not a key line.\n"
        ":::\n"
    )
    markers = parse_markers(draft, "t.md")
    # 7 inline markers + the callout's key line (line 11); "evidence: EV-999" in the
    # callout body is prose and must not parse.
    check("marker count", len(markers) == 8)
    check("marker line numbers", [m["line"] for m in markers] == [3, 4, 5, 6, 7, 8, 9, 11])
    check("multi-id parse", markers[6]["ids"] == ["EV-001", "EV-002"])
    check("callout key line parsed", markers[7]["ids"] == ["EV-001"])
    check("callout body prose ignored", all("EV-999" not in mk["ids"] for mk in markers))
    check("sentence context", markers[4]["sentence"] == "Fastest in the world.")

    audit = audit_markers(markers, index)
    m = audit["markers"]
    f = audit["findings"]
    check("supported", m["supported"] == 3)          # EV-001 solo + mixed marker + callout key line
    check("unsupported", m["unsupported"] == 3)      # CLAIM-UNSUPPORTED + unknown-only + retired-only
    check("coverage", m["coverage_pct"] == round(3 / 8 * 100, 1))
    check("unknown flagged", [r["id"] for r in f["unknown_ids"]] == ["EV-101"])
    check("typo suggestion", f["unknown_ids"][0]["suggestion"] == "EV-001")
    check("retired flagged", sorted(r["line"] for r in f["retired_ids"]) == [5, 9])
    check("restricted surfaced w/ text",
          f["restricted_ids"][0]["restrictions"] == "gov only")
    check("pending warned", [r["id"] for r in f["pending_ids"]] == ["EV-004"])
    check("unused approved", f["unused_approved"] == ["EV-005"])

    # Ambiguous typo suggestion declines to guess.
    amb = build_ledger_index({"items": [
        {"id": "EV-110", "approval_status": "approved"},
        {"id": "EV-102", "approval_status": "approved"},
    ]})
    check("ambiguous suggestion empty", suggest_id("EV-100", amb) == "")

    # Adapter: clamp + refs mapping + warning for out-of-range, no mutation.
    canonical, warnings = adapt_ledger_for_warrant(ledger)
    by_id = {i["id"]: i for i in canonical["items"]}
    check("clamp highest->high", by_id["EV-001"]["proof_strength"] == "high")
    check("clamp warning", any("EV-001" in w and "clamped" in w for w in warnings))
    check("out-of-range warned", any("EV-005" in w and "colossal" in w for w in warnings))
    check("evidence_refs built", by_id["EV-001"]["evidence_refs"] == ["a.md#§A"])
    check("original not mutated", ledger["items"][0]["proof_strength"] == "highest")

    # Marker inlining keeps the citation attached to its sentence.
    inlined = inline_markers("The alpha works well. <!-- evidence: EV-001 -->")
    check("trailing marker inlined", inlined == "The alpha works well (EV-001).")
    inlined2 = inline_markers("Alpha <!-- evidence: EV-001 --> works.")
    check("mid-sentence marker inlined", inlined2 == "Alpha (EV-001) works.")

    # Graceful degradation when the sibling repo is absent.
    missing = run_warrant(["text"], ledger, warrant_src="/nonexistent/warrant/src")
    check("fallback unavailable", missing["available"] is False)
    check("fallback reason", "falling back to marker-audit only" in missing["reason"])

    if failures:
        print("evidence_check_core selftest FAILED:", file=sys.stderr)
        for name in failures:
            print(f"  ✗ {name}", file=sys.stderr)
        return 1
    print("evidence_check_core selftest OK (all checks passed)")
    return 0


# ────────────────────────────────────────────────────────────────
# CLI
# ────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*",
                        help="one or more draft .md files followed by the ledger .json (last arg)")
    parser.add_argument("--json", action="store_true", help="emit full JSON result")
    parser.add_argument("--no-warrant", action="store_true", help="skip the warrant engine call")
    parser.add_argument("--warrant-src", default=None,
                        help="path to warrant-ledger/src (default: FPA_WARRANT_SRC env, "
                             f"then {DEFAULT_WARRANT_SRC})")
    parser.add_argument("--selftest", action="store_true", help="run the deterministic selftest")
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest()

    if len(args.paths) < 2:
        parser.error("need at least one draft .md and the ledger .json (ledger last)")
    *draft_args, ledger_arg = args.paths
    draft_paths = [Path(p) for p in draft_args]
    ledger_path = Path(ledger_arg)
    for p in [*draft_paths, ledger_path]:
        if not p.is_file():
            print(f"error: not a file: {p}", file=sys.stderr)
            return 2

    result = run_check(draft_paths, ledger_path,
                       warrant_src=resolve_warrant_src(args.warrant_src),
                       use_warrant=not args.no_warrant)
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json
          else render_human(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
