#!/usr/bin/env python3
"""
polish_docx.py - post-export polish for proposal Word documents.

Runs after tools/md_to_docx.py. For every .docx in a proposal's final/docx/:
  1. Optimizes table column widths - narrow short-content columns, widen wordy
     ones - instead of the converter's even split.
  2. White-glove table behavior: header row repeats across page breaks, rows
     never split mid-cell across pages, cell paragraph spacing tightened.
  3. Normalizes page margins to 1" (6.5" usable width on Letter).
  4. Adds a running header (the document's first H1 title, pages 2+).
  5. Adds a footer with the company name and a "Page X of Y" field (all pages).

Items 1-3 are also applied automatically by scripts/render-md-to-docx.py on
every .md -> .docx render (the standard white-glove rendering process); this
script remains the full-polish entry point for export (final/docx/), where the
header/footer treatment is added on top.

Usage:
  python tools/polish_docx.py --proposal <slug> [--company "EdgeRunner AI, Inc."]
  python tools/polish_docx.py --files path/to/a.docx path/to/b.docx
  python tools/polish_docx.py --files a.docx --tables-only   # skip header/footer
  python tools/polish_docx.py --files a.docx --register assertive

Register (2026-09-04, tools/register.py): --proposal reads working/proposal-type.md
and resolves the register from type_id; --register overrides. In the `strict`
register (white papers, briefs, RFIs; the default) every run is blackened and every
bold run inside a sentence is cleared, exactly as adopted 2026-09-02. In the
`assertive` register (far-rfp, ota-proposal, cso-full and the other scored
volumes) one short bold key phrase per paragraph is kept. In both registers the
callout sidebar tables emitted by md_to_docx.py keep their width, float, and
white-on-dark header - they are the proof-point boxes, not body text.

Idempotent: re-running re-applies the same polish. If you re-export from
markdown, re-run this script - the export step does not preserve it.
"""
import argparse, glob, os, sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from register import is_callout_table, resolve_register, STRICT, ASSERTIVE  # noqa: E402

# assertive register: a bold run inside a sentence survives if it is this short and
# it is the only one in the paragraph. Longer or repeated bold is still cleared.
KEY_PHRASE_MAX_WORDS = 6

USABLE_WIDTH = 6.5   # inches: 8.5" Letter minus 1" margins each side
MIN_COL = 0.5        # inches: minimum column width
WEIGHT_CAP = 40      # cap per-column weight so one very long column cannot
                     # starve the medium-content columns next to it


def optimize_table(table):
    ncols = len(table.columns)
    if ncols == 0:
        return
    maxlen = [1] * ncols
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < ncols:
                maxlen[i] = max(maxlen[i], len(cell.text.strip()))
    weights = [min(m, WEIGHT_CAP) for m in maxlen]
    total = float(sum(weights))
    widths = [USABLE_WIDTH * w / total for w in weights]
    # clamp to minimum, redistribute the deficit across the roomier columns
    deficit = 0.0
    free = []
    for i, w in enumerate(widths):
        if w < MIN_COL:
            deficit += MIN_COL - w
            widths[i] = MIN_COL
        else:
            free.append(i)
    if deficit > 0 and free:
        freetotal = sum(widths[i] for i in free)
        for i in free:
            widths[i] -= deficit * widths[i] / freetotal

    table.autofit = False
    tbl = table._tbl
    tblPr = tbl.tblPr
    layout = tblPr.find(qn('w:tblLayout'))
    if layout is None:
        layout = OxmlElement('w:tblLayout')
        tblPr.append(layout)
    layout.set(qn('w:type'), 'fixed')

    # set the table grid columns
    grid = tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for i, gridCol in enumerate(grid.findall(qn('w:gridCol'))):
            if i < ncols:
                gridCol.set(qn('w:w'), str(int(widths[i] * 1440)))
    # set every cell width so Word honors the fixed layout
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < ncols:
                cell.width = Inches(widths[i])
    return widths


def whiteglove_table(table):
    """Header row repeats on page breaks; rows never split; tight cell spacing."""
    if len(table.rows) > 1 and len(table.columns) > 1:
        trPr = table.rows[0]._tr.get_or_add_trPr()
        if trPr.find(qn('w:tblHeader')) is None:
            el = OxmlElement('w:tblHeader')
            el.set(qn('w:val'), 'true')
            trPr.append(el)
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        if trPr.find(qn('w:cantSplit')) is None:
            trPr.append(OxmlElement('w:cantSplit'))
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)


def set_margins(doc, inches=1.0):
    for section in doc.sections:
        section.left_margin = Inches(inches)
        section.right_margin = Inches(inches)
        section.top_margin = Inches(inches)
        section.bottom_margin = Inches(inches)


