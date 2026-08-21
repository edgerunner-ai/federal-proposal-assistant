# EdgeRunner AI — Consolidated Federal Company Profile

**Profile date:** 2026-05-08
**Profile version:** v2026-05-08 (consolidated)
**Maintained alongside (does not replace):** `capabilities.md`, `company-description.md`, `components-table.md`, `contract-vehicles.md`, `past-performance.md`, `published-research.md`, `evidence-ledger.json`

This file is a single-document federal company profile assembled from every EdgeRunner-related source in the repository as of 2026-05-08. Each section ends with a **Source-of-truth pointer** identifying the file(s) that should be updated when the underlying fact changes — keep this profile in sync by editing the source files first, then regenerating.

Items marked `[TODO: source needed]` are facts a federal company profile typically contains but which are not present anywhere in the repository. They are listed rather than guessed.

---

## 1. Company Overview

| Field | Value |
|---|---|
| Legal name | EdgeRunner AI, Inc. |
| Headquarters | Bellevue, WA |
| Founded | 2024 |
| Website | www.edgerunnerai.com |
| Funding | $17.5M raised to date (Seed + Series A) |
| 2026 operating-income projection | $5M (per Mystic Depot CSO Section 3.1) |
| Business size | **Small business** under NAICS 541511 (formal SBA size standard) |
| Socioeconomic set-aside certifications | None held |
| Headcount | `[TODO: source needed]` |
| Other office locations | `[TODO: source needed]` |

### Mission Statement (canonical, one paragraph)
EdgeRunner AI is a distributed tactical layer enabling secure, on-device execution of open-weight models in DDIL environments while capturing structured, mission-relevant data for GCC-level and enterprise refinement. Rather than replacing existing enterprise AI investments, EdgeRunner extends them to operators regardless of connectivity and transforms operational use into training-ready data — creating a continuous feedback loop from edge to enterprise and back.

### One-Sentence (for bios and footnotes)
EdgeRunner AI provides on-device AI execution, agentic workflows, and operational data capture for disconnected tactical environments.

**Source-of-truth pointer:** `my-company/company-description.md` (overview text); `my-company/past-proposals/mystic-depot-cso-2026/loe1-evaluation-harness.md` Section 3.1 (operating-income projection).

---

## 2. Federal Contracting Identifiers

| Field | Value |
|---|---|
| CAGE Code | 9Z176 |
| UEI | SLZTJUA8DBD3 |
| NAICS (Primary) | 541511 — Custom Computer Programming Services |
| Secondary NAICS | `[TODO: source needed]` (defense IT typically also uses 541512, 541330, 541715) |
| SAM.gov | Active |
| DUNS | Deprecated (UEI replaces) |

### Footer-bar format (single-line)
```
CAGE: 9Z176 · UEI: SLZTJUA8DBD3 · NAICS: 541511 · NASA SEWP · CDAO Tradewinds CSO · Active IL-6 IATT · Existing SOCOM Deployments
```

### Set-Aside Eligibility
- Small business under NAICS 541511 — Yes (formal SBA size)
- 8(a) / SDB / WOSB / SDVOSB / HUBZone — None held
- Nontraditional Defense Contractor — Yes (claimed and material to OTA submissions, per Mystic Depot CSO Section 3.1)

**Source-of-truth pointer:** `my-company/contract-vehicles.md`.

---

## 3. Contract Vehicles & Procurement Pathways

| Vehicle | Status | Notes |
|---|---|---|
| **NASA SEWP** | Awardable | Solutions for Enterprise-Wide Procurement — government-wide IT IDIQ |
| **CDAO Tradewinds CSO** | Direct-Award holder | USSF contract awarded under this pathway (see Section 6) |
| CDAO Tradewinds Marketplace | "Awardable" | Enables procurement through CDAO Marketplace without re-competing (distinct vehicle from Tradewinds CSO) |
| GSA Schedule (MAS) | Not held |
| Other IDIQs / consortium memberships | None held beyond the above (no SOSSEC / NSTXL / TReX) |

**Source-of-truth pointer:** `my-company/contract-vehicles.md`; `my-company/evidence-ledger.json` EV-020, EV-023.

---

## 4. Security Posture & Accreditations

### Authorization posture (corrected 2026-07-23 to match the 2026-07-02 accreditation adjudication and the current "honesty line" — cite an IATT as an IATT, not an ATO)
- **IL-6 Interim Authority to Test (IATT) — Active.** Covers the EdgeRunner AI Runtime + models. **State IL-6 IATT as a standalone claim.** Full IL-6 ATO expected October 2026 at ICOP deployment. *Do not describe this as an "ATO," "accredited," or "granted an ATO."* Per Bill's 2026-07-02 direction, **do not attribute the IATT to PMW 120 / Navy ICOP** in collateral; list Navy ICOP / PMW 120 separately as a program-of-record engagement (see Section 6). *(The July 2026 one-page slicks pair "Navy ICOP · IL-6 IATT" in one evidence cell — flagged for confirmation in `capabilities.md` Maintainer notes; keep them separate here.)*
- **IL-5 ATO — in progress** (U.S. Space Force SSC), expected August 2026. *Previously recorded here as "Active," which was inaccurate. Do not state as "in hand."*
- Accreditation covers the AI Runtime + models only — WarClaw, Ground Truth, EVELYN, and DORIS are **not** separately accredited.
- *Framing for proposal use:* an authorization from one program does not automatically translate to another command — each Authorizing Official issues their own. The credibility weight is that EdgeRunner is operating under a federal Authorizing Official's IL-6 IATT for the runtime + models, evidencing security architecture and compliance posture rather than blanket cross-command authority.

