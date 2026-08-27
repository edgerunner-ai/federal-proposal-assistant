# EdgeRunner AI Capabilities

> **Reframed 2026-07-23** around EdgeRunner's converged story: *fielding AI is a stack, not a model.* A capable model is the easy part; owning it, running it where the mission is, trusting it to act, and proving what it did is the work. EdgeRunner builds the whole stack on customer-owned silicon, with **no cloud in the critical path**. Source collateral: `edgerunner-papers/` (Fielding AI is a Stack, Capable Isn't Fieldable, Ground Truth Capability Readout, ecosystem/product briefings + slicks), the EdgeRunner Capabilities Library, and the Ground Truth / Warrant demo. See the **Maintainer notes** at the end for open confirmations before high-stakes citation.

## How to talk about maturity (use these labels, not looser ones)

EdgeRunner labels maturity honestly, and proposals must inherit that discipline:

- **Fielded / TRL 8**: running in a program of record (Navy ICOP / PMW 120).
- **Proven**: tested and measured (results are internal-evaluation, "reproducible on request," not certified benchmarks unless a published paper is cited).
- **Built**: runs today.
- **Building**: in active development, path clear.
- **Roadmap**: designed, path clear, not yet built.
- **Proof-of-concept (PoC)**: a single end-to-end run demonstrating feasibility (e.g., DORIS). Not fielded, not benchmarked.

**The honesty line (carry into every proposal).** We say a capability *implements the pattern of* a standard, never "compliant" (compliance is an accreditor's judgment, not a vendor's claim). We cite an **IATT as an IATT, not an ATO**. For Ground Truth we hold one line without exception: **attribution, not truth; fail toward caution; a receipt for every decision.** These are enforced by the prose-lint / prohibited-claims gate. Don't upgrade an IATT to an ATO or "proven" to "certified" in draft prose.

---

## The EdgeRunner Stack: five layers that make AI fieldable

EdgeRunner is not five products bolted together. They share one runtime, one authority model, and one design philosophy: **the mission owns its AI, and the AI proves itself.** Read bottom to top; all of it runs on hardware the customer owns.

| # | Layer | What it is | Maturity |
|---|---|---|---|
| 5 | **Ground Truth** (governance) | Model-agnostic verification/authorization layer over everything the AI says and does | Proven / Built |
| 4 | **WarClaw** (agentic orchestration) | Mission-workflow orchestration: tradecraft codified as auditable, versioned software | Built · TRL 7 (NGC2 demo) |
| 3 | **Secure runtime** | Hardware-agnostic, air-gapped, containerized inference engine | Fielded · active IL-6 IATT |
| 2 | **Custom adapters** | Per-MOS/AFSC LoRA adapters that fit any base model to a mission without full retrain | Proven |
| 1 | **Custom models** | Military-specific models on open-weight foundations, sized to the mission's hardware; BYOM | Fielded · TRL 8 |

**The spine: two principles run vertically through all five layers:**
1. **No cloud in the critical path.** EdgeRunner implements the stack on customer-provided silicon; the customer owns what is deployed.
2. **Authority is data, not weights.** The mission's authority lives in a signed *ledger*, not in the model's weights. Change the ledger, the policy floor, or the grounding mode, and the AI's outputs and an agent's permitted actions change with it, live, without retraining or redeploying the model. This is what makes "deploy in any environment, re-point to any policy" an engineering property rather than a promise.

**The four structural gaps the stack closes** (the "capable isn't fieldable" argument, use as the problem frame in narratives):
1. *You don't own it.* A model behind a vendor API can't be accredited, can't run disconnected, can't be guaranteed to behave the same tomorrow.
2. *It can't run where the mission is.* The edge is disconnected, on the unit's hardware, accredited to a specific impact level.
3. *It can't be trusted to act.* The moment a model stops answering and starts *doing*, a wrong step executes before anyone can catch it.
4. *It can't prove what it did.* An accreditor, an auditor, and a commander all need evidence of what authority an answer rested on and why an agent acted.

---

## The Edge Mission Loop: one loop, closed at the edge

The five products execute the **military-specific AI lifecycle at the edge, without connectivity**: **Sense → Reason → Act → Verify → Learn**, on the operator's own hardware, human-gated, sharper each pass. Conventional AI splits this loop across the cloud (trained in a data center, verified and retrained far from the fight); EdgeRunner runs the entire loop on one disconnected device.

| Loop stage | Product(s) | Role |
|---|---|---|
| **Sense** | EVELYN | Machine vision: target ID on live feeds; labeled datasets from a handful of seeds |
| **Reason** | EdgeRunner models + adapters | Military-tuned inference: corroboration, assessment, reporting |
| **Act** | WarClaw | Orchestrates the workflow; holds the human gate; writes the audit trail |
| **Verify** | Ground Truth | Grounds each claim (and, at the action frontier, each agent action) in approved authority; hands back a receipt |
| **Learn** | DORIS *(PoC)* / EVELYN | On-device adaptation: the model improves where the mission is |

**SPOTTER** is the flagship worked instance (unsolicited concept, working name, not a fielded product): an analyst types a new target of interest; **WarClaw** stands up a watch agent that tasks **EVELYN** (seeded, not retrained) to identify it on tactical UAS full-motion video; WarClaw tips the analyst with frame, confidence, timestamp, and frame-center geolocation from the video's own KLV metadata; the analyst confirms; **EdgeRunner models** corroborate against other intelligence and draft the reporting; **DORIS** is the phase-2 learning loop. All on one device, air-gapped. Positioned as *a tipping-and-cueing aid with a human in the loop, not a weapons-cueing or fire-control system.* (See `proposals/spotter/` and `edgerunner-papers/spotter-concept`.)

