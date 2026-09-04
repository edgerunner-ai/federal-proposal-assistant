#!/usr/bin/env python3
"""
tools/md_to_docx.py — Shared markdown-to-Word converter for federal-proposal-assistant.

Converts proposal draft .md files → .docx in proposals/<slug>/final/docx/.

Usage:
    # All drafts, both individual + combined (default):
    python tools/md_to_docx.py --proposal nato-diana-decision-superiority

    # Individual files only:
    python tools/md_to_docx.py --proposal myproposal --mode individual

    # Combined document only, custom name:
    python tools/md_to_docx.py --proposal myproposal --mode combined --combined-name "technical-volume"

    # Explicit ordered file list (filenames relative to drafts/):
    python tools/md_to_docx.py --proposal myproposal --files sec1.md sec2.md sec3.md

    # Explicit workspace root (if running from a different working directory):
    python tools/md_to_docx.py --proposal myproposal --workspace "C:/path/to/federal-proposal-assistant"

Supported markdown:
    # H1  ## H2  ### H3  #### H4  ##### H5  ###### H6
    **bold**  *italic*  ***bold-italic***  `code` (inline monospace)
    - bullets (with nested indent via leading spaces)
    1. numbered lists (with nested indent)
    | table | rows | (pipe-delimited, first row = bold header)
    > blockquote (indented, used for action captions)
    ``` fenced code blocks ``` (verbatim, monospace, auto-sized to fit column)
    <!-- figure: NAME --> (embeds graphics/rendered/NAME.png, centered, fit to column)
    :::callout TITLE ... ::: (proof-point sidebar: dark header bar, light body, floats
        right at 40% of the column with text wrapping; `evidence: EV-###` and
        `align: left` are optional key lines at the top of the block — see add_callout)
    --- horizontal rule (skipped — internal metadata separator)
    <!-- html comments --> (stripped, except figure markers above)
    *Note: ... lines (skipped — internal metadata)
"""

import argparse
import os
import re
import sys
from pathlib import Path

# ── Dependency check ─────────────────────────────────────────────────────────
try:
    from docx import Document
    from docx.shared import Pt, Inches, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    print("ERROR: python-docx not installed. Run: pip install python-docx", file=sys.stderr)
    sys.exit(1)


try:
    from register import CALLOUT_TAG  # tools/register.py, same directory
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from register import CALLOUT_TAG


# ── Constants ─────────────────────────────────────────────────────────────────
WORKSPACE_ROOT = Path(__file__).parent.parent  # tools/ → workspace root
BODY_FONT = "Calibri"
BODY_SIZE = Pt(11)
MARGIN_TOP = Inches(1.0)
MARGIN_BOTTOM = Inches(1.0)
MARGIN_LEFT = Inches(1.25)
MARGIN_RIGHT = Inches(1.25)
TEXT_WIDTH_INCHES = 8.5 - 1.25 - 1.25  # 6.0 inches usable width

# Callout sidebar (the VAULT proof-point box): 40% of the column, dark header bar with
# white bold title, light body, thin border. Red is not used here on purpose — on the
# light page it is reserved for the customer-facing end state inside figures.
CALLOUT_WIDTH_FRACTION = 0.40
CALLOUT_HEADER_FILL = "191C20"     # brand near-black
CALLOUT_BODY_FILL = "F2F2F2"
CALLOUT_BORDER = "393939"          # brand dark grey
CALLOUT_FONT_SIZE = Pt(10)


# ── Document setup ────────────────────────────────────────────────────────────

def setup_document(doc: Document) -> None:
    """Apply margins and default body font to every section."""
    for section in doc.sections:
        section.top_margin = MARGIN_TOP
        section.bottom_margin = MARGIN_BOTTOM
        section.left_margin = MARGIN_LEFT
        section.right_margin = MARGIN_RIGHT

    # Set default run font in Normal style
    style = doc.styles["Normal"]
    style.font.name = BODY_FONT
    style.font.size = BODY_SIZE


# ── Inline formatting ─────────────────────────────────────────────────────────

def add_formatted_runs(para, text: str) -> None:
    """
    Add text to a paragraph with inline formatting:
        ***bold-italic***  **bold**  *italic*  `code`
    """
    # Split on any inline marker
    pattern = re.compile(
        r'(\*\*\*[^*]+\*\*\*'   # ***bold-italic***
        r'|\*\*[^*]+\*\*'       # **bold**
        r'|\*[^*]+\*'           # *italic*
        r'|`[^`]+`)'            # `code`
    )
    parts = pattern.split(text)
    for part in parts:
        if not part:
            continue
        run = para.add_run()
        run.font.name = BODY_FONT
        if re.match(r'^\*\*\*[^*]+\*\*\*$', part):
            run.text = part[3:-3]
            run.bold = True
            run.italic = True
        elif re.match(r'^\*\*[^*]+\*\*$', part):
            run.text = part[2:-2]
            run.bold = True
        elif re.match(r'^\*[^*]+\*$', part):
            run.text = part[1:-1]
            run.italic = True
        elif re.match(r'^`[^`]+`$', part):
            run.text = part[1:-1]
            run.font.name = "Courier New"
            run.font.size = Pt(10)
        else:
            run.text = part


