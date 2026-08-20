---
pattern: polyglot-ingest-v3
title: One Model, Every Language / Format / File — three-group polyglot ingest with Operator key takeaway
tags: [edge-ai, multilingual, data-fusion, tactical-formats, file-types, air-gapped, sitrep, coa, operator-centered]
canonical_source: graphics/_proposal-specific/polyglot-ingest-v3/source.html
used_in: []
dimensions: 1400x1050
last_updated: 2026-05-27
related: polyglot-ingest (v1), polyglot-ingest-v2
---

# Polyglot Ingest v3 — "Every Language. Every Format. Every File."

Iteration on v2 that splits the input column into **three** distinct groups
(human languages / machine & tactical formats / file types) and adds a
prominent red key-takeaway callout band carrying the Operator-centered framing.

## What v3 changes vs. v2

- **Three input groups instead of two:**
  1. *Human languages* — added **Polski** (NATO ally signal) alongside English,
     日本語, Deutsch, 中文, العربية, Русский, Français, 한국어, Español.
  2. *Machine & tactical formats* — pure wire/tactical exchange formats:
     Link-16, Cursor-on-Target, USMTF, NATO STANAG, VMF, JREAP, NITF,
     MIL-STD-2525. (XML/JSON/HTML moved out — they're file types.)
  3. *File types* — HTML, XML, JSON, DOCX, XLSX, PDF, JPG, PNG, KML, GeoTIFF,
     MP3/WAV, MP4/H.264. Closer to what an operator drops on a workstation.
- **Red key-takeaway callout band** (the "red box" addition) running across the
  full width above the footer:
  > **KEY TAKE-AWAY** — We build EdgeRunner to *understand what the Operator
  > needs to understand* — so the Operator can *answer the questions only an
  > Operator can answer.*
- **Title updated** to "One Model. Every Language. Every Format. Every File."
- **Subtitle reframed** around the Operator: "Built to understand what the
  Operator needs to understand — on-device, air-gapped, local."
- **Canvas extended** to 1400×1050 (was 1400×900) to carry the third input card
  and the callout band without compressing chip density.
- **Convergence SVG** widened to 6 left-converging flow lines (one for each
  major chip region) feeding the model.

## What v3 keeps from v2
- Visual-uniformity-as-argument: every input chip shares identical shape, weight,
  border. Mono font is the only differentiator for machine/file types.
- Brand-red-only accent discipline.
- Three-beat tagline strip: **DISCONNECTED · DETERMINED · DECISIVE**.
- Center model node with EdgeRunner logo + "On-device · Air-gapped" + "One Model"
  pill + 6-tile capability cluster.
- Five labeled Q/A pairs on the right (SITREP / COA Update / Threat Assessment /
  Asset Recommendation / Mission Impact).
- Footer brand strip.

## Source decision
`freeform` — extends the polyglot-ingest pattern. **Library-promotion candidate:
yes.** v1, v2, and v3 should be promoted together as a sibling set — pick by
embed width and density tolerance.

## Action caption (place under the figure in Word — do not embed in graphic)

> *Figure X. One model consumes every input format equally and produces named
> deliverables.* EdgeRunner treats human languages, tactical wire-formats
> (Link-16, CoT, USMTF, NATO STANAG, JREAP), and ordinary file types (DOCX,
> PDF, JPG, KML, MP4) as a single token stream, so operators ask a single
> plain-language question and receive a categorized answer — SITREP, COA
> Update, Threat Assessment, Asset Recommendation, or Mission Impact — without
> translators, middleware, or off-device routing. Substantiated by deployed
> configurations at USASOC, 4ID, and Navy ICOP/PMW 120.

## What this graphic proves
That a single on-device model can ingest natural language, tactical wire
protocols, *and* arbitrary file types interchangeably and produce **named,
operator-grade deliverables** locally — and that the design center of the
product is the Operator's information need, not the data pipeline.

## Legibility check (1400×1050 canvas, 7.5" embed → 0.39 pt/px)
- Title 32px → 12.4pt ✓
- Tagline 18px → 7.0pt — fine for an all-caps tracked accent line
- Group headings 15px → 5.8pt — borderline; accent bar + ALL CAPS carry it
- Chip text 14–15px → 5.4–5.8pt — **borderline; the chip density is the proof.**
  Do not embed below 7.0".
- QA question 15px → 5.8pt
- Takeaway text 19px → 7.4pt — the read-this-first element
- Footer 14px → 5.4pt

Recommendation: embed v3 at **7.0"–7.5"** wide. For embeds ≤6.5", use v1.

## Picking among v1 / v2 / v3
- **v1** (1200×800, 2 input groups, 2 Q/A) — cleanest scan, best for half-column
  embeds, single-page executive summaries.
- **v2** (1400×900, 2 input groups, 6 caps, 5 Q/A) — labeled deliverables; best
  when the deliverable categories are the win theme.
- **v3** (1400×1050, 3 input groups + Operator takeaway) — fullest density;
  best for technical volume hero pages and pages where the "we ingest *everything*"
  argument is load-bearing.

## Files
- `source.html` — editable master
- `edgerunner-logo.png` — branding asset
- `rendered/polyglot-ingest-v3.png` — 2800×2100 PNG for Word embed
