---
pattern: warclaw-agentic-layer
title: WarClaw — a sandbox to automate any manual process
tags: [warclaw, agentic-layer, sandbox, automate-manual-process, pipelines, connectors, warfighter, models, data-systems, on-device-tools, websites, external-services, maven, advana, wdl, power-bi, geoint, entity-lookup, on-device, model-agnostic, no-rip-and-replace]
canonical_source: graphics/_library/warclaw-agentic-layer/source.html (built for the library from capabilities.md Layer 4 four-tier model + EV-104)
evidence: EV-104
used_in: []
dimensions: 1200x800
last_updated: 2026-07-23
---

# WarClaw — one agentic layer over your existing systems

The **breadth** companion to the [`discipline-as-software`](../discipline-as-software/README.md) figure. Where that figure is the deep-dive on WarClaw's *most advanced* use case (a full SOP run as a verified pipeline), this figure frames WarClaw as a **sandbox for automating any manual process** and makes the interface diversity explicit, so it doesn't read as "just an SOP-to-pipeline translator."

Three zones:

- **What WarClaw connects to** (left) — four *typed* resource categories, color-differentiated so they don't blend: **Models** (government-tuned & open-weight LLMs), **Data systems** (Maven, Advana/WDP, Power BI), **On-device tools** (SOCET GXP, imagery/GEOINT, entity & OOB lookups), and **Websites & external services** (OSINT sites, external APIs & feeds). *Connect to what you have — no rip-and-replace.*
- **WarClaw** (center) — the model-agnostic, on-device **sandbox for building automated pipelines**: connect · compose · automate · verify, with human gates and a full audit trail.
- **What warfighters can do with it** (right) — foundational → advanced: **Connect & retrieve**, **Compose skills**, then **Automate a whole process** (encode any manual SOP as a pipeline; Ground Truth verifies and signs each product → the Discipline-as-Software figure).

Tagline: *"If a warfighter does it by hand today, WarClaw can make it a pipeline."*

## When to use
Any time WarClaw is being introduced and the risk is that the audience files it under one narrow use case. Lead with this figure to establish the **connect-and-retrieve foundation** (the broad, everyday value over existing systems), then hand to `discipline-as-software` when the conversation goes deep on verified production. Reinforces the "we fit your environment / no lock-in" theme alongside the verification story.

## Reuse
- `source.html` — editable master; render to PNG with headless Chrome (`--window-size=1200,800 --force-device-scale-factor=2 --screenshot`).
- `preview.png` — 2400×1600, embeds at 6.5" full-column.
- Abstract pattern; named systems are **illustrative examples of the connector capability**, not certified integrations.

## Distribution
**Confirm connector maturity before external sharing.** WarClaw's connector framework is real (standard connectors / OpenAI-compatible interfaces per `my-company/capabilities.md` Layer 4). The **specific named systems** (Maven, Advana/WDP, Power BI, SOCET GXP, NGA/MARS) are shown as *examples of what the connector layer can front* — do not present any one of them as a built, tested, or fielded integration unless it has been confirmed as such. The verified-pipeline tier (right/advanced) is **built / demonstrated, lab-validated — not fielded or ATO'd** (see EV-104 and the `discipline-as-software` distribution note).