# ── Table parsing ─────────────────────────────────────────────────────────────

def _is_separator_row(line: str) -> bool:
    """True for lines like |---|:---|:---:| that separate header from body."""
    return bool(re.match(r'^\s*\|[\s\-:|]+\|\s*$', line.rstrip()))


def _is_table_line(line: str) -> bool:
    return line.strip().startswith('|')


def _parse_cells(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip('|').split('|')]


def process_table(doc: Document, table_lines: list[str]) -> None:
    """Render a markdown pipe-table as a Word table."""
    data_rows = [ln for ln in table_lines if not _is_separator_row(ln)]
    if not data_rows:
        return

    num_cols = len(_parse_cells(data_rows[0]))
    if num_cols == 0:
        return

    col_width = Inches(TEXT_WIDTH_INCHES / num_cols)

    table = doc.add_table(rows=len(data_rows), cols=num_cols)
    table.style = "Table Grid"

    for r_idx, row_line in enumerate(data_rows):
        cells = _parse_cells(row_line)
        is_header = r_idx == 0
        for c_idx in range(num_cols):
            cell_text = cells[c_idx] if c_idx < len(cells) else ""
            cell = table.rows[r_idx].cells[c_idx]
            # Set column width
            cell.width = col_width
            para = cell.paragraphs[0]
            para.paragraph_format.space_before = Pt(2)
            para.paragraph_format.space_after = Pt(2)
            add_formatted_runs(para, cell_text)
            if is_header:
                for run in para.runs:
                    run.bold = True

    # Add a blank paragraph after the table for breathing room
    doc.add_paragraph()


# ── List helpers ──────────────────────────────────────────────────────────────

def _detect_list_indent(line: str) -> int:
    """Return nesting level 0,1,2,... based on leading spaces (every 2 spaces = 1 level)."""
    stripped = line.lstrip(' \t')
    leading = len(line) - len(stripped)
    return min(leading // 2, 8)  # cap at 8 levels


def _add_list_para(doc: Document, text: str, style: str, level: int) -> None:
    """Add a bullet or numbered list paragraph at the given nesting level."""
    para = doc.add_paragraph(style=style)
    para.paragraph_format.left_indent = Inches(0.25 * (level + 1))
    add_formatted_runs(para, text)


# ── Code block ──────────────────────────────────────────────────────────────

def process_code_block(doc: Document, code_lines: list[str]) -> None:
    """Render a fenced code block verbatim in a monospace font.

    ASCII diagrams and pre-formatted tables only align in a fixed-width font.
    Font size is scaled down so the widest line fits the 6.0" text column.
    """
    if not code_lines:
        return
    max_len = max((len(ln) for ln in code_lines), default=1) or 1
    # Courier New advance width is ~0.6 em. Solve max_len * pt * 0.6 / 72 <= width.
    fit_pt = int((TEXT_WIDTH_INCHES * 72) / (0.6 * max_len))
    size = Pt(max(5, min(9, fit_pt)))
    for ln in code_lines:
        para = doc.add_paragraph()
        para.paragraph_format.space_before = Pt(0)
        para.paragraph_format.space_after = Pt(0)
        run = para.add_run(ln)  # verbatim — no inline-markdown parsing
        run.font.name = "Courier New"
        run.font.size = size
    doc.add_paragraph()  # breathing room after the block


# ── Figure embedding ────────────────────────────────────────────────────────

def add_figure(doc: Document, md_path: Path, fig_name: str) -> None:
    """Embed a rendered proposal figure referenced by `<!-- figure: NAME -->`.

    NAME resolves to `<proposal>/graphics/rendered/NAME.png` (the path
    /proposal-graphics renders to). The figure is centered and scaled to the
    text-column width, with height capped to one page so a tall graphic does
    not overflow. A missing PNG renders a visible placeholder rather than
    silently dropping the figure.
    """
    png = (md_path.parent.parent / "graphics" / "rendered" / f"{fig_name}.png").resolve()
    para = doc.add_paragraph()
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if not png.exists():
        run = para.add_run(f"[figure not found: {fig_name}]")
        run.italic = True
        run.font.name = BODY_FONT
        return
    w_in = TEXT_WIDTH_INCHES
    try:
        from PIL import Image as _PILImage
        with _PILImage.open(png) as im:
            iw, ih = im.size
        if iw and ih and (TEXT_WIDTH_INCHES * ih / iw) > 8.0:
            w_in = 8.0 * iw / ih  # height-constrained — keep within one page
    except Exception:
        pass  # PIL absent — width-only scaling still preserves aspect ratio
    para.add_run().add_picture(str(png), width=Inches(w_in))
    doc.add_paragraph()  # breathing room after the figure


# ── Callout sidebar ──────────────────────────────────────────────────────────

def _shade(cell, fill_hex: str) -> None:
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)


