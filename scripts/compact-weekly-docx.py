#!/usr/bin/env python3
"""Compact pass for the weekly growth update .docx.

The shared render-md-to-docx.py styling is proposal-grade (roomy); the weekly
growth update wants density — exec brief in ~2 pages. This pass tightens the
whole document in place: 10pt body, single line spacing, small paragraph gaps,
tighter headings, 9.5pt table text.

Usage: python scripts/compact-weekly-docx.py <path.docx>
"""
import sys
import docx
from docx.shared import Pt


def tighten_paragraph(p, size=None):
    pf = p.paragraph_format
    pf.line_spacing = 1.0
    pf.space_after = Pt(2)
    pf.space_before = Pt(0)
    if size is not None:
        for run in p.runs:
            run.font.size = size


def main(path):
    d = docx.Document(path)

    normal = d.styles['Normal']
    normal.font.size = Pt(9.5)
    normal.paragraph_format.line_spacing = 1.0
    normal.paragraph_format.space_after = Pt(2)

    for name, size, before in [('Heading 1', 13, 4), ('Heading 2', 11.5, 6), ('Heading 3', 10.5, 4)]:
        try:
            st = d.styles[name]
            st.font.size = Pt(size)
            st.paragraph_format.space_before = Pt(before)
            st.paragraph_format.space_after = Pt(2)
            st.paragraph_format.line_spacing = 1.0
        except KeyError:
            pass

    # Direct formatting wins over styles, so walk everything.
    for p in d.paragraphs:
        style = (p.style.name or '')
        if not style.startswith('Heading'):
            tighten_paragraph(p, Pt(9.5))
        else:
            tighten_paragraph(p)

    for table in d.tables:
        for row in table.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    tighten_paragraph(p, Pt(9.5))

    d.save(path)
    print(f'compacted: {path}')


if __name__ == '__main__':
    main(sys.argv[1])
