"""Build self-contained index.html gallery for EdgeRunner Graphics Library.

Walks _library/ and _proposal-specific/, generates 320px-wide thumbnails,
base64-embeds them in a single self-contained HTML file.

Run from graphics/ directory:
    python build-gallery.py

Output: index.html (single self-contained file, no external dependencies).
"""

from __future__ import annotations

import base64
import io
import json
import re
from pathlib import Path
from datetime import date

from PIL import Image

ROOT = Path(__file__).parent
LIBRARY = ROOT / "_library"
PROPOSAL = ROOT / "_proposal-specific"
THUMB_WIDTH = 320  # logical px in gallery card


def parse_frontmatter(readme_path: Path) -> dict:
    if not readme_path.exists():
        return {}
    text = readme_path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [s.strip() for s in v[1:-1].split(",") if s.strip()]
            fm[k.strip()] = v
    return fm


def thumb_b64(png_path: Path, width: int = THUMB_WIDTH) -> str:
    img = Image.open(png_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    ratio = width / img.width
    new_size = (width, int(img.height * ratio))
    img = img.resize(new_size, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=82, optimize=True)
    return base64.b64encode(buf.getvalue()).decode("ascii")


def collect_library() -> list[dict]:
    entries = []
    for pattern_dir in sorted(LIBRARY.iterdir()):
        if not pattern_dir.is_dir():
            continue
        png = pattern_dir / "preview.png"
        if not png.exists():
            continue
        fm = parse_frontmatter(pattern_dir / "README.md")
        entries.append({
            "slug": pattern_dir.name,
            "title": fm.get("title", pattern_dir.name),
            "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
            "used_in": fm.get("used_in", []) if isinstance(fm.get("used_in"), list) else [],
            "thumb": thumb_b64(png),
            "rel_path": f"_library/{pattern_dir.name}/",
        })
    return entries


# Distribution-marking rules. Default everything in _proposal-specific to "Confirm"
# until Bill vets each. Senate briefings were public testimony so flag-ok.
DIST_RULES = {
    "senate-": "public-ok",       # Senate briefings — public testimony material
    "dod-openweight-": "distributable",  # whitepaper designed for broad DoD distribution
}


def dist_class(slug: str) -> str:
    for prefix, klass in DIST_RULES.items():
        if slug.startswith(prefix):
            return klass
    return "confirm"


DIST_LABELS = {
    "public-ok": "Public OK",
    "distributable": "Distributable to Cleared Partners",
    "confirm": "Confirm Before Sharing Externally",
}


def collect_proposal_specific() -> list[dict]:
    entries = []
    for spec_dir in sorted(PROPOSAL.iterdir()):
        if not spec_dir.is_dir():
            continue
        png = spec_dir / "preview.png"
        if not png.exists():
            continue
        slug = spec_dir.name
        # derive a human title from slug
        title = slug.replace("-", " ").title()
        title = title.replace("Itdx26", "ITDX26").replace("Dod", "DoD").replace("Prc", "PRC")
        entries.append({
            "slug": slug,
            "title": title,
            "thumb": thumb_b64(png),
            "rel_path": f"_proposal-specific/{slug}/",
            "dist": dist_class(slug),
        })
    return entries


def proposal_group(slug: str) -> str:
    for prefix, name in [
        ("vulcan-", "Vulcan / JATF"),
        ("senate-manchurian-", "Senate — Manchurian Models"),
        ("senate-prc-", "Senate — PRC Open-Source Models"),
        ("extic-", "EXTIC 26-2"),
        ("dod-openweight-", "DoD Open-Weight Whitepaper"),
        ("socpac-", "SOCPAC"),
        ("digital-guardian-", "Digital Guardian Sim"),
    ]:
        if slug.startswith(prefix):
            return name
    return "Single-Figure Proposals"


def main():
    library = collect_library()
    proposals = collect_proposal_specific()

    # group proposal-specific
    grouped: dict[str, list[dict]] = {}
    for e in proposals:
        grouped.setdefault(proposal_group(e["slug"]), []).append(e)

    today = date.today().isoformat()
    html = build_html(library, grouped, today)
    out = ROOT / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size // 1024} KB)")


def build_html(library, grouped, today):
    css = """
    :root {
      --bg: #191c20;
      --panel: #22262b;
      --border: #393939;
      --accent: #ee2929;
      --text: #ffffff;
      --muted: #9f9f9f;
      --light: #c8c8c8;
    }
    * { box-sizing: border-box; }
    body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
      background: var(--bg); color: var(--text); line-height: 1.5; }
    .wrap { max-width: 1400px; margin: 0 auto; padding: 32px 40px 64px; }
    header { border-bottom: 2px solid var(--accent); padding-bottom: 16px; margin-bottom: 24px; }
    header h1 { margin: 0 0 4px; font-size: 28px; font-weight: 600; letter-spacing: -0.01em; }
    header .sub { color: var(--muted); font-size: 14px; }
    .dist-notice {
      background: rgba(238,41,41,0.08); border: 1px solid rgba(238,41,41,0.4);
      border-radius: 6px; padding: 14px 18px; margin: 20px 0 28px; color: var(--light);
      font-size: 14px;
    }
    .dist-notice strong { color: var(--accent); }
    h2 { font-size: 20px; margin: 36px 0 4px; font-weight: 600; }
    h2 + .section-sub { color: var(--muted); font-size: 13px; margin-bottom: 18px; }
    h3 { font-size: 15px; margin: 28px 0 12px; color: var(--accent); font-weight: 600;
      text-transform: uppercase; letter-spacing: 0.05em; }
    .grid {
      display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 18px;
    }
    .card {
      background: var(--panel); border: 1px solid var(--border); border-radius: 6px;
      overflow: hidden; display: flex; flex-direction: column;
      transition: border-color 0.15s, transform 0.15s;
    }
    .card:hover { border-color: var(--accent); transform: translateY(-2px); }
    .card .thumb { width: 100%; display: block; background: #0d0e10;
      aspect-ratio: 16 / 9; object-fit: contain; }
    .card .body { padding: 12px 14px 14px; flex: 1; display: flex; flex-direction: column; }
    .card h4 { margin: 0 0 6px; font-size: 14px; font-weight: 600; color: var(--text); }
    .card .meta { font-size: 11px; color: var(--muted); margin-bottom: 6px; }
    .card .path { font-size: 11px; color: var(--accent); font-family: ui-monospace, "SF Mono", monospace;
      word-break: break-all; margin-top: auto; padding-top: 8px; }
    .tag { display: inline-block; font-size: 10px; background: rgba(255,255,255,0.06);
      color: var(--light); padding: 2px 8px; border-radius: 10px; margin-right: 4px; margin-bottom: 4px;
      text-transform: uppercase; letter-spacing: 0.04em; }
    .dist-badge { display: inline-block; font-size: 10px; padding: 2px 8px; border-radius: 3px;
      text-transform: uppercase; letter-spacing: 0.04em; font-weight: 600; margin-bottom: 6px; }
    .dist-public-ok { background: rgba(80,180,80,0.15); color: #7dc77d; border: 1px solid rgba(80,180,80,0.4); }
    .dist-distributable { background: rgba(180,140,60,0.15); color: #d4a657; border: 1px solid rgba(180,140,60,0.4); }
    .dist-confirm { background: rgba(238,41,41,0.12); color: var(--accent); border: 1px solid rgba(238,41,41,0.4); }
    footer { margin-top: 48px; padding-top: 20px; border-top: 1px solid var(--border);
      color: var(--muted); font-size: 12px; }
    footer a { color: var(--accent); }
    """

    parts = [
        "<!DOCTYPE html>",
        '<html lang="en"><head>',
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<title>EdgeRunner Graphics Library</title>',
        f'<style>{css}</style>',
        '</head><body><div class="wrap">',
        '<header><h1>EdgeRunner Graphics Library</h1>',
        f'<div class="sub">Curated reference of proposal-grade graphics &middot; Last updated {today}</div>',
        '</header>',
        '<div class="dist-notice">',
        '<strong>Internal Use Only.</strong> These graphics were produced for EdgeRunner proposals and white papers. ',
        'Library entries (abstract patterns) are cleared for internal reuse across teams. ',
        'Proposal-specific entries reference customer programs — <strong>confirm distribution authority before sharing externally</strong>. ',
        'When in doubt, ask Bill Bal or Colton Malkerson.',
        '</div>',
        '<h2>Library &mdash; Canonical Reusable Patterns</h2>',
        '<div class="section-sub">Abstract patterns proven across multiple proposals. Reuse as-is or fork into your project.</div>',
        '<div class="grid">',
    ]

    for e in library:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in e["tags"][:4])
        used_in = ", ".join(e["used_in"][:5]) if e["used_in"] else ""
        parts.append(
            f'<div class="card">'
            f'<img class="thumb" src="data:image/jpeg;base64,{e["thumb"]}" alt="{e["title"]}">'
            f'<div class="body">'
            f'<h4>{e["title"]}</h4>'
            f'<div class="meta">{tags_html}</div>'
            + (f'<div class="meta">Used in: {used_in}</div>' if used_in else "")
            + f'<div class="path">{e["rel_path"]}</div>'
            f'</div></div>'
        )
    parts.append('</div>')

    parts.append('<h2>Proposal-Specific &mdash; Forkable Starting Points</h2>')
    parts.append('<div class="section-sub">Custom figures tied to specific programs. Reuse the structure, not the labels. Check distribution badge.</div>')

    group_order = [
        "Vulcan / JATF",
        "Senate — Manchurian Models",
        "Senate — PRC Open-Source Models",
        "EXTIC 26-2",
        "DoD Open-Weight Whitepaper",
        "SOCPAC",
        "Digital Guardian Sim",
        "Single-Figure Proposals",
    ]
    for group in group_order:
        if group not in grouped:
            continue
        parts.append(f'<h3>{group}</h3><div class="grid">')
        for e in grouped[group]:
            badge_class = f"dist-{e['dist']}"
            badge_label = DIST_LABELS[e["dist"]]
            parts.append(
                f'<div class="card">'
                f'<img class="thumb" src="data:image/jpeg;base64,{e["thumb"]}" alt="{e["title"]}">'
                f'<div class="body">'
                f'<div class="dist-badge {badge_class}">{badge_label}</div>'
                f'<h4>{e["title"]}</h4>'
                f'<div class="path">{e["rel_path"]}</div>'
                f'</div></div>'
            )
        parts.append('</div>')

    parts.append(
        '<footer>Maintained by Bill Bal &middot; '
        'Contribute via the team chat or by tagging Bill on a proposal that produces a reusable graphic. '
        'See CONTRIBUTING.md for the promotion criteria.'
        '</footer>'
    )
    parts.append('</div></body></html>')
    return "\n".join(parts)


if __name__ == "__main__":
    main()
