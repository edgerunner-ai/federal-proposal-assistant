# EdgeRunner AI — Published Research

## Paper 1: MilDeflect — Measuring and Eliminating Refusals in Military LLMs

**Full Title:** Measuring and Eliminating Refusals in Military Large Language Models
**Authors:** Jack FitzGerald, Dylan Bates, Aristotelis Lazaridis, Aman Sharma, Vincent Lu, Brian King, Yousif Azami, Sean Bailey, Jeremy Cao, Peter Damianov, Kevin de Haan, Joseph Madigan, Jeremy McLaurin, Luke Kerbs, Jonathan Tainer, Dave Anderson, Jonathan Beck, Jamie Cuticello, Colton Malkerson, Tyler Saltsman
**Affiliation:** EdgeRunner AI
**Pages:** 30
**Source file:** my-company/capability-papers/mil-deflect/mil_deflect.pdf

### Key Findings
- Commercial LLMs refuse up to 98.2% of legitimate military queries due to safety behaviors that misclassify military-domain content as harmful
- Developed the first gold benchmark for assessing military refusal rates, created by US Army and special forces veterans
- Tested 24 public models and 3 military models for refusal and deflection rates
- Soft deflection rates ranged from 0% to 21.3% across models
- Demonstrated abliteration technique on military-tuned gpt-oss-20b, achieving a 66.5 percentage point increase in answer rate with only 2% average relative decrease on other military tasks
- Argues for deeper specialization through mid-training and end-to-end post-training to achieve zero refusals and maximum military task accuracy

### Proposal Relevance
- **Proves the problem:** Commercial AI models are fundamentally unsuitable for military use without specialization — they refuse the exact queries warfighters need answered
- **Demonstrates EdgeRunner's research depth:** First-of-its-kind benchmark development, rigorous evaluation methodology
- **Supports the LoRA/fine-tuning value proposition:** Shows that model specialization dramatically improves military utility
- **Credibility marker:** Published research with reproducible methodology (arXiv preprints; not yet peer-reviewed)

### Quotable Claims for Proposals
- "Military LLMs must provide accurate information to the warfighter in time-critical and dangerous situations"
- EdgeRunner developed "the first dataset of its kind" for assessing military LLM refusal rates
- Hard rejection rates as high as 98.2% on legitimate military queries
- Abliteration achieved 66.5 point increase in answer rate with minimal performance regression

---

## Paper 2: EdgeRunner 20B — Military Task Parity with GPT-5 on the Edge

**Full Title:** EdgeRunner 20B: Military Task Parity with GPT-5 While Running on the Edge
**Authors:** Jack FitzGerald*, Aristotelis Lazaridis*, Dylan Bates*, Aman Sharma*, Jonnathan Castillo, Yousif Azami, Sean Bailey, Jeremy Cao, Peter Damianov, Kevin de Haan, Luke Kerbs, Vincent Lu, Joseph Madigan, Jeremy McLaurin, Jonathan Tainer, Dave Anderson, Jonathan Beck, Jamie Cuticello, Colton Malkerson, Tyler Saltsman
**Affiliation:** EdgeRunner AI
**Pages:** 19
**Source file:** my-company/capability-papers/edgerunner-20b/EdgeRunner_20B.pdf

### Key Findings
- EdgeRunner 20B is a fine-tuned version of gpt-oss-20b optimized for military tasks
- Trained on 1.6M high-quality records curated from military documentation and websites
- Introduces four new military test sets: combat arms, combat medic, cyber operations, and mil-bench-5k (general military knowledge)
- **Matches or exceeds GPT-5 task performance** with 95%+ statistical significance on military test sets
- No statistically significant regression on general-purpose benchmarks (ARC-C, GPQA Diamond, GSM8k, IFEval, MMLU Pro, TruthfulQA) — except GSM8k in low reasoning setting
- Demonstrates that small, locally-hosted models are ideal for data-sensitive military operations on air-gapped edge devices

### Proposal Relevance
- **GPT-5 parity claim is the headline:** A 20B parameter model running on-device matches the world's most capable cloud model on military tasks — this is the core EdgeRunner value proposition
- **Proves edge viability:** You don't need cloud-scale compute for military-grade AI performance
- **Training data methodology:** 1.6M curated records from military documentation shows systematic approach to domain specialization
- **Benchmark development:** Four new military-specific test sets demonstrate eval capability — supports the "mission-representative evaluation" service offering
- **No regression on general tasks:** Specialization doesn't break general capability — the model remains useful beyond its fine-tuned domain

### Quotable Claims for Proposals
- "EdgeRunner 20B matches or exceeds GPT-5 task performance with 95%+ statistical significance" on military test sets
- Trained on "1.6M high-quality records curated from military documentation and websites"
- "Small, locally-hosted models are ideal solutions for data-sensitive operations such as in the military domain"
- "Allowing for deployment in air-gapped edge devices" — directly supports DDIL positioning

