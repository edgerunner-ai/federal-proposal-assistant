# Federal Proposal Assistant
### A Shipley-aligned capture and proposal workflow for small defense contractors — process discipline, operationalized

---

## The Problem

Federal proposals are won or lost long before the writing starts. The work that actually determines the outcome — understanding the customer, assessing the competition, designing a credible solution, pricing to win — is the hard part. And for a small team, it's often skipped or rushed because there simply isn't enough time or enough people.

Then comes the writing itself. Graphics alone can take days. Compliance reviews get rushed. Red team feedback arrives too late to act on.

This tool changes that.

---

## What It Is

**Federal Proposal Assistant** operationalizes the Shipley capture and proposal process in software, built on [Claude Code](https://claude.ai/claude-code). Each step produces a structured artifact — submission summary, customer profile, competitor chart, requirements matrix, narrative spine, section drafts, compliance check, Gold Team review — and the sequence is what makes the final response compelling against the customer's actual problem.

It is **not** an AI proposal writer. That's a different (crowded, undefendable) category. It is **not** an automation tool that replaces capture judgment — relationship work, customer empathy, and the unwritten things in the air stay with you. What it replaces is **missing process discipline**: the steps your team would do if you'd been trained at Shipley and had three more people to run them.

The single value proposition: **the tool allows a user to answer requirements with a solution.** That is the hardest part of writing federal proposals. Technically excellent engineers default to describing the thing they built and submitting that description for every request. The workbench exists to defeat that solution-first failure mode by forcing requirement-first sequencing — and making it easier to follow than to bypass.

Built on the Shipley methodology — with a full reference library (`reference/methodology/`) covering the BD lifecycle, capture planning, color-team review protocols, and Shipley alignment — adapted for small teams that need to win competitive work without a full BD machine.

---

## What It Does

Thirty skills, grouped by phase. **You never run all of them.** Each proposal declares its type —
there are 18, from `rfi` and `rom` through `sbir-phase1`, `ota-white-paper`, `far-rfp`, and
`unsolicited-proposal` — and the type names the ordered subset of skills that apply and the ones
that explicitly do not. A skill invoked outside its type exits rather than producing output nobody
asked for. An RFI does not get a cost volume; a white paper does not get a storyboard.

**Setup** — once per company, then once per pursuit.
`setup-company` builds your profile: capabilities, past performance, contract vehicles, brand.
`new-proposal` scaffolds a workspace with that boilerplate pre-loaded and the type set.
`import-from-capture` pulls a qualified opportunity straight out of the capture pipeline instead.

**Capture** — decide whether to bid, and learn who you're bidding to.
`opportunity-quick-look` triages across 8 factors and will tell you to stop. `submission-summary`
pins down exactly what the customer requires you to hand over, and stops for your confirmation
before planning starts. `capture-portal-structure` captures a web-form portal's real section
limits before you draft into an assumed structure. `customer-intel`, `competitor-assessment`, and
`capture-scorecard` profile the buyer, the field, and your own readiness. `capture-intent` records
why you're bidding and what you may not claim.

**Planning** — decide what you're going to argue.
`proposal-manager` extracts evaluation criteria and seeds the compliance matrix.
`proposal-solution-architect` maps requirements to capabilities and designs the architecture.
`narrative-spine` writes the one-page plain-prose argument and **stops for your sign-off** — the
step that keeps the draft from being a tour of your product.

**Drafting** — build the thing.
`past-performance` and `pricing-analyst` run first, so the storyboard plans around real proof
points and real cost constraints. `proposal-storyboard` keys every section to the evaluation
factors it must win. `proposal-graphics` drafts the figures. `proposal-writer` drafts in two
passes — a loose in-voice argument, then a binding pass that attaches evidence and updates the
compliance matrix. `proposal-editor` tightens the prose without breaking either.

**Review** — find out what's wrong while you can still fix it.
`technical-review` runs twice: before drafting, to kill an unworkable approach before you spend
tokens on it, and after, to check the prose against the architecture. `compliance-check` diffs
required against covered. `evidence-check` audits every citation against the evidence ledger.
`red-team-review` scores the draft from a GS-14's chair — narrative, then a rubric-driven mock
evaluation with adjectival ratings and a pWin estimate, then final QA. `adversarial-review` sends
fresh-context agents in blind, seeing only what an outsider would see, and loops until a round
comes back clean. `proposal-patcher` applies audit findings surgically instead of rewriting.

**Submission** — `export-proposal` converts the markdown drafts to Word, Excel, and PowerPoint and
runs three blocking lint gates first. `capture-submission` snapshots the AI draft and your final
submitted version into a calibration corpus, so the framework learns from your real edits.

**Any time** — `status` shows where a proposal stands and what to run next. `dashboard` gives a
read-only portfolio view across every pursuit at once.

### Two orders of operations

The main pipeline builds prose inside a structure: storyboard first, then write into it. That is
right for an RFP scored section by section against a compliance matrix.

White papers invert it. **Track B** skips the storyboard and the editor entirely — the narrative
spine and the writer's loose pass replace the per-section field table, and `proposal-patcher`
replaces the global style edit. A spine runs lengthwise through an argument; a storyboard runs
crosswise through sections. A white paper needs the former, and forcing it through the lattice
produces something that complies with nothing in particular.

## Who It's For

Small and mid-sized defense contractors who:
- Are writing 5–20 proposals per year without a dedicated BD staff
- Pursue a mix of SBIR, CSO, OTA, BAA, and competitive RFPs
- Lose proposals because of gaps in analysis or writing quality, not gaps in capability
- Spend too much time on graphics, compliance matrices, and boilerplate

The workflow supports two modes:

- **Full Capture** — for competitive RFPs, IDIQ task orders, GSA MAS task orders, and recompetes. Complete Shipley-style competitive analysis, formal pricing, PPQ-format past performance.
- **Responsive** — for SBIR, CSO, OTA, BAA, and white papers. Lighter-weight process calibrated to the vehicle, with SBIR budget templates, OTA milestone schedules, and relevant experience narratives instead of formal PPQs.

You set your company's default. You override it per proposal when needed.

Over time, the `/capture-submission` skill feeds a calibration corpus with your real edits — letting the framework continuously close the gap between AI first-draft and submission-ready.

---

## What Stays on Your Machine

All of your files — solicitations, drafts, graphics, analysis, past performance, pricing — stay in your local directories. Claude processes them when you run a skill, but nothing is stored in a cloud database, shared with other users, or used to train AI models.

This matters for proposals involving proprietary capabilities, teaming strategies, and customer-sensitive information. Your crown jewels stay on your machine.

---

## The Graphics Difference

For most proposal teams, graphics are the bottleneck — they require a designer who may not understand the technical content, multiple revision cycles, and days of calendar time.

This tool generates proposal-ready graphics as HTML/SVG code that renders in any browser and screenshots directly into Word. Because the AI understands the solution it designed, every box says the right thing and every flow goes the right direction — from the first version. Revisions are conversational: *"make the font larger"* or *"add a third tier"* takes seconds.

Architecture diagrams, execution timelines, capability matrices, objectives graphics — all produced in minutes, not days.

---

## Getting Started

1. Install [Claude Code](https://claude.ai/claude-code) (requires a Claude subscription)
2. Clone the repo: `github.com/edgerunner-ai/federal-proposal-assistant`
3. Run `/setup-company` to create your company profile (one time, ~10 minutes)
4. Drop in a solicitation, run `/new-proposal`, follow the workflow

The first time through takes an hour or two. Once your company profile exists and you've run it once, each subsequent proposal moves faster.

---

*Built from real-world federal proposal experience. Feedback and contributions welcome.*
