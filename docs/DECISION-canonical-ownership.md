# Decision: Canonical Ownership Across the Proposal/Capture/Verification Repos — v2

**Status:** Proposed (pending Bill's ratification) · **Date:** 2026-07-06 (v2, same day) · **Type:** Cross-repo architecture decision
**Applies to:** `federal-proposal-assistant` (FPA), `capture-pipeline`, `proposal-workbench`, `edgerunner-warrant`
**Supersedes/relates:** FPA `docs/proposal-workbench-v2-architecture.md`, workbench `docs/FPA-SKILLS-MIGRATION-PLAN.md` + `docs/WARRANT-INTEGRATION-BRIEF.md`
**Copy of this file lives in each repo** at `docs/DECISION-canonical-ownership.md` (one-way synced from FPA, the decision's home).

> **v2 — corrected against the actual code after adversarial review + counter-audit (`FINAL-ADJUDICATION-2026-07-06.md`); supersedes v1, which contained factual errors about the codebase.** The main corrections: the workbench's capture files are not copies of capture-pipeline code (only `web_fetch.py` is a labeled port), so the "sync-fork" action was impossible as written; FPA's `bind`/evidence-check are LLM skill prompts, not code, so "migrate behind existing tests" was unexecutable for FPA; and the capture→proposal contract seed is merged and deployed (the "unmerged" charge against it was itself false). Every Required Action below is now executable against the repos as they exist.

---

## Context

Four repos have overlapping responsibilities and no declared owner per capability. As a result the same **capabilities** (not, for the most part, the same code) are implemented in multiple places and are drifting:

- **Capture capability overlaps.** capture-pipeline owns intake/triage/scoring/HubSpot with 7 live instances. The workbench maintains five capture-adjacent files (`hubspot_intake.py`, `capture_context.py`, `quick_look.py`, `bid_decision_gate.py`, `web_fetch.py`). Verified against capture-pipeline's full git history: **these are not copies** — only `web_fetch.py` is a genuine labeled port (of capture-pipeline's `app/doc_extract.py`); the rest are workbench-native with conceptual lineage only (`quick_look.py` descends from FPA's opportunity-quick-look playbook). The problem is a parallel intake/scoring path, which drifts *semantically* — no diff will ever show two scorers disagreeing.
- **Verification capability exists three times, in three different forms:** FPA's `bind`/evidence-check (**LLM skill prompts** — FPA has real verification infrastructure elsewhere: a 348-check smoke test, `dashboard/selftest.py`, `--selftest` flags, an evidence-ledger dashboard view, a deterministic evidence-citation lint — but **no pytest harness covering skill semantics**); the workbench's `evidence_gate.py`/`wbom.py`/`evidence_ledger.py` (**real code, with real tests**); and the engine in edgerunner-warrant.
- **Three ledger schemas.** The workbench's live ledger has **0/12 entries** with `evidence_refs` or `source_document_sha256` — the provenance anchors warrant needs for a real `supported` verdict. FPA's ledger is a third schema (`source_file`/`source_anchor`/`relevance_tags`; `proof_strength: "highest"` is outside warrant's documented low/medium/high range and is accepted silently). Warrant's aliasing (`approval_status`→`status`, `summary`→`claim`, `proof_strength`→`confidence`) was designed in at componentization (commit `f6a5098`, 2026-06-19) and retains unmapped fields in `raw` — the adapter is sound; the data feeding it is not yet.
- **Doctrine** (prose/voice) syncs workbench→FPA today, but capture and verification have **no declared sync direction** — the drift vector.
- **Warrant's signing/hash-chain/auth are on branch `trust-hardening-2026-07`** (pushed, unmerged). Until merged, "signing" is not a main-branch capability and must not be sold as built.

A SAM.gov or HubSpot change currently requires reasoning in two codebases (one with 7 live instances); a change to claim-verification requires edits in up to three places. This decision stops that.

## Decision

**Converge on shared assets, not on a single codebase.** Assign exactly one canonical home per capability. Every other repo consumes via a defined channel and never re-implements. Each row is marked CURRENT (true today) or ASPIRATIONAL (the target this decision creates).

### Canonical ownership table

| Capability | Canonical owner | State | Consumption rule for everyone else |
|---|---|---|---|
| Opportunity capture, triage, scoring, HubSpot intake | **capture-pipeline** | CURRENT for the pipeline; ASPIRATIONAL that the workbench consumes rather than runs its parallel path | Consume via the capture→proposal contract (below). Do **not** maintain a parallel intake/scoring path. |
| Proposal methodology & craft — skills, `reference/` corpus, rubrics, section patterns, pricing artifacts, evaluator rubrics | **federal-proposal-assistant** | CURRENT as authoring home; ASPIRATIONAL that workbench orchestrates the skills | Orchestrate as engine content (invoke the skills); do **not** ship thin re-implementations. |
| Prose / voice doctrine — PROSE-QUALITY-DOCTRINE, voice anchors | **proposal-workbench** (doctrine authoring happens there; sync runs workbench→FPA) | CURRENT (`sync-voice-anchors.sh` exists and runs this direction) | Consume via one-way sync. |
| Prose lint rules | **proposal-workbench** | **ASPIRATIONAL** — the workbench has not yet adopted the lint-rules file; this row is declared intent until it does | Consume via one-way sync once adopted. |
| Verification engine — canonical ledger schema, gate, WBOM, signing, evidence check | **edgerunner-warrant** | ASPIRATIONAL — three implementations exist today; signing pending the `trust-hardening-2026-07` merge | Consume as a library (`import warrant_ledger`) or service (`/api/verify`). Do **not** hand-roll siblings. |
| Non-expert gated workflow surface (desktop) | **proposal-workbench** | CURRENT, conditional on the Phase-1 gate (below) | — |
| Expert chat console + methodology R&D bench | **federal-proposal-assistant** | CURRENT | — |

Note the deliberate split that resolves v1's internal contradiction: **FPA owns skills/rubrics/methodology content; the workbench owns prose/voice doctrine.** The v1 phrase "FPA is the methodology source of truth" is retired — it collided with the doctrine row and invited exactly the ambiguity this table exists to kill.

### The rules that make it stick

1. **One canonical home per artifact.** If it's in the table, that repo is the only place it is authored.
2. **Sync is one-directional, out of the canonical home, via a script — never hand-copied.**
3. **No parallel feature development for the same capability in two repos.**
4. **Enforcement is mechanical, not social.** There is one developer; "bounce the PR" has no reviewer to do the bouncing. Instead: a **canonical-symbol manifest** (a small file listing owned capabilities/symbols per repo) is checked into **all four repos**, and a **pre-commit/CI check in each repo** greps commits for forbidden re-implementations (e.g., a fresh `evidence_gate`-shaped module outside warrant; a fresh HubSpot-intake or scoring path outside capture-pipeline) and fails with a pointer to the canonical home. Changing ownership means editing the manifest — a visible diff, not a quiet fork.

## Required actions (Phase 0)

Ordered by execution dependency and leverage. None are blocked by the gated Phase-1/2 work.

1. **Merge `trust-hardening-2026-07` to warrant main.** Prerequisite for the verification consolidation — the engine's signing/hash-chain/auth must be on main before anything migrates onto it. Write the known-gap note: **no IL-6 key-management story for signing exists yet.**

2. **Define the canonical ledger schema in warrant.**
   - Require `evidence_refs` and `source_document_sha256` for a real `supported` verdict; verdicts without provenance anchors are capped at what ID-existence can honestly support.
   - One-time FPA-ledger migration: `source_file`/`source_anchor` → `evidence_refs`; clamp `proof_strength: "highest"` → `"high"` (and stop accepting out-of-range values silently).
   - **Honest caveat, stated in the migration PR:** the workbench ledger as-is (0/12 entries with provenance fields) exercises only the weak, ID-existence half of the engine until those fields are backfilled. Backfill is follow-on work; do not let "we're on warrant" imply verdicts it can't yet issue.

3. **Workbench→warrant migration (do this one first of the two).**
   - This IS a real code-to-library migration, and it has real tests to migrate behind: `test_evidence_gate.py`, `test_wbom.py`, `test_evidence_ledger.py`, `test_evidence_audit.py`.
   - Keep the engine's citation-first deterministic path (what `evidence_gate.py` approximates).
   - *Bonus:* dogfoods Ground Truth on real internal work — a case study for the accreditation thread.

4. **FPA→warrant integration (not a code migration — there is no FPA verification code to port).**
   - **Gate:** first write a **golden-file test** — fixture draft + fixture ledger → expected findings — so "no regression" is falsifiable. FPA's smoke/selftest infra exists but does not cover skill semantics; this test is the missing harness.
   - **Enumerate both feature sets before moving anything.** Warrant's citation-first path proves **admissibility** (cited ID exists + approved + content-overlap floor), not **entailment**. FPA's evidence-check does different work: marker bookkeeping, unused-evidence surfacing, retired-ID and type-scoped-restriction enforcement.
   - Then: the evidence-check skill **calls the warrant service and consumes its verdict** for the overlapping (admissibility) subset; FPA's marker-audit features remain as a thin layer on top. Nothing is silently dropped.

5. **Decide the workbench capture question (a decision, not a sync-fork — no common ancestor exists to fork from).**
   - capture-pipeline is canonical for the capability. Bill decides: (a) the workbench **calls the capture→proposal contract** and retires its parallel intake/scoring path, or (b) the workbench's native path is **formally scoped** to what the contract cannot provide, in writing. Either is acceptable; undeclared parallelism is not.
   - Mechanical action either way: add a sync note to `proposal-workbench:web_fetch.py` naming its canonical source, `capture-pipeline:app/doc_extract.py` — the one genuine port. Do **not** add provenance notes to the other four files; they would be false.

6. **Freeze the capture→proposal contract as v1.**
   - The `proposal_kickoff_markdown` payload **is merged and deployed**: on master since 2026-04-20 (commit `bcf4e97`), working tree `web.py:2011`, present in all 27 branches. **Pin that commit and line in the contract doc.**
   - Deployment reality (per HANDOFF.md): deploys go from the **working tree**, and the active branch is `review-fixes-2026-07` — the contract freezes the *deployed* payload, which is why the pin matters.
   - Schema: qualified-opportunity (solicitation facts, Go/No-Go, POCs, competitive intel). FPA (`import-from-capture`) and the workbench consume the same v1. Additive changes only → `v2` when needed.

7. **Install the governance gate.** Check the canonical-symbol manifest into all four repos; add the pre-commit/CI grep per rule 4. Publish this table in all four repos. The PR-checklist line ("Does this change re-implement a capability owned by another repo?") survives as documentation; the grep is the enforcement.

## The Phase-1 gate — dated, owned, default-revert

The deferred hard decision in v1 is deferred no longer:

- **By 2026-08-31 (placeholder date — Bill to confirm), Bill runs workbench Test 1 (component-equivalence vs FPA) and Test 2 (non-expert end-to-end) and records the result.**
- **If the workbench has not passed both by that date, it reverts to a doctrine/measurement library, and FPA + capture-pipeline remain the only surfaces.**
- The default on silence is the revert. **Not deciding is the outcome that requires written justification** — running the tests does not.

## Explicitly out of scope for Phase 0 (gated, do not start)

- Absorbing capture-pipeline into a workbench "Capture Room" — **gated on** the Phase-1 gate passing **and** a customer wanting one pane of glass.
- Any capture-pipeline React rewrite.
- Multi-user / identity work in any app beyond what a repo already needs for its own reasons.
- Workbench ledger provenance backfill beyond what action 2 requires (it is named follow-on work, not a Phase-0 blocker).
- Retiring any app. Nothing is retired by this decision — except by the Phase-1 gate's own terms.

## Consequences

**Positive:** a SAM.gov/HubSpot change touches one codebase; a verification change touches one engine; the warrant engine gets dogfooded and hardened by real internal use; the durable assets (engine, corpus) are cleanly separable regardless of what happens to any surface; and every action above is executable against the repos as they exist — no engineer will discover this doc describes a codebase that isn't there.

**Costs/risks:**
- Migrating working verification onto the engine risks regressions — mitigated *differently per target*: workbench behind its four real test files; FPA behind the golden-file test that action 4 creates first, plus the feature-set enumeration that prevents silently dropping marker-audit capabilities.
- **Verdict inflation** — "we're on warrant" being read as "claims are verified" while the workbench ledger lacks provenance fields — mitigated by the canonical schema's requirement (action 2) and the stated caveat.
- One-developer discipline can't rely on review — mitigated by the mechanical gate (rule 4), not a checklist.
- Freezing the contract early risks churn — mitigated by versioning and additive-only changes; the payload has been stable in production since April 2026, which is evidence it's freezable.

## The one-month test of success

- A SAM.gov or HubSpot field change requires editing exactly **one** codebase.
- A change to how claims are verified requires editing exactly **one** engine.
- `calibration-status.py` and the verification path both point at a single owner.
- The pre-commit gate is live in all four repos and has fired at least zero times honestly (i.e., it runs; nobody has routed around it).

If those hold, convergence is working — regardless of how many UIs exist.
