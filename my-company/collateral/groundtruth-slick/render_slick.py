"""Render the Ground Truth one-page slick to a single landscape Letter PDF.

Run:  .venv/Scripts/python docs/render_slick.py
Out:  docs/EdgeRunner-GroundTruth-Slick.pdf
"""

import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent.resolve()
CONTENT = HERE / "groundtruth-slick.artifact.html"
PDF = HERE / "EdgeRunner-GroundTruth-Slick.pdf"

PRINT_CSS = """
  @page { size: Letter landscape; margin: 0; }
  html, body { background:#191c20; margin:0; }
  .gt-root { padding:16px 14px !important; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .sheet { width:100% !important; max-width:none !important; }
"""


def main():
    content = CONTENT.read_text(encoding="utf-8")
    html = (
        "<!doctype html><html lang='en'><head><meta charset='utf-8'>"
        "<title>EdgeRunner Ground Truth — Capability Slick</title>"
        f"<style>{PRINT_CSS}</style></head><body>{content}</body></html>"
    )
    tmp = HERE / "_slick_print.html"
    tmp.write_text(html, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        page.goto(tmp.as_uri())
        page.emulate_media(media="print", color_scheme="dark")
        page.wait_for_load_state("networkidle")
        page.pdf(path=str(PDF), landscape=True, format="Letter",
                 print_background=True, prefer_css_page_size=True,
                 margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()
    tmp.unlink(missing_ok=True)
    print("built", PDF.name)


if __name__ == "__main__":
    main()
