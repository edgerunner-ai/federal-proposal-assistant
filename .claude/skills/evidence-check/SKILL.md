---
name: evidence-check
description: Audit draft evidence citations against my-company/evidence-ledger.json — flag CLAIM-UNSUPPORTED, typos, retired/restricted IDs. Run after proposal-writer, before red-team-review --mode=gold.
phase: review
composes: [proposal-writer]
conflicts_with: []  # complementary to compliance-check; both feed red-team-review
---

# /evidence-check

## Purpose

Phase C of v1.5 introduces **evidence-grounded drafting**: every major claim in a proposal links to an evidence item in `my-company/evidence-ledger.json` via an HTML comment marker. This skill audits those links.

Running this skill tells you:
1. **Unsupported claims** — the writer flagged a claim but couldn't find evidence (or a claim slipped in without a marker at all — detection is heuristic)
2. **Typo'd or stale IDs** — the draft cites `EV-022` but the ledger has no such entry (or it's retired)
3. **Restricted-context violations** — an `approval_status: restricted` item was cited in a proposal type the restrictions forbid
4. **Unused evidence** — approved items in the ledger that no draft cites — strong proof points you might be missing in the narrative

Gold Team in `/red-team-review` automatically converts `CLAIM-UNSUPPORTED` markers into Weakness findings, so running `/evidence-check` and resolving its output **before** Gold Team saves you rework.

## Citation format (established in proposal-writing-patterns.md)

### Supported claim — HTML comment with one or more evidence IDs

```markdown
Our platform has operated at [customer] for 14 months in fully disconnected mode. <!-- evidence: EV-022 -->
```

Multiple IDs allowed:
```markdown
On-device inference <!-- evidence: EV-001 --> has been validated at operational scale <!-- evidence: EV-022, EV-055 -->.
```

### Unsupported claim — explicit marker

```markdown
Our on-device inference is the fastest in the industry. <!-- evidence: CLAIM-UNSUPPORTED -->
```

Writer should mark these explicitly when it can't find evidence. Gold Team treats them as Weaknesses until resolved.

## What it reads

1. `working/proposal-type.md` — determine proposal-type for restriction checks
2. `my-company/evidence-ledger.json` — the approved evidence library
3. `drafts/*.md` — scanned for `<!-- evidence: ... -->` markers by `scripts/evidence_check_core.py` (the deterministic checker this skill runs first). Since 2026-09-04 the same scan also audits the `evidence: EV-###` key line of every `:::callout` sidebar block (`proposal-writer` Step 2e); such a marker reports its context as `callout: <title>`. A callout with no `evidence:` line is not a marker at all, so it never shows in the count: treat a box without one as a missing citation and report it under unsupported claims.
4. `working/compliance-matrix.json` (if exists) — read rows to understand which claims should be evidence-backed
5. `working/proposal-plan.json` (if exists) — read discriminators (each should have evidence_refs)

## Algorithm — the code decides, this skill narrates and triages

