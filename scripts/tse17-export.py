#!/usr/bin/env python
"""
TSE17 Capabilities Overview exporter.

Renders proposals/<slug>/drafts/capabilities-overview.md to a submission-shaped
.docx at the TSE17-mandated Calibri 12pt, with the title page on its own page and
the 2-page body following. Strips authoring markers (HTML comments, the
"# TITLE PAGE"/"# PAGE 1"/"# PAGE 2" heading lines, and standalone `---` rules).

If Microsoft Word is available (pywin32), reports the AUTHORITATIVE page count of
the body via Word's own pagination and emits a PDF. The page limit excludes the
title page, so the compliant target is: title page (1) + body (<= 2) = <= 3 pages total.

Usage:
    python scripts/tse17-export.py --proposal tes17-aa-cognitive-partner
    python scripts/tse17-export.py --proposal <slug> --margins 1.0
"""
import argparse
import sys
import tempfile
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(WORKSPACE_ROOT / "tools"))

import md_to_docx as M  # noqa: E402
from docx import Document  # noqa: E402
from docx.shared import Pt, Inches  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402


def clean_lines(md_text: str):
    """Drop HTML comments, the TITLE/PAGE marker headings, and bare --- rules.
    Return (title_md, body_md) split at the first '# PAGE 1' marker."""
    out, in_comment = [], False
    for ln in md_text.splitlines():
        s = ln.strip()
        if s.startswith("<!--"):
            in_comment = True
        if in_comment:
            if "-->" in s:
                in_comment = False
            continue
        if s.startswith("# TITLE PAGE"):
            continue            # drop the meta heading, keep the title lines below it
        if s.replace("*", "").strip().upper() == "UNCLASSIFIED":
            continue            # marking is injected programmatically (see render); avoid duplication
        if s == "---":
            continue            # drop horizontal rules (we control page breaks)
        out.append(ln)

    # Split title vs body at the first PAGE marker
    title, body, seen_body = [], [], False
    for ln in out:
        if ln.strip().startswith("# PAGE "):
            seen_body = True
            continue            # drop the PAGE marker headings
        (body if seen_body else title).append(ln)
    return "\n".join(title).strip() + "\n", "\n".join(body).strip() + "\n"


def render(slug: str, margin_in: float):
    M.BODY_FONT = "Calibri"
    M.BODY_SIZE = Pt(12)
    M.MARGIN_TOP = M.MARGIN_BOTTOM = Inches(margin_in)
    M.MARGIN_LEFT = M.MARGIN_RIGHT = Inches(margin_in)

    proposal = WORKSPACE_ROOT / "proposals" / slug
    src = proposal / "drafts" / "capabilities-overview.md"
    out_dir = proposal / "final" / "docx"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_docx = out_dir / "capabilities-overview.docx"

    title_md, body_md = clean_lines(src.read_text(encoding="utf-8"))

    doc = Document()
    M.setup_document(doc)
    with tempfile.TemporaryDirectory() as td:
        tp, bp = Path(td) / "t.md", Path(td) / "b.md"
        tp.write_text(title_md, encoding="utf-8")
        bp.write_text(body_md, encoding="utf-8")
        M.convert_md_to_doc(tp, doc, page_break=False)
        M.convert_md_to_doc(bp, doc, page_break=True)   # body starts on page 2
    # Inject the classification marking as the first body paragraph (visible on the
    # title page and detectable by the structural lint, which scans doc.paragraphs).
    first = doc.paragraphs[0]
    mark = first.insert_paragraph_before("UNCLASSIFIED")
    mark.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in mark.runs:
        run.font.name = "Calibri"; run.font.size = Pt(12); run.font.bold = True

    tighten(doc)
    add_markings(doc, "UNCLASSIFIED")          # header + footer on every page
    doc.save(out_docx)
    return out_docx


def add_markings(doc, text):
    """Centered classification marking in the header and footer of every page."""
    for section in doc.sections:
        for region in (section.header, section.footer):
            region.is_linked_to_previous = False
            p = region.paragraphs[0]
            p.text = text
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in p.runs:
                run.font.name = "Calibri"
                run.font.size = Pt(10)
                run.font.bold = True


def tighten(doc):
    """Compact, still-readable spacing. TSE17 mandates Calibri 12pt + a 2-page
    limit but specifies no line/paragraph spacing — single-spaced with minimal
    inter-paragraph space is standard and lets us keep every Significant Strength."""
    for p in doc.paragraphs:
        pf = p.paragraph_format
        pf.line_spacing = 1.0
        style_name = (p.style.name or "")
        if style_name.startswith("Heading"):
            pf.space_before = Pt(3)
            pf.space_after = Pt(1)
        else:
            pf.space_before = Pt(0)
            pf.space_after = Pt(1)


def word_paginate(docx_path: Path):
    """Return (total_pages, pdf_path) using Word, or (None, None) if unavailable."""
    try:
        import win32com.client as win32
    except Exception as e:
        print(f"  (pywin32 unavailable: {e})")
        return None, None
    word = None
    try:
        word = win32.Dispatch("Word.Application")
        word.Visible = False
        d = word.Documents.Open(str(docx_path))
        d.Repaginate()
        pages = int(d.ComputeStatistics(2))  # wdStatisticPages
        pdf_path = docx_path.with_suffix(".pdf")
        d.SaveAs(str(pdf_path), FileFormat=17)  # wdFormatPDF
        d.Close(False)
        return pages, pdf_path
    except Exception as e:
        print(f"  (Word automation failed: {e})")
        return None, None
    finally:
        if word is not None:
            word.Quit()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--proposal", required=True)
    ap.add_argument("--margins", type=float, default=1.0,
                    help="Margins in inches, all sides (default 1.0).")
    a = ap.parse_args()

    out_docx = render(a.proposal, a.margins)
    print(f"  [OK] {out_docx.relative_to(WORKSPACE_ROOT)}  (Calibri 12pt, {a.margins}\" margins)")

    pages, pdf = word_paginate(out_docx)
    if pages is not None:
        body_pages = pages - 1  # page 1 is the (uncounted) title page
        verdict = "PASS" if body_pages <= 2 else "OVER LIMIT"
        print(f"  Total pages (incl. title): {pages}  ->  body pages: {body_pages}  [{verdict}]")
        if pdf:
            print(f"  [OK] {pdf.relative_to(WORKSPACE_ROOT)}")
    else:
        print("  Page count not verified (open the .docx in Word to confirm <=2 body pages).")


if __name__ == "__main__":
    main()
