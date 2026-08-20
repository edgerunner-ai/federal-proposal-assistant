# Prose-Lint Rules Port + Gate Wiring (Workbench Merge, 2026-06-04)

## Goal

Bring the new prose-quality rules authored in proposal-workbench into federal-proposal-assistant (FPA), and wire them into the export gate so they actually fire — not just exist as a script a human might remember to run.

This is the successor to [`WP-N2-PROSE-QUALITY-PORT-2026-05-30.md`](WP-N2-PROSE-QUALITY-PORT-2026-05-30.md). WP-N2 made FPA a consumer of the workbench prose-quality doctrine and voice anchors. This change ports the next batch of rules the workbench added (commit `7761b16`) and closes the wiring gap WP-N2 left open: `prose-lint.py` existed in FPA but no skill or gate invoked it.

## Origin

The rules were authored on the proposal-workbench branch `claude/workbench-structured-writing-approach-fZmVn` (commits `7761b16` prose-lint rules + doctrine, `163c737` generation-time prompting). On 2026-06-04 that branch was fast-forward merged into `chakmarebel/proposal-workbench` `master` (`ee6c6fb..163c737`, 11 new commits) and the merged branch was deleted from the remote.

The merge moved a large amount into the *workbench app* (the `discipline-as-software` white-paper set, doctrine-knowledge layering, a company doctrine-overrides panel, generation-time prompting). **None of that app code runs in FPA.** FPA is a Claude Code skill workspace; the only channel between the two repos is the doctrine sync, which carries markdown, not code. The portable surface for FPA was exactly two things: the prose-lint rules and the two paired doctrine sections.

## What Crossed Into FPA

1. **Four prose-lint rule groups** ported into `scripts/prose-lint.py`, adapted from the workbench's dataclass style to FPA's `(severity, line, message)` tuple style:
   - `EM_DASH` (**HIGH**, exit 1): em-/en-dash or `--` as sentence punctuation. Excludes markdown horizontal rules (`---`) and table separators (`|---|`) by requiring surrounding whitespace or word characters on the double-hyphen forms.
   - `META_COMMENTARY` (advisory): self-referential / performative-honesty prose ("saying so is itself a signal that we understand…", "in the interest of candor", "a capability we do not hold").
   - `PROHIBITED_CLAIM_TERMS` (advisory): categorical compliance diction (`fedramp`, `soc 2`, `iso 27001`, `cmmc`, `sprs`, `ato`, `accredited`, …) that needs an evidence-ledger citation. prose-lint cannot see ledger state, so these surface as advisories for a human or the evidence gate to confirm or move to a Gaps note.
   - `FORBIDDEN_ABSOLUTES` (advisory): implicit-superiority absolutes (`military-grade`, `battle-tested`, `unmatched`, `most secure`, `bank-grade`). Bare "best"/"only"/"first" deliberately excluded to avoid false positives.

2. **Two doctrine sections** applied to `reference/PROSE-QUALITY-DOCTRINE.md`, matching canonical workbench master so the next `tools/sync-voice-anchors.sh` run is a no-op for them:
   - "Self-narration and performative honesty -- a second tone-drift failure" (the mirror of ventriloquism: overreach about *our own* virtue rather than the *customer's* internal state).
   - "Typography -- no dashes as sentence punctuation".
   - Plus the paired em-dash fix on the existing ventriloquism line.

## Capability Assessment

The net delta is real but was **latent on arrival**:

- **New detection surface.** FPA's prose lint now catches dashes-as-punctuation (blocking), self-narration, prohibited-claim diction, and forbidden absolutes — on top of the pre-existing section-glyph, process-vocab, marketing-word, "we will", and repeated-opening checks.
- **Wiring gap (now closed).** Before this change, `prose-lint.py` was referenced only by itself and the doctrine doc. The CLAUDE.md pre-submit gate ran only `lint-document-structure.py` + `check-strengths.py`, and `/export-proposal` invoked no gate at all. The new rules fired only if a human ran the script by hand — real-world impact ≈ 0. **This change wires prose-lint into the export Preflight (HIGH blocks) and into the CLAUDE.md gate block.**
- **Generation-side gap (still open).** The workbench *also* prevents these at generation time (the `163c737` prompting changes). FPA only catches them at lint. `reference/editorial-voice-guide.md` still names only ventriloquism — nothing about dashes, self-narration, or prohibited-claim diction — so the model keeps *producing* them during drafting and we catch them afterward. Closing this would follow the WP-N2 pattern: inline the new rules into the editorial voice guide so the writer/editor see them in-context. **Not done here.** See Remaining Follow-Ups.

## Implementation

1. `scripts/prose-lint.py` — added the four rule-group constants (`EM_DASH`, `META_COMMENTARY`, `PROHIBITED_CLAIM_TERMS`, `FORBIDDEN_ABSOLUTES`) and their per-line checks inside `lint_file`; updated the module docstring's severity legend. (Committed as `8171840`.)
2. `reference/PROSE-QUALITY-DOCTRINE.md` — applied the two new doctrine sections and the paired em-dash fix. (Committed as `8171840`.)
3. `CLAUDE.md` — expanded the pre-submit gate block from two scripts to three; prose-lint listed first, with a paragraph describing what blocks (HIGH) vs. what is advisory.
4. `.claude/skills/export-proposal/SKILL.md` — added a blocking pre-submit gate as Preflight step 5: run `prose-lint.py` and `lint-document-structure.py` against the drafts before rendering any `final/` output; stop and report if either exits 1; re-run structural + `check-strengths.py --target docx` after the Word render.
5. `README.md` — added a "Pre-submit quality gates" section and noted the gate in the `/export-proposal` skills-table row.

## Determinism

Rules 1–2 are deterministic, stdlib-only Python and markdown. Rules 3–5 are documentation and skill-instruction changes — no new model calls, no new runtime behavior beyond invoking the existing deterministic gate scripts.

## Test Plan / Results

```bash
python scripts/prose-lint.py <dirty.md>   # 1 HIGH (em-dash) + advisories; exit 1
python scripts/prose-lint.py <clean.md>   # OK on prose w/ table, "---" rule, "10-20" range; exit 0
python scripts/skill-graph.py --validate-only      # OK: 28 skills, all refs valid
python scripts/build-skills-index.py --check       # OK: SKILLS.md up to date
bash scripts/smoke-test.sh                         # 339 passes, 0 warnings, 0 failures
```

All passed on 2026-06-04.

## Remaining Follow-Ups (not done)

- **Generation-side prevention.** Inline the new rules (no dashes, no self-narration, prohibited-claim diction) into `reference/editorial-voice-guide.md` so the writer/editor avoid them while drafting, per the WP-N2 inline pattern. This is the highest-value next step — it moves the rules from "catch after" to "don't produce".
- **Universal doctrine knowledge files.** The workbench added `prohibited-claims-doctrine.md`, `output-discipline.md`, and `acronyms-federal.md` under its backend knowledge dir. These are portable as FPA reference material (e.g. under `reference/`), and the prohibited-claim list could be tied to `my-company/evidence-ledger.json`.
- **Doctrine sync timing.** The two doctrine sections were hand-applied to match canonical master; a future `tools/sync-voice-anchors.sh` run will reproduce them as a no-op. No action needed unless the upstream doctrine diverges.

## Out Of Scope

- Porting any proposal-workbench *app* code (backend/frontend) — it does not run in FPA.
- The `discipline-as-software` white-paper content that merged to workbench master.
- Any change to the existing loose/bind model, voice-anchor wiring, or section-opening guidance.
