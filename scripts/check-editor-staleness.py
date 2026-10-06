#!/usr/bin/env python3
"""
check-editor-staleness.py — has the draft changed since the editor last ran?

The failure this closes (NAVWAR GenAI EPSS, 2026-08-27 to 2026-09-02): /proposal-editor
ran once, then the draft was rewritten seven times — restructure, positive-claim pass,
prose rebalance, two comment rounds, Q&A alignment — and none of those went back through
the editor. prose-lint reported 0 HIGH before every post, so a clean regex gate looked
like a clean edit. Two AI tells sat through five posted versions.

The editor is not a stage that runs once. It is a gate that must re-fire whenever the
draft materially changes. This script is the mechanism.

Rule: every top-level drafts/*.md must be OLDER than the most recent
    ## YYYY-MM-DD HH:MM — proposal-editor — ...
line in working/activity.md. drafts/loose/ is the pre-edit preimage and is exempt.

Resolution is one minute, because the log records HH:MM. A draft saved during the same
minute as the editor entry counts as covered by it: the editor edits, then logs, and both
usually land in the same minute. (Before 2026-10-06 the comparison used seconds against a
minute-resolution log, so every edit-then-log pair in one minute read as STALE.) Only a
save in a LATER minute than the entry is stale.

Exit codes:
  0  clean — every draft predates the last editor run
  1  STALE — one or more drafts changed after the last editor run (blocks export)
  2  no proposal-editor entry in activity.md at all, or the proposal cannot be resolved

Usage:
  python scripts/check-editor-staleness.py --proposal <slug>
  python scripts/check-editor-staleness.py --proposal <slug> --warn-only   # exit 0, print warning
  python scripts/check-editor-staleness.py --selftest
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import time
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Matches the activity-trail convention from CLAUDE.md. Time is optional because some
# hand-written entries omit it; those are treated as 00:00 and warned about, so a same-day
# draft edit still counts as newer. That pushes the log toward the convention rather than
# letting an untimed entry silently vouch for edits made later the same day.
EDITOR_LINE = re.compile(
    r"^##\s+(\d{4}-\d{2}-\d{2})(?:\s+(\d{2}:\d{2}))?\s+[—-]+\s+proposal-editor\b",
    re.MULTILINE,
)


def last_editor_run(activity: Path) -> tuple[datetime | None, bool]:
    """Return (latest editor timestamp, any_entry_lacked_a_time)."""
    if not activity.is_file():
        return None, False
    text = activity.read_text(encoding="utf-8", errors="replace")
    latest: datetime | None = None
    untimed = False
    for m in EDITOR_LINE.finditer(text):
        day, hhmm = m.group(1), m.group(2)
        if hhmm is None:
            untimed = True
            hhmm = "00:00"
        ts = datetime.strptime(f"{day} {hhmm}", "%Y-%m-%d %H:%M")
        if latest is None or ts > latest:
            latest = ts
    return latest, untimed


def draft_files(drafts: Path) -> list[Path]:
    # Top level only. drafts/loose/ is the pre-edit preimage by design.
    return sorted(p for p in drafts.glob("*.md") if p.is_file())


def _rel(p: Path) -> str:
    """Repo-relative for display; absolute when the path lives outside the repo (selftest)."""
    try:
        return str(p.relative_to(REPO_ROOT))
    except ValueError:
        return str(p)


def check(proposal_dir: Path, warn_only: bool = False) -> int:
    activity = proposal_dir / "working" / "activity.md"
    drafts = proposal_dir / "drafts"
    slug = proposal_dir.name

    if not drafts.is_dir():
        print(f"editor-staleness: no drafts directory at {drafts}", file=sys.stderr)
        return 2

    latest, untimed = last_editor_run(activity)
    files = draft_files(drafts)

    if latest is None:
        print(f"editor-staleness [{slug}]: NO proposal-editor entry in {_rel(activity)}")
        print("  The editor has never been logged as run on this proposal. Run /proposal-editor.")
        return 2

    if untimed:
        print(f"editor-staleness [{slug}]: note — a proposal-editor entry lacks HH:MM and was read as 00:00 "
              "that day. Log editor runs as '## YYYY-MM-DD HH:MM — proposal-editor — ...'.")

    # The log is minute-resolution: the entry covers every save up to the end of its minute.
    cutoff = latest + timedelta(minutes=1)
    stale: list[tuple[Path, datetime]] = []
    for f in files:
        mtime = datetime.fromtimestamp(f.stat().st_mtime)
        if mtime >= cutoff:
            stale.append((f, mtime))

    if not stale:
        print(f"editor-staleness [{slug}]: clean — {len(files)} draft(s), last editor run "
              f"{latest:%Y-%m-%d %H:%M}, nothing newer")
        return 0

    sev = "WARN " if warn_only else "STALE"
    print(f"editor-staleness [{slug}]: {sev} — last /proposal-editor run {latest:%Y-%m-%d %H:%M}; "
          f"{len(stale)} draft(s) modified after it:")
    for f, mtime in stale:
        delta = mtime - latest
        hrs = delta.total_seconds() / 3600
        print(f"    {_rel(f)}   modified {mtime:%Y-%m-%d %H:%M}  (+{hrs:.1f} h)")
    print("  The draft changed after the editor last ran. Re-run /proposal-editor before export or "
          "review; a clean prose-lint is not an edit.")
    return 0 if warn_only else 1


def selftest() -> int:
    """Deterministic, offline. Builds a throwaway proposal and exercises all three exits."""
    import shutil

    tmp = Path(tempfile.mkdtemp(prefix="editor-staleness-"))
    try:
        root = tmp / "proposals" / "selftest"
        (root / "working").mkdir(parents=True)
        (root / "drafts" / "loose").mkdir(parents=True)
        act = root / "working" / "activity.md"
        draft = root / "drafts" / "section.md"
        loose = root / "drafts" / "loose" / "section.md"
        failures = 0

        def expect(label: str, got: int, want: int) -> None:
            nonlocal failures
            ok = got == want
            failures += 0 if ok else 1
            print(f"  [{'ok' if ok else 'FAIL'}] {label}: exit {got} (want {want})")

        # Case 1: no editor entry at all -> 2
        act.write_text("## 2026-01-01 10:00 — proposal-writer — drafted → drafts/\n", encoding="utf-8")
        draft.write_text("prose\n", encoding="utf-8")
        expect("no editor entry", check(root), 2)

        # Case 2: editor ran AFTER the draft was written -> 0
        act.write_text(
            "## 2026-01-01 10:00 — proposal-writer — drafted → drafts/\n"
            "## 2099-01-01 12:00 — proposal-editor — polished → drafts/\n", encoding="utf-8")
        expect("editor newer than draft", check(root), 0)

        # Case 3: draft modified AFTER the editor -> 1
        act.write_text(
            "## 2026-01-01 10:00 — proposal-writer — drafted → drafts/\n"
            "## 2026-01-01 12:00 — proposal-editor — polished → drafts/\n", encoding="utf-8")
        time.sleep(0.01)
        draft.write_text("prose, edited later\n", encoding="utf-8")   # mtime = now > 2026-01-01
        expect("draft newer than editor", check(root), 1)

        # Case 4: same as 3 with --warn-only -> 0
        expect("draft newer, warn-only", check(root, warn_only=True), 0)

        # Case 5: loose/ preimage is exempt; only top-level counts
        act.write_text("## 2099-01-01 12:00 — proposal-editor — polished → drafts/\n", encoding="utf-8")
        loose.write_text("preimage edited now\n", encoding="utf-8")
        expect("loose/ exempt", check(root), 0)

        # Case 7: draft saved in the SAME minute as the editor entry -> 0 (edit, then log)
        import os
        same_min = datetime(2026, 1, 1, 12, 0)
        act.write_text("## 2026-01-01 12:00 — proposal-editor — polished → drafts/\n", encoding="utf-8")
        stamp = (same_min + timedelta(seconds=40)).timestamp()
        os.utime(draft, (stamp, stamp))
        expect("same-minute save covered", check(root), 0)

        # Case 8: draft saved in the NEXT minute -> 1
        stamp = (same_min + timedelta(seconds=61)).timestamp()
        os.utime(draft, (stamp, stamp))
        expect("next-minute save stale", check(root), 1)

        # Case 6: untimed editor entry parses (as 00:00) and does not crash
        act.write_text("## 2099-01-01 — proposal-editor — polished → drafts/\n", encoding="utf-8")
        expect("untimed entry tolerated", check(root), 0)

        print("selftest:", "PASS" if failures == 0 else f"FAIL ({failures})")
        return 0 if failures == 0 else 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    ap = argparse.ArgumentParser(description="Block export when drafts changed after the last /proposal-editor run.")
    ap.add_argument("--proposal", help="proposal slug under proposals/")
    ap.add_argument("--warn-only", action="store_true", help="report staleness but exit 0")
    ap.add_argument("--selftest", action="store_true", help="run the offline self-test and exit")
    args = ap.parse_args()

    if args.selftest:
        return selftest()
    if not args.proposal:
        ap.error("--proposal is required (or use --selftest)")
    proposal_dir = REPO_ROOT / "proposals" / args.proposal
    if not proposal_dir.is_dir():
        print(f"editor-staleness: no proposal at {proposal_dir}", file=sys.stderr)
        return 2
    return check(proposal_dir, warn_only=args.warn_only)


if __name__ == "__main__":
    sys.exit(main())
