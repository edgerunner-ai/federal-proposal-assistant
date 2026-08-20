#!/usr/bin/env python3
"""check-canonical-symbols.py — governance gate for canonical capability ownership.

DECISION-canonical-ownership rule 4 / action #7: enforcement is mechanical, not
social. This script reads docs/canonical-symbols.json and fails if a Python file
in this repo DEFINES a symbol whose capability is owned elsewhere (e.g. a fresh
gate/wbom/claim-extraction module that should delegate to `warrant_ledger`, or a
second marker-audit that should delegate to scripts/evidence_check_core.py).

Delegating is always fine — importing warrant_ledger or evidence_check_core does
not trip the gate; *re-defining* their owned symbols does. Files listed in the
manifest's allowed_files are the canonical implementations / this checker itself.

Usage:
  python scripts/check-canonical-symbols.py             # scan tracked *.py in the repo
  python scripts/check-canonical-symbols.py --staged    # scan only staged files (pre-commit)
  python scripts/check-canonical-symbols.py --selftest  # prove catch + pass on temp files

Exit: 0 = clean (or selftest passed), 1 = forbidden re-implementation found
(or selftest failed), 2 = manifest missing/unreadable (fail closed).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        _stream.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "docs" / "canonical-symbols.json"


def load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _definition_pattern(snippet: str) -> re.Pattern:
    """Match the snippet as a real top-of-line definition (def/class), not a call,
    an import, or a mention in a comment/string on an indented line."""
    return re.compile(r"(?m)^[ \t]*" + re.escape(snippet) + r"\s*[(\[:]")


def scan_file(path: Path, manifest: dict, rel: str) -> list[str]:
    if rel.replace("\\", "/") in manifest.get("allowed_files", []):
        return []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    violations = []
    for cap in manifest.get("capabilities", []):
        for snippet in cap.get("forbidden_definitions", []):
            if _definition_pattern(snippet).search(text):
                violations.append(
                    f"{rel}: defines `{snippet}` — capability '{cap['name']}' is owned by "
                    f"{cap['canonical_home']}; delegate instead of re-implementing"
                )
    return violations


def candidate_files(staged: bool) -> list[str]:
    if staged:
        cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"]
    else:
        cmd = ["git", "ls-files"]
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return [f for f in out.splitlines() if f.endswith(".py")]


def run_scan(staged: bool) -> int:
    if not MANIFEST.is_file():
        print(f"canonical-symbols: manifest missing at {MANIFEST} — failing closed", file=sys.stderr)
        return 2
    manifest = load_manifest(MANIFEST)
    violations: list[str] = []
    for rel in candidate_files(staged):
        p = ROOT / rel
        if p.is_file():
            violations.extend(scan_file(p, manifest, rel))
    if violations:
        print("canonical-symbols: forbidden re-implementation detected:", file=sys.stderr)
        for v in violations:
            print(f"  ✗ {v}", file=sys.stderr)
        print("  (ownership table: docs/DECISION-canonical-ownership.md; "
              "manifest: docs/canonical-symbols.json)", file=sys.stderr)
        return 1
    scope = "staged files" if staged else "tracked files"
    print(f"canonical-symbols: clean ({scope})")
    return 0


def selftest() -> int:
    failures: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            failures.append(name)

    manifest = {
        "capabilities": [{
            "name": "verification-engine",
            "canonical_home": "edgerunner-warrant (warrant_ledger)",
            "forbidden_definitions": ["def to_wbom", "class EvidenceGate"],
        }],
        "allowed_files": ["scripts/allowed_impl.py"],
    }

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        bad = tmp / "sneaky_gate.py"
        bad.write_text("def to_wbom(verdict):\n    return {}\n", encoding="utf-8")
        good = tmp / "delegator.py"
        good.write_text(
            "from warrant_ledger import to_wbom\n\n"
            "def report(v):\n    # to_wbom is imported, not re-defined\n"
            "    return to_wbom(v)\n",
            encoding="utf-8",
        )
        allowed = tmp / "allowed_impl.py"
        allowed.write_text("def to_wbom(v):\n    return {}\n", encoding="utf-8")

        check("catches re-definition", bool(scan_file(bad, manifest, "scripts/sneaky_gate.py")))
        bad2 = tmp / "bad2.py"
        bad2.write_text("class EvidenceGate:\n    pass\n", encoding="utf-8")
        check("catches class re-definition", bool(scan_file(bad2, manifest, "scripts/bad2.py")))
        check("delegation is allowed", scan_file(good, manifest, "scripts/delegator.py") == [])
        check("allowlisted canonical impl passes",
              scan_file(allowed, manifest, "scripts/allowed_impl.py") == [])
        mention = tmp / "mention.py"
        mention.write_text('DOC = "never write def to_wbom yourself"\n', encoding="utf-8")
        check("string mention not caught", scan_file(mention, manifest, "scripts/mention.py") == [])

    # The real repo must scan clean and the real manifest must parse.
    check("manifest exists", MANIFEST.is_file())
    if MANIFEST.is_file():
        real = load_manifest(MANIFEST)
        check("manifest has capabilities", bool(real.get("capabilities")))
        check("repo scans clean", run_scan(staged=False) == 0)

    if failures:
        print("check-canonical-symbols selftest FAILED:", file=sys.stderr)
        for name in failures:
            print(f"  ✗ {name}", file=sys.stderr)
        return 1
    print("check-canonical-symbols selftest OK (all checks passed)")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--staged", action="store_true", help="scan only staged files (pre-commit)")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    return run_scan(staged=args.staged)


if __name__ == "__main__":
    sys.exit(main())
