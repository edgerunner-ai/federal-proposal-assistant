# Claim Envelope

**What BD may state as fact, what must be phrased as intent, and what is prohibited — by
capability theme.**

Version 1 · Seeded 2026-07-31 · Owner: BD, with dispositions from the CTO shop

This is the write-back half of the BD ↔ CTO demand signal loop
([docs/BD-CTO-DEMAND-SIGNAL-SYNC.md](../docs/BD-CTO-DEMAND-SIGNAL-SYNC.md)). When the CTO shop
dispositions a gap, the answer lands in one of two places: a new `EV-###` in
[evidence-ledger.json](evidence-ledger.json) when the capability becomes provable, and a row here
saying what BD may now say about it.

It is the capability-keyed counterpart to
[reference/doctrine/prohibited-claims-doctrine.md](../reference/doctrine/prohibited-claims-doctrine.md),
which is keyed to diction. That file governs *how* a claim is phrased; this one governs *whether the
claim may be made at all*.

## How to use it

- **Before drafting**, read the rows for the themes the solicitation touches.
- **`Approved as fact`** language may be stated flatly and should carry the cited evidence ID.
- **`Approved as intent`** is the exact phrasing to use when the capability is real but not
  provable. Do not improve on it — the wording is the risk control.
- **`Prohibited`** claims do not appear in customer-facing material regardless of how the
  solicitation is worded. If a requirement can only be answered with a prohibited claim, that is a
  teaming decision or a declined question, not a drafting problem.
- **When a row is missing**, the theme has no envelope yet. Treat it as `needs-scoping`: write what
  the evidence ledger supports and nothing more, and raise it in the next brief.

Rows are dated because an envelope goes stale. A claim approved as intent nine months ago may now be
provable, or may have been dropped from the roadmap.

## Standing entries

These three predate the register and are the reason it exists. All are corrections BD had to make
after collateral had already gone out.

| Theme | Approved as fact | Approved as intent | Prohibited | Evidence | Dated |
|---|---|---|---|---|---|
| `ato-accreditation-artifacts` | Active **IL-5 ATO** (U.S. Space Force). Active **IL-6 IATT** — stated as "authorized to test at IL-6 under an active IATT." | "We support the customer through their accreditation process" for any environment where we hold no authorization. RMF-aligned artifact production. | "IL-6 ATO", "IL-6 accredited", "ATO granted". Attributing the IL-6 IATT to PMW 120, Navy ICOP, or any named unit. Claiming reciprocity from one program's authorization to another. | ledger | 2026-07-02 |
| `ato-accreditation-artifacts` | Nothing. **FedRAMP, SOC 2, and ISO 27001 are not held.** | Explain the posture instead: the product deploys on-premises and air-gapped inside the customer's own accredited boundary, not as a cloud service, so FedRAMP does not apply to it. | Any FedRAMP, SOC 2, or ISO 27001 status for EdgeRunner, in proposals, decks, or partner collateral. A partner's or hosting platform's FedRAMP posture may be described **only** when attributed to them by name. | — | 2026-07-26 |
| `mission-mos-finetuning` | Model tier nomenclature only (Light / Medium / Heavy) and the published benchmark results. | Tuning to a specific customer's mission data is "a path we bid," not completed work, unless a ledger item says otherwise. | Naming the open-weight source model behind any tier in customer-facing material. | ledger | see [reference_model_tiers](../.claude/../memory) |

Open items to confirm with Bill or the cyber lead before they can be claimed either way: CMMC level,
SPRS score.

## Themes awaiting a first disposition

Every theme in [reference/capability-themes.md](../reference/capability-themes.md) that is not
above has no envelope yet. The 2026-07-31 backfill put 131 signals in the register across 23
themes and 11 customers; nine of those signals are open gaps with no engineering answer. The first
Demand Signal Brief puts those nine in front of the CTO shop. Their dispositions become the next
rows in this table.

Three themes carry a known claim risk today because BD has already had to hedge them in a live
bid — they should be dispositioned first:

| Theme | Why it is urgent | Where it bit us |
|---|---|---|
| `cross-domain-model-update` | Asked by three customers as a scored requirement. We have no concrete mechanism to cite and have bid "the path" twice. | DIA DMA R3, DAF tactical edge SOW.3.1, CYBERCOM J9 R-11 |
| `robotic-autonomy-control` | Complete gap. Three questions declined in one RFI response. | Unmanned Ground Recovery REQ-1b, REQ-2, REQ-3 |
| `output-verification-attribution` | Ground Truth is prototype-stage (TRL 7) and is being asked for by four customers. The gap between what it does and what a fielded verification layer implies is where over-claiming would start. | DIA DMA R11, EXTiC TR-16, Digital Guardian F-8, CDAO ADL R1.3.3 |
