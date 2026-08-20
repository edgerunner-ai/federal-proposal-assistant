"""Render the EdgeRunner Military AI Suite one-pager (Letter, 1 page).

Hero: the containment/governance graphic (img/military-suite-graphic.png, produced by the
containment mock). Below it, a layer-by-layer description of the content in the graphic.
Voice matches the platform slick: sober, defense-native, honest maturity labels.

Run: .venv/Scripts/python docs/military_suite_onepager.py -> docs/EdgeRunner-Military-Suite-OnePager.pdf
"""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
IMG = HERE / "img"
PDF = HERE / "EdgeRunner-Military-Suite-OnePager.pdf"
GFX = (IMG / "military-suite-graphic.png").as_uri()

FOOT = ("""<div class='foot'>
        <div>EdgeRunner AI &middot; Bellevue, WA &middot; <span class='mono'>CAGE 9Z176 &middot; UEI SLZTJUA8DBD3 &middot; NAICS 541511</span></div>
        <div>Partnerships: dave@edgerunnerai.com</div>
      </div>""")

HTML = """<!doctype html><html><head><meta charset='utf-8'><style>
  @page { size: Letter portrait; margin: 0; }
  * { box-sizing: border-box; }
  html, body { background:#191c20; }
  body { font-family:'Segoe UI', Arial, sans-serif; color:#d6d8dc; margin:0;
         -webkit-print-color-adjust:exact; print-color-adjust:exact; }
  .page { padding:12mm 13mm; min-height:273mm; }
  .topbar { display:flex; justify-content:space-between; align-items:baseline;
            border-bottom:3px solid #ee2929; padding-bottom:9px; }
  .wm { font-size:22px; font-weight:800; letter-spacing:2px; color:#fff; }
  .wm b { color:#ee2929; }
  .wm .gt { color:#c8c8c8; font-weight:600; font-size:15px; letter-spacing:1px; }
  .tag { font-size:9.5px; color:#8a8a8a; text-transform:uppercase; letter-spacing:1.5px; }
  .intro { font-size:12px; color:#e6e8ec; font-weight:600; line-height:1.5; margin:13px 0 4px; }
  .intro b { color:#fff; }
  .gfx { width:80%; display:block; border-radius:9px; margin:3px auto 10px; }
  .seclabel { font-size:11px; font-weight:800; text-transform:uppercase; letter-spacing:1px;
              color:#ee2929; margin:2px 0 8px; }
  .gtblk { background:#1e1517; border:1px solid #48292b; border-left:4px solid #ee2929; border-radius:8px;
           padding:9px 14px; margin-bottom:10px; }
  .gtblk .h { font-size:12.5px; font-weight:800; color:#ff5b54; margin-bottom:3px; }
  .gtblk .d { font-size:9.9px; color:#c6ccd4; line-height:1.5; }
  .gtblk .d b { color:#fff; }
  .grid2 { display:flex; flex-wrap:wrap; gap:10px; }
  .blk { flex:0 0 calc(50% - 5px); background:#161c24; border:1px solid #2c3947; border-radius:8px;
         padding:9px 13px; }
  .blk.gold { border-color:#5c4d22; }
  .blk .h { font-size:12px; font-weight:800; margin-bottom:3px; }
  .blk.blue .h { color:#7fb1d0; }
  .blk.gold .h { color:#caa53a; }
  .blk .d { font-size:9.7px; color:#c2c8d0; line-height:1.5; }
  .blk .d b { color:#e6ebf1; }
  .foot { border-top:1px solid #333a42; margin-top:12px; padding-top:8px; font-size:9px;
          color:#8a8a8a; display:flex; justify-content:space-between; }
  .mono { font-family:Consolas, monospace; }
</style></head><body>
  <div class='page'>
    <div class='topbar'><div class='wm'>EDGE<b>RUNNER</b> <span class='gt'>&#8866; Military&nbsp;AI&nbsp;Suite</span></div>
      <div class='tag'>AI tailored for military use</div></div>

    <p class='intro'>EdgeRunner packages <b>military-tuned models</b>, a <b>deployable runtime</b>, <b>WarClaw</b> agents,
    and the <b>Ground Truth</b> governance layer into one suite &mdash; so what your AI says and does stays tied to
    approved doctrine, policy, and human authority, and is provable after the fact.</p>

    <img class='gfx' src='__GFX__'/>

    <div class='seclabel'>The suite, layer by layer</div>

    <div class='gtblk'>
      <div class='h'>Ground Truth &mdash; the governance layer (the boundary around everything)</div>
      <div class='d'>Zero-Trust for what AI <b>says</b> and <b>does</b>: every answer verified against approved sources,
      every proposed agent action authorized against signed policy &mdash; enforced in deterministic code, not prompts
      &mdash; each result carrying a tamper-evident <b>WBOM</b> receipt aligned to NIST AI RMF, DoD Responsible AI, and
      ICD 203/206. Output verification is available today; agent-authority is new and enters in observe mode. The same
      boundary can also govern models and agents you didn&#8217;t build.</div>
    </div>

    <div class='grid2'>
      <div class='blk blue'>
        <div class='h'>WarClaw &mdash; the agentic layer</div>
        <div class='d'>EdgeRunner&#8217;s agent framework. Compose <b>pipelines, tools, functions, and sub-agents</b> into
        mission workflows, with data handed off between agents. Test-run before deploy; schedule or trigger on demand.</div>
      </div>
      <div class='blk blue'>
        <div class='h'>EdgeRunner runtime &mdash; the application</div>
        <div class='d'>The deployable app operators work in &mdash; <b>chat, pipelines, functions, and web apps</b> in one
        workspace &mdash; running your own models on-device, from cloud to air-gapped edge.</div>
      </div>
      <div class='blk blue'>
        <div class='h'>Mission models + LoRA</div>
        <div class='d'>Military-owned &amp; operated, mission-tuned <b>EdgeRunner 20B/26B</b> and LoRA adapters, fine-tuned
        on 1.6M+ military records and matching or exceeding frontier models on military benchmarks. <b>EdgeRunner
        Unchained</b> answers the legitimate military questions commercial models refuse &mdash; full capability intact.</div>
      </div>
      <div class='blk gold'>
        <div class='h'>Warrant Toolkit &mdash; where the governance is built</div>
        <div class='d'>Where reviewers build and human-approve the <b>ledgers</b> Ground Truth checks against &mdash; DoD
        policy and doctrine, mission sources, and user-level authorities. Nothing governs until a human approves it.</div>
      </div>
    </div>

    __FOOT__
  </div>
</body></html>"""

HTML = HTML.replace("__GFX__", GFX).replace("__FOOT__", FOOT)


def main():
    tmp = HERE / "_military_suite.html"
    tmp.write_text(HTML, encoding="utf-8")
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page()
        page.goto(tmp.as_uri())
        page.wait_for_load_state("networkidle")
        page.wait_for_function("Array.from(document.images).every(i => i.complete && i.naturalWidth > 0)", timeout=15000)
        page.pdf(path=str(PDF), format="Letter", print_background=True,
                 margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        b.close()
    tmp.unlink(missing_ok=True)
    print("built", PDF.name)


if __name__ == "__main__":
    main()
