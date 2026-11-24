---
name: ledger-harvest
description: Mine a source — a submitted proposal, a published paper or briefing, an executed contract, a call or conference note — for capability, evidence, application, and expertise records, and propose them for approval into my-company/evidence-ledger.json. Run at the moment evidence is created (submission, publication, execution), not months later when a proposal author discovers a citation is missing. Feeds both proposal citation and opportunity identification.
phase: setup
composes: [capture-submission, evidence-check, setup-company]
conflicts_with: [evidence-check]  # evidence-check AUDITS drafts against the ledger; this one FEEDS the ledger from sources. Never let this skill judge a draft's citations, and never let evidence-check write entries.
---

# Ledger Harvest Skill

## Purpose

Keep `my-company/evidence-ledger.json` current by harvesting it from sources **at the moment
evidence is created**, rather than reconstructing it later.

The failure this exists to fix: the ledger records what we have *cited*, not what we can *prove*.
Evidence is created when a paper is published, a contract is signed, a demo is run, or a proposal is
submitted — but it enters the ledger only when some later author needs a citation and finds it
missing. On 2026-08-27 the ARL CRADA robotics result, submitted to the Government eight days
earlier, had no entry. Roughly half the published body of work had none either.

Read `docs/CAPABILITY-LEDGER-STRUCTURE-2026-08-27.md` before first use. It defines the four record
classes and the `evidentiary_tier` gate this skill writes.

## When to Use

Run it **when the source is created**, not when a proposal needs it:

- **A proposal is submitted.** Highest-value moment: every claim has survived review and gone to the
  Government. Runs naturally after `/capture-submission`.
- **A paper, briefing, or slick is published** to `edgerunner-papers` or `my-company/`.
- **A contract, CRADA, JWS, or agreement is executed.**
- **After a customer conversation, conference, or demo** that produced a quotable fact.
- **Backfill**, pointed at an existing asset.

Not a substitute for `/evidence-check`, which audits a draft's citations against the ledger. This
skill only writes the ledger; it never reads drafts to judge them.

## Invocation

```
/ledger-harvest --from <path-or-url> [--class evidence|application|capability|expertise] [--dry-run]
/ledger-harvest --backfill <directory>
```

`--dry-run` proposes without writing. Default is propose-then-confirm; nothing is written unsolicited.

## Inputs

### Always read
1. `my-company/evidence-ledger.json` — current state, ID maxima per prefix, and the historical gaps.
2. `docs/CAPABILITY-LEDGER-STRUCTURE-2026-08-27.md` — record classes and tier definitions.
3. `my-company/capabilities.md` — the canonical prose statement of the nine core capabilities and,
   critically, the **honesty constraints** (maturity vocabulary, what must not be claimed).
4. The source named in `--from`.

### Read if relevant
- `reference/schemas/evidence-ledger.schema.json`
- The submitting proposal's `working/submission-summary.md`, when harvesting from a submission —
  it establishes what was actually sent and when.

## The four record classes

| Class | Prefix | Write one when the source shows… |
|---|---|---|
| `capability` | `CAP-##` | A durable thing EdgeRunner does. **Rare.** There are nine; adding a tenth is a company decision, not a harvest. Default to no. |
| `evidence` | `EV-###` | A provable instance — a contract, a measured result, a demonstration, a customer statement. |
| `application` | `APP-###` | A use-case: capabilities mapped onto a mission problem and a customer context. May be entirely conceptual. |
| `expertise` | `EXP-##` | A named person's depth in a customer or mission space. |

**The most common harvest error is filing a use-case as a capability.** SPOTTER, Dead Reckoning,
the Ecosystem Slick, a Power BI integration — these are `application` records. They describe what
our capabilities were pointed at, not new things we can do. If the source describes a mission
problem, a customer, or a specific deployment, it is an `application`.

## The `evidentiary_tier` gate

Every `evidence` and `application` record needs one. This is the field that lets the register serve
proposal citation and opportunity identification at once.

| Tier | Test | Citable? |
|---|---|---|
| `contracted` | Performed under a contract or agreement, documented | Past performance / relevant experience |
| `measured` | A measured result with a stated method | Benchmark citation |
| `demonstrated` | Done and witnessed, not under contract, not measured | Yes, framed carefully — never as past performance |
| `designed` | Concept paper or architecture exists; not built | **No** as experience. Proposed approach only |
| `adjacent` | Not done; the capability plainly transfers | **No.** Opportunity identification only |

**When uncertain between two tiers, take the lower one.** An over-tiered entry becomes an
unsupported claim in a proposal, which is a scoring loss. An under-tiered entry costs a
conversation.

Tier is about *evidentiary strength*, not importance. A `designed` concept paper may be the most
strategically valuable record in the ledger and still be uncitable as experience.