---

## Paper 3: EdgeRunner Compression — Holistic On-Device Model Optimization

**Full Title:** EdgeRunner Compression: A Holistic Optimization Strategy for Delivering SOTA AI On-Device
**Author:** Vincent Lu (CTO), EdgeRunner AI
**Affiliation:** EdgeRunner AI
**Source file:** my-company/capability-papers/compression/EdgeRunner_Compression.docx
**Publication type:** Company technical publication (CTO-authored) describing a proprietary EdgeRunner technique. Cite with the same confidence as Papers 1 and 2. References, but is distinct from, the EdgeRunner 20B arXiv paper.

### Key Findings (EdgeRunner-reported)
- Production models compressed to **~3-4 bits per weight** on average (8-10x reduction) while retaining task accuracy; 3-5 bit models pushed close to 8-bit / higher-precision quality
- **20-30% lower KL-Divergence (KLD)**, measured to generalize across out-of-distribution data
- **50-90% error reduction** in short- and long-form evaluations, strongest when tuned MOS-specific
- **~50% error reduction in embedding models** (cosine error halved on embeddinggemma-300m vs a 5.8-bpw baseline)
- **Quantization-aware LoRAs roughly double** the KLD reduction (~2x) at the same adapter size
- "Efficiency Functions" model how quantization error propagates through a fully-quantized model for a *specific domain*, enabling automatic per-tensor candidate selection and auto-tuning to a target VRAM footprint (e.g., 4GB) and hardware platform (AMD/Nvidia)
- MOS-specific post-training tuning on 800GB-2TB of proprietary conversational data; pipeline runtime <3h for Medium (24B), <1h for Light (4B)
- Generalizes across dense, MoE, state-space, and convolutional architectures, plus LoRA adapters and embedding models

### Proposal Relevance
- **Closes the edge-vs-cloud capability gap on constrained hardware:** the mechanism that lets EdgeRunner fit Medium (24B) / Light (4B) models onto commodity GFE and forward edge devices without sacrificing task accuracy
- **Differentiator vs. naive quantization:** competitors who quantize off-the-shelf models uniformly measurably degrade accuracy and small-model schema/tool-call reliability — EdgeRunner's domain-aware, per-tensor compression does not (ghosting point, see EV-092)
- **Stability for agentic use:** reducing quantization error preserves schema-following, giving confidence that edge behavior matches cluster-trained/-evaluated behavior
- **Reinforces the LoRA/MOS specialization story:** quantization-aware LoRAs and MOS-specific tuning compound the accuracy gains

### Quotable Claims for Proposals (attribute as EdgeRunner-reported)
- EdgeRunner Compression delivers "20-30% less Kullback-Leibler Divergence (KLD), measured to generalize across out-of-distribution data"
- "Achieves 50-90% error reduction in both short and long-form evaluations, especially when tuned to be Military Occupation Speciality (MOS)-specific"
- Production models run at "3-4 bits per weight on average, an 8-10x reduction" while retaining task accuracy
- Engineers "set a target model size in bytes, with consideration for the target hardware platform (AMD, Nvidia, etc.), and it produces optimal models given a mix of constraints"

> **Citation discipline:** Cite with the same confidence as Papers 1 and 2 — this is EdgeRunner's published description of a proprietary compression technique. Attribute the numeric figures to EdgeRunner Compression (EdgeRunner-measured). Ledger refs: **EV-032** (published methodology), **EV-048** (compression capability claim), **EV-092** (ghost vs. naive quantization).

---

## How to Use These Papers in Proposals

### As Credibility Evidence
Reference these papers when claiming:
- EdgeRunner has deep military AI research expertise
- The team publishes research (two published arXiv papers plus a CTO-authored technical publication) with reproducible methodology
- Military model specialization is a proven, measurable capability

### As Technical Differentiators
- **MilDeflect:** proves the refusal problem exists and EdgeRunner solves it
- **EdgeRunner 20B:** proves edge models can match cloud models on military tasks
- **EdgeRunner Compression:** proves EdgeRunner can fit that capability onto constrained edge hardware (3-4 bits/weight) without losing task accuracy — and that naive quantization can't

### As Eval/Benchmark Capability
Both papers demonstrate EdgeRunner's ability to create mission-representative benchmarks — a service offering for customers who need to evaluate AI models against their specific requirements.

### Suggested Placement
- Executive summary: one sentence referencing GPT-5 parity
- Technical approach: reference training methodology and benchmark development
- Differentiators: full paragraph on published research as evidence of capability depth
- Past performance: list as published research alongside operational deployments