def _float_table(table, width_in: float, align: str) -> None:
    """Make `table` a text-wrapped floating table anchored at the current paragraph.

    Word positions a table with <w:tblpPr> relative to the margin and flows the
    following paragraphs around it. That is the only way python-docx can produce
    a sidebar; there is no frame or text-box API. Child order inside tblPr is
    schema-fixed (tblStyle, tblpPr, ..., tblW, ..., tblLayout, ..., tblDescription),
    so tblpPr goes straight after tblStyle and tblDescription goes last.
    """
    tbl = table._tbl
    tblPr = tbl.tblPr
    pPr = OxmlElement('w:tblpPr')
    pPr.set(qn('w:leftFromText'), '144')     # 0.1in gutter each side
    pPr.set(qn('w:rightFromText'), '144')
    pPr.set(qn('w:topFromText'), '0')
    pPr.set(qn('w:bottomFromText'), '144')
    pPr.set(qn('w:vertAnchor'), 'text')
    pPr.set(qn('w:horzAnchor'), 'margin')
    pPr.set(qn('w:tblpXSpec'), 'left' if align == 'left' else 'right')
    pPr.set(qn('w:tblpY'), '1')
    style_el = tblPr.find(qn('w:tblStyle'))
    if style_el is not None:
        style_el.addnext(pPr)
    else:
        tblPr.insert(0, pPr)
    overlap = OxmlElement('w:tblOverlap')
    overlap.set(qn('w:val'), 'never')
    pPr.addnext(overlap)

    dxa = str(int(width_in * 1440))
    tblW = tblPr.find(qn('w:tblW'))
    if tblW is None:
        tblW = OxmlElement('w:tblW')
        tblPr.append(tblW)
    tblW.set(qn('w:w'), dxa)
    tblW.set(qn('w:type'), 'dxa')

    layout = tblPr.find(qn('w:tblLayout'))
    if layout is None:
        layout = OxmlElement('w:tblLayout')
        tblPr.append(layout)
    layout.set(qn('w:type'), 'fixed')

    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH'):
        b = OxmlElement(f'w:{edge}')
        b.set(qn('w:val'), 'single'); b.set(qn('w:sz'), '6')
        b.set(qn('w:space'), '0'); b.set(qn('w:color'), CALLOUT_BORDER)
        borders.append(b)
    tblPr.append(borders)

    mar = OxmlElement('w:tblCellMar')
    for edge, w in (('top', '60'), ('left', '100'), ('bottom', '60'), ('right', '100')):
        m = OxmlElement(f'w:{edge}'); m.set(qn('w:w'), w); m.set(qn('w:type'), 'dxa')
        mar.append(m)
    tblPr.append(mar)

    desc = OxmlElement('w:tblDescription')
    desc.set(qn('w:val'), CALLOUT_TAG)
    tblPr.append(desc)

    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for gc in grid.findall(qn('w:gridCol')):
            gc.set(qn('w:w'), dxa)
    table.autofit = False
    for row in table.rows:
        for cell in row.cells:
            cell.width = Inches(width_in)


def add_callout(doc: Document, title: str, body_paras: list[str], align: str = 'right') -> None:
    """Render a proof-point sidebar: one cell, header bar then body.

    The header is a paragraph with dark paragraph shading (white bold title) pulled
    out to the cell edges with negative indents, and the body follows in the same
    cell on a light fill. One cell rather than two rows because Word ignores
    keep-with-next inside a FLOATING table and will happily leave a header row on
    the previous page; a single row marked cantSplit can never break.

    The table floats at CALLOUT_WIDTH_FRACTION of the column and the paragraphs
    that follow it in the source wrap around it, so the author places the block
    immediately BEFORE the paragraph it should sit beside. Tagged with
    tblDescription=CALLOUT_TAG so polish_docx leaves its width and colours alone
    and lint-rendered-artifact treats it as a sidebar.
    """
    width_in = TEXT_WIDTH_INCHES * CALLOUT_WIDTH_FRACTION
    table = doc.add_table(rows=1, cols=1)
    _float_table(table, width_in, align)
    row = table.rows[0]
    trPr = row._tr.get_or_add_trPr()
    if trPr.find(qn('w:cantSplit')) is None:
        trPr.append(OxmlElement('w:cantSplit'))

    cell = row.cells[0]
    _shade(cell, CALLOUT_BODY_FILL)
    # zero top margin on this cell so the header bar sits flush with the border
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    top = OxmlElement('w:top'); top.set(qn('w:w'), '0'); top.set(qn('w:type'), 'dxa')
    tcMar.append(top)
    tcPr.append(tcMar)

    hp = cell.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    hp.paragraph_format.space_before = Pt(0)
    hp.paragraph_format.space_after = Pt(3)
    hp.paragraph_format.left_indent = -Inches(100 / 1440)     # out to the cell border
    hp.paragraph_format.right_indent = -Inches(100 / 1440)
    pPr = hp._p.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear'); shd.set(qn('w:color'), 'auto'); shd.set(qn('w:fill'), CALLOUT_HEADER_FILL)
    pPr.append(shd)
    hr = hp.add_run(title.strip())
    hr.bold = True
    hr.font.name = BODY_FONT
    hr.font.size = CALLOUT_FONT_SIZE
    hr.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for text in body_paras:
        para = cell.add_paragraph()
        para.paragraph_format.space_before = Pt(0)
        para.paragraph_format.space_after = Pt(3)
        add_formatted_runs(para, text)
        for run in para.runs:
            run.font.size = CALLOUT_FONT_SIZE


