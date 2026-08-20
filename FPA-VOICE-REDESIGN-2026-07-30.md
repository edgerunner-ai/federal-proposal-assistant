# FPA Voice Redesign — Decision Record (2026-07-30)

**Trigger:** ~20 revision rounds on army-brevity-companion converged on the same complaint:
grammatically correct prose that reads as robotic AI proposalese. Three independent looks
reached the same root cause — Bill's read, this workspace's own diagnosis mid-session, and
a third-party audit of the FPA skills. This record captures the agreed diagnosis, what was
implemented the same night, and the deferred sprint plan.

**Companion precedent:** [PROPOSAL-AGENT-REDESIGN-2026-05-15.md](PROPOSAL-AGENT-REDESIGN-2026-05-15.md)

## The verified diagnosis

Every factual claim in the third-party audit checked out against the repo:

| # | Claim | Verified |
|---|---|---|
| 1 | `proposal-writer` draft-loose injects the evaluation model and instructs "lead with what the listed evaluation factors reward" (SKILL.md line ~132), contradicting PROSE-QUALITY-DOCTRINE's "write first, audit afterward" | Yes |
| 2 | `reference/voice-anchors/bill-passage.md` is an empty placeholder — no genuine Bill-written anchor exists | Yes (142-byte comment) |
| 3 | The anchors the writer imitates are AI-polished passages carrying the banned constructions ("The issue is not... The issue is...", "The result is not...", "The value is operational rather than abstract") | Yes (vulcan-jatf-opening.md, socpac-section-3-4.md) |
| 4 | The editor has Narrative Naturalization (Mode 5) but no authority to recompose sentences from preserved facts | Yes |
| 5 | The theme-statement pattern requires one opening sentence to carry claim + relevance + proof hook, structurally producing the overloaded sentence | Yes |
| 6 | The calibration loop collects data (`capture-submission`) but `/recalibrate-framework` is not built — the system records lessons and does not learn | Yes |

**Root cause, one sentence:** the framework composes like a compliance system and asks an
editor to make it sound written; the voice exemplars it imitates are themselves AI prose.

**North-star metric (adopted):** minutes of human rewriting remaining per submitted page.
Not "passed all skills."

## Done the same night (2026-07-30, commit ba006b0 + this change set)

1. **Voice Standard** (11 rules, active/declarative/operator-focused) appended to
   `proposal-writer` and `proposal-editor` SKILL.md.
2. **Lint tripwires:** `ai_proposalese` term list + `explainer_tail` pattern in
   `reference/prose-lint-rules.json`, consumed by `scripts/prose-lint.py` as ADVISORY.
   Mutation-tested both directions.
3. **`reference/voice-profiles/proposal.md`** — the Operational Proposal Correspondent
   persona (compose-time identity; the Voice Standard is the constraint set; the pairs are
   the examples).
4. **`reference/voice-pairs/proposal/`** — seed corpus of six paired rewrites harvested
   from the army-brevity-companion scrub, one failure mode per pair. These are the real
   before/afters from the live document, applied under Bill's direction; Bill should bless
   or edit them before they become canonical calibration data.
5. Durable memory: `feedback_active_declarative_prose.md`.

## Deferred to the post-submission sprint (do NOT run before the ONIX upload)

### Sprint 1 — stop generating the problem
- **Remove the evaluation-model injection from draft-loose.** One amendment to the
  audit's version: the injection was added deliberately (evaluator-upstream port, PR #5)
  because Gold Team used to trigger structural rewrites. Do not delete factor-targeting;
  move it. The section brief's "Customer question / Direct answer" fields carry the aim
  at the factor without exposing rubric vocabulary to the prose. Derive briefs FROM the
  storyboard; keep the storyboard as the scoring artifact.
- **Weaken the theme-statement mandate** in `reference/proposal-writing-patterns.md` to a
  section lead: sentence 1 answers, sentence 2 gives relevance, mechanism and proof follow.
  Coupled change: `red-team-review` Gold scores the four patterns, so its rubric must move
  in the same commit or Gold will flag every compliant section.
- **Replace the AI-polished anchors.** Bill writes or heavily edits three genuine anchors
  (`bill-proposal-opening.md`, `bill-technical-approach.md`, `bill-executive-summary.md`,
  150-300 words each, representative rather than impressive). Until then, the existing
  AI anchors should be retired or clearly demoted — imitating them regenerates the defect.
- **Add editor Mode 6 `voice-reconstruction`:** extract the paragraph's facts, evidence,
  requirement, and commitment; discard the sentence constructions; recompose in the voice
  profile; restore evidence markers; verify no coverage lost. This formalizes what the
  2026-07-30 session did manually.

### Sprint 2 — separate prose planning from scoring
- Split the storyboard's writer-facing fields into `working/section-briefs.md` (customer
  question, direct answer, essential facts, evidence, boundary, handoff) and keep the
  evaluator fields in a scoring map the loose writer never sees.
- **Bind-pass discipline:** three allowed actions only — attach evidence metadata, replace
  an unsupported claim with a bounded one, or return a content patch request that
  regenerates the paragraph. Never bolt missing scoring content onto an existing sentence;
  sentence-stapling is the documented origin of the explainer tails.
- Additional lint advisories (density-based, not per-instance): sentences over ~35 words,
  more than two contrast constructions per paragraph, repeated benefit tails
  ("allowing/enabling/ensuring"), paragraph openers on abstract nouns. Per-instance flags
  on "rather than" or "which" would fire constantly and train people to ignore the lint.
- `voice_profile` field added to proposal types, orthogonal to `narrative_mode`
  (proposal / white-paper / technical-paper / market-response / pricing).

### Sprint 3 — make the system learn
- Grow the pairs corpus to 10-20 with Bill-approved rewrites.
- Build `/recalibrate-voice` (narrow scope): diff AI drafts vs submitted prose from the
  calibration corpus, classify recurring sentence-level edits, propose (never auto-apply)
  updates to anchors, pairs, lint advisories, and the persona. Regression set before
  adoption.
- **Fast lane** for small responses: submission-summary → requirement map → architecture →
  spine → section briefs → writer → bind → compliance → voice-reconstruction → export.
  Full pipeline stays for flagship pursuits.

## Upstream-sync obligations

`reference/PROSE-QUALITY-DOCTRINE.md` and the doctrine files sync from
`chakmarebel/proposal-workbench` and must not be hand-edited here; the voice profile,
Voice Standard, and pairs should be ported upstream so the sync never walks the FPA copies
backward. `reference/prose-lint-rules.json` is FPA-authoritative until the workbench
adopts it (per CLAUDE.md), so the local lint changes are legitimate as-is.

## Open questions for Bill

1. Bless or edit the six seed pairs; supply the three genuine anchors when time permits.
2. Confirm the amendment on factor-targeting (keep it in planning, out of prose) matches
   intent — this preserves the fix that the evaluator-upstream port made for a real,
   documented failure.
3. Fast-lane threshold: which proposal types default to it (rfi, cso-brief, rom?).
