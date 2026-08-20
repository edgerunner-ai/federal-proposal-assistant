"""Render the Ground Truth capability briefing to a Letter PDF.

Reads the Artifact content file (style + markup, no doc wrapper), wraps it in a
standalone HTML doc with print CSS, and prints to PDF via Playwright — the same
toolchain as onepager.py.

Run:  .venv/Scripts/python docs/render_briefing.py
Out:  docs/EdgeRunner-GroundTruth-Briefing.pdf
"""

import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
CONTENT = HERE / "groundtruth-briefing.artifact.html"
PDF = HERE / "EdgeRunner-GroundTruth-Briefing.pdf"

PRINT_CSS = """
  @page { size: Letter portrait; margin: 12mm 0; }
  html, body { background:#191c20; margin:0; }
  /* tighten screen paddings for a leave-behind; keep components whole across pages */
  .gt-root { padding:0 14mm !important; min-height:auto !important;
             -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .hero { padding:22px 0 16px !important; }
  section { padding:20px 0 !important; }
  .mast, .hero, section, .gt-foot { break-inside:auto; }
  .step,.g-card,.mode,.dep,.figure,.receipt,.quote,.rag,.oneliner,.isnot .col,
  .receipt-grid,.tbl-wrap,.closer { break-inside:avoid; }
  h1,h2 { break-after:avoid; }
  .sec-label { break-after:avoid; }
"""


def main():
    content = CONTENT.read_text(encoding="utf-8")
    html = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<title>EdgeRunner Ground Truth — Capability Briefing</title>"
        f"<style>{PRINT_CSS}</style></head><body>{content}</body></html>"
    )
    tmp = HERE / "_briefing_print.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        page.goto(tmp.as_uri())
        page.wait_for_load_state("networkidle")
        page.pdf(path=str(PDF), format="Letter", print_background=True,
                 margin={"top": "12mm", "bottom": "12mm", "left": "0", "right": "0"})
        b.close()
    tmp.unlink(missing_ok=True)
    print("built", PDF.name)


if __name__ == "__main__":
    main()