_CALLOUT_OPEN = re.compile(r'^:::\s*callout\b\s*(.*)$')
_CALLOUT_KEY = re.compile(r'^(evidence|align)\s*:\s*(.+)$', re.IGNORECASE)


def parse_callout(lines: list[str], i: int) -> tuple[dict, int]:
    """Parse a `:::callout TITLE` ... `:::` block starting at lines[i].

    Returns ({title, align, evidence, paras}, index of the first line after the
    block). Key lines (`evidence:`, `align:`) are only recognised before the
    first body line. Body paragraphs are blank-line separated; hard-wrapped
    lines inside a paragraph are joined.
    """
    m = _CALLOUT_OPEN.match(lines[i].strip())
    info = {'title': (m.group(1) if m else '').strip(), 'align': 'right',
            'evidence': None, 'paras': []}
    i += 1
    cur: list[str] = []
    in_keys = True
    while i < len(lines) and lines[i].strip() != ':::':
        s = lines[i].strip()
        if in_keys and s:
            km = _CALLOUT_KEY.match(s)
            if km:
                key, val = km.group(1).lower(), km.group(2).strip()
                if key == 'align':
                    info['align'] = 'left' if val.lower() == 'left' else 'right'
                else:
                    info['evidence'] = val
                i += 1
                continue
        if s:
            in_keys = False
            cur.append(s)
        elif cur:
            info['paras'].append(' '.join(cur)); cur = []
        i += 1
    if cur:
        info['paras'].append(' '.join(cur))
    return info, i + 1  # consume the closing fence (or step past EOF if unclosed)


# ── Core converter ────────────────────────────────────────────────────────────

def strip_html_comments(raw: str) -> str:
    """
    Remove HTML comments, but keep `<!-- figure: ... -->` markers, which the
    render loop turns into embedded images.

    An inline comment sitting between two spaces (the common case: an evidence
    marker mid-paragraph) collapses to ONE space. Stripping it naively leaves a
    double space in the rendered document, which the white-glove standard flags
    and which a reader sees as a typo.

    NOTE: the collapse rule must stay single-line. With re.DOTALL, a `.*?` here
    backtracks across newlines whenever a comment is followed by a line break
    instead of a space, swallowing every paragraph up to the next
    space-followed `-->`. Using [^\\n]*? confines the match to one line. That
    bug silently deleted 687 characters from a shipped draft while still
    reporting [OK]; `--selftest` guards it.
    """
    raw = re.sub(r'[ \t]+<!--(?!\s*figure:)[^\n]*?-->[ \t]+', ' ', raw)
    return re.sub(r'<!--(?!\s*figure:).*?-->', '', raw, flags=re.DOTALL)


# ── Soft-wrap joining ─────────────────────────────────────────────────────────
#
# Markdown treats consecutive non-blank lines as ONE paragraph; only a blank line
# starts a new one. Authors here hard-wrap prose at ~95 columns, so without this
# every wrapped line became its own Word paragraph — the reader then had to delete
# at the end of each line to make a paragraph flow. It also broke inline formatting:
# add_formatted_runs' spans cannot cross a newline, so a **bold** phrase split by a
# wrap matched nothing and its asterisks rendered literally into the document.

# Internal metadata lines that are dropped rather than rendered. Hoisted to module
# scope so _starts_new_block treats them as boundaries instead of swallowing them
# into the preceding paragraph.
_SKIP_PATTERNS = (r'^-{3,}$', r'^\*Note', r'^\*\*UNCLASSIFIED\*\*$',
                  r'^\*UNCLASSIFIED\*$', r'^\*DRAFT\b', r'^\*Technical Execution Annex')