---

## LAYER 1: Custom Models (Fielded · TRL 8)

Sovereign intelligence you own and run. Military-specific models built on **open-weight foundations**, trained on military data (doctrine, policy, missions, and 16M+ real-world CamoGPT messages [CONFIRM CamoGPT data figure with CTO before citing externally]), and **sized to the mission's hardware envelope, not the other way around.**

> **In proposals and customer-facing material, refer to models by tier name only; do not name open-weight source models (Gemma, gpt-oss, Llama, etc.).** **Smaller is not lesser**: tier selection is a deployment choice, not a quality ladder. A Light-tier model in the operator's hand beats a frontier model that can't run there at all.

| Tier | Alt label | Operational Role | Model Range | Hardware Class | Optimized For | Typical Workloads |
|---|---|---|---|---|---|---|
| **Light** | Tier 1 | Immediate Operator AI | 1B - 4B | Handheld, tablet, laptop, TAK device (8 GB VRAM min) | Speed, low power draw, disconnected-ops survivability | Reporting, translation, entity extraction, voice assistant, structured-data capture at the point of work |
| **Medium** | Tier 2 | Tactical Mission Assistant | 7B - 26B | Rugged workstation, CANES afloat node, vehicle-mounted compute (16 GB VRAM rec.) | Multi-step reasoning, domain workflows at the edge | ISR fusion, technical-manual Q&A, planning support, MOS/AFSC-specialized assistants via LoRA adapters |
| **Heavy** | Tier 3 | Mission Cell / Edge AI Server | 70B - 400B+ | Edge AI server, shipboard node, fixed-site rack (multi-GPU) | Shared inference, deep analysis, on-prem fine-tuning | Multi-user analysis, model adaptation per command, LoRA training pipelines, doctrinal knowledge synthesis |
| **BYOM** | n/a | Bring Your Own Model || any open-weight | any of the above | No lock-in; competitive model refresh (MOSA) | Run gpt-oss / Mistral / Llama in the same runtime |

