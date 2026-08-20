# AFRL JADPACT II / MASH BAA — EdgeRunner AI (2026)

## Summary
- **Customer:** Air Force Research Laboratory (AFRL)
- **Program:** JADPACT II (Joint All-Domain Persistent Adaptive Collaborative Technologies)
- **Event:** Multi-Decision Advantage Sprint (MASH)
- **Contract number:** FA238426SB005 (Call 01) under BAA FA2384-26-S-B004
- **Type:** BAA demonstration submission
- **Title:** Mission-Trained Edge AI for Battle Management Decision Support
- **POC:** Dave Anderson
- **Date:** 14 March 2026
- **Total proposed cost:** $98,450
- **Outcome:** Submitted; under evaluation

## What This Proposal Is

EdgeRunner proposed a Battle Management AI Teammate — a containerized microservice integrating with a government-provided digital assistant orchestrator during the MASH live event. The system ingests operational data from a simulation environment and provides real-time AI-assisted decision support (COA generation, dependency identification, outcome assessment) aligned with the Transformational Model–Battle Management (TM-BM) framework.

This is a demonstration event proposal, not a multi-year development contract. Short period of performance, lean team, event-based deliverables.

## What's Reusable

### Technical framing (high reuse):
- **"Three core innovations" structure** — mission-trained operational AI models + secure runtime + domain-specific reasoning workflows. Clean, reusable framing for any AI decision support proposal.
- **Human-machine teaming language** — "AI recommendations are presented with transparent reasoning and supporting information, allowing battle managers to evaluate the system's suggestions." Strong for any human-in-the-loop or C2 AI proposal.
- **Prior applications paragraph** — polished summary of AFRL CRADA, HNI-ES (AFSC models on laptops), SAF/SQ IL5 deployment under Maj Gen Purdy, USASOC. Reuse and update as customer list grows.
- **20B model paragraph** — "trained on more than 1.6 million curated military data artifacts...demonstrated performance comparable to frontier models while operating entirely within a local computing environment." Strong credibility statement for any proposal requiring proof of mission AI capability.
- **Containerized microservice architecture** — modular four-layer design (data ingestion → mission AI models → reasoning engine → API integration layer). Reusable for any platform-integration or orchestration proposal.
- **Risk/mitigation table** — three risks (data interface variability, latency, multi-system interoperability) with specific mitigations. Clean format, adapt content per proposal.
- **SOW structure** — 5-task SOW format (deployment, API integration, simulation data processing, output delivery, post-event reporting) is reusable as a template for any demonstration/sprint event proposal.

### Cost volume (high reuse — this is a clean BAA cost model):
- Simple 4-category structure: Labor / Travel / Materials+Infrastructure / ODC
- Labor categories: Principal Investigator, AI/ML Engineer, Software Engineer, Program Manager
- Total $98,450 for a 2-week event + prep + reporting
- No GFE required (platform and models provided as part of demonstration)
- See `cost-volume.md` for full breakdown — use as template for similar demonstration bids

### Security questionnaire (unique — only example on file):
- 13-question AFRL S&T Protection format
- Answers follow NIST SP 800-171 framework throughout
- Covers: physical security, infosec, storage, transmission, disposal, reproduction, personnel, GFE/GFI, cybersecurity, OPSEC, insider threat, incident response, annual training
- See `security-questionnaire.md` — reuse answers directly for any AFRL BAA or similar requirement

## Files
- `_index.md` — this file
- `technical-volume.md` — full Vol 1 technical and management proposal
- `cost-volume.md` — full Vol 2 cost/business proposal with labor table and cost breakdown
- `security-questionnaire.md` — Appendix 2 Security Program Questionnaire (all 13 answers)

## Notes
- Written for an AFRL technical program manager audience, not a contracting officer — appropriate technical depth on TM-BM and battle management functions
- "Department of War" language does not appear here (AFRL uses standard DAF/DoD terminology)
- The TM-BM framework (13 subfunctions) is AFRL-specific — reference it only for AFRL/DAF battle management proposals
- The proposal covers only the MASH event demonstration, not full system development — cost and SOW scope reflect that; don't reuse cost numbers for a larger effort without scaling
- Submitted by Dave Anderson as POC; Sean Bailey completed the security questionnaire