def _starts_new_block(line: str) -> bool:
    """True if `line` begins a new markdown block rather than continuing a paragraph."""
    s = line.strip()
    if not s:
        return True
    if re.match(r'^#{1,6} ', s):                      # heading
        return True
    if re.match(r'^[-*] ', s):                        # bullet
        return True
    if re.match(r'^\d+\. ', s):                       # numbered item
        return True
    if s.startswith('> ') or s.startswith('```'):     # quote, code fence
        return True
    if _is_table_line(s):                             # table row
        return True
    if re.match(r'^<!--\s*figure:', s):               # figure marker
        return True
    if s.startswith(':::'):                           # callout fence
        return True
    if any(re.match(p, s) for p in _SKIP_PATTERNS):   # dropped metadata
        return True
    return False


# A continuation line only exists because the line before it hit the wrap column.
# A line ending well short of that column was broken on purpose — an addressee
# block ("For: ...", "From: ...", "Date: ..."), an address, a signature. Joining
# those is as wrong as splitting a paragraph. Drafts here wrap at ~95 columns, so
# anything reaching 60 is treated as having hit the margin.
WRAP_JOIN_MIN = 60


def _is_hard_break(raw: str) -> bool:
    """True if the author forced a line break with markdown's two-space convention."""
    return raw.endswith('  ') and raw.strip() != ''


def _continues(prev_raw: str) -> bool:
    """True if the line after `prev_raw` is a soft-wrap continuation of it."""
    return len(prev_raw.rstrip()) >= WRAP_JOIN_MIN and not _is_hard_break(prev_raw)


def _gather_wrapped(lines: list[str], i: int) -> tuple[str, int]:
    """Join lines[i] with its soft-wrapped continuations.

    Returns (joined text, index of the first line NOT consumed).
    """
    parts = [lines[i].strip()]
    j = i + 1
    while (j < len(lines)
           and not _starts_new_block(lines[j])
           and _continues(lines[j - 1])):
        parts.append(lines[j].strip())
        j += 1
    return ' '.join(parts), j


