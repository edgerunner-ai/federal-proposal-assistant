# EdgeRunner Graphics Library

A curated collection of proposal-grade graphics produced across EdgeRunner's federal proposal work. Made available company-wide so anyone building a deck, paper, or external talk can reach for a polished visual instead of starting from scratch.

**Maintained by:** Bill Bal (proposal team)
**Last updated:** 2026-05-26

---

## What's in here

Two collections:

**`_library/`** — canonical reusable patterns. Abstract figures that have proved themselves across multiple proposals — three-tier architecture, deployment spectrum, capability matrix, human–machine teaming, lifecycle loops, hardware tiers, callout boxes, and more. These are the gold copies; reuse them as-is or as a starting point for customization.

**`_proposal-specific/`** — custom figures from specific proposals (Vulcan/JATF, Senate briefings, EXTIC, DoD open-weight whitepaper, SOCPAC, Digital Guardian, etc.). Useful as fork-and-customize starting points, but they reference specific programs — see distribution notes below.

Each entry has:
- `preview.png` — the rendered graphic, ready to drop into a deck or doc
- `source.html` — the editable HTML source (open in browser to view at full size; edit and re-render if you want a variant)

The canonical browse interface is **`index.html`** — open it in any browser for a thumbnail gallery view of every figure in the library.

---

## How to use this

**To peruse:** open `index.html` in a browser. Scroll the gallery. Each card has the figure title, tags, and which proposals used it.

**To pull a graphic:**

| Your goal | What to do |
|---|---|
| Drop the same graphic into your deck | Right-click `preview.png` → download. Embed in your slide. |
| Use it as a starting point but customize labels | Download `source.html`. Open in browser to verify it loads, then edit the HTML directly (labels, colors, content). Re-save as HTML, then render to PNG with headless Chrome (see below). |
| Use the visual style but build something different | Open `source.html` in a text editor. Copy the styling section (colors, fonts, layout primitives) into your own HTML. The brand palette is consistent across the library. |

**Re-rendering HTML to PNG** (if you forked and edited):
```
chrome --headless --disable-gpu --screenshot="output.png" \
       --window-size=2400,1600 --device-scale-factor=2 \
       "file:///full/path/to/your/edited.html"
```

---

## Distribution & classification

This library is **internal to EdgeRunner**. Don't share the library itself outside the company.

**Individual graphics** have varying distribution rules — see the badge on each card in `index.html`:

| Badge | Meaning |
|---|---|
| **Public OK** | The graphic was produced for public-record material (e.g., Senate testimony). Cleared for external sharing. |
| **Distributable to Cleared Partners** | Designed for broad distribution within the contracting community (e.g., the DoD open-weight whitepaper). Confirm with Colton/Bill before sending. |
| **Confirm Before Sharing Externally** | References a specific customer program. Default treatment for proposal-specific figures. Get sign-off from Colton or the relevant program POC before sending outside EdgeRunner. |
| *(no badge — `_library/` entries)* | Abstract patterns, no customer specifics. Internal reuse is fine; external use should still be checked against current messaging. |

**When in doubt, ask Bill or Colton.** Misjudging on a Vulcan, SOCPAC, or Navy ICOP graphic could create a real problem.

---

## Brand consistency

Every library graphic uses EdgeRunner's brand palette:

- **Background:** `#191c20` (near-black)
- **Primary accent:** `#ee2929` (brand red)
- **Dark grey:** `#393939` (borders, structure)
- **Light grey:** `#c8c8c8` (body text)
- **White:** `#ffffff` (headings, primary labels)

If you build something for the library, match this palette. The visual consistency is part of why the library is valuable — it makes a stack of figures from different proposals read as one company's voice.

---

## Contributing

If you build a graphic for a deck, paper, or proposal that you think the rest of the company would benefit from, **send it to Bill**. The promotion path is described in `CONTRIBUTING.md`.

Short version: not every figure belongs in the library. The bar is "would another team member reach for this in a different context?" If yes, send it.

---

## Maintenance loop

- Bill is the librarian — handles promotions, distribution-marking, refreshes.
- The `/proposal-graphics` skill (used by the proposal team) automatically flags new figures as library-promotion candidates when they're built. Bill reviews those during periodic refreshes.
- This library is a **mirror** of the source-of-truth that lives in the proposal workspace on Bill's machine. The Drive copy refreshes on each promotion cycle.

---

## Folder map

```
graphics/
├── LIBRARY-README.md            ← this file
├── CONTRIBUTING.md              ← how to propose new library entries
├── CATALOG.md                   ← detailed reference catalog (more technical than this README)
├── index.html                   ← thumbnail gallery (open in browser to browse)
├── _library/                    ← canonical reusable patterns
│   ├── three-tier-architecture/
│   ├── capability-matrix/
│   ├── deployment-spectrum/
│   ├── human-machine-teaming/
│   ├── differentiator-comparison/
│   ├── platform-architecture/
│   ├── lifecycle-loop/
│   ├── enterprise-tactical-lifecycle/
│   ├── hardware-tiers/
│   ├── pilot-schedule/
│   └── callout-template/
└── _proposal-specific/          ← custom figures from specific proposals
    └── (24 entries, grouped by program in index.html)
```
