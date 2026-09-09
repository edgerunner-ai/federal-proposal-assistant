#!/usr/bin/env python3
"""check-mission-effect.py — the proposal-level outcome gate.

Verifies that a proposal states its Mission Effect Statement (problem, mission effect,
capability, cost, timeline) in `working/narrative-spine.md`, that the effect is written
in operator terms, and that the drafts (or the rendered .docx) still carry it. Doctrine:
`reference/methodology/mission-effect-translation.md` (adopted 2026-09-09). Modelled on
`check-strengths.py`: deterministic, offline, phrase-fingerprint based, `--selftest`.

Checks (HIGH blocks; ADVISORY reports):
  spine-block     HIGH      no "## Mission Effect" block in working/narrative-spine.md
  element         HIGH      one of the five labelled lines is missing or empty
  operator-terms  ADVISORY  the effect line has no operator-terms marker (time, decision,
                            risk, availability, what no longer has to happen)
  vendor-phrase   ADVISORY  the effect line uses a vendor phrase ("decision superiority",
                            "readiness", "transform", ...)
  carried         ADVISORY  the drafts / .docx do not carry the effect line's distinctive
                            phrases (< 50% coverage); HIGH with --strict
  cost-carried    ADVISORY  the drafts do not carry the cost line's distinctive phrases
  timeline        ADVISORY  the drafts do not carry the timeline line's distinctive phrases

Usage:
  python scripts/check-mission-effect.py --proposal <slug>                 # drafts
  python scripts/check-mission-effect.py --proposal <slug> --target docx   # final/docx
  python scripts/check-mission-effect.py --proposal <slug> --strict        # carried -> HIGH
  python scripts/check-mission-effect.py --selftest

Writes reviews/mission-effect-check.md. Exit 0 clean, 1 HIGH findings, 2 harness error.
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
from datetime import date
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent.parent

ELEMENTS = ("problem", "mission effect", "capability", "cost", "timeline")
ELEMENT_RE = re.compile(
    r"^\s*(?:[-*]\s*)?(?:\*\*)?(?P<label>problem|mission effect|effect|capability|cost|timeline)"
    r"(?:\*\*)?\s*[:.]\s*(?P<text>.+?)\s*$",
    re.IGNORECASE,
)
OPERATOR_MARKERS = {
    "time": r"\b(minute|hour|day|week|faster|sooner|before|within|time to|time-to|real time|near real|at the console|at the gear)\b",
    "decision": r"\b(decision|decide|decides|choose|call|act on|acted on)\b",
    "risk": r"\b(risk|error|wrong|fail|failure|catch|caught|stop|stopped|prevent|detect|detected|bounded|safe)\b",
    "availability": r"\b(offline|disconnected|without a network|without the network|no network|when the network|available|reach-back|reachback|on the workstation|on the laptop|at sea|in the field)\b",
    "no-longer": r"\b(no longer|never has to|never have to|instead of|without having to|without waiting|does not have to|do not have to)\b",
}
VENDOR_PHRASES = [
    "decision superiority", "transform", "world-class", "game-chang", "next-generation",
    "cutting-edge", "synerg", "revolutioni", "best-in-class", "ai-enabled", "leverage", "empower",
]
STOP = set("""the a an and or of to in on for with by from at as is are be that this these those it its
their our we you your they them than then when where which who whom what into onto over under
each every all any some no not more most less least very can will would should may might must
also both either neither only own same so too than up down out off just because before after
while during until since across against about above below between within without through""".split())


# ---------------------------------------------------------------- parsing
def parse_statement(spine_text: str) -> tuple[dict, list]:
    """Return ({element: text}, findings). Reads the '## Mission Effect' block only."""
    findings = []
    m = re.search(r"^##\s+Mission\s+Effect\b.*?$", spine_text, re.IGNORECASE | re.MULTILINE)
    if not m:
        findings.append(("HIGH", "spine-block", "working/narrative-spine.md has no '## Mission Effect' block"))
        return {}, findings
    rest = spine_text[m.end():]
    nxt = re.search(r"^##\s+", rest, re.MULTILINE)
    block = rest[: nxt.start()] if nxt else rest
    found: dict = {}
    for line in block.splitlines():
        em = ELEMENT_RE.match(line)
        if not em:
            continue
        label = em.group("label").lower()
        if label == "effect":
            label = "mission effect"
        text = em.group("text").strip()
        if text and label not in found and not text.startswith("<"):
            found[label] = text
    for el in ELEMENTS:
        if el not in found:
            findings.append(("HIGH", "element", f"'{el.title()}:' line missing or empty in the Mission Effect block"))
    return found, findings


def operator_terms(effect: str) -> tuple[list, list]:
    """Markers are searched after vendor phrases are removed, so "decision superiority"
    cannot pass as a decision effect."""
    low = effect.lower()
    vendor = [v for v in VENDOR_PHRASES if v in low]
    for v in vendor:
        low = low.replace(v, " ")
    hits = [k for k, rx in OPERATOR_MARKERS.items() if re.search(rx, low)]
    return hits, vendor


def fingerprint(text: str, k: int = 8) -> list[str]:
    """Distinctive content words: 5+ letters, not stop words, first occurrence order."""
    words = re.findall(r"[A-Za-z][A-Za-z\-]{4,}", text)
    out: list[str] = []
    for w in words:
        lw = w.lower()
        if lw in STOP or lw in out:
            continue
        out.append(lw)
    nums = re.findall(r"\b\d[\d,.]*\b", text)
    return (out + nums)[:k]


def coverage(phrases: list[str], target: str) -> tuple[float, list[str]]:
    if not phrases:
        return 0.0, []
    low = target.lower()
    missing = [p for p in phrases if p.lower() not in low]
    return 1 - len(missing) / len(phrases), missing


# ---------------------------------------------------------------- targets
def read_drafts(prop: Path) -> tuple[str, str]:
    files = sorted(p for p in (prop / "drafts").glob("*.md"))
    if not files:
        return "", "drafts/*.md (none found)"
    return "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in files), f"drafts/*.md ({len(files)} files)"


def read_docx_dir(prop: Path) -> tuple[str, str]:
    try:
        import docx  # python-docx
    except ImportError:
        return "", "final/docx (python-docx not installed)"
    files = sorted((prop / "final" / "docx").glob("*.docx"))
    if not files:
        return "", "final/docx/*.docx (none found)"
    parts = []
    for f in files:
        d = docx.Document(str(f))
        parts.extend(p.text for p in d.paragraphs)
        for t in d.tables:
            for row in t.rows:
                for c in row.cells:
                    parts.append(c.text)
    return "\n".join(parts), f"final/docx/*.docx ({len(files)} files)"


# ---------------------------------------------------------------- check
def check(prop: Path, target: str = "drafts", strict: bool = False) -> tuple[list, dict]:
    spine = prop / "working" / "narrative-spine.md"
    F: list = []
    if not spine.exists():
        F.append(("HIGH", "spine-block", "working/narrative-spine.md not found; run /narrative-spine"))
        return F, {}
    stmt, pf = parse_statement(spine.read_text(encoding="utf-8", errors="replace"))
    F.extend(pf)
    info = {"statement": stmt}
    if "mission effect" in stmt:
        hits, vendor = operator_terms(stmt["mission effect"])
        info["operator_terms"] = hits
        if not hits:
            F.append(("ADVISORY", "operator-terms",
                      "the effect line has no operator-terms marker (time, decision, risk, availability, what no longer has to happen)"))
        if vendor:
            F.append(("ADVISORY", "vendor-phrase", f"the effect line uses vendor language: {', '.join(vendor)}"))
    text, desc = read_docx_dir(prop) if target == "docx" else read_drafts(prop)
    info["target"] = desc
    if text and stmt:
        for el, rule in (("mission effect", "carried"), ("cost", "cost-carried"), ("timeline", "timeline")):
            if el not in stmt:
                continue
            cov, missing = coverage(fingerprint(stmt[el]), text)
            info[f"coverage:{el}"] = cov
            if cov < 0.5:
                sev = "HIGH" if (strict and rule == "carried") else "ADVISORY"
                F.append((sev, rule, f"{desc} carries {cov:.0%} of the {el} line's phrases; missing: {', '.join(missing[:6])}"))
    elif stmt and not text:
        F.append(("ADVISORY", "carried", f"{desc}: nothing to check yet"))
    return F, info


def render_report(slug: str, F: list, info: dict) -> str:
    lines = [f"# Mission Effect Check: {slug}", "",
             f"**Date:** {date.today().isoformat()} · **Target:** {info.get('target', 'n/a')} · "
             f"**Doctrine:** `reference/methodology/mission-effect-translation.md`", ""]
    stmt = info.get("statement") or {}
    if stmt:
        lines += ["## Statement as written in the spine", "", "| Element | Text |", "|---|---|"]
        for el in ELEMENTS:
            lines.append(f"| {el.title()} | {stmt.get(el, '(missing)')} |")
        lines.append("")
        ot = info.get("operator_terms")
        if ot is not None:
            lines.append(f"Operator-terms markers in the effect line: {', '.join(ot) if ot else 'none'}")
            lines.append("")
    highs = [f for f in F if f[0] == "HIGH"]
    advs = [f for f in F if f[0] == "ADVISORY"]
    lines += ["## Findings", "", f"**{len(highs)} HIGH, {len(advs)} advisory.**", ""]
    for sev, rule, detail in highs + advs:
        lines.append(f"- [{sev}] `{rule}`: {detail}")
    if not F:
        lines.append("- Clean: the statement is complete, in operator terms, and carried by the target.")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- selftest
def selftest() -> int:
    ok = True

    def expect(label, cond):
        nonlocal ok
        ok &= bool(cond)
        print(f"  [{'ok ' if cond else 'FAIL'}] {label}")

    with tempfile.TemporaryDirectory() as td:
        prop = Path(td)
        (prop / "working").mkdir(); (prop / "drafts").mkdir()
        # 1. no spine
        F, _ = check(prop)
        expect("missing spine is HIGH", any(f[1] == "spine-block" and f[0] == "HIGH" for f in F))
        # 2. spine without the block
        (prop / "working" / "narrative-spine.md").write_text("# Spine\n\n## Positioning\n\nx\n", encoding="utf-8")
        F, _ = check(prop)
        expect("missing block is HIGH", any(f[1] == "spine-block" for f in F))
        # 3. full statement, vendor effect, no drafts
        good = ("# Spine\n\n## Mission Effect\n\n"
                "**Problem:** Sailors maintain software that changes faster than training, disconnected.\n"
                "**Mission effect:** AI-enabled decision superiority and readiness for the fleet.\n"
                "**Capability:** EdgeRunner Mentor: local retrieval and a verification gate (EV-073).\n"
                "**Cost:** Phase 2 rough order of magnitude of $1.2M buys the pilot.\n"
                "**Timeline:** Fleet pilot from month twelve on Government authorization.\n\n## Positioning\n\ny\n")
        (prop / "working" / "narrative-spine.md").write_text(good, encoding="utf-8")
        F, info = check(prop)
        expect("complete block has no HIGH", not any(f[0] == "HIGH" for f in F))
        expect("vendor phrase flagged", any(f[1] == "vendor-phrase" for f in F))
        expect("no operator terms flagged", any(f[1] == "operator-terms" for f in F))
        # 4. operator-terms effect, drafts carry it
        good2 = good.replace("AI-enabled decision superiority and readiness for the fleet.",
                             "A technician at the console gets the right procedure faster than a manual, and a wrong answer is stopped before it is executed at sea.")
        (prop / "working" / "narrative-spine.md").write_text(good2, encoding="utf-8")
        (prop / "drafts" / "01.md").write_text(
            "A technician at the console gets the right procedure with its source faster than a manual; "
            "a wrong answer is stopped before it is executed at sea. Fleet pilot from month twelve on Government authorization.\n",
            encoding="utf-8")
        F, info = check(prop)
        expect("operator terms detected", info.get("operator_terms"))
        expect("effect carried by drafts (no 'carried' finding)", not any(f[1] == "carried" for f in F))
        expect("timeline carried", not any(f[1] == "timeline" for f in F))
        expect("cost not carried is ADVISORY", any(f[1] == "cost-carried" and f[0] == "ADVISORY" for f in F))
        # 5. strict: effect absent from drafts -> HIGH
        (prop / "drafts" / "01.md").write_text("Nothing relevant here.\n", encoding="utf-8")
        F, _ = check(prop, strict=True)
        expect("--strict makes uncarried effect HIGH", any(f[1] == "carried" and f[0] == "HIGH" for f in F))
        # 6. missing element
        (prop / "working" / "narrative-spine.md").write_text(good2.replace("**Cost:**", "**Price:**"), encoding="utf-8")
        F, _ = check(prop)
        expect("missing Cost line is HIGH", any(f[1] == "element" and "Cost" in f[2] for f in F))
        # 7. report renders
        rep = render_report("t", F, info)
        expect("report renders", "# Mission Effect Check" in rep and "| Problem |" in rep)
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--proposal", help="proposal slug under proposals/")
    ap.add_argument("--target", choices=("drafts", "docx"), default="drafts")
    ap.add_argument("--strict", action="store_true", help="an effect the target does not carry is HIGH")
    ap.add_argument("--no-report", action="store_true", help="do not write reviews/mission-effect-check.md")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.proposal:
        ap.error("--proposal is required (or --selftest)")
    prop = REPO_ROOT / "proposals" / args.proposal
    if not prop.is_dir():
        print(f"check-mission-effect: proposal not found: {prop}", file=sys.stderr)
        return 2
    F, info = check(prop, args.target, args.strict)
    highs = [f for f in F if f[0] == "HIGH"]
    advs = [f for f in F if f[0] == "ADVISORY"]
    tag = "FAIL" if highs else ("warn" if advs else "ok  ")
    print(f"{tag}  mission-effect [{args.proposal}] {info.get('target', '')}  ({len(highs)} high, {len(advs)} advisory)")
    for sev, rule, detail in highs + advs:
        print(f"        [{sev:<8}] {rule:<15} {detail}")
    if not args.no_report:
        out = prop / "reviews" / "mission-effect-check.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_report(args.proposal, F, info), encoding="utf-8")
        print(f"        report: {out.relative_to(REPO_ROOT)}")
    return 1 if highs else 0


if __name__ == "__main__":
    sys.exit(main())
