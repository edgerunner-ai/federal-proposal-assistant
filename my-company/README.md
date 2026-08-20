# my-company/

Your company's reusable knowledge base. Every proposal reads from this directory for boilerplate, capabilities, past performance, contract vehicles, brand, and graphic templates. `/setup-company` scaffolds this directory; subsequent proposals reference it without modification.

## Layout

| File / Dir | Purpose | Read by |
|---|---|---|
| [company-description.md](company-description.md) | One-paragraph / three-bullet / one-sentence company descriptions at varying lengths | `proposal-writer` (cover, exec summary), `customer-intel`, `sources-sought` |
| [capabilities.md](capabilities.md) | Company technical capabilities, deployment models, differentiators, proof points | `proposal-solution-architect` (capability matrix), `proposal-writer`, `competitor-assessment` |
| [components-table.md](components-table.md) | Product components / building blocks | `proposal-solution-architect`, `proposal-graphics` |
| [contract-vehicles.md](contract-vehicles.md) | Contract vehicles held (OTAs, GSA Schedules, IDIQs, consortium memberships) | `proposal-manager` (vehicle eligibility), `pricing-analyst` |
| [past-performance.md](past-performance.md) | Past-performance repository — contracts, customers, $, scope, CPARS, outcomes | `past-performance` skill (PP volume + PPQ narratives), `customer-intel` |
| [published-research.md](published-research.md) | Published research, white papers, patents | `proposal-manager` (discriminator evidence), `proposal-writer` |
| [distribution-statements.md](distribution-statements.md) | Company-specific distribution-statement defaults and guidance | `proposal-writer`, `proposal-graphics` |
| [brand-palette.md](brand-palette.md) | Brand colors, fonts, typography standards | `proposal-graphics`, `export-proposal` (docx/pptx styling) |
| [branding/](branding/) | Master logo files (PNG, SVG) — single source of truth for company logo across all proposals and presentations | `proposal-graphics`, `proposal-writer` (covers), all slide templates |
| [capability-papers/](capability-papers/) | Published/draft research papers (binary), one sub-project per paper — the source PDFs/docx referenced as evidence in proposals | Referenced as evidence in proposals |
| [collateral/](collateral/) | Company-wide marketing collateral (suite one-pager, Ground Truth briefing + slick) — generator scripts + source assets + rendered PDFs | Partner-shareable leave-behinds |
| [graphic-templates/](graphic-templates/) | Reusable HTML graphic templates (architecture diagrams, lifecycle loops, capability matrices, etc.) copied as starting points | `proposal-graphics` — adapts templates rather than designing from scratch |
| [past-proposals/](past-proposals/) | Redacted sections of past winning proposals, indexed for reuse as reference material | `proposal-writer`, `past-performance`, `red-team-review` (as examples of prior approved language) |
| [templates/](templates/) | (Optional) Branded Office templates — `proposal.docx`, `pricing.xlsx`, `briefing.pptx` — used by `/export-proposal` as base templates | `export-proposal` |

## What belongs here vs. where

- **Here** (`my-company/`): Stable, company-wide, used across every proposal
- **Per-proposal** (`proposals/<name>/inputs/`): Solicitation-specific inputs, customer context, opportunity-specific notes
- **Framework** (`reference/`): Type registry, pricing artifact specs, evaluator rubrics, writing patterns — the framework's knowledge, not yours

## When to update

- **company-description.md, capabilities.md:** Quarterly, or after major capability additions
- **past-performance.md:** After each contract close or CPARS refresh
- **contract-vehicles.md:** When a new vehicle is added or an existing one expires
- **brand-palette.md:** When brand identity changes
- **past-proposals/:** After each proposal is submitted and its outcome known (archive a redacted copy)

## Migration note

This directory was populated on 2026-04-22 from legacy content at `Claude Code Projects/proposals/reference/` and `proposals/inputs/02_edgeRunner/`. The pre-P1-P7 framework used those paths. The current framework reads from here.
