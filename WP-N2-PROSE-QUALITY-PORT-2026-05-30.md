# WP-N2 -- FPA Prose-Quality Doctrine Port

## Goal

Port the shared federal proposal prose-quality doctrine and canonical voice anchors from proposal-workbench into federal-proposal-assistant (FPA), closing the remaining Track A prose-quality gaps without disturbing the Track A work FPA already implements.

WP-N2 makes FPA a consumer of the doctrine published by proposal-workbench in WP-N1:

- `reference/PROSE-QUALITY-DOCTRINE.md`
- `reference/voice-anchors/*.md`
- `tools/sync-voice-anchors.sh`

The port also places the most operational voice-doctrine rules directly into FPA's editorial voice guide so writer/editor skills see them in-context while drafting.

## Current State To Build On

FPA is already ahead of the original redesign baseline.

Already implemented:

- **A1 narrative spine:** `.claude/skills/narrative-spine/SKILL.md` creates the one-page pre-prose argument and human sign-off point.
- **A2 loose/bind split:** `.claude/skills/proposal-writer/SKILL.md` documents `draft-loose`, `bind`, and `full`, with composition structurally separated from evidence binding.
- **A4 section-opening de-mandate:** the writer and editorial guide already reject repeated formulaic openings and require concern-first openings.
- **A6 rubric inversion:** the writer already says "No writing to pass Gold Team" during the loose pass.

Remaining N2 gaps:

- **A3 voice anchors:** FPA has no `reference/voice-anchors/` directory.
- **Reframe, then polish doctrine:** FPA's voice/style references do not yet name ventriloquism or require bounded epistemic phrasing for customer-internal claims.

Canonical sources:

- `proposal-workbench/PROSE-QUALITY-DOCTRINE.md` -- canonical shared doctrine.
- `proposal-workbench/reference/voice-anchors/*.md` -- canonical voice anchors.
- `proposal-workbench/tools/consumer-sync-template.sh` -- consumer sync template.
- `proposal-workbench/docs/cross-app-doctrine-sync.md` -- pull-side, consumer-owned sync model.
- `PROPOSAL-AGENT-DIAGNOSIS-2026-05-15.md` -- FPA diagnosis explaining the 70% prose ceiling.
- `PROPOSAL-AGENT-REDESIGN-2026-05-15.md` -- Track A prescription N2 completes for FPA.

## Implementation

### 1. Add The Consumer Sync Script

Copy proposal-workbench's `tools/consumer-sync-template.sh` into FPA as:

```text
tools/sync-voice-anchors.sh
```

Keep the default settings:

- `WORKBENCH_REPO=chakmarebel/proposal-workbench`
- `WORKBENCH_REF=master`
- `DEST_DOCTRINE=reference/PROSE-QUALITY-DOCTRINE.md`
- `DEST_ANCHORS=reference/voice-anchors`

Make the script executable. This repo consumes doctrine intentionally; it does not use cross-repo automation.

### 2. Run The Sync

Run `tools/sync-voice-anchors.sh` from the FPA repo root.

The sync must create:

- `reference/PROSE-QUALITY-DOCTRINE.md`
- `reference/voice-anchors/vulcan-jatf-opening.md`
- `reference/voice-anchors/socpac-section-3-4.md`
- `reference/voice-anchors/bill-passage.md`

`bill-passage.md` is intentionally comment-only until a confirmed Bill-written passage is added upstream.

### 3. Inline Operative Voice Doctrine

Add a `Voice doctrine -- reframe, then polish` section near the top of `reference/editorial-voice-guide.md`.

The inline section must:

- point to `reference/PROSE-QUALITY-DOCTRINE.md` as canonical;
- name *ventriloquism* as the failure mode;
- preserve the reframe -> polish order;
- include bounded-epistemic phrasing examples;
- state that objective facts may remain declarative while unstated customer priorities/challenges/decisions/posture require bounded phrasing;
- add a `Voice anchors -- imitation, not rules` subsection pointing at `reference/voice-anchors/`.

