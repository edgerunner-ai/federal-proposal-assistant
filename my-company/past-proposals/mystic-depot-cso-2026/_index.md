# DIU Mystic Depot CSO — Team EdgeRunner AI (2026)

## Summary
- **Customer:** DIU / ODNI (Office of the Director of National Intelligence)
- **Type:** Commercial Solutions Offering (CSO)
- **Topic:** Vendor-agnostic AI Test, Evaluation, Verification & Validation (TEVV) infrastructure — both the evaluation harness (LOE1) and the benchmark development platform (LOE2)
- **Team:** EdgeRunner AI (prime) + BigBear.ai + Lockheed Martin
- **Submission date:** March 24, 2026
- **Outcome:** Submitted; under evaluation

## What LOE1 and LOE2 Are

**LOE1 — Evaluation Harness (the execution control plane)**
EdgeRunner provides the secure runtime and protocol layer that governs how any AI model is tested — configuration, tool access, agent behavior, logging, scoring. Models plug in; the harness runs them identically across cloud, classified, and DDIL environments. BigBear.ai adds agentic/human-in-the-loop evaluation. Lockheed adds adversarial testing and audit.

**LOE2 — Benchmark Development Platform (the benchmark factory)**
EdgeRunner leads the methodology for creating, versioning, and governing mission-specific benchmarks. Bronze/Silver/Gold dataset tiers, NIST AI RMF-aligned lifecycle, cryptographically signed versioned releases, adversarial augmentation to prevent gaming. Benchmarks are delivered via API to any execution system (including LOE1).

The two LOEs are designed to be separable: LOE2 produces benchmarks; LOE1 executes them. The government owns both.

## What's Reusable

### Positioning language (high reuse):
- **"Vendor-agnostic, government-owned"** framing — strong for any TEVV, evaluation, or AI governance opportunity. The argument that current benchmarks are vendor-controlled and gaming-susceptible is reusable broadly.
- **Protocol-centric architecture language** — separating evaluation definition, execution, and scoring into modular layers is a clean conceptual frame reusable in any AI platform proposal.
- **Bronze/Silver/Gold dataset tiering** — concrete, explainable methodology for benchmark development. Reuse for any data pipeline or AI training proposal.
- **"Integration over invention"** Phase I framing — "Phase I delivers by integrating existing, fielded capabilities, reducing technical risk." Strong for CSO/OTA proposals where evaluators want speed to capability, not R&D promises.
- **Company traction paragraph** (Section 3.1) — current operational customers list + $17.5M raised + $5M 2026 operating income projection. Update numbers as needed; the format is polished.
- **Nontraditional Defense Contractor** statement — important for OTA compliance; reuse in any OTA proposal.

### Architecture concepts (reuse in solution design):
- Evaluation Protocol Layer as a "control plane" separating models from execution logic
- Model Abstraction Layer enabling commercial API + government-hosted + edge-deployed models through one interface
- Environment-agnostic execution (identical protocol across IL4/5/6, air-gapped, DDIL)
- Full execution traceability (intermediate steps, tool interactions, inputs/outputs captured as structured records)

### Teaming structure:
- EdgeRunner = core platform / harness / methodology lead
- BigBear.ai = agentic workflows, human-in-the-loop, operational scenarios
- Lockheed Martin = TEVV, adversarial testing, audit/provenance (CATO/ArcCert), continuous monitoring

## Graphics
- `loe1-graphic-1.png` — **Evaluation Harness Architecture** — circular diagram showing Evaluation Harness at center (Protocol Layer, Model Abstraction, Execution Environment, Benchmark Integration Interface), surrounded by three team-role panels: Execution Engine (EdgeRunner: container runtime, multi-model APIs, DDIL execution), Measurement Suite (BigBear: HELM/Inspect/AgentDojo, human-AI scoring, agentic pipelines), Monitoring & Audit (Lockheed: real-time drift, CATO/ArcCert logging, structured report API). Reusable for any team-based platform architecture.
- `loe2-graphic-1.png` — **Benchmark Development Framework (LOE2)** — 5-step vertical pipeline: Requirements & Design → Dataset Curation → Version & Quality Control → Validation & Review → Publish & Deliver. Bottom tags: Safety / Reasoning / Coding / Multimodal / Agentic / DDIL / Edge. Reusable for any data pipeline, benchmark, or evaluation methodology proposal.

## Files
- `_index.md` — this file
- `loe1-evaluation-harness.md` — full LOE1 submission text
- `loe2-benchmark-platform.md` — full LOE2 submission text
- `loe1-graphic-1.png` — Evaluation Harness Architecture diagram
- `loe2-graphic-1.png` — Benchmark Development Framework pipeline

## Notes
- Written for a DIU/ODNI technical audience familiar with ML evaluation concepts — appropriate technical depth
- "Department of War" (DoW) is the document's term for DoD — artifact of the solicitation's language
- Both LOEs were submitted as standalone documents but reference each other; the separation is deliberate (government can award one or both)
- LOE2 Section 2.2.1 describes EdgeRunner's "production-proven Bronze dataset workflow" — this is a specific differentiator worth calling out in future TEVV or data pipeline proposals