### Authorization Footprint
- Navy approved-applications list — EdgeRunner is listed (via ICOP)
- IL-2 through IL-6 multi-domain operation supported (per akamai-gcds white paper Section 3.1)
- SECRET / TS spaces supported (per Application Arsenal capabilities brief)
- CAC-enabled access to secure DoD networks
- Cross-domain deployment patterns supported

### Risk Management Framework
- RMF-aligned architecture
- NIST AI RMF flywheel architecture (built and documented for Mystic Depot LOE1)
- Traceable, auditable AI outputs with local data control

### Other Cybersecurity Certifications
- CMMC level: `[TODO: source needed]`
- NIST SP 800-171 / SPRS score: `[TODO: source needed]` (AFRL JADPACT security questionnaire answered using NIST 800-171 framework throughout, but no published score in repo)
- ISO 27001 / SOC 2 / FedRAMP: Not held — do not claim

**Source-of-truth pointer:** `my-company/capabilities.md` Section Secure Deployment & IL Architecture; `my-company/evidence-ledger.json` EV-022 (IL-6 IATT), EV-014 (Navy ICOP); `my-company/past-proposals/jadpact-mash-baa-2026/security-questionnaire.md`.

---

## 5. Core Capabilities & Differentiators

### Products

> These map to the converged **five-layer EdgeRunner stack** (Models → Adapters → Runtime → WarClaw → Ground Truth) executing the **Edge Mission Loop** (Sense/Reason/Act/Verify/Learn) on customer-owned silicon, no cloud in the critical path. See `capabilities.md` for the full stack, the "authority is data, not weights" spine, and per-layer maturity. Label maturity honestly (see the maturity vocabulary in `capabilities.md`).