**The audit itself is deterministic code, not hand-reasoning.** Do NOT re-derive the
marker classifications yourself. Run the checker first and reason over its JSON output
(migration boundary: `docs/evidence-check-feature-map.md`; governance:
`docs/DECISION-canonical-ownership.md` action #4).

### Step 1: Run the deterministic checker

```bash
python scripts/evidence_check_core.py <proposal>/drafts/*.md my-company/evidence-ledger.json --json
```

(The ledger path is always the **last** argument. Add `--no-warrant` to skip the engine
call; `--warrant-src <path>` / `FPA_WARRANT_SRC` point at a non-default warrant checkout.)

The JSON gives you everything the old hand-audit produced:
- `markers` — total / supported / unsupported / `coverage_pct` (marker-denominated, the FPA contract)
- `findings.unsupported_claims` — every `CLAIM-UNSUPPORTED` marker with file/line/sentence
- `findings.unknown_ids` — typo'd/missing IDs, each with a nearest-ID `suggestion` when unambiguous
- `findings.retired_ids` — retired evidence cited (must be replaced or removed)
- `findings.restricted_ids` — restricted evidence cited, **with the restrictions text** (see Step 2)
- `findings.pending_ids` — `pending_review` citations (warn: don't submit until approved)
- `findings.unused_approved` — approved evidence no draft cites
- `warrant` — the canonical verification engine's verdicts (see Step 3)

If the ledger file does not exist, emit a warning: "No evidence ledger found at `my-company/evidence-ledger.json`. Run the Phase C seeding process (see reference/examples/evidence-ledger.example.json) to create one." Exit with a "framework-not-ready" status but don't fail the skill.

### Step 2: Adjudicate what the code cannot

Two findings need YOUR judgment on top of the checker's facts:
- **Restricted citations → violation or legitimate?** For each `findings.restricted_ids` row, read the restrictions text against `working/proposal-type.md` (distribution, audience, proposal type). Forbidden context → **RESTRICTED_VIOLATION**; permitted context → note as compliant restricted use.
- **Unused evidence → worth citing?** For each `findings.unused_approved` ID, check the ledger entry's `relevance_tags` against the current proposal's domain (from `working/proposal-plan.json` win themes or the proposal type's evaluator framing) and surface fits as "Consider citing."

### Step 3: Consume the warrant verdicts (when available)

The checker also calls the canonical verification engine (`warrant_ledger`, from the
edgerunner-warrant repo) with the FPA ledger adapted in-memory to the canonical schema.
Warrant proves citation **admissibility** (cited ID exists + approved + content-overlap
floor), *not* entailment. When `warrant.available` is true, triage:
- `citation-weak` verdicts — an approved ID stapled to a sentence that shares almost no content with the cited entry (cite-spam suspect). Flag for the author; never auto-accept.
- `gate.decision` (`pass`/`flag`/`block`) and `summary.grounding_rate` — report as advisory context for Gold Team. Export blocking stays with the pre-submit scripts.
- The `wbom` block — the portable audit receipt; reference it in the review artifact.

When `warrant.available` is false (the engine repo isn't on this machine), the checker
says so and the marker audit above is complete on its own — report the fallback, don't
approximate the missing verdicts.

### Step 4: Update the coverage metric

Update `working/compliance-matrix.json`'s summary block with an `evidence_coverage_pct` field, using `markers.coverage_pct` from the checker (writer of that file is `compliance-check`; this skill is allowed to update the `evidence_coverage_pct` field only).

Or if the matrix doesn't exist (e.g., type has no compliance_sources), just report coverage inline in the review.

## What it writes

### `reviews/evidence-check.md`

```markdown
# Evidence Check — <proposal name>

**Date:** <timestamp>
**Ledger:** my-company/evidence-ledger.json (N approved, M pending, K retired, J restricted)
**Drafts scanned:** N files
**Total claim markers:** N
**Supported:** N (coverage: X%)
**Unsupported:** N
**Unknown IDs:** N
**Retired IDs cited:** N
**Restricted violations:** N

## Unsupported claims

(Each flagged `CLAIM-UNSUPPORTED` marker)

- **drafts/technical-approach.md §3.2 line 47:** "Our on-device inference is the fastest in the industry."
  - Recommendation: find/add evidence (consider EV-055 which benchmarks pipeline speed) OR soften claim OR remove.

## Unknown / typo'd IDs

- **drafts/executive-summary.md line 18:** cited `EV-222` — not found in ledger. Likely typo for `EV-022`?

## Retired IDs cited

(list — these must be replaced or removed before submission)

## Restricted violations

(list — these citations violate the evidence item's restrictions for the current proposal type)

## Unused approved evidence worth considering

- **EV-031 (named_personnel):** Dr. Jane Doe — DARPA continuity. Tags: darpa, neuro-symbolic. Fits this proposal's DARPA emphasis.
- **EV-067 (capability_claim):** FedRAMP Moderate. Tags: fedramp, il5, ato. Might strengthen AoI-4 response.

## Coverage summary

- Total claim markers: N
- Supported: N (X%)
- Unsupported: N
- Target: zero unsupported markers before Gold Team

## Warrant engine (advisory)

(Only when `warrant.available` — otherwise state: "Warrant engine unavailable on this machine; marker audit is authoritative.")

- Gate: <pass|flag|block> — <reasons>
- Grounding rate (claim-sentence denominated, floor not census): X%
- Citation-weak (cite-spam suspects): N — list file/sentence for author review
- WBOM receipt: attached / summarized
```

### Updated `working/compliance-matrix.json` (if present)

Adds or updates `summary.evidence_coverage_pct`.

### Activity trail

Append to `working/activity.md`:

```
## <timestamp> — evidence-check — <N supported> / <M unsupported> / <K unknown> / <J retired>, coverage <X>% → reviews/evidence-check.md
```

Append to `working/ai-runs.jsonl`:

```json
{"schema_version":"ai-run.v1","timestamp":"<ts>","skill":"evidence-check","proposal_id":"<slug>","job_type":"review","notes":"deterministic scan, no AI invocation"}
```

Note: this skill is **primarily deterministic** — it's a structural diff, not an AI inference task. It should log a run entry anyway for audit completeness, but `model`, `input_tokens_estimate`, and `output_tokens_estimate` can all be `null`.

## When to run

1. **After every `/proposal-writer` pass** — catches typos and unsupported claims while the writer's context is fresh
2. **Before every `/red-team-review --mode=gold`** — Gold Team treats unsupported claims as automatic weaknesses, so fix them first
3. **Before final `/export-proposal`** — submission gate: target zero unsupported, zero retired, zero restricted violations

## Rules

- **Never modify drafts/*.md.** This skill is read-only over drafts. User resolves findings by editing drafts themselves or re-running writer on specific sections.
- **Never modify the evidence ledger.** Ledger is curated by the user or `/setup-company`. This skill reports; user curates.
- **Never invent evidence IDs.** If an unknown ID is found, flag it. Do not "fix" it by creating a new ledger entry.
- **Always update `working/compliance-matrix.json`** with the evidence_coverage metric (if the matrix exists) so Gold Team and dashboard see current coverage.

## When the ledger doesn't exist yet

If `my-company/evidence-ledger.json` is missing, emit guidance rather than failing:

> **No evidence ledger found.**
>
> This workspace expects `my-company/evidence-ledger.json` to be populated from your actual past performance, capabilities, and credentials. See `reference/examples/evidence-ledger.example.json` for the shape, and `reference/schemas/evidence-ledger.schema.json` for the full schema.
>
> To seed your ledger from your existing `my-company/` content:
> 1. Read `my-company/past-performance.md` and `my-company/capabilities.md`
> 2. Create one `EV-###` entry per distinct proof point (contract, deployment, credential, capability claim)
> 3. Set `approval_status: "approved"` for items cleared for public citation
> 4. Commit the file locally (it's gitignored — stays on your machine)
>
> Until the ledger exists, Phase C drafts can still be produced; they just won't be citation-backed. Plan to seed the ledger before your next major proposal.
