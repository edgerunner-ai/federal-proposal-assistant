---
pattern: polyglot-ingest
title: One Model, Every Language — polyglot ingest into local model
tags: [edge-ai, multilingual, data-fusion, tactical-formats, air-gapped, sitrep, coa]
canonical_source: graphics/_proposal-specific/polyglot-ingest/source.html
used_in: []
dimensions: 1200x800
last_updated: 2026-05-27
---

# Polyglot Ingest — "One Model. Every Language."

## Objective
Show that EdgeRunner's on-device model treats human languages (English, Japanese,
German, Mandarin, Arabic, Russian) and machine/tactical formats (JSON, HTML, C++,
Link-16, USMTF, Cursor-on-Target, NITF, KML) as a **single equal-status token
stream** — no translation layer, no external service, no cloud dependency. Same
prompt, same model, same answer in any environment.

## Source decision
`freeform` — no library match. **Library-promotion candidate: yes** (this is a
reusable "polyglot ingest / unified inference" pattern; nothing equivalent exists
in `_library/`).

## Action caption (place under the figure in Word — do not embed in graphic)

> *Figure X. One model consumes every input format equally.* EdgeRunner treats
> human languages and wire-format tactical feeds (Link-16, CoT, USMTF, NITF, KML)
> as a single token stream, so operators can ask a single plain-language question
> — "Give me a SITREP" — and receive a fused answer without translators,
> middleware, or off-device routing. Substantiated by deployed configurations at
> USASOC, 4ID, and Navy ICOP/PMW 120.

## What this graphic proves
That a single on-device model can ingest natural language and tactical wire formats
interchangeably and answer operator-grade questions locally — collapsing the
translation, fusion, and analytics middleware stack into one component.

## Layout (1200 × 800, embed at 6.5" full-column)
- Title bar (top, red underline): **"One Model. Every Language."** + subtitle.
- Three-column body:
  - **Left — Inputs:** two grouped chip stacks
    - *Human languages* — English, 日本語, Deutsch, 中文, العربية, Русский
    - *Machine & tactical formats* — JSON, HTML, C++, Link-16, USMTF, CoT, NITF, KML
  - **Center — The model:** rounded square node, brand-red glow, "EdgeRunner /
    On-device · Air-gapped / One Model". SVG flow lines converge from the left
    chips into the node and diverge to the right outputs.
  - **Right — Operator queries:** two question cards ("Give me a SITREP" / "How
    does the last hour's activity change my COAs?") with one-line answers, plus a
    red-accent commitment callout: "Same model, same prompt — SCIF, FOB, or
    aircraft."
- Footer brand strip.

## Component list
- 1 title bar, 1 subtitle
- 2 input group cards × 6–8 chips each (chip count is the visual proof — many
  formats, one shape)
- 1 model node (with brand pill + sub-note)
- 1 SVG convergence overlay (5 lines in, 3 lines out, brand-red gradient)
- 2 query cards (label / question / answer)
- 1 commitment callout
- 1 footer strip

## Color / grouping logic
- Brand red (`#ee2929`) reserved for: title underline, accent bars on group
  headers, flow-line gradient, model border + glow, brand pill, commitment
  callout border, query answer left-rule.
- All input chips share the **same shape, weight, and border** — that visual
  uniformity is the argument. Mono font on machine chips is the only
  distinguishing cue, intentionally subtle.
- Two-column model fill (radial red + linear panel gradient) makes the model the
  obvious convergence point without using a different color family.

## Legibility check (1200×800 canvas, 6.5" embed → 0.39 pt/px)
- Title 34px → 13.3pt ✓
- Group headings 18px → 7.0pt — **borderline; OK for grouped chip headers,
  acceptable because chips themselves carry the load**
- Chip text 17–18px → 6.6–7.0pt — **borderline at 6.5" embed.** If embedding at
  full page width (7.5"), this passes. If embed shrinks below 6", regenerate with
  larger chip text.
- Query question text 20px → 7.8pt ✓
- Footer 15px → 5.9pt (acceptable for footer)

Recommendation: embed at **6.5"–7.5"** wide. Do not shrink below 6".

## Files
- `source.html` — editable master (this is the source of truth)
- `rendered/polyglot-ingest.png` — 2400×1600 PNG for Word embed

## Notes for future use
- Swap the language list per customer (e.g., add Korean / Farsi / Pashto for
  INDOPACOM / CENTCOM bids).
- Swap the tactical format list per program (e.g., add VMF, ATAK, STANAG-4609 for
  full-motion video bids).
- The operator queries on the right are the **only** part to retune per
  proposal — match the customer's own vocabulary (e.g., "Give me a SPOTREP" for
  SOF, "What changed in the last sortie cycle?" for AF).
