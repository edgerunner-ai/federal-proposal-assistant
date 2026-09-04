#!/usr/bin/env python3
"""
tools/register.py — the one place that decides which formatting register a proposal is in,
and how to recognise the callout sidebar tables the renderer emits.

Two registers (see reference/style-guide.md, "Register by Proposal Type"):

  strict     white-paper family, briefs, RFIs, SBIR: flat institutional prose. All text
             black, bold only for a leading label. This is the 2026-09-02 rule set from the
             NAVWAR EPSS lessons and it stays as written.
  assertive  far-rfp / ota-proposal / cso-full and the other scored volumes: the register
             the Octo VAULT tech volume is written in (reference/winning-examples/
             usaf-vault-octo-2020-lessons.md). Coloured heading and table-header rows are a
             design choice, not a machine tell; one short bold key phrase per paragraph is
             a scanning device; the sidebar callout carries a proof point in white on dark.

Nothing here reads the drafts. Callers pass a type_id, a proposal slug, or a path to
working/proposal-type.md. Unknown or absent input resolves to `strict`, so every existing
call site keeps its current behaviour until it opts in.

The callout sidebar table is tagged with <w:tblDescription w:val="fpa-callout"/> when
tools/md_to_docx.py emits it; `is_callout_table` reads the tag back so polish and lint can
leave the sidebar's white-on-dark header alone.
"""
from __future__ import annotations

import re
from pathlib import Path

try:
    from docx.oxml.ns import qn
except ImportError:  # pragma: no cover - callers already require python-docx
    qn = None  # type: ignore

REPO_ROOT = Path(__file__).resolve().parent.parent

STRICT = "strict"
ASSERTIVE = "assertive"

# type_id values (reference/proposal-types/*.md) that write in the assertive register.
ASSERTIVE_TYPES = frozenset({
    "far-rfp", "ota-proposal", "cso-full", "idiq-to", "gsa-mas-task-order", "baa",
})

CALLOUT_TAG = "fpa-callout"

_TYPE_ID_RE = re.compile(r"^\s*type_id\s*:\s*([A-Za-z0-9_-]+)", re.MULTILINE)


def register_for_type(type_id: str | None) -> str:
    """Map a type_id to a register. Unknown or empty -> strict."""
    if not type_id:
        return STRICT
    return ASSERTIVE if type_id.strip().lower() in ASSERTIVE_TYPES else STRICT


def type_id_from_file(proposal_type_md: Path) -> str | None:
    """Read `type_id:` from a working/proposal-type.md (frontmatter or body)."""
    try:
        text = proposal_type_md.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = _TYPE_ID_RE.search(text)
    return m.group(1) if m else None


def resolve_register(*, register: str | None = None, type_id: str | None = None,
                     proposal: str | None = None, workspace: Path | None = None) -> str:
    """Resolve a register from whichever hint the caller has, in this precedence:
    explicit register > type_id > proposal slug (reads working/proposal-type.md) > strict.
    """
    if register:
        r = register.strip().lower()
        if r not in (STRICT, ASSERTIVE):
            raise ValueError(f"unknown register {register!r}; use {STRICT} or {ASSERTIVE}")
        return r
    if type_id:
        return register_for_type(type_id)
    if proposal:
        root = workspace or REPO_ROOT
        return register_for_type(type_id_from_file(root / "proposals" / proposal / "working" / "proposal-type.md"))
    return STRICT


def is_callout_table(table) -> bool:
    """True for the sidebar tables tools/md_to_docx.py emits (tagged in tblPr)."""
    if qn is None:
        return False
    try:
        tblPr = table._tbl.tblPr
    except AttributeError:
        return False
    if tblPr is None:
        return False
    desc = tblPr.find(qn("w:tblDescription"))
    return desc is not None and desc.get(qn("w:val")) == CALLOUT_TAG


def _selftest() -> int:
    ok = True

    def check(label: str, cond: bool) -> None:
        nonlocal ok
        ok &= cond
        print(f"  [{'ok ' if cond else 'FAIL'}] {label}")

    check("far-rfp is assertive", register_for_type("far-rfp") == ASSERTIVE)
    check("white-paper is strict", register_for_type("white-paper") == STRICT)
    check("cso-brief stays strict (NAVWAR EPSS rules)", register_for_type("cso-brief") == STRICT)
    check("unknown is strict", register_for_type("something-new") == STRICT)
    check("None is strict", register_for_type(None) == STRICT)
    check("explicit register wins", resolve_register(register="assertive", type_id="white-paper") == ASSERTIVE)
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "proposal-type.md"
        p.write_text("---\ntype_id: ota-proposal\ndisplay_name: x\n---\n", encoding="utf-8")
        check("type_id parsed from frontmatter", type_id_from_file(p) == "ota-proposal")
    try:
        resolve_register(register="loud")
        check("bad register rejected", False)
    except ValueError:
        check("bad register rejected", True)
    print("selftest:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(_selftest())