def convert_md_to_doc(md_path: Path, doc: Document, page_break: bool = False) -> int:
    """
    Parse one markdown file and append its content to doc.
    Returns the number of non-blank lines processed.
    """
    raw = md_path.read_text(encoding="utf-8")
    # Strip YAML frontmatter (--- ... ---) at the start of the file.
    if raw.startswith('---'):
        end = raw.find('\n---', 3)
        if end != -1:
            raw = raw[end + 4:]
    raw = strip_html_comments(raw)
    lines = raw.split('\n')

    if page_break:
        doc.add_page_break()

    line_count = 0
    i = 0
    while i < len(lines):
        raw_line = lines[i]
        s = raw_line.rstrip()
        stripped = s.strip()

        # Blank line
        if not stripped:
            i += 1
            continue

        # Skip internal metadata: horizontal rules, *Note lines, classification
        # markings, and version stamp italic lines at the foot of each document.
        if any(re.match(p, stripped) for p in _SKIP_PATTERNS):
            i += 1
            continue

        # Fenced code block ``` ... ``` — render verbatim in a monospace font
        if stripped.startswith('```'):
            i += 1
            code_lines: list[str] = []
            while i < len(lines) and not lines[i].lstrip().startswith('```'):
                code_lines.append(lines[i])
                line_count += 1
                i += 1
            i += 1  # consume the closing fence (or step past EOF if unclosed)
            process_code_block(doc, code_lines)
            continue

        # H1
        if re.match(r'^# [^#]', stripped):
            doc.add_heading(stripped[2:].strip(), level=1)
            line_count += 1; i += 1; continue

        # H2
        if re.match(r'^## [^#]', stripped):
            doc.add_heading(stripped[3:].strip(), level=2)
            line_count += 1; i += 1; continue

        # H3
        if re.match(r'^### [^#]', stripped):
            doc.add_heading(stripped[4:].strip(), level=3)
            line_count += 1; i += 1; continue

        # H4
        if re.match(r'^#### [^#]', stripped):
            doc.add_heading(stripped[5:].strip(), level=4)
            line_count += 1; i += 1; continue

        # H5
        if re.match(r'^##### [^#]', stripped):
            doc.add_heading(stripped[6:].strip(), level=5)
            line_count += 1; i += 1; continue

        # H6
        if re.match(r'^###### [^#]', stripped):
            doc.add_heading(stripped[7:].strip(), level=6)
            line_count += 1; i += 1; continue

        # Table — collect consecutive table lines
        if _is_table_line(stripped):
            tbl = []
            while i < len(lines) and _is_table_line(lines[i].rstrip()):
                tbl.append(lines[i].rstrip())
                i += 1
            process_table(doc, tbl)
            line_count += len(tbl)
            continue

        # Callout sidebar — :::callout TITLE ... :::
        if _CALLOUT_OPEN.match(stripped):
            info, nxt = parse_callout(lines, i)
            if info['title'] or info['paras']:
                add_callout(doc, info['title'] or 'Proof point', info['paras'], info['align'])
            line_count += nxt - i; i = nxt; continue

        # Figure marker — <!-- figure: NAME --> on its own line
        fig_m = re.match(r'^<!--\s*figure:\s*([A-Za-z0-9._-]+)\s*-->$', stripped)
        if fig_m:
            add_figure(doc, md_path, fig_m.group(1))
            line_count += 1; i += 1; continue

        # Bullet list (- or * prefix, possibly indented)
        bullet_m = re.match(r'^(\s*)[-*] (.+)', s)
        if bullet_m:
            level = _detect_list_indent(s)
            text, nxt = _gather_wrapped(lines, i)
            text = re.sub(r'^\s*[-*]\s+', '', text)
            _add_list_para(doc, text, "List Bullet", level)
            line_count += nxt - i; i = nxt; continue

        # Numbered list (possibly indented). Word's "List Number" style shares one
        # numbering counter across every list in the document, so a second numbered
        # list continues at 4, 5, 6... Emit the markdown's own literal number instead;
        # each list then renders exactly as authored.
        num_m = re.match(r'^(\s*)(\d+)\. (.+)', s)
        if num_m:
            level = _detect_list_indent(s)
            text, nxt = _gather_wrapped(lines, i)
            text = re.sub(r'^\s*\d+\.\s+', '', text)
            para = doc.add_paragraph()
            para.paragraph_format.left_indent = Inches(0.25 * (level + 1))
            add_formatted_runs(para, f"{num_m.group(2)}. {text}")
            line_count += nxt - i; i = nxt; continue

        # Blockquote (> ...) — used for action captions
        if stripped.startswith('> '):
            # Consume every line of the quote, then join — a caption wrapped across
            # three lines is one paragraph, and its inline markers only resolve once
            # the lines are joined.
            qparts = []
            while i < len(lines) and lines[i].strip().startswith('> '):
                qparts.append(lines[i].strip()[2:].strip())
                line_count += 1; i += 1
                # Same margin test as prose: a quote line that stopped short of the
                # wrap column ends the quote's current line on purpose.
                if not _continues(lines[i - 1]):
                    break
            para = doc.add_paragraph()
            para.paragraph_format.left_indent = Inches(0.4)
            para.paragraph_format.space_before = Pt(2)
            para.paragraph_format.space_after = Pt(2)
            para.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
            add_formatted_runs(para, ' '.join(qparts))
            for run in para.runs:          # the whole quote reads as an aside
                run.italic = True
                run.font.size = Pt(10)
            continue

        # Regular paragraph with inline formatting. Consume soft-wrapped
        # continuation lines so the paragraph flows in Word as authored.
        text, nxt = _gather_wrapped(lines, i)
        para = doc.add_paragraph()
        para.paragraph_format.space_before = Pt(0)
        para.paragraph_format.space_after = Pt(6)
        add_formatted_runs(para, text)
        line_count += nxt - i; i = nxt

    return line_count


# ── Discovery ─────────────────────────────────────────────────────────────────

def discover_drafts(drafts_dir: Path) -> list[Path]:
    """
    Return all .md files in drafts_dir sorted alphabetically.
    This matches the naming convention (01-..., 02-..., etc.) used in proposal drafts.
    """
    files = sorted(drafts_dir.glob("*.md"))
    return files


# ── Main ──────────────────────────────────────────────────────────────────────

def selftest() -> int:
    """
    Deterministic, offline guard on strip_html_comments.

    Case 2 is the regression that matters: a comment followed by a newline must
    not swallow the paragraphs that follow it. Expectations are written against
    the *rendered* result, so each case is passed through the same
    `raw_line.rstrip()` the render loop applies — a comment that ends a line
    leaves a trailing space, and that space never reaches the document.
    """
    def rendered(src: str) -> str:
        return '\n'.join(l.rstrip() for l in strip_html_comments(src).split('\n'))

    cases = [
        ("inline marker collapses to one space",
         "A claim. <!-- evidence: EV-001 --> Next.",
         "A claim. Next."),
        ("comment before newline does not eat following paragraphs",
         "Para one. <!-- evidence: EV-001 -->\n\nPara two.\n\nPara three. <!-- x --> end",
         "Para one.\n\nPara two.\n\nPara three. end"),
        ("figure markers survive for the image loop",
         "<!-- figure: fig1.png -->",
         "<!-- figure: fig1.png -->"),
        ("multi-line block comment is stripped whole",
         "Before.\n<!-- PATCH-BLOCKED: multi\nline note -->\nAfter.",
         "Before.\n\nAfter."),
        ("two inline markers in one line",
         "Two <!-- a --> markers <!-- b --> inline.",
         "Two markers inline."),
        ("figure marker survives alongside a stripped comment",
         "Text. <!-- evidence: EV-002 -->\n<!-- figure: fig2.png -->",
         "Text.\n<!-- figure: fig2.png -->"),
    ]

    failures = []
    for label, src, want in cases:
        got = rendered(src)
        status = "ok " if got == want else "FAIL"
        print(f"  [{status}] {label}")
        if got != want:
            failures.append((label, src, got, want))

    for label, src, got, want in failures:
        print(f"\n  {label}\n    in  : {src!r}\n    got : {got!r}\n    want: {want!r}")

    failures += _selftest_softwrap()
    failures += _selftest_callout()

    print("selftest:", "PASS" if not failures else "FAIL")
    return 0 if not failures else 1


