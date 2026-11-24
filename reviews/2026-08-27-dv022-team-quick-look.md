# Opportunity Quick Look — OSW26BZ05-DV022 (team-based: EdgeRunner + DeNOVO)
**Date:** 2026-08-27
**Source:** SBIR Direct to Phase II (DoD SBIR 26.5, DSIP)
**Program:** Signal Classification and Anomaly Detection in Contested Spectral Environments
**Customer:** OSD (TPOC listed as "None" — DSIP Topic Q&A is the only channel)
**Ceiling Value:** Not stated in topic (OSD D2P2 typically low-seven figures)
**Response Deadline:** 2026-09-23 12:00 ET
**Contract Type:** SBIR Phase II (Direct)

**Variant note:** run at Bill's direction as a *team-based* triage — EdgeRunner records from the expanded evidence ledger (2026-08-27 restructure: CAP-01 through CAP-09 now cover capabilities beyond past performance and product demos), DeNOVO capabilities from their ASP-B whitepaper as recorded in `proposals/spectrum-sentinel/working/teammate-denovo-fit.md`. Partner facts are attributed, not ledger-verified; they carry a "DeNOVO confirms" duty everywhere they appear. No proposal workspace exists; output to `reviews/` by design.

---

## Quick Look Scorecard

| # | Factor | Status | Assessment |
|---|--------|--------|------------|
| 1 | Mission Fit | 🟢 (team) / 🟡 (EdgeRunner alone) | The RF core maps to DeNOVO's CODA (fielded emitter classification/anomaly, per their whitepaper); every non-RF attribute maps to EdgeRunner CAP records at Proven-or-better maturity (CAP-02, CAP-03, CAP-04, CAP-07, CAP-09). EdgeRunner alone is 🟡: real capabilities transferring into an RF mission we hold no capability record for. |
| 2 | Customer Fit | 🟡 | The ledger's `expertise` class holds zero records, so customer fit could not be assessed from the register — stated rather than guessed. No direct OSD relationship; DeNOVO's IC/SIGINT pedigree and EdgeRunner's cross-DoD deployments are adjacent routes, and no TPOC exists to work regardless. |
| 3 | Funding Status | 🟢 | Funded D2P2 SBIR award vehicle, award inside 12 months, published topic in an open solicitation. |
| 4 | Size and Scope Fit | 🟢 | SBIR small-business lane; both companies are SBCs. Sub-share economics for EdgeRunner (~one third), which is the right price for a first OSD entry with this partner. |
| 5 | Schedule Fit | 🟡 | Four weeks to close is workable, but the real clock is shorter: DeNOVO prime decision this week, releasable benchmark evidence by ~Sep 5, Q&A closes ~Sep 9 — and the GenAI EPSS submission (Sep 10) overlaps the same window. |
| 6 | Competitive Position | 🟡 | The team's discriminator (fielded classifier + deterministic explainability receipts) is real, and EdgeRunner's supporting evidence is citable at high tiers (EV-031, EV-030, EV-002, EV-022, EV-104). But the load-bearing D2P2 evidence is DeNOVO's, unverified by us, and the topic's specific demand — quantified results on open-source/synthetic benchmark sets — is confirmed by neither party yet. Capability fits; the decisive evidence is not yet in hand. |
| 7 | Common Sense Barriers | 🟡 | Three resolvable items: EdgeRunner cannot prime (existing-prototype clause + 50% work-share — resolved by DeNOVO priming); CMMC Level 2 (Self) projected (EdgeRunner posture an open item); DeNOVO's SBIR eligibility is theirs to certify. No FCL required at proposal. |
| 8 | Submission Mechanism | 🟢 | DSIP document upload under the published 26.5 BAA — format authority is the BAA + topic, fully knowable now. EdgeRunner has submitted through DSIP before; as prime, DeNOVO submits. |

**Score: 4 Green / 4 Yellow / 0 Red** (team basis)

---

## Capability and Evidence Basis

**Capabilities exercised — EdgeRunner (ledger)**

| Record | Capability | Maturity | How DV022 uses it |
|---|---|---|---|
| CAP-04 | Ground Truth | Proven / Built | Attribute 2 (transparent, certifiable "why"): deterministic claim-checking with portable receipts wrapping the classifier's attribution. No TRL is claimed for Ground Truth per the standing rule. |
| CAP-02 | Secure runtime | Fielded | Containerized, hardware/OS-agnostic on-device inference — the delivery vehicle for attribute 6 and the tactical end of attribute 4. |
| CAP-03 | Agentic orchestration (WarClaw) | Built | Encoding the SIGINT analytic process as an auditable, versioned pipeline — the C5ISR workflow integration in the EdgeRunner sub-scope. |
| CAP-07 | Model compression + published benchmarking | Proven | Attribute 4 (CPU-class efficiency) and, importantly, attribute-style credibility: we have published, quantified benchmark discipline of exactly the kind the D2P2 documentation demands. |
| CAP-09 | LoRA adapter development | Proven | Attribute 5 (accuracy improves with data): adapter-based continuous specialization without full retraining — a co-owned story with DeNOVO's retraining pipeline. |
| CAP-06 | DORIS (on-device adaptation) | Proof-of-concept | Roadmap color only for in-enclave model improvement. Never described as fielded ("very immature" — Bill, 2026-08-27). |
| CAP-08 | Autonomy experience with ARL | Demonstrated | Adjacent credibility: on-device models orchestrating behavior on Government platforms (EV-124/125/126); relevant to the tactical-integration story, confined to fundamental research per the JWS (EV-128). |

