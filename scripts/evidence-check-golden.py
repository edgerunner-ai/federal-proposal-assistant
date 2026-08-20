#!/usr/bin/env python3
"""evidence-check-golden.py — golden-file regression gate for the evidence-check
deterministic core (and its warrant integration).

DECISION-canonical-ownership action #4 gate: fixture draft + fixture ledger →
expected findings, so "no regression" in the FPA→warrant migration is falsifiable.
Fixtures are SYNTHETIC (tests/fixtures/evidence-check/) — no real proposal or
company data — and cover: an OK citation, a typo'd ID, a retired ID, a restricted
ID, an explicit CLAIM-UNSUPPORTED marker, a cite-spam sentence, a pending-review
ID, and an uncited-but-approved ledger entry.

Marker-audit expectations are asserted exactly. Warrant expectations are keyed by
cited ID → verdict status set (robust to the engine's claim-extraction heuristics
changing sentence counts) and are asserted only when the sibling engine is
importable; otherwise the harness asserts the graceful-fallback contract instead.
The fallback path itself is always asserted via a bogus --warrant-src.

Usage:
  python scripts/evidence-check-golden.py             # run the golden comparison
  python scripts/evidence-check-golden.py --selftest  # same, for smoke-test.sh
  python scripts/evidence-check-golden.py --verbose

Exit: 0 = golden expectations hold, 1 = regression / expectation mismatch,
2 = harness setup problem (missing fixtures, unreadable files).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

# Windows consoles default to cp1252, which can't print the check glyphs.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures" / "evidence-check"
DRAFT = FIXTURES / "draft.md"
LEDGER = FIXTURES / "ledger.json"
EXPECTED = FIXTURES / "expected-findings.json"


def load_core():
    """Import scripts/evidence_check_core.py by path (repo scripts aren't a package)."""
    path = ROOT / "scripts" / "evidence_check_core.py"
    spec = importlib.util.spec_from_file_location("evidence_check_core", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--selftest", action="store_true",
                        help="alias for the default golden run (smoke-test convention)")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    for f in (DRAFT, LEDGER, EXPECTED):
        if not f.is_file():
            print(f"golden: missing fixture {f}", file=sys.stderr)
            return 2

    core = load_core()
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    exp_audit = expected["marker_audit"]
    exp_warrant = expected["warrant"]

    failures: list[str] = []
    passes = 0

    def check(name: str, condition: bool, detail: str = "") -> None:
        nonlocal passes
        if condition:
            passes += 1
            if args.verbose:
                print(f"  ✓ {name}")
        else:
            failures.append(f"{name}{f' — {detail}' if detail else ''}")

    result = core.run_check([DRAFT], LEDGER,
                            warrant_src=core.resolve_warrant_src(None), use_warrant=True)

    # ── Marker audit: exact ────────────────────────────────────────
    check("ledger counts", result["ledger"]["counts"] == exp_audit["ledger_counts"],
          f"got {result['ledger']['counts']}")
    check("marker tallies", result["markers"] == exp_audit["markers"],
          f"got {result['markers']}")

    f = result["findings"]
    check("unsupported claims",
          [{k: r[k] for k in ("file", "line", "sentence")} for r in f["unsupported_claims"]]
          == exp_audit["unsupported_claims"],
          f"got {f['unsupported_claims']}")
    check("unknown ids + typo suggestion",
          [{k: r[k] for k in ("file", "line", "id", "suggestion")} for r in f["unknown_ids"]]
          == exp_audit["unknown_ids"],
          f"got {f['unknown_ids']}")
    check("retired ids",
          [{k: r[k] for k in ("file", "line", "id")} for r in f["retired_ids"]]
          == exp_audit["retired_ids"],
          f"got {f['retired_ids']}")
    check("restricted ids + restrictions text",
          [{k: r[k] for k in ("file", "line", "id", "restrictions")} for r in f["restricted_ids"]]
          == exp_audit["restricted_ids"],
          f"got {f['restricted_ids']}")
    check("pending ids",
          [{k: r[k] for k in ("file", "line", "id")} for r in f["pending_ids"]]
          == exp_audit["pending_ids"],
          f"got {f['pending_ids']}")
    check("unused approved evidence",
          f["unused_approved"] == exp_audit["unused_approved"],
          f"got {f['unused_approved']}")

    # ── Warrant integration: keyed by cited ID ─────────────────────
    w = result["warrant"]
    if w.get("available"):
        for warning in exp_audit["adapter_warnings_contain"]:
            check(f"adapter warning: {warning}", warning in w.get("adapter_warnings", []),
                  f"got {w.get('adapter_warnings')}")
        got_statuses: dict[str, set] = {}
        for v in w["verdicts"]:
            for cid in v["cited_ids"]:
                got_statuses.setdefault(cid, set()).add(v["status"])
        for cid, statuses in exp_warrant["cited_statuses"].items():
            check(f"warrant status for {cid}", got_statuses.get(cid) == set(statuses),
                  f"got {sorted(got_statuses.get(cid, []))}, want {statuses}")
        check("gate decision", w["gate"]["decision"] == exp_warrant["gate_decision"],
              f"got {w['gate']}")
        for key in exp_warrant["wbom_required_keys"]:
            check(f"wbom has '{key}'", key in w.get("wbom", {}))
        check("wbom gate mirrors gate",
              (w.get("wbom", {}).get("gate") or {}).get("decision") == exp_warrant["gate_decision"])
    else:
        print(f"golden: warrant engine unavailable ({w.get('reason')}) — "
              "asserting marker-audit + fallback contract only")
        check("fallback reason present", bool(w.get("reason")))

    # ── Graceful degradation is always asserted ────────────────────
    fallback = core.run_check([DRAFT], LEDGER,
                              warrant_src=str(FIXTURES / "no-such-engine"), use_warrant=True)
    check("fallback: unavailable flag", fallback["warrant"]["available"] is False)
    check("fallback: explains itself",
          "falling back to marker-audit only" in fallback["warrant"].get("reason", ""),
          f"got {fallback['warrant'].get('reason')}")
    check("fallback: marker audit unchanged",
          fallback["markers"] == result["markers"] and fallback["findings"] == result["findings"])

    print(f"evidence-check golden: {passes} checks passed, {len(failures)} failed"
          + ("" if w.get("available") else " (warrant engine absent — fallback mode)"))
    if failures:
        for name in failures:
            print(f"  ✗ {name}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
