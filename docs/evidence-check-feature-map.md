# Evidence-Check Feature Map — FPA vs the Warrant Engine

**Status:** Phase-0 deliverable (DECISION-canonical-ownership action #4) · **Date:** 2026-07-06
**Companion code:** `scripts/evidence_check_core.py` (deterministic checker), `scripts/evidence-check-golden.py` (golden-file gate), `tests/fixtures/evidence-check/` (synthetic fixtures)

This document enumerates exactly what FPA's `/evidence-check` skill does versus what the
`warrant_ledger` engine (edgerunner-warrant, reference branch `trust-hardening-2026-07`) does,
and marks each feature **MIGRATE** (warrant owns it), **KEEP** (FPA-only, stays as a thin layer),
or **BOTH** (warrant does the core, the FPA layer adds proposal context). This is the migration
boundary: nothing moves, and nothing is silently dropped, except per this table.

Two framing facts that shape every row:

1. **FPA's evidence-check is marker bookkeeping, not claim extraction.** It audits author-placed
   `<!-- evidence: EV-### -->` HTML-comment markers against `my-company/evidence-ledger.json`.
   It never decides which sentences *should* have been cited.
2. **Warrant proves citation ADMISSIBILITY, not entailment.** Its citation-first path confirms a
   cited ID exists, is approved/in-force, and clears a deterministic content-overlap floor
   (anti-cite-spam). Its semantic path produces review *candidates*, never verifications.

## Feature table

| # | Feature | FPA evidence-check today | warrant_ledger today | Disposition |
|---|---------|--------------------------|----------------------|-------------|
| 1 | Marker parsing — extract `<!-- evidence: ... -->` markers with file/line/sentence locations | Yes (LLM skill prompt, Step 2) | No — warrant extracts claim *sentences* and reads bare `EV-###` ids inside them; it has no concept of the HTML-comment marker convention or of file/line bookkeeping | **KEEP** — deterministic in `evidence_check_core.py` (`audit_markers`) |
| 2 | Typo'd / unknown ID detection | Yes (Step 3, `UNKNOWN_ID`) with "likely typo for EV-0xx?" suggestion | Partial — `STATUS_UNKNOWN` when a cited id is not in the ledger; **no** nearest-ID typo suggestion | **BOTH** — warrant issues the unknown verdict; the FPA layer adds the edit-distance typo suggestion (`evidence_check_core.suggest_id`) |
| 3 | Retired-ID enforcement | Yes (Step 3, `RETIRED`) | Yes — `STATUS_RETIRED` on the citation path | **MIGRATE** — warrant's verdict is authoritative; core reports it 1:1 (and reproduces it in fallback mode) |
| 4 | Restricted-ID detection | Yes (Step 3) | Yes — `STATUS_RESTRICTED` on the citation path | **MIGRATE** (detection) — see row 5 for adjudication |
| 5 | Type-scoped restriction adjudication — does this proposal type / distribution violate the entry's free-text `restrictions`? | Yes — the skill reasons over the restrictions prose against `working/proposal-type.md` | No — warrant flags `restricted` but has no proposal-type context and does not interpret free-text restrictions | **KEEP** — the deterministic core surfaces every restricted citation *with its restrictions text*; the LLM skill layer adjudicates violation vs. legitimate restricted use |
| 6 | `CLAIM-UNSUPPORTED` marker handling | Yes — each marker listed as an unsupported claim to resolve | Yes — `has_unsupported_marker` forces an unsupported verdict regardless of citations | **BOTH** — warrant enforces it per claim-sentence; core keeps the per-marker file/line report the skill output needs |
| 7 | Pending-review ID warning (`approval_status: pending_review`) | Yes (Step 3, `PENDING_REVIEW` — warn, don't fail) | No distinct status — any non-`approved` status that isn't retired/restricted is simply not citable (falls out as unsupported) | **KEEP** — core classifies pending distinctly so the "don't submit until approved" warning survives |
| 8 | Unused approved evidence surfacing | Yes (Step 4) with `relevance_tags` overlap hinting | Yes — `Verdict.unused_entry_ids` (approved entries no claim matched) | **BOTH** — warrant computes the set; the FPA layer keeps the relevance-tag "consider citing" narration |
| 9 | Coverage metric (`supported / total markers`) + `compliance-matrix.json` `evidence_coverage_pct` update | Yes (Step 5) | Different denominator — `grounding_rate` is over extracted claim-*sentences*, not author markers | **KEEP** — the marker-denominated coverage number is FPA's contract with `/status`, the dashboard, and Gold Team; warrant's grounding_rate is reported alongside, never substituted |
| 10 | Claim-sentence extraction (recall-biased assertive-sentence detector) | No — explicitly out of scope for the skill | Yes — `extract_claim_sentences` | **MIGRATE** — arrives only via the warrant call; FPA gains it, never re-implements it |
| 11 | Citation admissibility + content-overlap floor (anti-cite-spam `citation-weak` downgrade) | No | Yes — `align_claim` / `citation_overlap` (`DEFAULT_CITATION_OVERLAP_FLOOR = 0.20`) | **MIGRATE** — this is net-new signal for FPA drafts (an approved ID stapled to an unrelated sentence now gets flagged) |
| 12 | Semantic candidate matching (embedding fallback, human-review candidates) | No | Yes — optional, bring-your-own embedder; candidates never auto-promote | **MIGRATE** — available through the warrant call when an embedder is configured; not exercised by the deterministic golden test |
| 13 | Gate (pass / flag / block enforcement policy) | No — the skill reports; humans decide | Yes — `gate(verdict, Policy)` | **MIGRATE** — the combined output includes the gate decision; FPA treats it as advisory input to Gold Team, not an export blocker (export blocking stays with the pre-submit scripts) |
| 14 | WBOM (portable audit receipt, ledger content-hash binding; signing pending the trust-hardening merge) | No | Yes — `to_wbom` / `wbom_content_hash` / `sign_wbom` | **MIGRATE** — emitted in the combined output when the engine is present; FPA never builds its own receipt format |
| 15 | Report narration / triage (`reviews/evidence-check.md`, activity trail, recommendations) | Yes — the skill's primary output | No — `render_report` is a plain-text summary, not the FPA review artifact | **KEEP** — the LLM skill narrates and triages over the deterministic core's JSON; the code decides, the skill explains |

## Ledger schema note (the third schema)

FPA's `my-company/evidence-ledger.json` uses `source_file`/`source_anchor`/`relevance_tags`/`detail`/
`customer`, and `proof_strength` includes `"highest"` — outside warrant's documented low/medium/high
range. Warrant's loader already aliases `approval_status`→`status`, `summary`→`claim`,
`proof_strength`→`confidence` and keeps unmapped fields in `raw`, so most of the shape flows through.
The remaining deltas are handled by an **in-memory adapter** in `evidence_check_core.py` (the real
ledger file is never modified):

- `source_file` + `source_anchor` → `evidence_refs: ["<source_file>#<source_anchor>"]`
- `proof_strength: "highest"` → clamped to `"high"`, with an adapter warning (no more silent
  acceptance of out-of-range values — any unrecognized value is warned and passed as-is)
- everything else rides through warrant's existing aliasing

The one-time *file* migration of the FPA ledger to the canonical schema is DECISION action #2
(owned by warrant) — this adapter is the bridge until then.

## Degradation contract

The warrant engine lives in a sibling repo that won't exist on other machines. The core checker
therefore treats warrant as an optional layer: if `warrant_ledger` cannot be imported (path knob:
`--warrant-src` / `FPA_WARRANT_SRC`, default `C:\Users\wbal9\CODEX projects\edgerunner-warrant\warrant-ledger\src`),
it reports `warrant.available: false` with the reason and falls back to **marker-audit only** —
every KEEP row above still runs; the MIGRATE rows are simply absent, never approximated.
