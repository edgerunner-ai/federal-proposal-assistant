---
pattern: polyglot-ingest-v2
title: One Model, Every Language & Format — polyglot ingest with capability cluster + labeled answers
tags: [edge-ai, multilingual, data-fusion, tactical-formats, air-gapped, sitrep, coa, threat-assessment]
canonical_source: graphics/_proposal-specific/polyglot-ingest-v2/source.html
used_in: []
dimensions: 1400x900
last_updated: 2026-05-27
related: polyglot-ingest (v1 — simpler, 1200x800)
---

# Polyglot Ingest v2 — "One Model. Every Language. Every Format."

Iteration on the v1 polyglot-ingest pattern, incorporating the strongest moves
from a ChatGPT-generated reference: labeled answer categories, a capability
cluster under the model, and an expanded chip set. Visual-uniformity-as-argument
(all input chips identical shape/weight) and brand-red-only accent discipline
are preserved.

## What v2 adds over v1
- **Labeled answer categories** — each operator question pairs with a tagged
  output type (SITREP, COA Update, Threat Assessment, Asset Recommendation,
  Mission Impact). Concrete deliverables, not just example one-liners.
- **Capability cluster under the model** — six on-brand capability tiles
  (Normalizes / Understands Context / Correlates & Infers / Runs Locally /
  Protects Data / Operates Disconnected) without bloating the model node itself.
- **Expanded chip set** — French, Korean, Spanish added to languages; XML, NATO
  STANAG, KML/GeoTIFF, Voice/Audio, Video/ISR, Logs/CSV added to formats.
- **Three-beat tagline** above the model — "DISCONNECTED · DETERMINED ·
  DECISIVE" — in brand red, on-brand.
- **EdgeRunner logo inside the model node** (replacing the text wordmark) plus
  in the footer brand strip.
- **Larger canvas** (1400×900) to carry the extra density without crowding chips
  or shrinking text below the legibility floor.

## What v2 deliberately did NOT take from the reference
- **Stock platform photos** (jet, tank, ship, drone, soldier, radar) — would
  shift the argument from *format uniformity* to *sensor coverage*, weakening
  the visual proof.
- **Competing accent colors** (cyan flow lines + green capability icons + amber)
  — kept brand red as the single accent.
- **Tagline strip baked into the bottom of the graphic** — that's the action
  caption's job in the Word doc, not inside the figure.
- **Operator photo on the bottom-right** — humanizes but distracts.

## Source decision
`freeform` — extends the new polyglot-ingest pattern. **Library-promotion
candidate: yes** (v2 supersedes v1 for proposals that want the labeled-deliverables
treatment; v1 stays as the simpler/cleaner option).

## Action caption (place under the figure in Word — do not embed in graphic)

> *Figure X. One model consumes every input format equally and produces named
> deliverables.* EdgeRunner treats human languages and wire-format tactical
> feeds (Link-16, CoT, USMTF, NITF, KML, NATO STANAG, ISR video, voice) as a
> single token stream, so operators ask a single plain-language question and
> receive a categorized answer — SITREP, COA Update, Threat Assessment, Asset
> Recommendation, or Mission Impact — without translators, middleware, or
> off-device routing. Substantiated by deployed configurations at USASOC, 4ID,
> and Navy ICOP/PMW 120.

## What this graphic proves
That a single on-device model can ingest natural language and tactical wire
formats interchangeably and produce **named, operator-grade deliverables**
locally — collapsing the translation, fusion, and analytics middleware stack
into one air-gapped component.

## Layout (1400 × 900, embed at 7.5" full-page-width on 8.5×11 portrait)

- **Row 1** (title bar, red underline): "One Model. Every Language. Every Format."
- **Row 2** (red 3-beat tagline): "DISCONNECTED · DETERMINED · DECISIVE"
- **Body** (3-column grid):
  - **Left — Inputs:**
    - *Human languages* card: 9 language chips + "…and more"
    - *Machine, wire & tactical formats* card: 13 format chips + "…and more"
  - **Center — Model + Capabilities:**
    - Glowing red-bordered square with EdgeRunner logo, "On-device · Air-gapped",
      "One Model" pill, micro-note "Every input is just tokens."
    - 2×3 capability tile grid below: Normalizes / Understands Context /
      Correlates & Infers / Runs Locally / Protects Data / Operates Disconnected
    - SVG convergence overlay: 5 lines in, 5 lines out, brand-red gradient
  - **Right — Q/A:**
    - 5 question/answer cards. Each: a quoted operator question + a red
      left-rule answer with an uppercase red category label.
- **Footer:** EdgeRunner logo (left) + tagline (right)

## Color / grouping logic
- Brand red (`#ee2929`) reserved for: title underline, tagline (3-beat), accent
  bars on group headers, flow-line gradient, model border + glow, brand pill,
  capability tile marks, question quote marks, answer left-rule, category labels.
- All input chips share identical shape, weight, and border. Mono font on
  machine chips is the only distinguishing cue.

## Legibility check (1400×900 canvas, 7.5" embed → 0.39 pt/px)
- Title 32px → 12.4pt ✓
- Tagline 18px → 7.0pt — fine for an all-caps tracked accent line
- Group headings 16px → 6.2pt — borderline; the accent bar + ALL CAPS carry it
- Chip text 15–16px → 5.8–6.2pt — borderline; **the chip density is the proof**,
  so this is acceptable, but do not shrink the embed below 7.0"
- QA question 15px → 5.8pt — borderline; rely on quote-mark framing for scan
- Footer 14px → 5.4pt (acceptable for footer)

Recommendation: embed v2 at **7.0"–7.5"** wide. For embeds at 6.5" or smaller,
use v1 instead — it was designed for that range.

## Files
- `source.html` — editable master
- `edgerunner-logo.png` — branding asset (copied from `my-company/branding/`)
- `rendered/polyglot-ingest-v2.png` — 2800×1800 PNG for Word embed