def _all_paragraphs(doc, skip_callouts=False):
    """Every paragraph in the document, including those inside table cells.
    With skip_callouts, the sidebar tables from md_to_docx.py are left out."""
    for p in doc.paragraphs:
        yield p
    for t in doc.tables:
        if skip_callouts and is_callout_table(t):
            continue
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    yield p


def blacken_text(doc):
    """Force every run to automatic (black) text.

    Coloured headings — the blue Word applies to Heading 1/2/3 by default — read as a
    machine-generated document to a government reviewer. Adopted 2026-09-02 on Bill's
    direction. Applied to runs AND to the underlying styles, because a run that inherits
    its colour from a style has no run-level colour to clear.

    Callout sidebars are exempt in every register: their white title on the dark
    header bar is the box's whole design, and blackening it makes the title vanish.
    """
    n = 0
    for p in _all_paragraphs(doc, skip_callouts=True):
        for r in p.runs:
            if r.font.color is not None and r.font.color.rgb is not None:
                r.font.color.rgb = RGBColor(0, 0, 0)
                n += 1
    for st in doc.styles:
        try:
            if st.font is not None and st.font.color is not None and st.font.color.rgb is not None:
                st.font.color.rgb = RGBColor(0, 0, 0)
                n += 1
        except (AttributeError, NotImplementedError, ValueError):
            continue
    return n


def unbold_midsentence(doc, register=STRICT):
    """Strip bold from runs that are not leading a paragraph or a list item.

    Bold is for a topic label, a heading, or the lead-in of a bullet. Bold applied to a
    word or clause inside a sentence for emphasis is a well-known tell of machine-written
    prose, and a government reviewer reads it that way. Adopted 2026-09-02 on Bill's
    direction.

    A run is treated as a LEAD-IN, and keeps its bold, while every run from the start of
    the paragraph so far has been bold or whitespace. The first non-bold run with real
    text ends the lead-in; every bold run after that point is cleared.
    Headings are left alone entirely.

    In the `assertive` register (scored volumes; the VAULT convention) ONE bold run of
    at most KEY_PHRASE_MAX_WORDS words per paragraph is kept after the lead-in as a
    scanning device; a second bold run, or a longer one, is still cleared.
    """
    cleared = 0
    allowance = 1 if register == ASSERTIVE else 0
    for p in _all_paragraphs(doc):
        style = (p.style.name or '') if p.style else ''
        if style.startswith('Heading') or style in ('Title', 'Subtitle'):
            continue
        in_leadin = True
        kept = 0
        for r in p.runs:
            has_text = bool(r.text.strip())
            if in_leadin:
                if not has_text:
                    continue          # whitespace does not end the lead-in
                if r.bold:
                    continue          # still inside the lead-in label
                in_leadin = False     # first unbolded words: the sentence has begun
                continue
            if r.bold:
                if kept < allowance and len(r.text.split()) <= KEY_PHRASE_MAX_WORDS:
                    kept += 1
                    continue
                r.bold = False
                cleared += 1
    return cleared


def whiteglove(doc, register=STRICT):
    """The standard white-glove pass applied to every rendered .docx:
    content-proportional column widths, repeating headers, unsplit rows,
    tight cell spacing, 1-inch margins, all-black text, no mid-sentence bold
    (one short key phrase allowed in the assertive register).
    Callout sidebars keep their own width, float, and colours.
    No header/footer (export adds that)."""
    set_margins(doc)
    for table in doc.tables:
        if is_callout_table(table):
            continue
        optimize_table(table)
        whiteglove_table(table)
    blacken_text(doc)
    unbold_midsentence(doc, register)
    return len(doc.tables)


def _page_field(paragraph, instr):
    run = paragraph.add_run()
    b = OxmlElement('w:fldChar'); b.set(qn('w:fldCharType'), 'begin')
    t = OxmlElement('w:instrText'); t.set(qn('xml:space'), 'preserve'); t.text = instr
    e = OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'), 'end')
    run._r.append(b); run._r.append(t); run._r.append(e)
    run.font.size = Pt(9)
    return run


def first_title(doc):
    for p in doc.paragraphs:
        sn = (p.style.name or '') if p.style else ''
        if sn.startswith('Heading 1') or sn == 'Title':
            if p.text.strip():
                return p.text.strip()
    for p in doc.paragraphs:
        if p.text.strip():
            return p.text.strip()
    return ''


def style_runs(paragraph, size=9, grey=True):
    for r in paragraph.runs:
        r.font.size = Pt(size)
        if grey:
            r.font.color.rgb = RGBColor(0x60, 0x60, 0x60)