def _selftest_softwrap() -> list:
    """Guard the soft-wrap join.

    Drafts here are hard-wrapped at ~95 columns. Before this join every wrapped
    line became its own Word paragraph, so prose arrived in Word as a column of
    short lines the reader had to repair by hand — and any inline span split by a
    wrap (**bold** most often) failed to match and leaked its asterisks into the
    document. Both symptoms have one cause, so both are asserted here.
    """
    import tempfile
    from docx import Document as _Doc

    # Lines are written at the ~95-column width the drafts actually use, because
    # the join is decided by whether a line reached the wrap column.
    src = (
        "For: Scott Shaul, MASS Group\n"
        "From: Bill Bal, EdgeRunner AI\n"
        "Date: 17 August 2026\n"
        "\n"
        "Drop-in blocks keyed to the current draft. Blocks A-C sit in Section 5 of the paper, and\n"
        "Block D appends to Section 6.\n"
        "\n"
        "The score updates as the floor runs, closing the gap between a self-assessed MRL 5-6 and a\n"
        "**structurally evident MRL 7** that a program office can audit.\n"
        "\n"
        "- A bullet long enough to reach the wrap column and therefore continue onto a second\n"
        "  source line without starting anything new.\n"
        "- A short bullet.\n"
        "\n"
        "> *Figure 1. One platform advances all four readiness clocks from a single capture.* The\n"
        "> evidence is a byproduct of the same digital work execution that runs the floor.\n"
    )

    with tempfile.TemporaryDirectory() as td:
        md = Path(td) / "s.md"
        md.write_text(src, encoding="utf-8")
        doc = _Doc()
        setup_document(doc)
        convert_md_to_doc(md, doc)
        paras = [p for p in doc.paragraphs if p.text.strip()]
        joined = " ".join(p.text for p in paras)

    checks = [
        ("wrapped paragraph becomes one paragraph",
         "Section 5 of the paper, and Block D appends to Section 6." in joined),
        ("short deliberate lines stay separate",
         any(p.text.strip() == "For: Scott Shaul, MASS Group" for p in paras)
         and any(p.text.strip() == "Date: 17 August 2026" for p in paras)),
        ("wrapped bullet becomes one list item",
         any("wrap column and therefore continue onto a second source line" in p.text
             for p in paras)),
        ("bullet count is not inflated by wrapping",
         sum(1 for p in paras if p.style.name == "List Bullet") == 2),
        ("bold split across a wrap resolves to a bold run",
         any(r.bold and "structurally evident" in r.text for p in paras for r in p.runs)),
        ("no literal markdown reaches the document",
         "**" not in joined and "*Figure" not in joined),
        ("wrapped blockquote becomes one italic paragraph",
         any("single capture. The evidence is a byproduct" in p.text
             and all(r.italic for r in p.runs) for p in paras)),
    ]

    failures = []
    for label, passed in checks:
        print(f"  [{'ok ' if passed else 'FAIL'}] {label}")
        if not passed:
            failures.append((label, "<soft-wrap sample>", "see above", "joined output"))
    return failures


