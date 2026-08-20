---
pattern: discipline-as-software
title: Discipline as Software (WarClaw + Ground Truth verified pipeline)
tags: [warclaw, ground-truth, discipline-as-software, agentic-pipeline, sop-as-software, roles-as-agents, verification, no-model-in-loop, icd-203, icd-206, wbom, intel-production, air-gapped]
canonical_source: graphics/_library/discipline-as-software/source.html (built for the library from EV-104 / the warrant-demo suite)
evidence: EV-104
used_in: []
dimensions: 1200x800
last_updated: 2026-07-22
---

# Discipline as Software (WarClaw + Ground Truth verified pipeline)

Visualizes EdgeRunner's three-layer "Discipline as Software" pattern (evidence: **EV-104**):

- **WarClaw encodes the process** — a fixed pipeline where the SOP's roles become agents (ingest per source, drafting analyst, and **peer reviewer + duty editor held as separate model identities so no role grades its own work**).
- **Ground Truth enforces the standards** — approved ledgers (evidence of record + production standards: ICD 203, ICD 206, unit SOP) checked at **deterministic gates with no model in the verification loop**; outcomes are pass / held-for-analyst / released-with-signed-WBOM-receipt.
- **The government-tuned model provides the judgment** inside each role, fenced on both sides.

Tagline: *"Your SOPs are already software specs. WarClaw compiles them."*

## When to use
Any proposal, brief, or slick that needs to show *how* EdgeRunner turns a defined analytic process into verified, standards-compliant output (intel production, doctrine QA, triage). This is the **deep-dive on WarClaw's most advanced use case** — lead with the [`warclaw-agentic-layer`](../warclaw-agentic-layer/README.md) breadth figure first to establish that WarClaw also connects to and retrieves from existing systems (Maven, Advana/WDP, Power BI, etc.), so this pipeline reads as the top of a spectrum rather than WarClaw's only trick. Pairs with the vendor-agnostic-substrate figure (one open API + tenants + verification) when the story is both "open model choice" and "verified mission products."

## Reuse
- `source.html` — editable master; render to PNG with headless Chrome (`--window-size=1200,800 --device-scale-factor=2`).
- `preview.png` — 2400×1600, embeds at 6.5" full-column.
- Abstract pattern (no customer specifics); scenarios are notional. Internal reuse is fine.

## Distribution
**Confirm maturity framing before external sharing.** This depicts a **built / demonstrated, lab-validated** capability — **not fielded or ATO'd**. Keep that caveat with any external use; do not imply a program of record. Self-authoring the pipeline from the CONOP is roadmap. See EV-104 and `my-company/capabilities.md` Layer 4.