| Component | Stack layer | Description | Maturity |
|---|---|---|---|
| **EdgeRunner AI Runtime / Inference Runners** | Runtime | Hardware-agnostic, air-gapped, containerized on-device LLM inference for DDIL (Intel/AMD/NVIDIA/Qualcomm/Apple; ONNX/CUDA/Vulkan/Metal); OpenAI-compatible, MOSA-compliant, Bring-Your-Own-Model; extends MAVEN/Advana to the edge | Fielded · active IL-6 IATT |
| **Custom Models (Light / Medium / Heavy)** | Models | Military-specific models on open-weight foundations, sized to the mission's hardware envelope; EdgeRunner Medium is the current product; GPT-5 task parity at the edge (published research); Heavy 120B in development; BYOM (no lock-in) | Fielded · TRL 8 |
| **Automated LoRA & Fine-Tuning Platform** | Adapters | Self-service LoRA creation and fine-tuning at the GCC level without vendor involvement; per-MOS/AFSC adapters delivered in 30–60 days | Proven |
| **WarClaw** | Agentic orchestration | Mission-workflow orchestration — tradecraft codified as versioned, validated, **auditable software** (Tool→Skill→Role→Mission Workflow), human-gated, with a first-class execution record; **orchestration, not autonomy**. Built on the OpenClaw framework; released April 2, 2026; runs 100% on-device (servers/workstations/laptops); native Microsoft Office integrations (PowerPoint/Word/Excel/Teams/Outlook); applies ICD 203 conventions. In the SOCOM JATF concept, orchestrates UxS packs and surfaces only high-value decisions to the operator. | Built · TRL 7 (Army NGC2 demo — demonstration, not a PoR) |
| **OpenClaw (framework)** | — | Open agent framework underlying WarClaw; provides the OpenAI-compatible API surface and integration model. | Framework |
| **Ground Truth** (eng. "Warrant") | Governance | Model-agnostic verification/authorization layer that grounds each AI claim — and, at the action frontier (`/api/check_action`), each agent action — in a human-approved evidence ledger; pass/flag/block gate; portable **signed WBOM receipt**; **attribution, not truth; fail toward caution**; built to ICD 203/206. Not separately accredited; **no TRL — do not assign one.** | Proven / Built |
| **EVELYN** | Machine vision / data labeling | Edge machine vision — live target ID and training-ready dataset labeling from a handful of seeds (**seeded, not trained**); COCO/YOLO/Pascal VOC exports; validated on IR/night/fog; resilient to adversarially poisoned imagery; ~7,800+ labels/hour on an offline laptop. Used by the SDA TAP Lab and U.S. Space Systems Command. | TRL 7 · CDAO Tradewinds Awardable (Jul 2026) |
| **DORIS** | Learning loop | On-device, offline document→dataset→LoRA fine-tune→GGUF export pipeline with a **judge-LLM quality gate**; adapts the *reasoning* model where the mission is (distinct from EVELYN's no-retrain vision lane). | Proof-of-concept |
| **Edge Platform** | Cross-cutting | Connects edge to GCC and enterprise — model delivery, data return, and continuous improvement across all tiers | Fielded |

### Services

| Component | Description |
|---|---|
| **MOS-Specific LoRAs** | Mission-tailored Military Occupational Specialty adapters built at the GCC level |
| **LLM Mid- and Post-Training** | Custom mid-training and post-training for mission-specific use cases at GCC or enterprise level |
| **Mission-Representative Benchmark Development** | Bronze/Silver/Gold dataset tiering, NIST AI RMF-aligned lifecycle, cryptographically signed versioned releases (per Mystic Depot LOE2) |

### Technical Capabilities (summary)

- **On-device AI execution.** Fully air-gapped (zero internet/cloud dependency); cross-OS (Windows, Linux, macOS); hardware-agnostic silicon (Intel, AMD, NVIDIA, Qualcomm, Apple); 8 GB VRAM minimum (Light tier), 16 GB recommended (Medium tier), workstation/edge-server class (Heavy tier); deployable as binary or containerized web-hosted application; OpenAI-compatible API; MOSA-compliant; Bring-Your-Own-Model architecture.
- **Military-specialized models.** EdgeRunner Medium — the current flagship product — demonstrates GPT-5-class task parity at the edge (the published "EdgeRunner 20B" research, 95%+ statistical significance, 1.6M curated military records, is the citation for that parity). MilDeflect eliminates 98%+ commercial-LLM refusal via abliteration (66.5-point answer-rate improvement); LoRA adapters for Combat Arms, Combat Medic, Cyber, Logistics, Acquisitions, with 90-day delivery committed for Special Forces (18-series), PSYOP (37-series), Civil Affairs (38-series). Domain-aware compression to ~3–4 bits/weight retains task accuracy where naive quantization degrades it.
- **Agentic orchestration (WarClaw).** Mission-workflow orchestration as versioned, validated, auditable software (Tool→Skill→Role→Mission Workflow); human approval gates; first-class execution record; on-device, no cloud round-trips. Productizes the older "agentic workflow automation" capability (multi-step local agents; acquisitions/FAR agents; agents for drones/robotics/autonomous systems per ARL JWS).
- **Output governance & verification (Ground Truth).** Deterministic claim-to-approved-authority verification after any model or RAG pipeline; pass/flag/block gate; portable signed WBOM receipt; doctrine-/Section-L-M-as-a-ledger; the emerging action-authorization frontier (`/api/check_action`). Attribution, not truth; fails toward caution.
- **On-device model adaptation (DORIS, PoC).** Offline document→dataset→LoRA→GGUF fine-tuning with a judge-LLM quality gate — the reasoning-model learning loop at the edge.
- **Retrieval-Augmented Generation.** Local PDF/PPT/Word/structured-data ingestion; citation-backed, doctrine-grounded outputs; FAR parsing and large-corpus search. (RAG feeds a model context; Ground Truth audits what the model said — keep the two distinct.)
- **Intelligence processing.** 25+ language translation, transcription, summarization, entity extraction, link analysis, pattern-of-life modeling, COA generation; SIGINT/HUMINT/GEOINT/OSINT/MASINT discipline coverage; image and facial recognition.
- **Battle management & JADC2.** AI Battle Management Teammate aligned to TM-BM framework (13 subfunctions); containerized microservice integration into OSA / RADIS DevSecOps pipelines.
- **Computer vision.** YOLO model development; Vision-Language Models for multi-modal edge AI; onboard UAS deployment (productized as EVELYN — see Products).
- **Neuro-symbolic AI.** ML + Automated Reasoning composition (DARPA CLARA TA1 pursuit).

### Deployment Models
- Government-furnished laptops/workstations (HP and Panasonic Toughbook ruggedized platforms validated)
- Tactical systems (ATAK)
- Edge servers / fly-away kits
- Containerized web-hosted (IL-5/IL-6)
- Distributed edge infrastructure (via Akamai partnership)

### Differentiators (canonical list — aligned to `capabilities.md`)
1. **Fieldable, not just capable** — EdgeRunner ships the whole stack (own it · run it at the edge · govern it · prove it), not a model behind an API
2. Operates when the network doesn't — zero cloud, zero latency penalty; no cloud in the critical path
3. **Authority is data, not weights** — one stack re-points to any unit's SOP, agency's rules, or classification regime by swapping the signed ledger, live, without retraining
4. GPT-5 parity on military tasks at the edge (published research, arXiv)
5. Fits that capability onto constrained hardware — domain-aware compression to ~3–4 bits/weight retains accuracy where naive quantization degrades it
6. **Every AI output is attributable and auditable** — Ground Truth verifies each claim against approved facts and emits a portable signed WBOM receipt (attribution, not truth; human-gated; fail toward caution)
7. **Tradecraft as auditable software** — WarClaw runs versioned, validated skills with a human gate and a first-class execution record; orchestration, not autonomy
8. Purpose-built military AI, not adapted commercial AI; refusal problem solved (MilDeflect)
9. Edge-to-enterprise feedback loop (structured data capture → continuous refinement; EVELYN/DORIS learning loops)
10. Proven in special operations (USASOC, 4th ID, USSF, Navy ICOP)
11. Fastest path to contract (Tradewinds Awardable — runtime and, since Jul 2026, EVELYN — + Tradewinds CSO Direct Award + active IL-6 IATT; IL-5 ATO in progress)
12. Zero marginal inference cost after deployment (no per-token billing, no per-user licensing)

**Source-of-truth pointer:** `my-company/capabilities.md`; `my-company/components-table.md`; `my-company/published-research.md` (technical claims).

---

## 6. Past Performance — Operational Deployments & Active Contracts

*Dollar values and periods of performance intentionally omitted — solid figures not on file. Add per-proposal as needed.*

| Customer | Program | Role | Status | Source / Notes |
|---|---|---|---|---|
| USASOC — 1st SFG | SOF AI Pilot | Vendor (deployment) | Operational | `past-performance.md` Section 1; EV-099, EV-108, EV-059 |
| USASOC — 7th SFG | SOF AI Pilot | Vendor (deployment) | Operational | `past-performance.md` Section 1; EV-099, EV-108, EV-059 |
| USASOC — 10th SFG | SOF AI Pilot | Vendor (deployment) | Operational | `past-performance.md` Section 1; EV-099, EV-108, EV-059 |
| JFK Special Warfare Center & School | SOF Training Integration | Vendor (deployment) | **UNVERIFIED** | **No ledger entry exists.** The former EV-004 cite pointed at a Space Force item after the 2026-07-24 rebuild. Do not cite until a ledger entry is created |
| 4th Infantry Division | NGC2 (Next-Gen C2) | Vendor (deployment) | Deployed | First conventional-force deployment; EV-099. Separate 1st SBCT sustainment work: EV-109 |
| **U.S. Navy — ICOP (NIWC Atlantic / PMW 120)** | **Integrated Common Operating Picture** | **Vendor (program-of-record deployment)** | **Active** | Furthest-along engagement; program of record; TRL 8. On Navy approved-applications list. Full IL-6 ATO expected Oct 2026 at ICOP deployment. *(State the runtime's IL-6 IATT separately — do not attribute the IATT to ICOP in collateral.)* EV-014 + EV-022. |
| **U.S. Space Force** | **TradeWinds CSO Direct Award (transitioned from prior research collab)** | **Prime, production contract** | **Active** | EV-023. Distinct from the Tradewinds Marketplace Awardable status (EV-020). |
| **U.S. Space Systems Command (SSC)** | **EVELYN — edge dataset rapid-generation** | **Vendor** | **Operational** | Per WarClaw/JATF brief Section 5; ledger entry needed. |
| **SDA TAP Lab (Space Development Agency)** | **EVELYN — edge dataset rapid-generation** | **Vendor** | **Operational** | Per WarClaw/JATF brief Section 5; ledger entry needed. |
| DAF / HNI-ES | AFSC-specific AI on government laptops (Acquisitions, Logistics) | Vendor | `[TODO: status]` | `capabilities.md` Section Proof Points |
| SAF/SQ (Maj Gen Purdy) | IL-5 Azure portal — acquisitions AI pilot | Vendor | `[TODO: status]` | `capabilities.md`; JADPACT technical volume |
| JSOC | Pilot — `[TODO: details restricted]` | `[TODO: role]` | Pilot | EV-061 — restricted; cite only in Government-distribution proposals (Distribution B+). |


> **EV-column corrected 2026-08-20.** This table previously cited EV-001 through EV-005 for the
> rows above. Those IDs became U.S. Space Force order items in the 2026-07-24 ledger rebuild and the
> mapping was never re-pointed, so drafts citing them passed `/evidence-check` while pointing at the
> wrong evidence. `my-company/past-performance.md` Section 1 is the maintained narrative for these rows.

### Research Agreements & Collaborations

| Partner | Agreement Type | Status | Source |
|---|---|---|---|
| Air Force Research Laboratory (AFRL) | CRADA | Active | `past-performance.md`; EV-010 |
| Army Research Laboratory (ARL) | Joint Work Statement (JWS) — AI agents for drones/robotics/CV | Active | `past-performance.md`; EV-011 |
| NIWC Atlantic | Research Collaboration (parent relationship for Navy ICOP) | Active | `past-performance.md`; EV-012 |
| U.S. Space Force | Research Collaboration (transitioned to active contract — see EV-023) | Transitioned | `past-performance.md`; EV-013 |

### Recent Submissions (under evaluation)

| Solicitation | Number | Customer | Submitted | Value | Notes |
|---|---|---|---|---|---|
| **AFRL JADPACT II / MASH (Mission-Trained Edge AI for Battle Management Decision Support)** | FA238426SB005 (Call 01) under BAA FA2384-26-S-B004 | AFRL | 2026-03-14 | $98,450 | Demonstration sprint. POC Dave Anderson. `past-proposals/jadpact-mash-baa-2026/` |
| **DIU Mystic Depot CSO (LOE1 + LOE2 — vendor-agnostic AI TEVV infrastructure)** | `[TODO: contract number]` | DIU / ODNI | 2026-03-24 | — | Prime with BigBear.ai + Lockheed Martin. `past-proposals/mystic-depot-cso-2026/` |
| IDX26 SIGINT White Paper | W91RUS26SFTHU | Army | 2026-02 | — | EV-080 |
| **SOCOM JATF — WarClaw + EVELYN (Agentic Decision Dominance)** | `[TODO: solicitation number]` | SOCOM JATF | `[TODO: submission date]` | — | Pairs WarClaw (orchestration) + EVELYN (vision/dataset) for the "Overburdened Operator" problem. Source: `D:\One Drive Excluded Docs\SOCOM Warclaw JATF.docx`. **Should be archived under `my-company/past-proposals/socom-warclaw-jatf-2026/` once submitted.** |

### Product Releases & Public Announcements

| Release | Date | Channel | Source |
|---|---|---|---|
| **EdgeRunner WarClaw — Agentic Decision Dominance at the Tactical Edge** | 2026-04-02 | Press release (Rubenstein PR) | `D:\One Drive Excluded Docs\Press Release_ EdgeRunner Releases "WarClaw"...docx` |

**Source-of-truth pointer:** `my-company/past-performance.md` (table source); `my-company/evidence-ledger.json` (most current — includes Navy ICOP / IL-6 / USSF Tradewinds CSO updates from 2026-05-05 not yet propagated to `past-performance.md`); `my-company/past-proposals/` (full text of recent submissions).

> **Sync gaps to fix in the ledger and human-readable files:**
> - `past-performance.md` does not yet reflect Navy ICOP (EV-014), IL-6 ATO for CMI (EV-022), USSF Tradewinds CSO Direct Award (EV-023), JADPACT/MASH submission, Mystic Depot CSO submission, or the WarClaw release.
> - `evidence-ledger.json` does not yet contain entries for: EVELYN at SDA TAP Lab; EVELYN at U.S. Space Systems Command; WarClaw product (capability + April 2 release); OpenClaw framework; SOCOM JATF customer engagement; NASA SEWP awardable status; the restructured partnership categories in Section 9.

---

## 7. Active Programs (currently in flight)

> WarClaw is a **released product**, not an in-flight program — see Section 5 (Products) and Section 6 (Product Releases). The active programs below are pursuit/submission efforts, not the product roadmap.

| Slug | Opportunity | Status | Notes |
|---|---|---|---|
| `socom-warclaw-jatf` | SOCOM JATF — WarClaw + EVELYN for the "Overburdened Operator" / Collective Autonomy challenge | Brief delivered; pursuit active | Source: `D:\One Drive Excluded Docs\SOCOM Warclaw JATF.docx`. Archive once submission status confirmed. |
| `mystic-depot` | DIU CSO — AI eval harness (LOE1) + benchmark repository (LOE2) | Submitted; under evaluation | Compliance gaps flagged in red team review (ROM pricing, teammate descriptions, LOE2 editing artifacts) |
| `clara` | DARPA CLARA TA1 — neuro-symbolic AI (ML + AR composition) | Active — ~8-page technical section | Teaming partners with AR/logic-programming depth needed |
| `socpac` | SOCPAC PaceSetter — MAVEN extension with open-weight/offline models | Active | Time-sensitive (Bala Selvam departs 2026-07-31) |
| `ITDX26-AI-Analyst` | Army FCC/ICED — AI prototype for 16 MI analytical tasks | Conditional GO; 10-page white paper stage | Gate Phase 2/3 on deadline, funded follow-on, CUI compliance, vendor count |
| `nato-diana-decision-superiority` | NATO DIANA Decision Superiority | In progress | Web-form submission |
| `ae-mmp` | `[TODO: full title]` | In progress | |
| `akamai-gcds` | Akamai Government Content Delivery Service — EdgeRunner artifact distribution + multi-domain (IL-2 through IL-6) hardening | In progress | |
| `application-arsenal` | NIWC-PAC Application Arsenal Enterprise Engineering and Lifecycle Support | In progress | Capability matrix has GAPs flagged: CDS engineering, OSA/ACS pipeline experience |
| `cybercom-j9` | `[TODO: full title]` | In progress | |
| `dod-openweight-whitepaper` | `[TODO: full title]` | In progress | |
| `extic-26-2`, `jadpact-mash-baa-2026`, `ngb-enterprise-data-ai`, `senate-manchurian-models`, `senate-prc-open-source-models` | `[TODO: status — directories present in proposals/ but not in CLAUDE.md active list]` | | |

**Source-of-truth pointer:** `CLAUDE.md` Section Active Proposals; `proposals/` directory; `my-company/past-proposals/` for closed/submitted artifacts.

---

## 8. Research & Publications

### Paper 1 — Measuring and Eliminating Refusals in Military Large Language Models (MilDeflect)
- 30 pages; EdgeRunner AI authorship
- First gold benchmark for assessing military refusal rates, created by US Army and special-forces veterans
- Tested 24 public models + 3 military models
- Hard rejection rates as high as 98.2% on legitimate military queries
- Demonstrated abliteration on military-tuned gpt-oss-20b: 66.5-point answer-rate increase, only 2% average relative decrease on other military tasks
- Source PDF: `my-company/capability-papers/mil-deflect/mil_deflect.pdf`

### Paper 2 — EdgeRunner 20B: Military Task Parity with GPT-5 While Running on the Edge
- 19 pages; EdgeRunner AI authorship
- Fine-tuned from gpt-oss-20b on 1.6M curated military records
- Introduces four military test sets: combat arms, combat medic, cyber operations, mil-bench-5k
- Matches or exceeds GPT-5 on military tasks at 95%+ statistical significance
- No statistically significant regression on general benchmarks (ARC-C, GPQA Diamond, GSM8k, IFEval, MMLU Pro, TruthfulQA) except GSM8k in low-reasoning setting
- Source PDF: `my-company/capability-papers/edgerunner-20b/EdgeRunner_20B.pdf`

### Internal Benchmark Suites (developed in-house)
mil-deflect-bronze, mil-deflect-gold, combat arms, combat medic, cyber ops, mil-bench-5k

### Patents / Other Publications
- `[TODO: source needed]`

**Source-of-truth pointer:** `my-company/published-research.md`; `my-company/capability-papers/`.

---

## 9. Teaming & Partners

Partnerships are categorized below. The first three are stable, named relationships; the fourth (Teaming Partners) is intentionally a **log** rather than a roster — teaming relationships are pursuit-specific, and per-proposal documents (`proposals/<slug>/working/teaming-strategy.md`, etc.) are the authoritative record of any given prime/sub structure.

### 9.1 Resellers
Channel partners who resell EdgeRunner products into federal customers.

| Partner | Notes |
|---|---|
| Carahsoft | Federal channel reseller |
| Panasonic | Reseller (also a ruggedized-laptop platform — Toughbook class) |
| HP | Reseller (also a ruggedized-laptop platform) |
| AMD | Reseller |

### 9.2 Infrastructure Vendors
Companies whose infrastructure EdgeRunner runs on or integrates with.

| Vendor | Notes |
|---|---|
| Armada | Edge infrastructure |
| Akamai | Distributed edge infrastructure for defense workloads |
| AWS | Cloud infrastructure |
| Microsoft (Azure) | Cloud infrastructure (also includes IL-5 Azure portal pilot under SAF/SQ — see Section 6) |

### 9.3 AI Frontier-Model Providers
Frontier model providers whose models EdgeRunner integrates with or hosts on-device.

| Provider | Notes |
|---|---|
| OpenAI | Frontier models |
| Meta | Frontier / open-weight models (Llama family) |
| Google | Frontier models (Gemini, Gemma) |
| xAI | Frontier models (Grok) |
| All NATO-based model providers | Aggregate inclusion (e.g., Mistral and other allied-nation providers) |

### 9.4 Teaming Partners (running log)
Companies EdgeRunner has teamed with on a federal solicitation, in any prime/sub configuration. Listed for **future-pursuit awareness only** — does not imply an active or exclusive teaming agreement. Per-proposal teaming structure is documented in the relevant `proposals/<slug>/` directory.

| Teaming Partner | First-known engagement | Source |
|---|---|---|
| Dynamo AI | Application Arsenal (NIWC-PAC) | `proposals/application-arsenal/inputs/02_yourCompany/edgerunner-capabilities.md` |
| BigBear.ai | DIU Mystic Depot CSO | `my-company/past-proposals/mystic-depot-cso-2026/_index.md` |
| Lockheed Martin | DIU Mystic Depot CSO | `my-company/past-proposals/mystic-depot-cso-2026/_index.md` |
| Armada | `[TODO: first-known engagement]` | — |
| Metronome | `[TODO: first-known engagement]` | — |

*(Append rows here as new teaming relationships are formed — one row per company on first use, regardless of how many subsequent pursuits.)*

### Strategic Technology Partnerships (named in product collateral)
Per the SOCOM WarClaw/JATF brief Section 5: "EdgeRunner is currently funded through Series A ($17.5M) and maintains strategic partnerships with **NVIDIA, Intel, and Defense Unicorns**." NVIDIA and Defense Unicorns do not yet have a clean home in the four categories above:
- **NVIDIA** — silicon partnership (could fit Resellers or a new "Silicon" category alongside AMD); `[TODO: confirm category]`
- **Defense Unicorns** — defense software partner; `[TODO: confirm category — likely Teaming or Infrastructure]`
- **Intel** — already strategic per the JATF brief; `[TODO: confirm whether Reseller or Infrastructure]`

> **Sync gaps to fix:**
> - `my-company/partnerships.md` is referenced as the source file by EV-050–EV-056 in the evidence ledger but **does not exist on disk** as of 2026-05-08. Recommend creating it using the four-category structure above and retiring the old "Commercial OEM" / "Defense Integrator" labels in EV-050–EV-056.
> - Evidence ledger entries EV-050 (HP), EV-051 (Panasonic), and EV-052 (AMD) are typed as `commercial OEM` but per the new categorization they are **Resellers**. Update the ledger.
> - Evidence ledger does not yet contain entries for: Carahsoft, Armada, AWS, Microsoft, OpenAI, Meta, Google, xAI, NVIDIA, Defense Unicorns, Dynamo AI, Metronome.

**Source-of-truth pointer:** This section, plus per-proposal teaming docs at `proposals/<slug>/working/teaming-strategy.md`. The evidence ledger should be re-aligned to this categorization.

---

## 10. Key Personnel

Drawn from author lists on published research, JADPACT POC fields, and security-questionnaire signatories. Roles below are explicit only where the source named them.

| Name | Role (where stated) | Source |
|---|---|---|
| **Tyler Xuan Saltsman** | **Co-Founder & CEO** | WarClaw press release, 2026-04-02 |
| Jack FitzGerald | First author on both papers — research lead implied | `published-research.md` |
| Dave Anderson | POC for AFRL JADPACT/MASH submission (Dave@edgerunnerai.com) | `past-proposals/jadpact-mash-baa-2026/_index.md` |
| Sean Bailey | Head of Prototype Engineering (completed AFRL security questionnaire) | `past-proposals/jadpact-mash-baa-2026/security-questionnaire.md` |
| Aristotelis Lazaridis, Dylan Bates, Aman Sharma, Jonnathan Castillo, Yousif Azami, Jeremy Cao, Peter Damianov, Kevin de Haan, Luke Kerbs, Vincent Lu, Joseph Madigan, Jeremy McLaurin, Jonathan Tainer, Jonathan Beck, Jamie Cuticello, Colton Malkerson, Brian King | Research / engineering staff (paper co-authors) | `published-research.md` |

### Public-Relations POC
- Stephen Francy, Rubenstein PR — sfrancy@rubensteinpr.com — (212) 805-3017 (per WarClaw press release)

### Designated Federal Contracting POC
- `[TODO: source needed]` — different from technical/research POCs above

**Source-of-truth pointer:** `my-company/published-research.md`; `my-company/past-proposals/jadpact-mash-baa-2026/`.

---

## 11. Distribution Statements (federal markings used)

EdgeRunner default markings (full text in `my-company/distribution-statements.md`):
- **Statement A** — Approved for public release; distribution unlimited
- **Statement B** — U.S. Government agencies only
- **Statement C** — Government & contractors
- **Statement D** — DoD & DoD contractors only (recommended default for SOCPAC-type submissions)
- **Statement F** — Directed only
- **CUI // FEDCON** — when document contains proprietary capabilities, pricing, or sensitive but unclassified technical detail

**Source-of-truth pointer:** `my-company/distribution-statements.md`.

---

## 12. Brand & Visual Identity

- Brand palette and design system: `my-company/brand-palette.md`, `my-company/brand-design-system.md`, `my-company/aura-digital-design-scheme.md`
- Master logos (single source of truth): `my-company/branding/`, plus the SVG variants at `my-company/aura-digital-*.svg`
- Reusable graphic templates: `my-company/graphic-templates/`

**Source-of-truth pointer:** files listed above.

---

## 13. Update History

| Date | Change | Source-of-truth |
|---|---|---|
| 2026-07-23 | **Accreditation correction + converged-stack alignment.** Corrected Section 4, the footer bar, the differentiator list, and the Navy ICOP past-performance row from "IL-6 ATO Active" / "IL-5 ATO Active" to the adjudicated posture — **active IL-6 IATT** (runtime + models; full IL-6 ATO expected Oct 2026), **IL-5 ATO in progress** (expected Aug 2026) — and stopped attributing the IL-6 IATT to Navy ICOP per Bill's 2026-07-02 direction. Companion to the same-day rewrite of `capabilities.md` around the converged five-layer stack (models→adapters→runtime→WarClaw→Ground Truth) and the addition of WarClaw, DORIS, refreshed Ground Truth/EVELYN, and evidence entries EV-077/078/079/094/095/096. **Section 5 product prose reconciled to the rewrite** — Products table reframed to the five-layer stack with maturity labels, Ground Truth and DORIS added, EVELYN throughput metric corrected (~7,800 labels/hr laptop, replacing the stale "100+ images/sec"), technical-capabilities summary and differentiators aligned. | `capabilities.md`; `evidence-ledger.json` EV-022 |
| 2026-05-08 (v2) | **Bill clarifications + WarClaw integration.** Added WarClaw (product, released 2026-04-02), OpenClaw (framework), EVELYN deployments at SDA TAP Lab and U.S. Space Systems Command, SOCOM JATF customer engagement. Confirmed IL-6 ATO covers CMI workloads. Resolved business size (Small under NAICS 541511, no socioeconomic certs). Added NASA SEWP as awardable IDIQ. Confirmed no GSA MAS, ISO 27001, SOC 2, or FedRAMP. **Restructured Section 9 partnerships into four categories** (Resellers / Infrastructure Vendors / AI Frontier-Model Providers / Teaming Partners log) per Bill's direction; flagged ledger-restructure follow-ups. Confirmed Tyler Xuan Saltsman as Co-Founder & CEO. Source files: `D:\One Drive Excluded Docs\SOCOM Warclaw JATF.docx`; `D:\One Drive Excluded Docs\Press Release_ EdgeRunner Releases "WarClaw"...docx`. | This file |
| 2026-05-08 (v1) | **Initial consolidated profile.** Captures every EdgeRunner-related fact in the repository, including Navy ICOP / IL-6 ATO / USSF Tradewinds CSO Direct Award additions made to the evidence ledger on 2026-05-05, and recent past-proposal artifacts (JADPACT/MASH, Mystic Depot CSO) submitted in March 2026. | This file (assembled from all `my-company/` sources) |
| 2026-05-05 | Evidence ledger updated with EV-014 (Navy ICOP), EV-022 (IL-6 ATO), EV-023 (USSF TradeWinds CSO Direct Award), EV-050–EV-056 (HP, Panasonic, AMD, Intel, Akamai, Lockheed, BigBear partnerships) | `my-company/evidence-ledger.json` |
| 2026-04-22 | Evidence ledger seeded from existing profile files | `my-company/evidence-ledger.json` |
| 2026-04-22 | `my-company/` directory populated from legacy `Claude Code Projects/proposals/reference/` and `proposals/inputs/02_edgeRunner/` | `my-company/README.md` Section Migration note |

---

## 14. Open TODOs (rolled up from the document)

### Source-file sync work (high-priority — propagate this profile back to the rest of `my-company/`)
- **Propagate** Navy ICOP, IL-6 ATO for CMI, USSF Tradewinds CSO Direct Award, JADPACT/MASH submission, Mystic Depot CSO submission, WarClaw release, EVELYN at SDA TAP Lab, EVELYN at U.S. Space Systems Command, NASA SEWP awardable status, and SOCOM JATF engagement into `past-performance.md`, `capabilities.md`, `contract-vehicles.md`, and `components-table.md`.
- **Create** `my-company/partnerships.md` using the four-category structure in Section 9 (Resellers / Infrastructure Vendors / AI Frontier-Model Providers / Teaming Partners log). The evidence ledger references this file as the source for EV-050–EV-056 but it does not exist on disk.
- **Re-categorize** evidence-ledger entries EV-050 (HP), EV-051 (Panasonic), EV-052 (AMD) from `commercial OEM` to `reseller`. EV-054 (Akamai) re-type from `defense integrator` to `infrastructure vendor`.
- **Add ledger entries** for: Carahsoft (reseller), Armada (infrastructure + teaming log), AWS (infrastructure), Microsoft (infrastructure), OpenAI / Meta / Google / xAI (AI frontier-model providers), NVIDIA (technology partner — category TBD), Defense Unicorns (technology partner — category TBD), Dynamo AI (teaming log — Application Arsenal), Metronome (teaming log), WarClaw (capability), OpenClaw (framework), EVELYN at SDA TAP Lab, EVELYN at U.S. Space Systems Command, SOCOM JATF engagement, NASA SEWP vehicle.
- **Move** the SOCOM JATF brief into `my-company/past-proposals/socom-warclaw-jatf-2026/` with an `_index.md` matching the JADPACT/Mystic-Depot pattern.
- **Move / reference** the WarClaw press release as a `my-company/capability-papers/` entry alongside `mil-deflect/mil_deflect.pdf` and `edgerunner-20b/EdgeRunner_20B.pdf`.

### Categorization questions for Bill
- Where do **NVIDIA**, **Intel**, and **Defense Unicorns** belong in the four-category partnership structure? (Currently flagged as `[TODO: confirm category]` in Section 9.)
- Should the running teaming log in Section 9.4 also include **AFRL**, **ARL**, and other research collaborators, or are those distinct enough to keep in Section 6?

### Federal-profile fields still unfilled (no source in repo)
- Headcount and other office locations
- Secondary NAICS codes (defense IT typically also uses 541512, 541330, 541715)
- CMMC level
- NIST SP 800-171 / SPRS score (JADPACT security questionnaire used the framework, but no published score)
- Designated federal contracting POC (distinct from technical / PR POCs)
- Patents and additional publications beyond the two papers in `published-research.md`
- Earliest-engagement dates for Armada and Metronome teaming entries

---

*End of profile. To regenerate: re-read every file in `my-company/` plus `proposals/<active>/inputs/02_yourCompany/` and any `past-proposals/<id>/_index.md`, then update sections + Update History above.*
