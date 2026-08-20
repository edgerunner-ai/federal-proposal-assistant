# Federal Proposal Assistant

A Shipley-aligned capture and proposal workflow that enforces **requirement-first sequencing**. You follow the steps; the tool teaches the process by being used; the artifact at the end is Shipley-compliant — even if you've never taken Shipley training.

Built for senior engineers, SMEs, and small-team capture leads who write federal proposals without a formal BD machine behind them. The tool's job is to make requirement-first feel *less effortful* than the solution-first habit it exists to defeat.

Built on [Claude Code](https://claude.ai/claude-code).

> **New here?** Start with the [Overview](OVERVIEW.md) — a plain-language introduction to what this tool does and who it's for.
>
> **Are you an AI agent?** Read [docs/AGENT-ORIENTATION.md](docs/AGENT-ORIENTATION.md) — the mental model, the mechanically-enforced gates, and the traps, in one pass.

## Quick Start

### Prerequisites

**Required:**
- [Claude Code](https://claude.ai/claude-code) installed (CLI, desktop app, or IDE extension)
- A Claude account with an active subscription

**Required for specific features:**

| Feature | Runtime dependency | How to install |
|---|---|---|
| Graphic rendering (HTML → PNG) | Headless Chrome | Chrome for Windows (or Chromium). The `proposal-graphics` skill invokes `chrome --headless`. |
| Office export (`/export-proposal`) | [`anthropic-skills:docx`](https://github.com/anthropics/skills) + [`anthropic-skills:xlsx`](https://github.com/anthropics/skills) + [`anthropic-skills:pptx`](https://github.com/anthropics/skills) | Install via Claude Code's skill marketplace. The `/export-proposal` skill delegates all Office format conversion to these. |
| Node-based graphics build scripts (used by some older proposals like `dod-openweight-whitepaper/`) | Node.js + puppeteer | `npm install` inside the proposal dir if a `package.json` is present |
| Smoke test (`bash scripts/smoke-test.sh`) | Bash (Git Bash on Windows) | Ships with Git for Windows |

**Optional:**
- Microsoft Word (for reviewing .docx output and Save-As-PDF for submission)
- Microsoft Excel (for reviewing .xlsx pricing and compliance workbooks)
- Microsoft PowerPoint (for reviewing .pptx briefings)

### Setup (10 minutes)

```bash
# 1. Clone the repo
git clone https://github.com/YOUR-ORG/federal-proposal-assistant.git
cd federal-proposal-assistant

# 2. Open in Claude Code
claude

# 3. Run company setup (one-time)
/setup-company
```

The setup skill will ask for your company name, capabilities, past performance, contract vehicles, and optionally your brand colors. It generates reusable boilerplate files in `my-company/` that every future proposal will reference.

### Start a Proposal

```bash
# 4. Create a new proposal workspace
/new-proposal
```

You'll be asked for the proposal name, customer, and type. Then:

```bash
# 5. Drop your solicitation into the inputs folder
#    (PDF, DOCX, or markdown — Claude will read it)

# 6. Run the workflow in sequence:
/customer-intel                 # Research customer — open source intel + relationship template
/proposal-manager               # Analyze solicitation, compliance framework, win themes, bid/no-bid
/competitor-assessment          # Research competitors, Bidder Comparison Chart, teaming gaps (competitive bids)
/proposal-solution-architect    # Design solution against approved plan + competitor assessment
/past-performance               # Map PP repository to eval criteria, draft PPQ narratives
/pricing-analyst                # Build cost model and cost volume narrative
/proposal-graphics              # Create visual concepts + HTML graphics
/proposal-writer                # Draft all sections
/red-team-review                # Score like a government evaluator
```

## How It Works

### The Workflow

```
Customer Intel → Proposal Plan → Competitor Assessment → Solution Architecture → PP + Pricing → Graphics → Draft → Red Team → Submission
      ↑                ↑                   ↑                       ↑                  ↑              ↑         ↑         ↑
  AI searches      AI builds           AI researches           AI designs          AI maps PP    AI renders  AI writes  AI scores
  open source +    compliance          competitors via         from your           to criteria    HTML files  sections   & rewrites
  you fill in      framework &         open source +           capabilities        + builds
  relationship     win themes          teaming gaps            + competitor        cost volume
  knowledge                                                    assessment
```

### Skills

| Skill | What It Does |
|-------|-------------|
| `/setup-company` | One-time setup — creates your company profile and boilerplate |
| `/new-proposal` | Scaffolds a new proposal workspace, **selects a proposal type from the registry**, and generates a type-specific Next Steps list |
| `/opportunity-quick-look` | Rapid triage of a new opportunity — go/hold/no-go before committing effort |
| `/customer-intel` | Researches the customer via open source (budget docs, awards history, key personnel, hot buttons) and produces a profile template for you to complete with relationship knowledge |
| `/proposal-manager` | Analyzes the solicitation — builds compliance framework, **seeds the compliance matrix**, evaluates criteria, defines win themes, recommends bid/no-bid |
| `/competitor-assessment` | Researches likely competitors via open source, builds weighted Bidder Comparison Chart, identifies teaming gaps, generates strategy statements |
| `/capture-scorecard` | 9-dimension readiness stoplight — go/no-go before committing proposal resources |
| `/proposal-solution-architect` | Designs the solution against the approved plan and competitor assessment — requirements matrix, capability mapping, architecture concept |
| `/past-performance` | Maps your PP repository to evaluation criteria, selects best references, drafts PPQ narratives and past performance volume |
| `/pricing-analyst` | Dispatches on the proposal type's `pricing_artifact` to produce the right vehicle-specific artifact — ROM, SBIR budget, OTA milestones, CSO commercial, or FAR cost volume. Templates in [`reference/pricing-artifacts/`](reference/pricing-artifacts/). |
| `/proposal-graphics` | Creates proposal-ready HTML graphics (architecture diagrams, timelines, matrices) |
| `/proposal-writer` | Drafts all proposal sections from the approved architecture, **applies the four winning patterns** (theme statements, discriminator proof points, action captions, ghosting — see [`reference/proposal-writing-patterns.md`](reference/proposal-writing-patterns.md), gated by proposal type), **updates the compliance matrix** as sections land |
| `/compliance-check` | Diffs required vs. covered requirements, recomputes coverage counters, writes `reviews/compliance-gaps.md`. Run after each writer pass. |
| `/evidence-check` | Audits evidence citations in drafts against `my-company/evidence-ledger.json` — flags unsupported claims (`CLAIM-UNSUPPORTED` markers), typo'd IDs, retired evidence, and unused proof points. Run after `/proposal-writer`, before Gold Team. Writes `reviews/evidence-check.md`. |
| `/red-team-review` | Pink (compliance, delegates to `/compliance-check`) → Red (narrative) → **Gold (rubric-driven scoring using [`reference/evaluator-rubrics/`](reference/evaluator-rubrics/) — adjectival ratings, Strengths/Weaknesses/Deficiencies with cited evidence, pWin estimate)** → White Glove |
| `/status` | Read-only: shows proposal type, pipeline progress, compliance coverage, and next recommended command. Use any time. |
| `/export-proposal` | **Converts markdown drafts to native Office formats.** Runs the **pre-submit quality gates** (prose-lint, structural lint, Strength preservation) in Preflight and blocks on any HIGH finding, then produces .docx (Word narratives), .xlsx (compliance matrix, pricing artifacts), .pptx (optional briefings), + graphics rendered to PNG. Writes to `final/`. User opens Word and saves as PDF for submission. Uses `anthropic-skills:docx/xlsx/pptx` and supports branded base templates at `my-company/templates/`. |
| `/capture-submission` | Snapshots the AI-generated draft and your final submitted version into `corpus/calibration/` for framework learning. Run twice: once after `/proposal-writer` (before editing) to capture the AI baseline, and again after submission to record your edits and improvement notes. |
| `/import-from-capture` | Imports a qualified opportunity from the capture-pipeline with solicitation facts and Go/No-Go pre-populated |

### Directory Structure

```
federal-proposal-assistant/
├── CLAUDE.md                        ← AI operating instructions
├── .claude/skills/                  ← Skill catalog (one directory per skill)
├── reference/                       ← Reusable standards and libraries
│   ├── methodology/                 ← Shipley-aligned BD process: bd-process, capture-planning,
│   │                                   color-teams, shipley-alignment
│   ├── proposal-conventions/        ← Vehicle-specific structural conventions (far-rfp, sbir,
│   │                                   gsa-mas, …) calibrated from real submissions
│   ├── proposal-types/              ← One file per proposal type — registry used by /new-proposal
│   ├── proposal-writing-patterns.md ← Four winning patterns: theme statements, discriminator
│   │                                   proof points, action captions, ghosting
│   ├── evaluator-rubrics/           ← Gold Team scoring rubrics per vehicle
│   ├── section-patterns/            ← Reusable section templates with placeholders
│   ├── graphic-templates/           ← Parametric HTML/SVG templates (three-tier-architecture,
│   │                                   capability-matrix, pitch-deck-conventions, …)
│   ├── pricing-artifacts/           ← Vehicle-specific pricing templates
│   ├── distribution-statements.md   ← Classification & distribution markings
│   └── style-guide.md               ← Federal proposal writing conventions
├── corpus/                          ← Calibration corpus (gitignored except structure)
│   └── calibration/                 ← (AI draft, final submission, edit notes) tuples per proposal
│                                       populated by /capture-submission; used by /red-team-review
│                                       --mode=lessons-learned to improve framework conventions
├── dashboard/                       ← Local Streamlit dashboard (`streamlit run dashboard/app.py`)
│                                       reads JSON sidecars to show portfolio state at a glance
├── templates/                       ← Empty proposal scaffold (copied by /new-proposal)
├── my-company/                      ← YOUR company profile (generated by /setup-company)
│   ├── company-description.md
│   ├── capabilities.md
│   ├── contract-vehicles.md
│   ├── past-performance.md
│   ├── evidence-ledger.json         ← Approved proof points, citations, metrics (used by /evidence-check)
│   └── brand-palette.md             ← Optional brand colors for graphics
└── proposals/                       ← Your proposals live here
    └── [proposal-name]/
        ├── inputs/                  ← Source materials
        │   ├── 00_priority/         ← Solicitation, eval criteria
        │   ├── 01_customer/         ← Mission context, constraints
        │   ├── 02_yourCompany/      ← Your capabilities (auto-seeded from my-company/)
        │   ├── 03_teammates/        ← Partner capabilities
        │   ├── 04_patterns/           ← Reference architectures
        │   ├── 05_graphic_standards/  ← Brand templates, visual standards (INPUTS only)
        │   └── 06_notes/              ← Meeting notes, raw inputs
        ├── working/                    ← Analysis artifacts + activity log
        ├── drafts/                     ← Proposal sections (markdown authoring)
        ├── graphics/                   ← Rendered HTML graphics + PNG (for Word embed)
        ├── reviews/                    ← Red team findings
        └── final/                      ← Native Office exports (docx/xlsx/pptx/pdf) — from /export-proposal
```

## What You Provide

| Step | What You Drop In | Where |
|------|-----------------|-------|
| 1 | Solicitation / RFP / white paper instructions | `inputs/00_priority/` |
| 2 | Customer context (mission, problem, constraints) | `inputs/01_customer/` |
| 3 | Your capabilities are auto-seeded from `my-company/` | `inputs/02_yourCompany/` |
| 4 | Teammate capabilities (if teaming) | `inputs/03_teammates/` |
| 5 | Reference architectures or past winning approaches | `inputs/04_patterns/` |
| 6 | Meeting notes, call summaries, raw inputs | `inputs/06_notes/` |

## What AI Produces

| Output | Location | Format |
|--------|----------|--------|
| Requirement matrix | `working/requirement-matrix.md` | Markdown table |
| Capability mapping | `working/capability-matrix.md` | Markdown table |
| Solution strategy | `working/solution-strategy.md` | Structured markdown |
| Architecture concept | `working/architecture-concept.md` | Structured markdown |
| Graphics specs | `working/graphics-brief.md` | ASCII wireframes + layout instructions |
| Rendered graphics (HTML) | `graphics/*.html` | Browser-viewable authoring master |
| Rendered graphics (PNG) | `graphics/rendered/*.png` | 2x DPI for Word embed |
| Draft sections | `drafts/*.md` | Markdown authoring layer |
| Red team findings | `reviews/*.md` | Issue table + recommended rewrites |
| Final Word documents | `final/docx/*.docx` | **Primary submission narrative format** |
| Final Excel workbooks | `final/xlsx/*.xlsx` | Compliance matrix, pricing artifacts |
| Final PowerPoint decks | `final/pptx/*.pptx` | Optional briefings, kickoff decks |
| Submission PDFs | `final/pdf/*.pdf` | User-produced via Word's Save As PDF |
| Package manifest | `final/PACKAGE.md` | Index of every deliverable |

## Graphics — Why This Changes Everything

For most proposal teams, graphics are the bottleneck. They require a dedicated graphic designer, multiple briefing cycles, and days of back-and-forth. Often the designer doesn't fully understand the technical content, and the result is either beautiful but inaccurate, or accurate but ugly.

**This tool eliminates that bottleneck.** The same AI that understands your solution architecture produces the visuals — and because it generates code (HTML/SVG), not pixel art, every element is precise, editable, and revision-ready.

### How It Works

Claude doesn't generate images like DALL-E or Midjourney. It writes **HTML and SVG code** that your browser renders as pixel-perfect graphics. This is a fundamental difference:

| | Image Generation AI (DALL-E, Midjourney) | This Tool (HTML/SVG) |
|--|---|---|
| **Output** | Raster image — pixels you can't edit | Structured code — every element is addressable |
| **Accuracy** | Approximate — may hallucinate labels, misspell text | Exact — text, labels, and structure are code, not guesses |
| **Revisions** | Regenerate from scratch and hope | Conversational: "make the font bigger" → CSS change in seconds |
| **Technical content** | Doesn't understand what it's drawing | Reads your architecture docs and draws from understanding |
| **Brand compliance** | No control over colors/fonts | Exact hex codes from your brand palette |
| **Print quality** | Resolution-dependent | Scales perfectly — SVG is resolution-independent |

### Why the Results Are So Good

1. **Context awareness.** Claude reads your solution strategy, architecture, and draft sections *before* generating graphics. Every box says the right thing, every flow goes the right direction, and every commitment matches the text — from the first version.

2. **HTML/SVG is the perfect medium.** Proposal graphics are structured information — boxes, arrows, labels, tables, timelines. They're not photographs. HTML/SVG is literally designed to render structured information, and Claude is exceptionally good at writing it.

3. **Instant iteration.** "Make the font bigger" is a CSS change. "Move the labels above the arrows" is an SVG coordinate adjustment. "Switch to our brand colors" is a hex value replacement. Each revision takes seconds, not a designer's calendar day.

4. **Encoded design knowledge.** The graphics skill contains hard-won lessons: minimum font sizes for print legibility (≥10pt body, ≥12pt headings, ≥18pt titles when embedded at standard column widths — enforced and checked in White Glove review), anti-patterns to avoid (emoji icons, text overlapping arrows, classification badges cluttering boxes), and proven layout patterns. Every graphic starts from a professional foundation.

5. **One person, full capability.** A proposal manager who can't draw a straight line in PowerPoint can now produce architecture diagrams, execution timelines, and capability matrices by describing what they need in plain English.

### What This Replaces

| Traditional Process | This Tool |
|---|---|
| Writer briefs graphic designer (30 min) | Claude reads the architecture directly |
| Designer produces first draft (4-8 hours) | First version generated in under a minute |
| 2-3 revision cycles (1-2 days) | Revisions are conversational, instant |
| Designer may not understand the tech | AI built the architecture *and* the graphic |
| Final graphic is a static image | Final graphic is editable code |
| Brand compliance requires manual checking | Brand palette applied automatically |
| **Total: 1-3 days per graphic** | **Total: 5-15 minutes per graphic** |

### Built-In Graphic Patterns

The skill includes proven patterns for common proposal visuals:

- **Three-tier architecture** — Horizontal bands (Enterprise → GCC → Edge) with registry pills, boundary lines, and flow arrows
- **Lifecycle loop** — Four nodes in a diamond with circular arc arrows and a center concept label
- **Capability matrix** — Products vs. Services two-column layout with accent-colored headers
- **Execution timeline** — Swim lane with parallel workstreams, phase columns, gate markers, and commitment callouts
- **Objectives** — Technical vs. Operational side-by-side with numbered items
- **Operational capabilities** — Row-based feature list with accent bars

### Brand Colors

If you provide brand colors in `my-company/brand-palette.md`, all graphics use your palette automatically. Specify your primary accent, background, text colors, and tier treatments — and every graphic is on-brand from the first render.

If no brand palette is provided, a professional default palette (dark background, clean typography, gold/blue accents) is applied.

## Tips

- **Run skills in order.** The architect skill feeds the writer, which feeds the reviewer. Skipping steps produces weaker output.
- **Iterate on graphics in HTML.** The HTML files are the primary deliverable — edit them directly for refinements rather than regenerating from specs.
- **Red team early.** Run `/red-team-review` on a partial draft to catch structural issues before writing all sections.
- **Captions go in the document, not the graphic.** Keep figure numbers and captions in your Word doc text, not embedded in the HTML graphic.
- **Check the section patterns.** `reference/section-patterns/` has fill-in-the-blank templates for every standard proposal section, organized by vehicle.
- **Run `/evidence-check` before Gold Team.** Resolving `CLAIM-UNSUPPORTED` markers before the Gold Team pass saves a round of rework — Gold Team automatically converts them to Weakness findings.
- **Capture every submission.** Run `/capture-submission` after writing (before you edit) and again after submission. This is how the framework learns from your real edits over time.
- **Portfolio visibility.** `streamlit run dashboard/app.py` gives a read-only view of all active proposals, compliance coverage, and AI run costs — useful when working multiple opportunities in parallel.

## Supported Proposal Types

Each type has a dedicated file in [`reference/proposal-types/`](reference/proposal-types/) declaring required skills, pricing artifact, page target, and evaluator framing. `/new-proposal` presents the menu and configures the workspace accordingly.

| Type ID | Vehicle | Pricing artifact | Page target |
|---|---|---|---|
| `far-rfp` | FAR Part 15 RFP | FAR cost volume | per Section L |
| `idiq-to` | IDIQ / GWAC task order | FAR cost volume | 10-30 |
| `gsa-mas-task-order` | GSA MAS BPA / task order | FAR cost volume | per PWS |
| `cso-brief` | CSO Solution Brief (Phase 1) | ROM | 5-10 |
| `cso-full` | CSO Full Proposal (Phase 2) | Commercial-item | 15-30 |
| `baa` | Broad Agency Announcement | FAR cost volume | 15-30 |
| `ota-white-paper` | OTA White Paper | ROM | 5-10 |
| `ota-proposal` | OTA Full Proposal | Milestone payments | 20-40 |
| `sbir-phase1` | SBIR Phase I | SBIR budget | per topic |
| `sbir-phase2` | SBIR Phase II | SBIR budget | per topic |
| `white-paper` | Unsolicited / directed | None | 3-10 |
| `rfi` | RFI response | None | 5-15 |
| `sources-sought` | Sources Sought | None | 2-5 |
| `rom` | Standalone ROM | ROM | 1-3 |

Adding a new type is a single-file change under `reference/proposal-types/` — no skill code changes required.

## Security & Data Handling

### Why This Is Better Than Uploading to ChatGPT

When you paste a proposal into ChatGPT or upload documents to a web-based AI, you have **no control over where that data goes.** It's uploaded to a third-party server, potentially used for model training, and you've lost custody of your content. For federal proposals containing proprietary capabilities, pricing strategies, teaming arrangements, and customer-specific intelligence, that's a serious problem.

This tool is different:

| | ChatGPT / Web AI | Federal Proposal Assistant |
|--|---|---|
| **Where files live** | Uploaded to cloud servers you don't control | On your local machine, in folders you own |
| **What you upload** | Entire documents, pasted wholesale | Only the content Claude needs to process for a specific task |
| **Training data** | Your content may train future models | Claude Code conversations are [not used for training](https://www.anthropic.com/policies) |
| **File structure** | Scattered across chat sessions | Organized, version-controlled, reusable across proposals |
| **Institutional memory** | Lost when the chat session ends | Persisted in skills, reference files, and company boilerplate |
| **Audit trail** | None | Git-trackable: every file change is visible |

### What Stays on Your Machine
- All files in `my-company/` — your capabilities, past performance, contract vehicles, pricing
- All files in `proposals/` — solicitations, drafts, analysis, graphics, reviews
- The skills and reference files — they're just local markdown files
- HTML graphics — rendered locally in your browser

### What Is Transmitted to Anthropic's API
When you run a skill, Claude reads files from your local directories and processes them. The **content of those files** passes through Anthropic's API during that processing. This is true of any AI tool that analyzes your documents — the key differences are:

1. **You control which files Claude reads.** It only processes what's in the proposal's `inputs/` and `working/` directories. Sensitive material you don't put there is never touched.
2. **No persistent storage.** Anthropic does not retain your conversation data for model training under their commercial terms.
3. **Selective processing.** Unlike pasting an entire 200-page RFP into ChatGPT, the skills read specific sections for specific tasks.

### Handling Sensitive / CUI / Classified Material

For proposals involving Controlled Unclassified Information (CUI) or sensitive content:

- **Isolate sensitive material.** Keep classified or highly sensitive source documents outside the proposal directory. Manually summarize key points into `inputs/06_notes/` in sanitized form. Claude works from your summaries.
- **Self-hosted API.** Organizations running Claude through AWS Bedrock or GCP Vertex AI keep all API traffic within their own cloud boundary. The skills work identically — just configure Claude Code to point at your endpoint.
- **Air-gapped environments.** When local model support becomes available in Claude Code, the entire workflow runs on-device with zero data transmission.

**Bottom line:** Your proposal files live on your machine, in your Git repo, under your control. AI processes only what you explicitly ask it to, under commercial terms that prohibit training on your data. That's fundamentally different from pasting your company's crown jewels into a chat window.

### Protecting proposal data (git-boundary guard)

This repo has a remote at `github.com/chakmarebel/federal-proposal-assistant`, **currently private** (verified 2026-08-01). The only thing keeping `proposals/`, `my-company/`, `signals/`, and the calibration corpus off that remote is `.gitignore` — a single `git add -f`, a stray `git add -A` on an untracked path, or an accidental gitignore edit can leak live solicitations, pricing, teaming, and customer intel. Treat the private setting as a second lock, not the first one: the guard assumes the repo could become public or gain collaborators at any time.

A **git-boundary guard** backstops `.gitignore`. It inspects the *staged* index and refuses any commit or push that stages sensitive paths (`proposals/`, `my-company/`, `signals/`, `corpus/calibration/<slug>/`, root-level `drafts/` `working/` `scrubs/` `reviews/`, and root `campaign_rollup.md` / `watchlist_table.md`), printing exactly what's staged and how to unstage it.

**Arm it once after cloning** (git does not track `.git/hooks/`, so a fresh clone ships unprotected):

```bash
bash scripts/install-hooks.sh          # points core.hooksPath at the tracked hooks/ dir
bash scripts/install-hooks.sh --verify # confirm it's armed
```

This installs both a **pre-commit** and a **pre-push** hook (redundant by design — pre-push catches a commit made with `--no-verify`). To check the current index by hand at any time, or to prove the guard itself works:

```bash
bash scripts/check-git-boundary.sh            # scan the staged index now
bash scripts/check-git-boundary.sh --selftest # prove it catches a staged proposal file
```

The guard's selftest is also asserted by `scripts/smoke-test.sh`, so CI/smoke runs fail if the leak protection ever breaks. If you genuinely intend to publish something under a protected path, edit `is_sensitive_path` in `scripts/check-git-boundary.sh` — do not bypass the hook.

#### The guard is path-based, so it cannot see content

`is_sensitive_path()` matches paths, not what is inside a file. A tracked file under `scripts/` or
`reference/` can therefore carry protected material and the guard will pass it. That is not a
defect — content inspection would be unreliable and noisy — but it means the path list is a
backstop, not a substitute for judgment about what goes into a tracked file.

**Known accepted exception (reviewed 2026-08-01):**

| File | What it carries | Why it is tracked |
|---|---|---|
| `scripts/backfill-demand-signals.py` | Customer and program names (DIA, USAFRICOM, USCYBERCOM J9, NATO DIANA, CDAO, Army Materiel Command, DAF AFLCMC, a Navy SOW) and candid gap admissions in its `STATUS` curation table — e.g. "Question declined. Physical manipulation is entirely outside the product line." | The curation table is the record of human judgment applied to the 2026-07-31 backfill. Inlining it is what makes that backfill auditable and reproducible from a fresh clone. Moving it to an untracked data file would keep the paths clean and make the result unreproducible. |

**Files committed before the guard existed stay tracked until untracked by hand.** The guard
inspects the staged index, so it stops *new* leaks; `.gitignore` does not untrack anything already
in the index. `scrubs/` and `my-company/` content landed 2026-05-30 and 2026-06-03; the hooks
arrived in July.

*Resolved 2026-08-01:* the ten `scrubs/` files (HubSpot deal IDs, dollar values, customer intel)
were removed from the index with `git rm --cached`. They remain on disk and are now ignored like any
other `scrubs/` content.

*Resolved 2026-08-04:* `my-company/evidence-ledger.json` and `my-company/past-performance.md`
untracked the same way. Both are still read from the working tree by `/evidence-check` and
`scripts/check-strengths.py`, which is unaffected — but the ledger now has **no copy in git at all**,
so the backup routine (`~/.claude/backups` after every append) remains worth running even here,
where the ledger is tracked — a tracked file is still destroyable by an uncommitted-changes stomp.

*Deliberately tracked in this repository:*

| Path | Contains | Why it is tracked |
|---|---|---|
| `my-company/**` | Company profile, evidence ledger, past performance, claim envelope, collateral | Tracked so collaborators stop working from stale snapshot zips. **Readable by every `edgerunner-ai` org member**, not just the direct collaborators: the org base repository permission is `write` and flows to all members, and GitHub does not permit a repo permission below the org base. Write for that audience, and move `my-company/` back out before making the repo internal or public. |
| `docs/framework-audit-2026-05.md` | Internal framework audit, names pursuits | Low sensitivity, no downstream consumer. Moved out of `reviews/` on 2026-08-20 so its path stops tripping the boundary guard. |

Confirm current state any time:

```bash
git ls-files | grep -E "^(scrubs|reviews|drafts|working|proposals|my-company|signals)/"
```

**`git rm --cached` clears `HEAD`, not history.** Every untracked file above is still reachable in
earlier commits. A genuine scrub needs `git filter-repo` (or BFG) plus a force push, which rewrites
shared history — worth doing before this repo goes public or gains collaborators, and not worth
doing casually while it is private and single-user.

This exception was accepted **on the condition that the remote stays private and single-user.**
Revisit it the moment either changes — if the repo goes public or gains collaborators, move the
curation table to `signals/backfill-curation.json` (untracked, boundary-protected) and have the
script read it. Nothing else in the tracked tree carries customer-identifying content at this
level of specificity; a quick audit:

```bash
git ls-files | xargs grep -ilE "USAFRICOM|USCYBERCOM|NATO DIANA|Army Materiel|AFLCMC" 2>/dev/null
```

## Requirements

- Claude Code (CLI) with an active Claude subscription
- A text editor for reviewing outputs
- A browser for viewing HTML graphics
- Microsoft Word or Google Docs for final document assembly

See the [Prerequisites](#prerequisites) table at the top for detailed runtime dependencies by feature.

## Pre-submit quality gates

Some defects survive Red Team / Gold Team / White Glove because they're introduced *after* those reviews — a section inserted without renumbering, a Significant Strength compressed out during a page-cut, an em-dash or a self-congratulatory sentence the model slipped in. `/export-proposal` runs three deterministic gate scripts in its Preflight step, before it renders any `final/` output. Each exits 1 on a blocking finding and stops the export:

```bash
python scripts/prose-lint.py --proposal <slug>             # prose quality / AI smell
python scripts/lint-document-structure.py --proposal <slug> # section numbering, figure refs, markings
python scripts/check-strengths.py --proposal <slug> --target docx  # Gold Team Strength preservation
```

`prose-lint.py` blocks (HIGH) on the section-sign glyph, em-/en-dashes or `--` used as sentence punctuation, and internal process vocabulary ("storyboard", "gold team", "narrative spine", …) leaking into customer-facing prose. It also surfaces advisories — marketing words, self-narration / performative-honesty commentary, prohibited-claim diction (FedRAMP, ATO, "accredited", …) without an evidence-ledger citation, and forbidden absolutes ("military-grade", "battle-tested", …) — which are reported but do not block. The rules track [`reference/PROSE-QUALITY-DOCTRINE.md`](reference/PROSE-QUALITY-DOCTRINE.md), the shared doctrine synced from the proposal-workbench project. You can run any gate by hand at any time; `/export-proposal` enforces them automatically.

## Framework integrity check

After cloning (or after making framework changes), run the smoke test to verify internal consistency — referenced files exist, proposal-type registry resolves cleanly, no deprecated paths remain, scaffold structure matches expectations:

```bash
bash scripts/smoke-test.sh
```

273+ checks run in under a second. Exits 0 on pass, 1 on fail with specific issues listed. Run this before any PR that touches skills, type registry, or reference files.

## Worked Examples

See [`examples/`](examples/) for fictional, redacted example workspaces showing the shape of a completed proposal:

- **[cso-brief-acme/](examples/cso-brief-acme/)** — CSO Solution Brief demonstrating the type registry, compliance matrix, all four writing patterns (theme statements, discriminator proof points, action captions, ghosting), ROM pricing artifact, and rubric-based Gold Team scoring.

Start here if this is your first proposal with the framework. The example's own README gives a guided tour.

## Contributing

This workflow was developed through real-world federal proposal writing. If you improve a skill or add a new pattern, please contribute it back.

## License

MIT
