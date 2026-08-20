# Skill Merge Proposal

**Date:** 2026-05-11
**Scope:** `federal-proposal-assistant/.claude/skills/` — 25 SKILL.md files inventoried.
**Status:** PROPOSAL ONLY — no merges or deletions executed. Awaiting Bill's review and explicit go-ahead before any consolidation.

> **Partially superseded on 2026-05-12.** The `audience: evaluator | internal` vocabulary recommended in this audit was replaced by `phase: setup|capture|planning|drafting|review|submission|inspection` after honest second-look review — the binary was too coarse and duplicated the SKILLS.md lifecycle grouping. The audit's `conflicts_with` recommendations were applied as proposed. The remaining unsettled item is the `new-proposal` ↔ `import-from-capture` consolidation (see [`../SKILLS-OPTIMIZATION-2026-05-12.md`](../SKILLS-OPTIMIZATION-2026-05-12.md) for context).

---

## Method

- Read every SKILL.md and characterized each by: purpose, workflow position, primary inputs, primary outputs, trigger phrases, and audience (evaluator-facing vs. internal-analysis).
- Estimated pairwise overlap by judgment — intent and content shape, not literal diff. Treated >~30% overlap as a merge candidate; lower overlap with high process-bleed risk treated as a "sharpen `conflicts_with`" candidate instead.
- Did NOT compute every C(25,2)=300 pair. Focused on pairs that share inputs, outputs, lifecycle phase, or trigger phrases.

## Inventory snapshot (audience tagging — proposed)