## Workflow

### Step 1 — Read the source completely

No skimming. A harvest that invents a number is worse than no harvest, because the entry will carry
a `verified_at` date and be trusted.

### Step 2 — Extract candidates

For each candidate, capture:
- Which of the four classes it is
- `summary` — one sentence, specific, no marketing register
- `detail` — what was done, by whom, when, under what instrument, with what result
- `source_file` and `source_anchor` — **mandatory**. An untraceable entry is worse than none
- `evidentiary_tier` and the one-line reason
- `capabilities` — which of CAP-01..CAP-09 it exercises
- `relevance_tags`
- For `application`: the mission problem and customer context, even hypothetical
- For `expertise`: person, space, depth, currency

### Step 3 — Check for duplicates and supersession

Search the ledger before proposing. If an entry covers the same fact:
- Materially better provenance → propose **enriching** the existing entry
- The old one is now wrong → propose **retiring** it and adding a replacement, with a `notes` line
  naming the superseded ID
- Same fact, no improvement → **drop it**

Never create a second entry for a fact that already has one.

### Step 4 — Allocate IDs

- Find the maximum numeric ID **per prefix** and allocate above it.
- **Never allocate into a gap.** The gaps in the `EV-` sequence are scars from the 2026-07-24
  overwrite; reusing one silently re-points every historical citation. As of 2026-08-27 the unusable
  `EV-` gaps are: 15–19, 24–29, 33–39, 49, 62–66, 68, 69, 81–89, 97, 98.

### Step 5 — Present for approval

Show a table: proposed ID, class, tier, summary, source, and — for anything above `designed` — the
specific words in the source that justify the tier. **Stop and wait.** Nothing is written until the
human approves. Approve, edit, or reject each row.

### Step 6 — Write

- Append approved entries. Never rewrite existing ones except an approved enrichment.
- Preserve formatting exactly: `json.dumps(d, indent=2, ensure_ascii=False)`, LF line endings,
  trailing newline. Writing it any other way produces a ~1,800-line diff that hides the real change.
- Append a dated line to the ledger's `_comment` saying what was added and why.
- Update `generated_at`.
- Verify the diff is proportionate to the change before finishing. A large diff means the formatting
  was broken, not that the harvest was large.

### Step 7 — Commit

**The ledger has no recovery path when uncommitted.** The 2026-07-24 overwrite lost ~49 entries for
exactly this reason, and the file's own `_comment` records the rule: commit after every append.

A pre-commit guard blocks this file. Read the guard before committing rather than assuming a plain
commit works, and never bypass it with `--no-verify`.

### Step 8 — Report

State what was added, what was skipped and why, and what could not be tiered without a human
decision.

## Rules

- **Propose, never write unsolicited.** The ledger's worth is that it is trusted.
- **Provenance or nothing.** No `source_file` and `source_anchor`, no entry.
- **Tier down when uncertain.**
- **Applications are not capabilities.** Nine capabilities exist; adding one is a company decision.
- **Do not launder aspiration into evidence.** A concept paper is `designed`, however good it is.
- **Respect the honesty constraints in `capabilities.md`** — the IATT-not-ATO line, no FedRAMP /
  SOC 2 / ISO 27001, unfunded pilots are relevant experience and never past performance, no TRL for
  Ground Truth. A harvest that contradicts those is a defect.
- **Append-only.** Retire, never delete.
- **IDs above max, per prefix, never into a gap.**

## Anti-patterns

- Harvesting a proposal draft rather than the **submitted** version — drafts contain claims that were
  cut in review.
- Creating an entry from a marketing document's adjectives. Harvest the fact, not the framing.
- Tiering a demo as `contracted` because it happened at a customer site.
- Bulk-writing dozens of entries in one pass without approval. Batch by product line, approve,
  commit, then the next batch.
- Filing an `application` for a customer we have served and calling it `adjacent`, or filing one for
  a customer we have not and calling it `demonstrated`.

## Activity Trail

Append one line to the ledger's `_comment` (this skill is workspace-global, so there is no per-
proposal `working/activity.md` to write unless invoked from within a pursuit; when it is, log there
too):

```
## <timestamp> — ledger-harvest — <N> records from <source>: <classes and tiers> → my-company/evidence-ledger.json
```

## Integration

- **`/capture-submission`** — run this immediately after, on the submitted artifact.
- **`/evidence-check`** — consumes what this produces. It audits; this feeds. Keep them separate.
- **`/opportunity-quick-look`** — should read `application` and `expertise` records at every tier
  when assessing customer and mission fit. That is the mechanism that stops the workspace from only
  recognizing opportunities resembling our early ones.
- **`/past-performance`** — must filter to `contracted` and `measured` only.