def _selftest_callout() -> list:
    """Guard the callout sidebar: parsed, rendered as a tagged floating table, keys
    not rendered as body, following paragraph still present to wrap around it."""
    import tempfile
    from docx import Document as _Doc
    from register import is_callout_table

    src = (
        "## 2.1 Architecture\n"
        "\n"
        ":::callout Architecture at Kessel Run\n"
        "evidence: EV-045\n"
        "align: left\n"
        "EdgeRunner AI currently leads platform operations for **22 clusters** across three\n"
        "regions that handle more than 1 billion transactions per month.\n"
        "\n"
        "A second paragraph in the box.\n"
        ":::\n"
        "\n"
        "Body paragraph that should wrap around the box and remain in the document as prose.\n"
    )
    with tempfile.TemporaryDirectory() as td:
        md = Path(td) / "c.md"
        md.write_text(src, encoding="utf-8")
        doc = _Doc()
        setup_document(doc)
        convert_md_to_doc(md, doc)
        tables = doc.tables
        t = tables[0] if tables else None
        cell_paras = [p.text for p in t.rows[0].cells[0].paragraphs] if t else []
        cell_texts = [cell_paras[0], " ".join(cell_paras[1:])] if cell_paras else []
        body_text = " ".join(p.text for p in doc.paragraphs)
        tblPr = t._tbl.tblPr if t else None
        pPr = tblPr.find(qn('w:tblpPr')) if tblPr is not None else None

    checks = [
        ("one callout table emitted", len(tables) == 1),
        ("table is tagged as a callout", t is not None and is_callout_table(t)),
        ("header row carries the title", bool(cell_texts) and cell_texts[0] == "Architecture at Kessel Run"),
        ("key lines are not rendered", not any("evidence:" in c or "align:" in c for c in cell_texts)),
        ("wrapped body joins and bold resolves",
         len(cell_texts) > 1 and "22 clusters across three regions" in cell_texts[1] and "**" not in cell_texts[1]),
        ("two body paragraphs kept", t is not None and len(cell_paras) == 3),
        ("single row so the box can never split", t is not None and len(t.rows) == 1),
        ("table floats with text wrap", pPr is not None and pPr.get(qn('w:tblpXSpec')) == 'left'),
        ("following prose survives outside the box", "wrap around the box" in body_text),
    ]
    failures = []
    for label, passed in checks:
        print(f"  [{'ok ' if passed else 'FAIL'}] {label}")
        if not passed:
            failures.append((label, "<callout sample>", "see above", "callout"))
    return failures


def main():
    parser = argparse.ArgumentParser(
        description="Convert proposal markdown drafts to Word .docx files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--proposal",
                        help="Proposal slug (directory name under proposals/)")
    parser.add_argument("--selftest", action="store_true",
                        help="run deterministic offline self-test on comment stripping")
    parser.add_argument("--mode", choices=["individual", "combined", "both"],
                        default="both",
                        help="Output mode (default: both)")
    parser.add_argument("--combined-name", default="full-proposal-combined",
                        help="Stem for the combined .docx file (default: full-proposal-combined)")
    parser.add_argument("--files", nargs="+", metavar="FILE",
                        help="Explicit ordered file list (names relative to drafts/). "
                             "Overrides auto-discovery.")
    parser.add_argument("--workspace", default=None,
                        help="Path to federal-proposal-assistant root. "
                             "Defaults to the parent of the tools/ directory.")
    args = parser.parse_args()

    if args.selftest:
        return selftest()
    if not args.proposal:
        parser.error("--proposal is required (or use --selftest)")

    # Resolve paths
    workspace = Path(args.workspace) if args.workspace else WORKSPACE_ROOT
    proposal_dir = workspace / "proposals" / args.proposal
    drafts_dir = proposal_dir / "drafts"
    out_dir = proposal_dir / "final" / "docx"

    if not proposal_dir.exists():
        print(f"ERROR: Proposal directory not found: {proposal_dir}", file=sys.stderr)
        sys.exit(1)
    if not drafts_dir.exists():
        print(f"ERROR: drafts/ directory not found at {drafts_dir}", file=sys.stderr)
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    # Determine which files to convert
    if args.files:
        md_files = [drafts_dir / f for f in args.files]
        missing = [f for f in md_files if not f.exists()]
        if missing:
            for m in missing:
                print(f"ERROR: File not found: {m}", file=sys.stderr)
            sys.exit(1)
    else:
        md_files = discover_drafts(drafts_dir)
        if not md_files:
            print(f"ERROR: No .md files found in {drafts_dir}", file=sys.stderr)
            sys.exit(1)

    print(f"Proposal : {args.proposal}")
    print(f"Drafts   : {drafts_dir}")
    print(f"Output   : {out_dir}")
    print(f"Mode     : {args.mode}")
    print(f"Files    : {[f.name for f in md_files]}")
    print()

    outputs = []

    # ── Individual files ──────────────────────────────────────────────────────
    if args.mode in ("individual", "both"):
        for md_path in md_files:
            doc = Document()
            setup_document(doc)
            n = convert_md_to_doc(md_path, doc)
            out_path = out_dir / (md_path.stem + ".docx")
            doc.save(out_path)
            outputs.append(out_path)
            print(f"  [OK] {out_path.name}  ({n} lines)")

    # ── Combined document ─────────────────────────────────────────────────────
    if args.mode in ("combined", "both"):
        doc2 = Document()
        setup_document(doc2)
        total = 0
        for idx, md_path in enumerate(md_files):
            n = convert_md_to_doc(md_path, doc2, page_break=(idx > 0))
            total += n
        out_path2 = out_dir / f"{args.combined_name}.docx"
        doc2.save(out_path2)
        outputs.append(out_path2)
        print(f"  [OK] {out_path2.name}  ({total} lines total, {len(md_files)} sections)")

    print()
    print(f"Done — {len(outputs)} file(s) written to {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