def add_header_footer(doc, company):
    title = first_title(doc)
    for section in doc.sections:
        section.different_first_page_header_footer = True

        # header on pages 2+ only (page 1 already shows the H1 title)
        hp = section.header.paragraphs[0]
        hp.text = title
        hp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        style_runs(hp)
        section.first_page_header.paragraphs[0].text = ''

        # footer on every page: company name, then Page X of Y
        for fp in (section.footer.paragraphs[0],
                   section.first_page_footer.paragraphs[0]):
            fp.text = ''
            fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = fp.add_run(company + '      |      Page ')
            run.font.size = Pt(9)
            run.font.color.rgb = RGBColor(0x60, 0x60, 0x60)
            _page_field(fp, 'PAGE')
            of = fp.add_run(' of ')
            of.font.size = Pt(9)
            of.font.color.rgb = RGBColor(0x60, 0x60, 0x60)
            _page_field(fp, 'NUMPAGES')


def polish(path, company, tables_only=False, register=STRICT):
    doc = Document(path)
    ntables = whiteglove(doc, register)
    if not tables_only:
        add_header_footer(doc, company)
    doc.save(path)
    suffix = 'white-glove' if tables_only else 'white-glove + header/footer'
    print(f'  [OK] {os.path.basename(path)} - {ntables} table(s), {suffix}, {register} register')


def selftest():
    """Callout sidebars survive the pass; the assertive allowance keeps exactly one
    short bold phrase; the strict register clears every mid-sentence bold."""
    import tempfile
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from md_to_docx import add_callout, setup_document, TEXT_WIDTH_INCHES, CALLOUT_WIDTH_FRACTION
    fails = 0

    def check(label, ok):
        nonlocal fails
        fails += 0 if ok else 1
        print(f"  [{'ok ' if ok else 'FAIL'}] {label}")

    def build():
        d = Document(); setup_document(d)
        d.add_paragraph('Intro paragraph.')
        add_callout(d, 'Architecture at Kessel Run', ['Body with **22 clusters** inside.'])
        p = d.add_paragraph('Lead-in: ')
        p.runs[0].bold = True
        p.add_run('prose with ')
        r1 = p.add_run('one key phrase'); r1.bold = True
        p.add_run(' and ')
        r2 = p.add_run('a second bold phrase'); r2.bold = True
        p.add_run(' and ')
        r3 = p.add_run('a bold run that is far too long to be a key phrase at all'); r3.bold = True
        p.add_run('.')
        return d, p

    with tempfile.TemporaryDirectory() as td:
        for reg, want_bold in ((STRICT, 0), (ASSERTIVE, 1)):
            d, p = build()
            whiteglove(d, reg)
            t = d.tables[0]
            head = t.rows[0].cells[0].paragraphs[0].runs[0]   # header paragraph of the single cell
            check(f'{reg}: callout header stays white', str(head.font.color.rgb) == 'FFFFFF')
            check(f'{reg}: callout width untouched',
                  abs(t.rows[0].cells[0].width.inches - TEXT_WIDTH_INCHES * CALLOUT_WIDTH_FRACTION) < 0.01)
            check(f'{reg}: callout still floats', t._tbl.tblPr.find(qn('w:tblpPr')) is not None)
            mid = [r for r in p.runs[1:] if r.bold]
            check(f'{reg}: {want_bold} mid-sentence bold run(s) kept', len(mid) == want_bold)
            check(f'{reg}: lead-in keeps bold', p.runs[0].bold is True)
            if reg == ASSERTIVE:
                check('assertive: the kept phrase is the first short one', mid and mid[0].text == 'one key phrase')
    print('selftest:', 'PASS' if fails == 0 else f'FAIL ({fails})')
    return 0 if fails == 0 else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--proposal')
    ap.add_argument('--files', nargs='*')
    ap.add_argument('--company', default='EdgeRunner AI, Inc.')
    ap.add_argument('--tables-only', action='store_true',
                    help='apply the white-glove table/margin pass only (no header/footer)')
    ap.add_argument('--register', choices=[STRICT, ASSERTIVE],
                    help='formatting register; defaults from --proposal type_id, else strict')
    ap.add_argument('--selftest', action='store_true')
    args = ap.parse_args()

    if args.selftest:
        sys.exit(selftest())
    register = resolve_register(register=args.register, proposal=args.proposal)

    if args.files:
        targets = args.files
    elif args.proposal:
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        targets = sorted(glob.glob(os.path.join(
            root, 'proposals', args.proposal, 'final', 'docx', '*.docx')))
    else:
        ap.error('pass --proposal <slug> or --files <paths>')

    if not targets:
        print('No .docx files found.'); sys.exit(1)
    print(f'Polishing {len(targets)} document(s):')
    for t in targets:
        polish(t, args.company, tables_only=args.tables_only, register=register)
    print('Done.')


if __name__ == '__main__':
    main()