The full doctrine lives in `reference/PROSE-QUALITY-DOCTRINE.md`; the voice guide carries only the operative drafting snippet.

### 4. Wire Voice Anchors Into Skills

Modify only these two skill bodies:

- `.claude/skills/proposal-writer/SKILL.md`
- `.claude/skills/narrative-spine/SKILL.md`

Add `reference/voice-anchors/*.md` to each skill's mandatory inputs.

For `proposal-writer`, the note must say anchors are read before composing the loose draft, orient cadence/confidence, must not have content reused, and take precedence over banned-word lists when they conflict.

For `narrative-spine`, the note must say anchors orient the spine's cadence because the spine is the first place voice matters and carries forward into the writer.

Do not alter the existing loose/bind model, no-Gold-Team-writing rule, or section-opening guidance.

### 5. Add Cross-References

Add a short pointer in `CLAUDE.md`:

```markdown
**Voice doctrine.** See `reference/PROSE-QUALITY-DOCTRINE.md` (canonical, synced from `chakmarebel/proposal-workbench` via `tools/sync-voice-anchors.sh`).
```

Add a similar pointer to `reference/style-guide.md`. Do not duplicate the full inline doctrine in the style guide.

## Determinism

WP-N2 is documentation, skill instruction, and sync-script work only. It adds no model calls and no runtime behavior.

The sync script is deterministic for a given `WORKBENCH_REPO` and `WORKBENCH_REF`: it replaces the doctrine file and anchor directory with the canonical upstream files.

## Acceptance Criteria

- `tools/sync-voice-anchors.sh` exists, is executable, and keeps the proposal-workbench defaults.
- Running the script creates `reference/PROSE-QUALITY-DOCTRINE.md` plus all three canonical voice anchors.
- Re-running the script without upstream changes produces no file diff.
- `reference/editorial-voice-guide.md` includes the reframe/polish and ventriloquism guard section.
- `reference/style-guide.md` and `CLAUDE.md` point to the canonical doctrine.
- `proposal-writer` and `narrative-spine` list `reference/voice-anchors/*.md` as mandatory inputs.
- Skill graph validation still passes.
- Skill index check still passes.

## Test Plan

Run from the FPA repo root:

```bash
tools/sync-voice-anchors.sh
tools/sync-voice-anchors.sh
git diff --exit-code -- reference/PROSE-QUALITY-DOCTRINE.md reference/voice-anchors tools/sync-voice-anchors.sh
python scripts/skill-graph.py --validate-only
python scripts/build-skills-index.py --check
```

Manual review:

- Confirm the editorial voice guide's inserted section reads naturally with the surrounding context.
- Confirm no unrelated skill behavior changed.

## Out Of Scope

- WP-N3 copilot port.
- Any further Track A changes: A1, A2, A4, and A6 are already implemented in FPA.
- Any Track B narrative-first tool work.
- Any other `SKILL.md` modifications.
- Refactoring existing FPA style or workflow content unrelated to voice doctrine.

## File By File

- `tools/sync-voice-anchors.sh`: copied sync script from proposal-workbench.
- `reference/PROSE-QUALITY-DOCTRINE.md`: synced canonical doctrine.
- `reference/voice-anchors/*.md`: synced canonical anchors.
- `reference/editorial-voice-guide.md`: inline operative voice doctrine.
- `reference/style-guide.md`: one-line doctrine pointer.
- `CLAUDE.md`: one-line doctrine pointer.
- `.claude/skills/proposal-writer/SKILL.md`: mandatory voice-anchor input.
- `.claude/skills/narrative-spine/SKILL.md`: mandatory voice-anchor input.
- `WP-N2-PROSE-QUALITY-PORT-2026-05-30.md`: implementation spec.

## Sequencing

1. Branch `pe-n2-prose-quality-port` from `origin/main`.
2. Write this spec.
3. Copy and chmod the sync script.
4. Run the sync.
5. Inline the operative voice doctrine.
6. Wire voice anchors into proposal-writer and narrative-spine.
7. Add CLAUDE/style-guide cross-references.
8. Run sync idempotence and skill validation.
9. Commit, push, and open a PR.