| Skill | Workflow phase | Audience | Primary output |
|---|---|---|---|
| opportunity-quick-look | Pre-bid triage | internal | working/quick-look.md |
| capture-portal-structure | Pre-bid (web-form only) | internal | inputs/00_priority/portal-format.md |
| capture-scorecard | Pre-kickoff readiness | internal | working/capture-scorecard.md |
| capture-intent | Pre-storyboard strategy | internal | working/capture-intent.md |
| customer-intel | Pre-architecture research | internal | working/customer-profile.md |
| competitor-assessment | Pre-architecture research | internal | working/competitor-assessment.md |
| proposal-manager | Plan extraction | internal | working/proposal-plan.{md,json} + compliance-matrix.md |
| proposal-solution-architect | Design | internal | working/requirement-matrix.md + capability-matrix.md + architecture-concept.md |
| past-performance | Drafting | evaluator | drafts/past-performance.md |
| pricing-analyst | Drafting | evaluator | drafts/<pricing-artifact>.md |
| proposal-storyboard | Pre-prose plan | internal | working/storyboard.md |
| technical-review | Feasibility gate | internal | reviews/technical-review-{approach,drafts}.md |
| proposal-graphics | Drafting | evaluator | working/graphics-brief.md + graphics/*.html |
| proposal-writer | Drafting | evaluator | drafts/*.md |
| proposal-editor | Drafting polish | evaluator | drafts/edited/*.md |
| compliance-check | Review | internal | reviews/compliance-gaps.md (updates matrix) |
| evidence-check | Review | internal | reviews/evidence-check.md |
| red-team-review | Review (multi-mode) | internal | reviews/{red,gold,white-glove,lessons-learned}-*.md |
| export-proposal | Submission packaging | evaluator | final/* |
| capture-submission | Post-submit calibration | internal | corpus/calibration/<slug>/ |
| import-from-capture | Workspace bootstrap | internal | proposals/<slug>/ |
| new-proposal | Workspace bootstrap | internal | proposals/<slug>/ |
| setup-company | One-time setup | internal | my-company/* |
| status | Inspection (read-only) | internal | (stdout only) |
| dashboard | Inspection (read-only, portfolio) | internal | (Streamlit UI only) |

Note: the user's example frontmatter listed `audience: evaluator` for proposal-writer. In this domain, `evaluator` vs. `internal` is the natural binary — `hill` doesn't apply. I propose using `audience: evaluator | internal` (drop `hill` for this repo).

---

## Findings

### True merge candidate (>30% overlap)

#### M1 — `new-proposal` ↔ `import-from-capture` (~60% overlap)

**Shared content:**
- Both scaffold `proposals/<slug>/` with the identical directory tree (inputs/00–06, working, drafts, graphics, reviews, final/...).
- Both seed `inputs/02_yourCompany/` from `my-company/*.md` using the same precedence rules.
- Both copy `my-company/distribution-statements.md` → `inputs/00_priority/` with the same fallback.
- Both seed `working/proposal-type.md` from `reference/proposal-types/<type_id>.md` and write the initial activity-log entry.
- Both write a `working/proposal-brief.md` from a near-identical template.

**Difference:** how the source data is collected — `new-proposal` asks the user interactively; `import-from-capture` reads a JSON payload from `capture-pipeline` (file / URL / paste).

**Evidence of implicit coupling:** `import-from-capture` SKILL.md already says "Use the **same scaffold contract as `/new-proposal`** — refer to `.claude/skills/new-proposal/SKILL.md` (Steps 2, 3, 3b) for the authoritative layout and seeding logic. Re-stating here only for visibility; if the two ever drift, `/new-proposal` is canonical." The skill already knows it's a thin variation.

**Recommendation: MERGE.**

Proposed merged skill: `new-proposal` (keep the name; it's the more general).
- Add `source: manual | capture-export | capture-url` as a mode parameter.
- The interactive scaffold flow becomes `source=manual` (default — preserves current behavior).
- The JSON-driven flow becomes `source=capture-export <path>` or `source=capture-url <url>`.
- Everything past the data-collection step (directory creation, my-company seeding, proposal-type.md, activity.md, proposal-brief.md, graphics-template copy) becomes shared code path.

**Risk: LOW.**
- Two skills already share an explicit contract; merging makes that contract code rather than prose.
- No external callers reference `import-from-capture` by name except the capture-pipeline export button's user-facing instructions ("download this JSON and run /import-from-capture"). That UI string would need a one-line update.
- CLAUDE.md references both — would need a one-line update.

**Alternative (if Bill prefers to keep two names):** keep both but extract the scaffold into a shared internal helper at `scripts/scaffold_proposal.py` and have both SKILL.md files call it. This solves drift without changing the user-visible skill surface. Lower-blast-radius but doesn't address the core duplication.

---

### Borderline candidates (~25–35% overlap)

These are pairs where overlap is real but the skills serve sequenced, distinct purposes. Recommendation for all: **keep separate, add sharp `conflicts_with` frontmatter** so the boundary is documented in-skill, not just in CLAUDE.md.

#### B1 — `opportunity-quick-look` ↔ `capture-scorecard` (~35%)

Both are go/no-go assessments with stoplight scoring, but at different points:
- quick-look = 5–10 min triage on a fresh opportunity, BEFORE `proposal-manager`. Inputs: just the solicitation. Output: pursue/pass/hold.
- capture-scorecard = 10–15 min readiness check, AFTER `proposal-manager` + `competitor-assessment`. Inputs: proposal-plan.md, competitor-assessment.md, customer-profile.md. Output: go/no-go on bid resources.

**Recommendation:** keep separate. Add to each:
- `capture-scorecard`: `conflicts_with: [opportunity-quick-look]` with comment "Don't run before proposal-manager — scorecard requires plan and competitive picture; use opportunity-quick-look for raw-solicitation triage."
- `opportunity-quick-look`: `conflicts_with: [capture-scorecard]` with comment "This is raw-solicitation triage; capture-scorecard is for post-plan readiness. Do not combine."

**Risk: LOW.** Process-bleed risk if the AI runs scorecard with no proposal-plan.md — it would either fail or hallucinate. The conflicts_with note is preventive.

#### B2 — `red-team-review --mode=gold` ↔ `technical-review --phase=drafts` (~30%)

Both run on completed drafts. Both produce reviews. Both check whether claims hold up.
- technical-review = chief-engineer perspective; flags architectural integrity, integration realism, ATO plausibility, claim truthfulness from an engineering standpoint.
- red-team-review --mode=gold = source-selection-evaluator perspective; rubric-driven adjectival ratings, S/W/D findings, pWin.

**Recommendation:** keep separate. Both should run; they're complementary lenses. Document explicitly that neither replaces the other.

- `technical-review`: `conflicts_with: [red-team-review]` with comment "Do not produce adjectival ratings or pWin estimates — that's red-team-review --mode=gold's job. Stay in the engineering-feasibility lane."
- `red-team-review`: `conflicts_with: [technical-review]` with comment "Do not assess architectural feasibility or integration realism from an engineering standpoint — that's technical-review's job. Evaluate from the evaluator's seat."

**Risk: LOW.** Currently both skills' SKILL.md respect the boundary. Frontmatter makes the discipline durable across future edits.

#### B3 — `compliance-check` ↔ `evidence-check` (~25–30%)

Both deterministic-leaning scans of `drafts/`. Both write to `reviews/`. Different concerns: compliance-check tracks requirement coverage; evidence-check tracks citation-marker integrity.

**Recommendation:** keep separate (they're complementary review gates, both feed red-team-review). Add `composes: []` to clarify they don't depend on each other but red-team-review composes both.

**Risk: LOW.** Already well-documented.

#### B4 — `status` ↔ `dashboard` (~30% in inputs read, near-zero in output mode)

Already documented: status = current-proposal CLI; dashboard = portfolio Streamlit. No real risk; explicit cross-reference in dashboard's SKILL.md.

**Recommendation:** keep separate, document in `conflicts_with` for completeness.

**Risk: LOW.**

---

### Sharpen-conflicts-with candidates (<30% but high process-bleed risk)

#### C1 — `proposal-writer` ↔ `proposal-editor` (~20% overlap, HIGH process-bleed risk)

writer drafts; editor polishes. Both touch `drafts/`. The writer's SKILL.md explicitly says: "Write for completeness and clarity. Do not optimize for brevity or tone polish; that is handled by `/proposal-editor`. The writer's job is to land every required point with traceable evidence; the editor's job is to tighten the prose."

This is exactly the kind of boundary that erodes silently. Strongly recommend `conflicts_with` frontmatter on both.

- `proposal-writer`: `conflicts_with: [proposal-editor]` — "Do not optimize for tone, brevity, or voice polish. Drafting prioritizes completeness and traceable evidence. Editorial pass is a separate skill."
- `proposal-editor`: `conflicts_with: [proposal-writer]` — "Do not re-derive claims, re-pull evidence, or invent new proof points. Editorial pass preserves the writer's content and tightens prose only."

**Risk of NOT doing this: MEDIUM.** Process-bleed makes Gold Team rewrites more expensive (writer over-polishes; editor under-polishes; both happen).

#### C2 — `red-team-review` ↔ `compliance-check` (historical overlap, now <10%)

The red-team-review SKILL.md notes its historical "Pink" team did compliance, which has been moved to `/compliance-check`. The boundary is fresh and could regress.

**Recommendation:** `red-team-review`: `conflicts_with: [compliance-check]` — "Do not re-run requirement-coverage diff. Compliance coverage is owned by /compliance-check, which writes reviews/compliance-gaps.md. Red-team consumes that output."

**Risk of NOT doing this: MEDIUM.** Easy regression as the SKILL.md grows.

---

### Confirmed-low-overlap pairs (no action needed, listed for completeness)

These pairs were considered and judged below the threshold:
- `proposal-manager` ↔ `proposal-solution-architect` (~25%, sequential — manager extracts, architect designs)
- `capture-intent` ↔ `competitor-assessment` (~20%, capture-intent says what to ghost; competitor-assessment provides the language)
- `capture-intent` ↔ `proposal-manager` (~15%, different strategy layers)
- `capture-portal-structure` ↔ `proposal-manager` (compose — portal-structure runs first for web-form types)
- `capture-submission` ↔ `red-team-review --mode=lessons-learned` (compose — submission captures, lessons reads)
- `proposal-storyboard` ↔ `proposal-graphics` (~15%, storyboard's "Graphic Argument" feeds graphics)
- `setup-company` ↔ `new-proposal` (one-time vs per-proposal; <5%)
- `past-performance` ↔ `proposal-writer` (sequential; PP feeds writer)

---

## Summary

| Recommendation | Pair | Action |
|---|---|---|
| **MERGE** | new-proposal ↔ import-from-capture | Consolidate into `new-proposal` with `source: manual\|capture-export\|capture-url` parameter |
| Sharpen `conflicts_with` | opportunity-quick-look ↔ capture-scorecard | Frontmatter only |
| Sharpen `conflicts_with` | technical-review ↔ red-team-review | Frontmatter only |
| Sharpen `conflicts_with` | compliance-check ↔ evidence-check | Frontmatter only |
| Sharpen `conflicts_with` | status ↔ dashboard | Frontmatter only |
| **Sharpen `conflicts_with` (HIGH PRIORITY)** | proposal-writer ↔ proposal-editor | Frontmatter only — this is the process-bleed pattern Bill flagged |
| **Sharpen `conflicts_with` (regression risk)** | red-team-review ↔ compliance-check | Frontmatter only |

**One merge proposed. Six pairs of sharpened `conflicts_with` frontmatter proposed.** All sharpening can ship in Step 3 (Item 1) without merge approval. Only the new-proposal/import-from-capture merge requires explicit Bill go-ahead.

---

## Risks

- **For the merge:** the JSON-driven path in `import-from-capture` has more downstream consumers than `new-proposal` (capture-pipeline's export button instructs users to "run /import-from-capture"). Renaming or removing that command will break that flow. Mitigation: either keep `import-from-capture` as an alias that dispatches to `new-proposal --source=capture-export`, or accept the breakage and update the capture-pipeline UI string.
- **For the `audience` tagging:** I'm proposing `audience: evaluator | internal` (dropping `hill`). If Bill wants `hill` or a different vocabulary (e.g., `pre-bid | drafting | review | post-submit | meta`), I can re-tag in Step 3.
- **For Item 5 in general:** none of these are urgent. The proposal-writer/proposal-editor and red-team-review/compliance-check sharpenings ARE worth doing soon because their boundaries are fresh and prone to regression.

---

## What I am NOT proposing

- No deletions.
- No skill renames (other than the one optional alias above).
- No CLAUDE.md restructuring.
- No changes to the `reference/` or `templates/` directories.
- No retroactive changes to existing proposal-instance worktrees under `proposals/<slug>/.claude/`.

---

## Pending Bill's decision

1. Approve / reject / modify the `new-proposal` + `import-from-capture` merge.
2. Approve / reject / modify the `audience: evaluator | internal` tag vocabulary.
3. Approve sharpened `conflicts_with` to be applied in Step 3 (Item 1) — this is the default path unless Bill objects.

I will not execute any merges in this session even if approved here. Step 3 will apply only the `conflicts_with` frontmatter sharpening; an actual merge becomes a separate dedicated task.
