# Structuring the ledger for two jobs — capability register and citation store

Decision record, 2026-08-27. Supersedes the open question left in
`LEDGER-MAINTENANCE-PROPOSAL-2026-08-27.md`, answered by Bill: this is a log of **EdgeRunner's
capabilities along with our experience**, not a proposal citation store that happens to hold
capabilities.

## The problem with the current shape

`evidence-ledger.json` is one flat `items` array where `type` does double duty — it marks both
*what kind of thing this is* (`partnership`, `benchmark_result`) and *how strong it is*
(`capability_claim` vs `past_performance`). That works when the only consumer is a proposal author
picking citations. It fails the moment the register also has to answer "could we credibly go after
this?"

Two failures follow, and they pull in opposite directions:

- **Opportunity identification fails by being too narrow.** Everything in the ledger is something we
  have already done, for a customer we have already served. Query it to decide whether to chase an
  opportunity and it will keep pointing at chatbot/DDIL for Army, AF, and SOCOM — because that is
  what the early record contains. The register silently encodes our history as our boundary.
- **Proposal citation fails by being too loose.** If the fix for the above is to add aspirational
  entries, they become indistinguishable from contracted facts at citation time, and unsupported
  claims are a proposal-killer.

The mistake in my 2026-08-27 gap analysis was treating SPOTTER, Dead Reckoning, the Ecosystem Slick
and the Machine Vision workflow as missing *capabilities*. They are not capabilities. They are
**use-cases** — mappings of core capability onto a mission problem. Recording them as capabilities
would inflate what we claim to do; recording them nowhere loses the thing Bill actually wants, which
is a wide surface for opportunity identification.

## The nine core capabilities

Per Bill, 2026-08-27. These are the durable things EdgeRunner does. Everything else is an
application of one or more of them.

| # | Capability | Nearest section in `capabilities.md` |
|---|---|---|
| 1 | Model training for military | Layer 1 — Custom Models |
| 2 | Secure runtime for AI in military environments | Layer 3 — Secure Runtime |
| 3 | Agentic orchestration and workflows for military | Layer 4 — WarClaw |
| 4 | Ground Truth | Layer 5 — Governance |
| 5 | EVELYN | EVELYN — Machine Vision & Data Labeling |
| 6 | DORIS (immature) | DORIS — On-Device Model Adaptation |
| 7 | Novel model compression and published performance benchmarks | Layer 2 — Model Optimization & Compression |
| 8 | Autonomy experience with ARL | Domain-Specific AI for Embodied Autonomous Systems |
| 9 | LoRA adapter development | Layer 2 — Custom Adapters |

## The structure

**One file, four record classes, one gating field.** Not four files — the whole value is that a
single query can cross from a capability to the evidence that proves it to the missions it could
serve.

### Record classes

| Class | ID prefix | Answers | Example |
|---|---|---|---|
| **capability** | `CAP-##` | What can we do? | CAP-03 Agentic orchestration |
| **evidence** | `EV-###` | What can we assert to the Government? | EV-124 Warthog autonomous waypoint exploration |
| **application** | `APP-###` | Where could this go? | APP-### SPOTTER: prompt-tasked target ID on tactical UAS FMV |
| **expertise** | `EXP-##` | Can we credibly reach this customer? | EXP-## Bill Bal — Navy PEO / acquisition |

Existing `EV-###` entries keep their IDs and meaning. Nothing renumbers. The new classes get their
own prefixes so the ID spaces never collide.

### The gating field — `evidentiary_tier`

Every `evidence` and `application` record carries one. This is the single mechanism that lets one
store serve both jobs.

| Tier | Meaning | Citable in a proposal? |
|---|---|---|
| `contracted` | Performed under a contract or agreement, documented | Yes — past performance / relevant experience |
| `measured` | A measured result with a stated method | Yes — benchmark citation |
| `demonstrated` | We did it and it was witnessed, but not under contract and not measured | Yes, with careful framing — never as past performance |
| `designed` | Concept paper or architecture exists; not built | **No** as experience. Usable as a *proposed* approach |
| `adjacent` | We have not done it; the capability plainly transfers | **No.** Opportunity identification only |

**The two jobs then become two queries over the same store:**

- *Opportunity identification* reads every class and every tier, and treats `designed` and
  `adjacent` as first-class. This is what lets us look at a mission or a customer we have never
  served and reason about whether we could reach it.
- *Proposal citation* filters to `evidence` records at `contracted`, `measured`, or `demonstrated`,
  with a `source_file` and `source_anchor` present. `/evidence-check` enforces this — anything
  cited that is `designed` or `adjacent` is a finding, not a citation.

### Why `application` records matter most for Bill's concern

An `application` is a triple: **capabilities used × mission problem × customer context**, plus a
tier. Because the tier can be `designed` or `adjacent`, applications can exist for missions and
customers we have never touched. That is precisely the surface that stops us from only seeing
opportunities that look like our early ones.

SPOTTER is an `application` at `designed` — it uses CAP-05 (EVELYN) and CAP-03 (orchestration)
against a tactical UAS FMV target-identification problem for an IC customer. Nothing about it is
past performance. Everything about it is a reason to look at IC ISR opportunities we would
otherwise filter out.

### Why `expertise` records are the missing asset class

Bill: *"I have massive domain knowledge in several customer spaces, and other ER employees bring the
same level of expertise to others."* None of that is anywhere in the workspace today, and it is
often the deciding factor in whether an unfamiliar opportunity is actually reachable. An `expertise`
record names the person, the customer or mission space, the depth, and whether it is current.

This is the answer to "we are interested in all use cases and customers within the Department and
IC" — capability tells you what we can build, expertise tells you whose door we can credibly walk
through.

## Migration

Non-destructive and incremental.

1. Add `record_class` to every existing item, defaulting to `evidence`. Nothing breaks —
   `/evidence-check` already only reads `EV-` IDs.
2. Seed the nine `CAP-##` records from `capabilities.md`, which already carries the maturity
   vocabulary and the honesty constraints.
3. Backfill `application` records from `edgerunner-papers` and the concept-paper corpus, at
   `designed`, linked to the capabilities they use.
4. Add `expertise` records from Bill and the team. This one needs people, not parsing.
5. Add `evidentiary_tier` to existing `EV-` records. Mechanical for most: `type: past_performance`
   → `contracted`, `benchmark_result` → `measured`, `capability_claim` → judgment.

Steps 1–3 are automatable with human approval. Step 4 is an interview. Step 5 wants a review pass.

## What does not change

- Append-only. Retire, never delete.
- IDs allocate above the current max **within each prefix**. Never into a historical gap.
- Nothing enters without provenance.
- A human approves every entry.
- File formatting stays `indent=2`, LF, `ensure_ascii=False`.