> **[CONFIRM: tier boundaries]** The public one-page slicks describe tiers more loosely (Light 0.5B+/4GB, Medium 4B+/8GB, Heavy 24B+/40GB enclave) than this table (which matches the EdgeRunner Compression paper's Medium≈24B / Light≈4B). The boundaries differ materially at the Heavy floor. Treat this table as the internal reference; reconcile with CTO before publishing exact parameter/VRAM cutoffs in a capability matrix.

**Tier-specific inherent advantages** (frame as advantages, not "compromises vs. frontier"):
- **Light**: sub-second time-to-first-token; runs on GFE already in the operator's hand; no thermal envelope problem; no network dependency.
- **Medium**: GPT-class task accuracy without ceding data to commercial cloud; fits a tactical power/bandwidth budget. Demonstrated GPT-5 task parity at this tier (Paper 2, EV-031).
- **Heavy**: frontier-class capability inside the security boundary; centralized fine-tuning/LoRA training closer to the data. 120B in development; EdgeRunner can retrain any open-weight model up to and beyond 400B parameters under contract.

**Sovereignty is the point of owning the model**: a model you can accredit, run offline, and depend on to behave the same tomorrow, which no rented API offers a classified mission. And *owned no longer means outgunned:* EdgeRunner's published research (EdgeRunner 20B, Paper 2 / EV-031) reports **GPT-5 parity across four military test sets at 95%+ statistical significance**, on 1.6M curated, SME-validated military training records. Because the rest of the stack is model-agnostic, this layer is a choice, not a lock-in.

- **EdgeRunner Medium**: flagship military-tuned model (the *current product*); GPT-5-class task parity at the edge.
- **EdgeRunner Light**:1-4B tier for the most constrained edge hardware; rapid iteration, VRAM-premium tactical deployments.
- **EdgeRunner Heavy**: 70B+ tier; 120B in development.
- **MilDeflect**: eliminates 98%+ commercial-LLM refusal on legitimate military queries; 66.5-point answer-rate improvement via abliteration (Paper 1 / EV-030).
- Military evaluation benchmarks: mil-deflect-bronze/gold, combat arms, combat medic, cyber ops, mil-bench-5k.

Reference graphic: `my-company/graphic-templates/08-model-tier-reference.html` (`.png` for Word). `[CONFIRM with Bill / CTO whether the published 20B is a precursor to Medium or a separate research demo before re-citing in new proposals.]`

## LAYER 2: Custom Adapters (Proven)

Per-mission fit, without a full retrain. A general model doesn't speak a specific mission's language; EdgeRunner builds **military-specialist LoRA adapters, tuned per MOS / AFSC**, that refine any base model to a mission without retraining it from scratch.

- Initial mission-specific adapters delivered in **30-60 days** (doctrine-grounded and SME-vetted), orders of magnitude cheaper than retraining.
- **Operational today:** Combat Arms, Combat Medic, Cyber, Logistics, Acquisitions (plus PED, Mission Planning per the stack collateral).
- **90-day delivery committed:** Special Forces (18-series), PSYOP (37-series), Civil Affairs (38-series).
- Adapters change what the model *knows*; **authority** (what it is *allowed to say and do*) is handled separately as data, not baked into weights. Two independent dials: swap the **adapter** to change the mission the model is fluent in; swap the **ledger** to change the authority it must answer to.
- Abliteration, DPO, and on-policy distillation across all tiers: Light for rapid iteration, Heavy for production-scale training runs.

### Model Optimization & Compression (EdgeRunner Compression)
The mechanism that fits Medium (24B) / Light (4B) models onto commodity GFE and forward edge devices without sacrificing task accuracy (Paper 3 / EV-032, EV-048; ghost vs. naive quantization EV-092).
- Production models compressed to **~3-4 bits/weight** on average (8-10× reduction) while retaining task accuracy; 3-5-bit models perform close to 8-bit quality.
- "Efficiency Functions" model domain-specific quantization-error propagation for statistical, per-tensor candidate selection, not uniform quantization.
- Auto-tunes a model to a target VRAM footprint (e.g., 4 GB) and platform (AMD/Nvidia): engineers set target size in bytes, pipeline produces the optimal model.
- MOS-specific post-training tuning (800 GB-2 TB proprietary data); pipeline runtime <3h (Medium), <1h (Light).
- Quantization-aware LoRAs roughly double KLD reduction at the same adapter size.
- Generalizes across dense, MoE, state-space, convolutional architectures, plus LoRA adapters and embedding models.
- EdgeRunner-reported gains: 20-30% lower KL-Divergence; 50-90% error reduction in short/long-form evals (strongest MOS-specific); ~50% embedding-model error reduction.

## LAYER 3: Secure Runtime (Fielded · active IL-6 IATT)

The hardware-agnostic inference engine that holds models, adapters, and orchestration together: **runs where the mission is, disconnected, on the mission's hardware.**

- Fully air-gapped operation (zero internet/cloud dependency); operates in DDIL environments.
- Runs on laptops, workstations, tablets, ATAK-enabled devices, edge servers, fly-away kits.
- Hardware-agnostic silicon runners: **Intel, AMD, NVIDIA, Qualcomm, Apple**; backends **ONNX, CUDA, Vulkan, Metal**. 8 GB VRAM min (Light); 16 GB rec. (Medium); workstation/edge-server class (Heavy).
- Cross-OS: Windows, Linux, macOS. Deployable as binary or containerized web-hosted application.
- **Integration surface:** OpenAI-compatible API (systems built for GPT-4/Claude plug in unmodified), REST, gRPC, SQL; **MOSA-compliant** so model components are competitively upgradeable. Bring Your Own Model (BYOM).
- Extends the enterprise to the edge, carrying **MAVEN** and **Advana** intelligence forward to the unit where reach-back fails, with no cloud in the critical path.
- Keeps a local decision point over a cached, signed copy of the mission's authority, with a defined degraded mode.
- Deployment footprints: air-gap, GovCloud, on-prem, hybrid.

### Secure Deployment & IL / Accreditation posture
- **Active IL-6 Interim Authority to Test (IATT)** covering the AI Runtime + models. **Cite as an IATT, not an ATO.** Full IL-6 ATO expected October 2026 at ICOP deployment. *(State IL-6 IATT as a standalone claim; list Navy ICOP / PMW 120 separately as a program-of-record engagement; see Maintainer notes on the pairing.)*
- **IL-5 ATO: in progress** (U.S. Space Force SSC), expected August 2026. *Do not state as "in hand."*
- Accreditation covers EdgeRunner's AI Runtime + models only; **WarClaw, Ground Truth, EVELYN, and DORIS are not separately accredited.**
- CAC-enabled access to secure DoD networks; RMF-aligned; NIST AI RMF flywheel architecture; cross-domain deployment patterns; Docker-compatible containerized microservices.

## LAYER 4: WarClaw · Agentic Orchestration (Built · TRL 7)

**WarClaw is mission-workflow orchestration: tradecraft codified as versionable, validated, auditable software.** It is the control plane between operators and their existing tools/data, running fully on-device on the EdgeRunner Runtime, **model-agnostic** over the runtime's models. Released as a commercial product April 2026; in active development.

**Orchestration, not autonomy: WarClaw sequences the work; people approve the decisions.** An agent may act only when its intended action can be justified; the Ground Truth layer authorizes or blocks that action and writes the receipt.

**Four-tier composition model:**
- **Tool**: an atomic capability such as a data query, API call, or inference job (SOCET GXP, NGA Entity Lookup, MARS OOB).
- **Skill**: an SME-authored tradecraft playbook, versioned like software (e.g., `geoint-exploitation v2.3`, `sigint-ped v1.8`, `osint-triage v3.1`).
- **Role**: composes skills against doctrine (All-Source S2, GEOINT Analyst, Mission Planner).
- **Mission Workflow**: routes a joint mission (SOF Targeting, ATO Build, All-Source PED).

**Key properties:**
- Skills are auditable software: versionable, validated, separable, reusable across workflows. "A prompt is a habit; a skill is versioned, validated software."
- **The execution record is a first-class output:** every run logs which skills ran at what version, over what data, who approved what (e.g., "4 lanes · 3 skills · 2 approvals · 1 typed product," sha256-stamped, on-device). Every output is attributable.
- Human approval gates by design; analyst-reviewed lanes; approval before consequential steps.
- Applies **ICD 203** conventions: stated confidence levels, Most Likely / Most Dangerous COA formulations.
- Synthesizes typed outputs (assessments, orders, briefs); native to disconnected/DDIL operation, no cloud round-trip.
- Integrates by OpenAI-compatible interfaces and standard connectors: "integration by standard API, not bespoke engineering per deployment."
- Console: converse / build pipelines / orchestrate multiple watch agents from one screen.

**Maturity / proof:** **TRL 7**: prototype demonstrated in an operational environment, tested with real data sources via the Army **Next-Generation Command and Control (NGC2)** program, June 2026. *Honesty caveat: NGC2 was a demonstration with real data, not a contract delivery or a program of record.* Anchor mission: SOF targeting. Expanding: All-source PED, C2 decision support (COA generation, fires sequencing, mission-planning briefs), ATO build, Logistics, Intel/ISR.

**Demonstrated: "Discipline as Software" (intelligence production).** Beyond the NGC2 C2 demo, WarClaw + Ground Truth + the government-tuned model has been built and demonstrated end-to-end, air-gapped on a single box, running an analyst's SOP as a pipeline: the SOP's roles become separate agents (including a peer reviewer and duty editor held as **distinct model identities so no role grades its own work**); Ground Truth enforces the production standards (ICD 203/206 + the unit SOP) at deterministic gates **with no model in the verification loop**, unverified judgments are **held for the analyst**, and every released product carries a **signed WBOM receipt**. Flagship demos: an all-source **Daily Update** pipeline; a full **JIOC Commander's Daily Update** SOP on live OSINT (three model roles, peer review + duty editor, Annex A product); and an all-source **INTSUM** assessment that publishes to a product library which re-verifies and signs on ingest (tamper-evident). *Maturity: built / demonstrated, lab-validated, not fielded or ATO'd; demo scenarios notional/UNCLASSIFIED; self-authoring the pipeline from the CONOP is roadmap.* One line: **"Your SOPs are already software specs; WarClaw compiles them."**

**Demonstrated: conversational operation ("Operator").** A thin control layer lets an operator drive the stack in plain language and stay out of the tooling. State a goal, and Operator maps it to one of a few governed actions: **verify** an answer against an approved ledger, **run** a mission pipeline by name, or **build** a new Ground-Truth-gated pipeline from an uploaded document. Intent routing is **deterministic (rule-based, not model-emitted), so it is auditable**; consequential actions (run and build) **hold at an operator-approval gate** before they execute, and every verified answer returns a **signed WBOM receipt**. Governance stays on even when the interface goes quiet. Demonstrated end-to-end: from a unit removable-media SOP, Operator built a new verified pipeline, confirmed it live, then answered a real question at full attribution (Ground Truth PASS) with a released product, all through chat and no console. *Maturity: built and demonstrated as a proof-of-concept, not fielded; the **build** action is a narrow demonstration (verified-Q&A pipelines from a document) of the "self-author the pipeline from the CONOP" step that stays roadmap for general workflows.* One line: **"You bring the problem and the document; EdgeRunner builds, checks, and runs the pipeline, and hands back the receipt."**

**Demonstrated: checklists compiled into software processes (the reusable pattern).** The pattern is the capability; the individual workflows are **user-built, with measured effectiveness, not productized offerings.** A written procedure becomes an executable process by composing four things the stack already provides: a **pipeline** that encodes the steps, **agents** that hold the roles, **skills and connectors** that reach the tools and data the step needs, and a **deterministic gate** that checks each product against the standard before it moves. A human approves at named steps and a signed receipt records what the run stood on.

EdgeRunner puts the guarantee in the process rather than the prose. Output wording varies between runs; the **properties do not** - traceability to approved evidence, conformance to the stated format, and refusal when neither can be established. A bounded pipeline delivers that predictability. Additional training does not: training raises typical quality, while the architecture around the model is what holds output to a standard.

**Measured, on EdgeRunner's own workflow corpus (internal evaluation, reproducible on request):**
- **The scaffolding carries the work, not the model.** Across 17 workflows built from operational requirements: 98 executed steps, of which **68 are deterministic code, 19 are model calls, 9 are conditions** - the model is roughly a fifth of the executed work.
- **Governed and ungoverned runs of the same task are directly comparable.** Workflows ship in A/B pairs - the same task once *unassisted* (the model answers with no rules or evidence identifiers supplied) and once *gated*. The unassisted run answers fluently without citations and will invent evidence identifiers; the gated run traces every claim to approved evidence and holds what does not trace. The contrast is the demonstration.
- **A generative model is unreliable as the verifier. Ours is not one.** On an internal hand-labelled entailment set the on-device 26B scored 7/10 (its reasoning variant 6/10), and **5 of 10 cases changed verdict across identical runs at temperature zero.** This is the measured basis for Ground Truth's deterministic core and for keeping no model in the verification loop. The evaluation harness ships with the workflow so the measurement can be repeated after any model or prompt change.
- **Scoping a model's inputs is a stronger control than filtering its outputs.** Where a workflow must not surface certain material, restricting what the model is shown - rather than redacting what it produces - removed withholdable content entirely in tested runs, against a counterfactual where the same task with unrestricted inputs produced it. A model cannot disclose what it never received.

**How they are delivered.** Workflows are packaged individually with the pipeline definition, a runbook, the data the steps read, an installer, and an **Ed25519-signed manifest** declaring dependencies, install route, step composition and runtime requirements. A **verifier ships with the library**. A recipient confirms for themselves that nothing was changed, added or removed. Any file present but not covered by the signature fails the check; it does not merely warn. A WarClaw application screen is declarative configuration. EdgeRunner therefore **generates an operator click-to-run screen for each workflow from its own definition**, and the installer re-points the screen's action to the identifier assigned on the receiving system.

**Why this fits military customers specifically.** The pattern requires a written-down standard to check against. In most commercial environments process lives in habit rather than documentation, and there is nothing for a gate to enforce. Military process is documented - doctrine, SOPs, ROE, analytic standards, unit TACSOPs - each with a proponent and an approval authority. **We are not asking a unit to adopt a new process; we are instrumenting the one it already runs.** Adoption therefore requires no process change.

*Maturity: the pattern is **built** and demonstrated repeatedly; individual workflows are **user-built demonstrations**, lab-validated on notional or UNCLASSIFIED scenarios, **not fielded and not accredited.** Measured figures are internal evaluation on EdgeRunner's own corpus, not customer-environment results or certified benchmarks. Workflows currently execute arbitrary code steps. That keeps them quick to build. Template-only assembly is the form suited to a controlled deployment boundary; it follows the Pipeline Builder path and remains an MVP.* One line: **"A checklist is already a software spec; we compile it, gate it, and hand back the receipt."**

Evidence: EV-072 (WarClaw C2 / NGC2 demo, TRL 7), EV-079 (orchestration-as-auditable-software capability), EV-104 (Discipline-as-Software intel-production pipeline, demonstrated air-gapped), EV-105 (conversational "Operator" orchestration, demonstrated PoC), EV-110 (governed-workflow delivery model + measured step composition), EV-113 (input-scoping leakage control, measured), EV-116 (untrusted-oracle adjudication of external model output, PoC), EV-117 (generative model unreliable as verifier - measured design rationale), EV-118 (signed, verifiable workflow delivery), EV-119 (generated operator screens).

> Lineage note: WarClaw is built on the **OpenClaw** open agent framework (the OpenAI-compatible API surface and integration model). Prior collateral described WarClaw as "the warfighter's digital adjutant" / "military-specific JARVIS" with native Microsoft Office (PowerPoint/Word/Excel/Teams/Outlook) integrations, still valid; the current framing leads with orchestration-as-auditable-software.

## LAYER 5: Ground Truth · Governance (Proven / Built)

Ground Truth (engineering name **"Warrant"**) is a **model-agnostic verification layer** that sits *after* any model or RAG pipeline and checks whether each claim in an answer traces to a **human-approved evidence ledger** built from sources the commander already signed. It does not generate text. **Authority is inherited from the issuing source and never adjudicated by AI; the citation check and gate need no model in the loop.** *"RAG retrieves context; Ground Truth resolves authority."*

**One line, held without exception: it checks *attribution to approved authority, not truth*, and it *fails toward caution*.** It will withhold or flag before it certifies something it can't trace. Built to **ICD 203** analytic-tradecraft standards (and **ICD 206** sourcing); every output links back to verifiable evidence or is flagged.

**Core loop (the foundation):** Approved ledger → deterministic verify → gate (**pass / flag / block**) → **WBOM receipt**.
- **Green / amber / red attribution.** Every claim is Supported (traces to an approved source line → PASS), Needs-review (a match a human must confirm → FLAG, never auto-promoted), or Unsupported (→ BLOCK). Retired/restricted status flags superseded or withdrawn sources.
- **Portable audit receipt (WBOM, Warrant Bill of Materials).** An attachable "SBOM-for-AI-output" showing exactly which approved facts warrant each claim. Now **signed & hash-chained (Ed25519 + SHA-256)**, binding the answer to the exact ledger version checked so later alteration is detectable; carries a **governance manifest** (superseded/expired/stale entries + accountable owners). "The artifact an accreditor accepts."
- **Human-gated ledger.** "People approve; models propose." Entries are proposed until a designated reviewer confirms fidelity to the source; only approved entries are citable; only high-confidence authoritative entries auto-correct; softer matches are surfaced for human judgment.
- **Three enforcement levels.** L1 Annotate (visibility only, default, no workflow change) · L2 Correct-from-source (flag and correct conflicting statements with source shown) · L3 Constrain-to-sources (model may state only what an approved entry supports and must cite it; anything else refused).
- **Deployment patterns.** Inline sidecar · API (answer in → checked answer + receipt out) · Batch/CI gate · Authoring studio. Targets: cloud, accredited enclave, on-prem, edge/disconnected; the deterministic core needs no network, no retraining (air-gap-ready).

**What shipped on top (July 2026 capability readout, "unified on main"):**
- **Deeper verification:** *anti-cite-spam floor* (a cited ID that doesn't overlap the claim is downgraded to review); *entailment cascade* (**validated live**: catches a claim topically identical to approved doctrine but semantically its opposite); *scope router* (out-of-scope claims marked, not force-verdicted); *conflict-sensitive ledgers* (a clean-but-unjudged answer on safety-critical doctrine is flagged, never passed clean); *claim segmenter* (compound sentences split into discrete claims, each checked; coverage measured).
- **Fieldable-at-edge scale:** persistent vector index (O(N) → ~O(log N); cold start ~53s → <1s; int8, 4× smaller); multi-ledger router (routes across many ledgers without silently dropping one); signed index artifacts (verified against a public key before use).
- **Living-authority governance:** effective-dating & supersession (superseded entries yield a `superseded` verdict and the gate blocks them); freshness windows + named accountable owners; canonical schema with provenance anchors + document hash.
- **Hardening:** authenticated control plane (bearer token + loopback bind + audit log on every mutating route); **IL-6 key custody** documented for accredited/air-gapped deployments.
- **Authorize, the new frontier: from verifying what AI *says* to authorizing what an agent *does*.** The same warrant gate now governs agent **actions**: a proposed action is checked against a human-approved policy ledger (**allow / deny / default-deny** for anything unrecognized) and carries a receipt. Delivered as an **`/api/check_action`** endpoint (the second enforcement point). *Note: the answer-verification side is built and demoed; per-action authorization and the assurance hardening around it are the active build-out (largely roadmap on the action side).*
- **Tradecraft-review component** grades a finished document for completeness against a pluggable standard (ICD-203, ICD-206, OPORD, answer-quality, or a custom rubric authored from a policy or an RFP's **Section L/M**), yielding a compliance scorecard.

**Doctrine / guidance-as-a-ledger.** Validate authoritative guidance once into a "gold" ledger; layered echelon ledgers with monotone-tightening precedence let lower echelons add but never override higher guidance.

**Measured results (internal evaluation, "characterizes the current build, reproducible on request", not certified benchmarks):**
- **6/6** citation-spoof attempts caught, **0** false positives.
- **1,946 pages** across **8** capstone manuals governed into **3,913** rule entries (the demo repo shows a 4,054-entry, 10-source corpus; cite the figure matching your source).
- Verification near-flat at scale: ~2s at 100 entries, **~2.9s (warm)** at ~3,900 entries.
- 70/70 approved rules anchored verbatim to source; review-by-exception auto-clears **66%** of extraction candidates.
- Honesty tiers (demo): *assisted* (proves the plumbing) / *unassisted* (model alone → everything BLOCK/FLAG, **zero false passes**) / *retrieval-augmented* (the realistic production middle tier).

**Maturity.** Built + Proven; **TRL 7** (system prototype demonstration in an operational environment, per the DoD Technology Readiness Assessment Guidance) because First Army ran it on their own mission threads, in their environment, not on a representative surrogate. Confirmed by Bill Bal 2026-08-27; this retires the earlier "do not assign a TRL" instruction and supersedes the TRL-5 figure in the 2026-08-26 adjudication sheet, which did not originate with the CTO. TRL 7 is a maturity statement only. Validation context is **First Army** (doctrine-as-a-ledger; three documented field failures, including a silent 116→6 undercount and fabricated doctrine, each turned into a *reported* error). No ATO of its own; only EdgeRunner's AI Runtime + models are accredited. Components: ledger-builder (propose facts), warrant-ledger (verify, emit WBOM), tradecraft-review (standards/rubric completeness), `/api/check_action` (action gate). Evidence: EV-073 (verification layer), EV-074 (doctrine/guidance-as-a-ledger + standards check), EV-094 (measured results + signed WBOM), EV-095 (action-authorization frontier).

**Standards convergence (the "Capable Isn't Fieldable" argument, use as the Ground Truth win theme).** U.S. and allied guidance has converged on treating every AI system and agent as an untrusted actor that must be authorized for what it does and logged when it does it: **NIST SP 800-53** (under DoD RMF, the accreditation gate), **DoD Zero Trust Reference Architecture v2.0 (FY2027 target)** (deny-by-default, per-request least-privilege authorization for every non-person entity), **DoD AI Ethical Principles: Governable & Traceable**, **Five Eyes agentic-AI guidance**, NIST SP 800-207/207A, agent-identity work. Reduced to **five operative properties** every AI answer/action must carry: (1) denied by default, (2) authorized per request on its justification, (3) logged in a signed, portable record, (4) least privilege scoped to authority, (5) disengage-able, human-gated on high impact. Ground Truth delivers the **answer side** today (pass/flag/block gate, per-answer WBOM, answers scoped to cited authority, all Built); the **action side** is the build-out. *No DFARS/CMMC mandate binds a contractor to this yet; the posture is "the reference implementation before the mandate lands" (strategy, not fielded fact).* WBOM aligns to the SBOM family accreditation pipelines already consume; it sits *alongside* content-provenance standards (C2PA/Content Credentials answer "who signed this"; Ground Truth answers "is this grounded in approved authority").

---

## EVELYN · Machine Vision & Data Labeling (Fielded · TRL 7)

**EVELYN** (EdgeRunner's Versatile Environment for Labeling and Yielding New datasets) is an edge-deployable machine-vision system: it identifies targets on live sensor feeds and converts collected imagery into labeled, training-ready datasets, **on a laptop, offline, from a handful of seed examples.** One embedding engine, **two use cases**, recognizing objects by **similarity in embedding space rather than by retraining** ("seeded, not trained").

- **Use case 1 · Live target identification:** novel objects on live feeds in seconds from a text prompt or single seed, no retraining.
- **Use case 2 · Image labeling:** segmentation masks, boxes, keypoints; the embedding vector store refines as analysts correct.
- Engine loop: segment candidate regions → embed → match against seeded examples. Two paths: **Path A · Direct** (embedding-match on frames, novel target seeded on the spot) and **Path B · Trained** (EVELYN-built dataset trains a compact fixed-class detector for edge power budgets, the demonstrated path).
- **Standards-native exports:** COCO, YOLO, Pascal VOC. Every dataset ships with its manifest; every label traces to a real frame (no synthetic imagery).
- Human-in-the-loop; validated on **IR, night-vision, and fog**; person identification across appearance changes; **correctly classifies adversarially poisoned images** that mislead conventional YOLO detectors. Air-gapped, no external API calls; same software laptop → datacenter.
- **Metrics (demonstration / internal eval):** 180K+ labeled detections from 1M+ frames, seeded with 32 images/class across seven drone types → trained a working multi-object tracking model (annotation in hours, not weeks); **7,800+ labels/hour on a laptop** (offline CPU), 42,000+/hour on cloud GPUs. "Scales with hardware, not people." Free on hardware you own.
- **Maturity:** **TRL 7**: demonstrated in a military laboratory on real-world data (Army xTech demo; SDA TAP Lab and U.S. Space Systems Command engagements). **CDAO Tradewinds Awardable, July 2026** (listed on the Tradewinds Solutions Marketplace). *Honest gaps EdgeRunner itself flags: native streaming ingest (video is frame-based today), sustained frame-rate/latency on named SFF hardware against a live feed, precision/recall vs. a trained baseline, and native cross-frame track association.* Evidence: EV-070, EV-077.

## DORIS · On-Device Model Adaptation (Proof-of-Concept, not fielded)

**DORIS** (Document Orchestration, Refinement, Intelligence & Synthesis) turns a unit's own documents into a fine-tuned model: **organize → generate a training set → fine-tune → export, entirely on-device and offline, data never leaving the box, no data scientist in the loop.** It is the *learning loop for the reasoning model*; it adapts an existing base model (LoRA/fine-tune) and is deliberately **not** a vision-detector trainer (that is EVELYN's no-retrain lane) and not a foundation-model trainer.

**Four-step pipeline:** (1) Ingest & organize (PDF/DOCX/MD, OCR for scans; embedded and clustered into role-specific collections) → (2) Generate the dataset (autonomous Q&A generation with a **judge-LLM quality gate** validating completeness, relevance, factual consistency, "a judge, not a labeler") → (3) Fine-tune (LoRA or full; hardware-aware, auto-detects CUDA GPU / Apple Silicon / CPU; 4-bit quant + gradient checkpointing; checkpoint-resilient across power loss/thermal throttling) → (4) Export & deploy (SafeTensors + quantized **GGUF Q4-Q8** + a generated model card).

- **Maturity: proof-of-concept, stated emphatically.** Results are from a **single end-to-end run** on edge hardware (NVIDIA Jetson Thor), over military/tactical doctrine: 35 datasets · 12,993 Q&A pairs generated autonomously (~8.3 days on one endpoint; projected ~40h with five parallel endpoints); a Light-tier LoRA in ~9.2h (4,875 steps / 3 epochs); 86% training-loss reduction (4.61 → 0.64). *"Not a benchmark, not a fielded result; reproducible on request."* Earlier in maturity than EVELYN and WarClaw; a background process measured in hours to days.
- **Build path ahead (roadmap):** throughput (days → hours via multi-endpoint), hardening & accreditation, integration into the Runtime + WarClaw, vision-language fine-tuning on operational imagery.
- Evidence: EV-096.

---

## Other Technical Capabilities

### Retrieval-Augmented Generation (RAG)
- Local document ingestion (PDF, PPT, Word, structured data); citation-backed, doctrine-grounded outputs; FAR parsing and large-corpus search (millions of PDFs in milliseconds). *(RAG feeds a model context; Ground Truth audits what the model said; keep the two distinct in proposals.)*

### Intelligence Processing
- Translation: 25+ languages/dialects; transcription, summarization, entity extraction, cross-dataset correlation.
- Image recognition, facial recognition for HVI dossiers; link analysis, pattern-of-life modeling, COA generation.
- Discipline coverage: SIGINT, HUMINT, GEOINT, OSINT, MASINT.

### Battle Management & JADC2
- AI Battle Management Teammate aligned to TM-BM framework (13 subfunctions); COA generation, sequencing, evaluation.
- Containerized microservice integration into OSA / RADIS DevSecOps pipelines; sensor-data ingestion, operational-context modeling, real-time decision support.

### Agentic Workflow Automation
- Multi-step AI agent execution fully local (no cloud round-trips); acquisitions-focused agents (FAR parsing, procurement docs); agents for drones, robotics, autonomous systems (ARL JWS). Composable modular agent framework per intelligence task or operational workflow. *(WarClaw is the productized, auditable form of this; see Layer 4.)*
- **Turning a checklist into a software process** is the reusable pattern: pipeline (the steps) + agents (the roles) + skills/connectors (the tools and data) + a deterministic gate (the standard), with human approval at named steps and a signed receipt. Applied to intelligence production, acquisition capture, engineering triage and C-UAS decision support. *Individual workflows are user-built demonstrations with measured effectiveness, not productized capabilities - see Layer 4 for the maturity statement and the measured figures.*

### Domain-Specific AI for Embodied Autonomous / Robotic Systems (ARL CRADA 25-0047-J001)
Live CRADA with U.S. Army DEVCOM ARL, "Domain Specific AI for Robotic Deployments in Support of the Warfighter" (effective 2025-09-18; no-cost option, fundamental-research-only, no CUI/classified data).
- **Research focus:** GenAI-powered agents on embodied autonomous systems: how multiple SLMs/VLMs operate together on a constrained onboard system, each with a distinct role. Fine-tune open foundation models on military doctrine + image sets of key targets → specialized SLMs/VLMs → field-test on ARL robotic hardware.
- **Division of resources:** EdgeRunner contributes AI training compute infrastructure (~$5M/yr est., incl. IP); ARL contributes datasets, robotic hardware, test facilities (~$250K/yr est.). No personnel exchange.
- **Background IP disclosed (reduced to practice):** EdgeRunner **ODIN** (on-device inference software, HW/OS-agnostic, local vector store); EdgeRunner **EVELYN** (automated AI-powered data annotation; on-device similarity search against a pre-loaded vector store of target imagery); training methodology for fine-tuning lightweight object detection/classification models; pretrained models optimized for **detecting drones, guns, and tanks** (all flagged as IP the USG has an interest in).
- Positions EdgeRunner as a decision-/perception-layer contributor to autonomous ground/robotic efforts; **not** a claim to full platform autonomy, navigation, or physical manipulation, which EdgeRunner does not build.

### Machine Vision / Computer Vision
- YOLO model development and deployment; Vision-Language Models (VLMs) for multi-modal edge AI; onboard UAS/platform deployment of offline specialized vision models; CV for sensor-data exploitation and autonomous-system decision support. *(Productized as EVELYN; see above.)*

### Neuro-Symbolic AI
- ML + Automated Reasoning composition (DARPA CLARA TA1 pursuit); applied to complex multi-domain operational analysis.

---

## Deployment Models
- Government-furnished laptops/workstations (HP and Panasonic Toughbook ruggedized platforms validated)
- Tactical systems (ATAK)
- Edge servers / fly-away kits
- Containerized web-hosted (IL-5/IL-6)
- Distributed edge infrastructure (via Akamai partnership)

## Differentiators
1. **Fieldable, not just capable**: EdgeRunner ships the whole stack (own it · run it at the edge · govern it · prove it), not a model behind an API.
2. **Operates when the network doesn't**: zero cloud, zero latency penalty; no cloud in the critical path.
3. **Authority is data, not weights**: one stack re-points to any unit's SOP, any agency's rules, any classification regime by swapping the signed ledger, live, without retraining.
4. **GPT-5 parity on military tasks at the edge** (published research, arXiv).
5. **Fits that capability onto constrained hardware**: domain-aware compression to 3-4 bits/weight retains accuracy where naive quantization degrades it.
6. **Every AI output is attributable and auditable**: Ground Truth verifies each claim against approved facts and emits a portable, signed WBOM receipt (attribution, not truth; human-gated; fail toward caution).
7. **Tradecraft as auditable software**: WarClaw runs versioned, validated skills with a human gate and a first-class execution record; orchestration, not autonomy.
8. **Mission-ready, not just capable**: we deliver a bounded process with a standard enforced at each step and a human gate where it matters, so what is guaranteed is that output *meets the standard* - not that the wording is identical. Predictability is a property of the process, not the model.
9. **Purpose-built military AI**, not adapted commercial AI; refusal problem solved via MilDeflect.
10. **Edge-to-enterprise feedback loop**: structured data capture → continuous refinement (EVELYN/DORIS learning loops).
11. **Proven in special operations** (USASOC, 4th ID, USSF, Navy ICOP).
12. **Fastest path to contract**: Awardable on CDAO Tradewinds (EdgeRunner runtime and, since July 2026, EVELYN); a DoD program can issue a task order directly.

## Proof Points (Summary)
- **Program of record:** U.S. Navy ICOP / PMW 120 (NIWC Atlantic), furthest-along engagement, TRL 8, fielded.
- **Operational pilots:** USASOC (1st, 7th, 10th SFG; JFK SWCS); 4th Infantry Division (NGC2); active Army/Navy/Space Force formations.
- **R&D:** AFRL CRADA; ARL CRADA 25-0047-J001 / JWS (embodied-autonomy SLMs/VLMs; disclosed IP: ODIN, EVELYN, drone/gun/tank detectors); AI2C; NIWC Atlantic; U.S. Space Force research collaboration.
- **WarClaw:** Army NGC2 demonstration with real data (June 2026), demo, not PoR.
- **EVELYN:** Army xTech demo; SDA TAP Lab; U.S. Space Systems Command; CDAO Tradewinds Awardable (July 2026).
- **Ground Truth:** First Army doctrine-as-a-ledger validation; measured verification results (internal eval).
- **DORIS:** single on-device adaptation PoC run (Jetson Thor).
- **Procurement:** CDAO Tradewinds Awardable; USSF Tradewinds CSO Direct Award; NASA SEWP awardable.
- **Published research:** MilDeflect, EdgeRunner 20B, EdgeRunner Compression.

## Company Facts
- Founded 2024, Bellevue WA · Small business under NAICS 541511
- $17.5M raised (Seed + Series A)
- CAGE: 9Z176 | UEI: SLZTJUA8DBD3 | NAICS: 541511
- SAM.gov Active | CDAO Tradewinds Awardable | **active IL-6 IATT** (Runtime + models; full IL-6 ATO expected Oct 2026) | IL-5 ATO in progress (USSF SSC, expected Aug 2026)
- Partnerships POC: Dave Anderson, Head of Partnerships, dave@edgerunnerai.com

---

## Maintainer notes: open confirmations before high-stakes citation

1. **Model-tier boundaries** differ between this internal table (Light 1-4B / Medium 7-26B / Heavy 70-400B+) and the public slicks (Light 0.5B+ / Medium 4B+ / Heavy 24B+). Reconcile with CTO before publishing exact cutoffs in a capability matrix. `[CONFIRM]`
2. **IL-6 IATT ↔ Navy ICOP pairing.** Bill's 2026-07-02 direction: state IL-6 IATT as a standalone claim and do **not** attribute the IATT to PMW 120 / Navy ICOP in collateral; list Navy ICOP separately as a program-of-record engagement. The July 2026 one-page slicks (ecosystem, machine-vision) compress "Navy ICOP · IL-6 IATT" into one evidence cell; the long-form "Fielding AI is a Stack" keeps them separate. This ledger keeps them **separate** (the conservative reading). `[CONFIRM whether the slick pairing is now sanctioned.]`
3. **CamoGPT 16M-message training figure** appears in the stack collateral; confirm it is releasable at the target distribution before external citation. `[CONFIRM]`
4. **Ground Truth is TRL 7** (First Army, operational environment; corrected 2026-08-27, retiring the earlier "no TRL" rule). It is still not operationally fielded and holds no ATO of its own, and it must never be cited as past performance: no contract instrument covers the First Army work. All Ground Truth / DORIS / EVELYN metrics are internal-evaluation / "reproducible on request," not certified benchmarks.
5. **Action-authorization (`/api/check_action`) is partly demoed but largely roadmap on the action side.** Cite the answer-verification layer as Built; describe per-action governance as the active build-out, not a delivered capability.
6. **Zero-trust "reference implementation before the mandate" framing** is pre-decisional strategy from an internal enablement plan, not a fielded fact. Do not imply a binding DFARS/CMMC mandate exists.
7. **Downstream sync:** `components-table.md`, `edgerunner-profile.md` (Section 4 still says "IL-6 ATO Active" / "IL-5 ATO Active", now stale vs. the IATT correction), `published-research.md`, and `evidence-ledger.json` should be reconciled to this ledger. Evidence IDs cited above: WarClaw EV-072/EV-079; Ground Truth EV-073/EV-074/EV-094/EV-095; DORIS EV-096; EVELYN EV-070/EV-077; converged stack EV-078 (EV-077/078/079/094/095/096 were added to the evidence ledger in this update; EV-072/073/074 already existed). Note EV-071 is on-device translation, EV-075 is cleared personnel, EV-076 is teaming agreements; do not confuse them with the products above.
