#!/usr/bin/env python3
"""
lint-rendered-artifact.py — format checks on the .docx that will actually be reviewed or
submitted. Everything here is deterministic and was found late and by accident on the
NAVWAR GenAI EPSS pursuit (Aug–Sep 2026): a 20-page render caused by table column widths,
figure labels at 7.5pt, blue headings, mid-sentence bold, four space-before-period artifacts,
and an 11pt body against a 12pt instruction.

This is the "late formatting editor" — as a script, because every check is mechanical.
lint-submission-file.py owns prose HIGH rules and placeholders on the final upload; this
owns layout and typography on every rendered copy, review or final.

Checks (HIGH blocks; ADVISORY reports):
  page-count      HIGH      pages exceed --pages (title page excluded with --exclude-title)
  font-size       HIGH      Normal style or any body run below --font-pt
  text-colour     HIGH      any run with a non-black explicit colour
  mid-bold        HIGH      bold inside a sentence (not a heading / label / bullet lead-in)
  orphan-punct    HIGH      space before . , ; (renderer stripped a comment and left the gap)
  placeholder     HIGH      bracketed placeholder shipped (delegates to lint-submission-file)
  figure-legib    HIGH<7pt  smallest label (24px convention) renders below the floor
                  ADV <9pt
  table-widths    ADVISORY  a column's width share is far below its content share
  title-break     ADVISORY  --exclude-title but no page break before the first heading

Page count uses Word COM when pywin32 is present; otherwise an ESTIMATE from word count
(clearly labelled) so the gate still runs on machines without Word.

Usage:
  python scripts/lint-rendered-artifact.py drafts/brief.docx --pages 5 --font-pt 12 --exclude-title
  python scripts/lint-rendered-artifact.py --selftest

Exit codes: 0 clean, 1 HIGH findings, 2 harness error.
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import re
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

try:
    import docx  # python-docx
    from docx.shared import Pt
    from docx.oxml.ns import qn
except ImportError:
    print("lint-rendered-artifact: python-docx not installed", file=sys.stderr)
    sys.exit(2)

# Figure convention from the graphics brief: the smallest label is 24px on a 1200px-wide
# logical canvas, i.e. 2% of canvas width, and it must render at >= 9pt when embedded.
# Expressed as a FRACTION, not pixels, because figures are rasterized at 2x for print and
# the PNG's pixel width is then 2400 while the label is still 2% of it. 7pt is unreadable.
MIN_LABEL_FRACTION = 24 / 1200
FIGURE_FLOOR_PT = 9.0
FIGURE_HARD_PT = 7.0
WORDS_PER_PAGE_ESTIMATE = 480   # 12pt single-spaced, 1" margins, with headings

Finding = tuple[str, str, str]   # (severity, rule, detail)


# ---------------------------------------------------------------- helpers
def _placeholder_finder():
    """Reuse lint-submission-file's bracket scanner; the filename has a hyphen, so load by path."""
    p = REPO_ROOT / "scripts" / "lint-submission-file.py"
    spec = importlib.util.spec_from_file_location("lint_submission_file", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod.find_bracket_placeholders


def _all_paragraphs(d):
    for p in d.paragraphs:
        yield p
    for t in d.tables:
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    yield p


def _is_heading(p) -> bool:
    st = (p.style.name or "") if p.style else ""
    return st.startswith("Heading") or st in ("Title", "Subtitle")


def _page_count(path: Path) -> tuple[int | None, str]:
    """(pages, source). Word COM if available, else None."""
    try:
        import win32com.client  # type: ignore
    except ImportError:
        return None, "estimate"
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(str(path.resolve()), False, True)
        pages = int(doc.ComputeStatistics(2))
        doc.Close(False)
        word.Quit()
        return pages, "word"
    except Exception as exc:  # COM present but Word failed
        return None, f"estimate (Word COM failed: {exc.__class__.__name__})"


# ---------------------------------------------------------------- checks
def lint(path: Path, pages: int | None, font_pt: float | None,
         exclude_title: bool) -> list[Finding]:
    d = docx.Document(str(path))
    F: list[Finding] = []
    find_ph = _placeholder_finder()

    body_paras = [p for p in _all_paragraphs(d) if p.text.strip()]

    # --- font size ---
    if font_pt:
        normal = d.styles["Normal"].font.size
        if normal is not None and normal.pt < font_pt:
            F.append(("HIGH", "font-size",
                      f"Normal style is {normal.pt:g}pt; instruction is {font_pt:g}pt"))
        small = 0
        for p in body_paras:
            if _is_heading(p):
                continue
            for r in p.runs:
                if r.font.size is not None and r.font.size.pt < font_pt and r.text.strip():
                    small += 1
        if small:
            F.append(("HIGH", "font-size",
                      f"{small} body run(s) carry an explicit size below {font_pt:g}pt"))

    # --- colour, mid-sentence bold, orphan punctuation, placeholders ---
    coloured = midbold = 0
    orphan: list[str] = []
    for p in body_paras:
        txt = p.text
        for r in p.runs:
            c = r.font.color
            if c is not None and c.rgb is not None and str(c.rgb) != "000000":
                coloured += 1
        if not _is_heading(p):
            lead = True
            for r in p.runs:
                if not r.text.strip():
                    continue
                if lead:
                    if r.bold:
                        continue
                    lead = False
                    continue
                if r.bold:
                    midbold += 1
        for m in re.finditer(r"\S \s*[.,;]", txt):
            orphan.append(txt[max(0, m.start() - 25):m.end() + 5].strip())
        for s, e in find_ph(txt):
            F.append(("HIGH", "placeholder", txt[max(0, s - 20):e + 20].strip()))
    if coloured:
        F.append(("HIGH", "text-colour", f"{coloured} run(s) with a non-black colour (blue headings read as machine-written)"))
    if midbold:
        F.append(("HIGH", "mid-bold", f"{midbold} bold run(s) inside a sentence; bold is for labels and lead-ins only"))
    for o in orphan[:6]:
        F.append(("HIGH", "orphan-punct", f"...{o}"))
    if len(orphan) > 6:
        F.append(("HIGH", "orphan-punct", f"...and {len(orphan) - 6} more"))

    # --- figure legibility ---
    try:
        from PIL import Image
        for i, shp in enumerate(d.inline_shapes, 1):
            w_in = shp.width.inches
            try:
                rid = shp._inline.graphic.graphicData.pic.blipFill.blip.embed
                part = d.part.related_parts[rid]
                px_w = Image.open(io.BytesIO(part.blob)).size[0]
            except Exception:
                continue
            label_pt = MIN_LABEL_FRACTION * w_in * 72.0     # raster-scale independent
            if label_pt < FIGURE_HARD_PT:
                F.append(("HIGH", "figure-legib",
                          f"figure {i}: a {w_in:.2f}in embed puts the smallest label (2% of canvas width) at "
                          f"{label_pt:.1f}pt (floor {FIGURE_FLOOR_PT:g}pt); {px_w}px source"))
            elif label_pt < FIGURE_FLOOR_PT:
                F.append(("ADVISORY", "figure-legib",
                          f"figure {i}: 24px label renders at {label_pt:.1f}pt, under the {FIGURE_FLOOR_PT:g}pt floor"))
    except ImportError:
        F.append(("ADVISORY", "figure-legib", "Pillow not installed; figure legibility not checked"))

    # --- table column proportionality (the whiteglove bug) ---
    for ti, t in enumerate(d.tables):
        if len(t.rows) < 2:
            continue
        ncols = len(t.rows[0].cells)
        widths = []
        for c in t.rows[0].cells:
            widths.append(c.width.inches if c.width else 0.0)
        if not any(widths):
            continue
        content = []
        for ci in range(ncols):
            L = sorted(len(r.cells[ci].text) for r in t.rows if ci < len(r.cells))
            content.append(max(L[max(0, int(round(0.85 * (len(L) - 1))))], 1))
        wsum, csum = sum(widths), sum(content)
        ci = content.index(max(content))
        wshare, cshare = widths[ci] / wsum, content[ci] / csum
        if cshare > 0.5 and wshare < 0.6 * cshare:
            F.append(("ADVISORY", "table-widths",
                      f"table {ti}: widest-content column holds {cshare:.0%} of text but {wshare:.0%} of width "
                      f"(columns {[round(w, 2) for w in widths]}in) — expect inflated page count"))

    # --- title page discrete ---
    if exclude_title:
        first_heading = next((p for p in d.paragraphs if _is_heading(p) and p.text.strip()), None)
        broke = False
        for p in d.paragraphs:
            if p is first_heading:
                break
            if p._p.findall(".//" + qn("w:br")):
                for br in p._p.findall(".//" + qn("w:br")):
                    if br.get(qn("w:type")) == "page":
                        broke = True
        if not broke:
            F.append(("ADVISORY", "title-break",
                      "--exclude-title given but no page break before the first heading; the title page "
                      "is only excluded from the limit if it is a discrete page"))

    # --- page count ---
    if pages:
        n, src = _page_count(path)
        if n is None:
            words = sum(len(p.text.split()) for p in body_paras)
            n = max(1, round(words / WORDS_PER_PAGE_ESTIMATE))
        counted = n - 1 if exclude_title else n
        label = "" if src == "word" else f"  [{src}: ~{WORDS_PER_PAGE_ESTIMATE} words/page]"
        if counted > pages:
            F.append(("HIGH", "page-count",
                      f"{counted} counted page(s) against a limit of {pages}"
                      f"{' (title page excluded)' if exclude_title else ''}{label}"))
        else:
            F.append(("INFO", "page-count", f"{counted} of {pages} pages{label}"))
    return F


# ---------------------------------------------------------------- selftest
def selftest() -> int:
    from docx.shared import RGBColor, Inches
    from PIL import Image
    tmp = Path(tempfile.mkdtemp(prefix="lint-rendered-"))
    bad, good = tmp / "bad.docx", tmp / "good.docx"
    png = tmp / "fig.png"
    Image.new("RGB", (1200, 800), (25, 28, 32)).save(png)
    failures = 0

    def expect(label: str, ok: bool) -> None:
        nonlocal failures
        failures += 0 if ok else 1
        print(f"  [{'ok' if ok else 'FAIL'}] {label}")

    # --- a document that trips every HIGH rule ---
    d = docx.Document()
    d.styles["Normal"].font.size = Pt(11)                      # font-size
    h = d.add_heading("Blue Heading", 1)                       # colour (Word default blue)
    for r in h.runs:
        r.font.color.rgb = RGBColor(0x2F, 0x54, 0x96)
    p = d.add_paragraph("A sentence with ")
    r = p.add_run("emphasis"); r.bold = True                   # mid-bold
    p.add_run(" and a gap before the period .")               # orphan-punct
    d.add_paragraph("Value is [NEEDS: confirm].")              # placeholder
    d.add_picture(str(png), width=Inches(3.0))                 # 24px at 3.0in of 1200px = 4.3pt -> HIGH
    for _ in range(60):
        d.add_paragraph("filler " * 60)                        # ~3600 words -> ~8 estimated pages
    d.save(bad)
    F = lint(bad, pages=5, font_pt=12, exclude_title=False)
    rules = {f[1] for f in F if f[0] == "HIGH"}
    for want in ("font-size", "text-colour", "mid-bold", "orphan-punct", "placeholder",
                 "figure-legib", "page-count"):
        expect(f"bad doc fires {want}", want in rules)

    # --- a clean document ---
    d = docx.Document()
    d.styles["Normal"].font.size = Pt(12)
    p = d.add_paragraph()
    r = p.add_run("Label."); r.bold = True
    p.add_run(" Plain prose, correctly punctuated.")
    d.add_picture(str(png), width=Inches(6.5))                 # 9.4pt -> clean
    d.save(good)
    F = lint(good, pages=5, font_pt=12, exclude_title=False)
    highs = [f for f in F if f[0] == "HIGH"]
    expect("clean doc has no HIGH", not highs)
    if highs:
        for f in highs:
            print("      unexpected:", f)

    print("selftest:", "PASS" if failures == 0 else f"FAIL ({failures})")
    return 0 if failures == 0 else 1


# ---------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description="Layout and typography checks on rendered .docx files.")
    ap.add_argument("files", nargs="*", help=".docx files to check")
    ap.add_argument("--pages", type=int, help="page limit from the solicitation")
    ap.add_argument("--font-pt", type=float, help="minimum body font size from the solicitation")
    ap.add_argument("--exclude-title", action="store_true",
                    help="the solicitation excludes the title page from the page limit")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.files:
        ap.error("give at least one .docx (or --selftest)")

    worst = 0
    for f in args.files:
        path = Path(f)
        if not path.is_file():
            print(f"lint-rendered-artifact: not found: {path}", file=sys.stderr)
            return 2
        F = lint(path, args.pages, args.font_pt, args.exclude_title)
        highs = [x for x in F if x[0] == "HIGH"]
        advs = [x for x in F if x[0] == "ADVISORY"]
        infos = [x for x in F if x[0] == "INFO"]
        tag = "FAIL" if highs else ("warn" if advs else "ok  ")
        print(f"{tag}  {path}  ({len(highs)} high, {len(advs)} advisory)")
        for sev, rule, detail in highs + advs + infos:
            print(f"        [{sev:<8}] {rule:<13} {detail}")
        worst = max(worst, 1 if highs else 0)
    return worst


if __name__ == "__main__":
    sys.exit(main())