**Capabilities exercised — DeNOVO (partner-attested, per their ASP-B whitepaper; they confirm)**

| Asset | DV022 use | Verification duty |
|---|---|---|
| CODA emitter ID/classification/anomaly (fielded, TRL-8 per DeNOVO) | The RF core; the "existing prototype" the D2P2 clause requires | DeNOVO substantiates in their volume |
| TEMPO/Synthweaver synthetic VITA-49 I/Q | Attribute 5 data-scarcity answer | DeNOVO confirms releasability |
| Calibration-first / abstain methodology; acceptance-criteria discipline | Attributes 2 and 5 | Methodology citable now |
| RKE2/OCI MLOps, IL4-to-classified promotion | Attribute 6 | DeNOVO confirms current state |

**Applications / Expertise:** the ledger's `application` and `expertise` classes hold no records yet — the 2026-08-27 restructure defined them, but harvest has not populated them. Customer Fit above is correspondingly conservative.

**Citable evidence if we bid** (EdgeRunner side, high tiers only)

| Record | Summary | Strength |
|---|---|---|
| EV-031 | EdgeRunner 20B published benchmarks — quantified-metrics precedent in the exact style the D2P2 documentation demands | highest |
| EV-030 | Mil-Deflect published refusal-rate benchmark | highest |
| EV-002 / EV-102 | Containerized deployment into the USSF IL-5 accredited environment | highest |
| EV-022 | IL-6 IATT — "authorized to test at IL-6 under an active IATT," no unit attribution | highest |
| EV-104 | WarClaw + Ground Truth end-to-end, air-gapped, single-system demonstration | high |
| EV-094 / EV-095 | Ground Truth instrumentation and action-gate | high |
| EV-075 | Six cleared staff (four Secret, two TS/SCI); no FCL — posture stated, not needed at proposal here | high |

**Register gaps this surfaced** (feed for `/ledger-harvest`):

1. **No capability record covers RF/spectrum ML** — consistent with the deliberate teaming strategy and the new `rf-signal-classification` demand theme; the gap is a decision already made, but it should exist as an explicit register fact rather than an absence.
2. **`expertise` class is empty.** This triage ran Customer Fit blind. The military SMEs behind the published benchmarks (Army officers, special-missions and cyber backgrounds) are exactly EXP-record material.
3. **`application` class is empty** — the Spectrum Sentinel concept itself is a `designed`-tier application record for spectrum missions that would have raised Mission Fit here on the EdgeRunner-alone lens.
4. **No measured CPU inference numbers in the ledger.** We assert edge efficiency (CAP-07, EV-092); an EV with measured on-CPU latency/throughput would convert attribute 4 from credible to citable.
5. **Partner capabilities have no home.** DeNOVO's CODA/TEMPO facts live in one proposal's working file; a recurring teammate deserves a durable, clearly-attributed record so team-based triage does not depend on which pursuit folder someone remembers.

---

## Bottom Line

As a team this is a well-shaped, funded, small-business-lane D2P2 whose six attributes split cleanly along the partnership seam: DeNOVO owns the RF core and the D2P2 evidence gate, EdgeRunner owns trust, delivery, and integration with Proven-or-better ledger records behind each. The expanded ledger widens EdgeRunner's credible sub-scope beyond the earlier fit review — CAP-07 and CAP-09 put us co-owner of the efficiency and continuous-improvement attributes, not just the explainability layer. The single decisive risk is unchanged: the open-benchmark evidence the topic demands is confirmed by neither party, and without it the proposal is non-responsive regardless of team quality.

## Recommendation

**PURSUE** (as subcontractor; DeNOVO primes) — 4 Green / 4 Yellow / 0 Red, with no Red in Mission Fit, Customer Fit, or Barriers. Rationale: the team covers all six attributes with named, mostly-citable capability records, and every Yellow is a sequencing or confirmation task, not a fit problem.

## Recommended Next Steps

1. Send the team brief and get DeNOVO's prime decision by ~Sep 2 (`drafts/2026-08-27-dv022-denovo-team-brief.docx` — already prepared).
2. Benchmark-evidence confirmation by ~Sep 5: DeNOVO's releasable open/synthetic results, or a fast TorchSig/RadioML-class run with TEMPO augmentation. This is the go/no-go.
3. Expand the proposed EdgeRunner sub-scope statement to claim attributes 4 and 5 as co-owned (CAP-07, CAP-09) when the teaming discussion turns to work split.
4. Confirm CMMC Level 2 (Self) posture on both sides before submission.
5. Run `/ledger-harvest` against the five register gaps above — items 2 and 3 (empty expertise and application classes) degrade every future quick-look, not just this one.
