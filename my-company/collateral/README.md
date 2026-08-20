# collateral/

Company-wide marketing collateral for the EdgeRunner Military AI Suite — finished
leave-behinds plus the scripts that render them. One sub-folder per deliverable, each
self-contained (generator + source assets + rendered PDF). These are suite-level pieces;
per-paper artifacts live in [../capability-papers/](../capability-papers/).

Each generator uses Playwright (Chromium) to print HTML to PDF. From a sub-folder:

```
python military_suite_onepager.py   # or render_briefing.py / render_slick.py
```

(Requires `playwright` + `playwright install chromium`.)

| Sub-folder | Deliverable | Generator | Source assets |
|---|---|---|---|
| [military-suite-onepager/](military-suite-onepager/) | `EdgeRunner-Military-Suite-OnePager.pdf` — one-page suite overview built around the Ground Truth containment graphic | `military_suite_onepager.py` | `img/military-suite-graphic.png` (the composed hero; the other `img/*.png` are the source WarClaw / Operator screenshots behind it) |
| [groundtruth-briefing/](groundtruth-briefing/) | `EdgeRunner-GroundTruth-Briefing.pdf` — Ground Truth capability briefing | `render_briefing.py` | `groundtruth-briefing.artifact.html` |
| [groundtruth-slick/](groundtruth-slick/) | `EdgeRunner-GroundTruth-Slick.pdf` — one-page Ground Truth slick (landscape) | `render_slick.py` | `groundtruth-slick.artifact.html` |

> Migrated here 2026-07-16 from the `edgerunner-warrant` repo (`warrant-toolkit-demo/docs/`),
> which is a product/code repo — this marketing collateral belongs in the company knowledge base.
> Note: `military-suite-graphic.png` is a rendered export; its own generator (the containment
> mock) was not migrated. To re-compose the hero graphic you still need that source in the
> warrant demo app.
