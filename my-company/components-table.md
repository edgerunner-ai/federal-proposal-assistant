# EdgeRunner AI — Components (Products & Services)

> The products below map to the converged EdgeRunner stack — five layers on customer-owned silicon, no cloud in the critical path (see `capabilities.md` for the full stack, maturity labels, and the "authority is data, not weights" spine). Label maturity honestly in proposals: **Fielded/TRL 8** (runtime + models via Navy ICOP), **TRL 7** (WarClaw, EVELYN), **Built/Proven** (Ground Truth), **Proof-of-concept** (DORIS).

## Products
| Component | Stack layer | Description | Maturity |
|-----------|-------------|-------------|----------|
| **EdgeRunner AI Runtime / Inference Runners** | Runtime | Hardware-agnostic, air-gapped, containerized platform for hosting and inferencing open-weight models on edge devices (Intel/AMD/NVIDIA/Qualcomm/Apple; ONNX/CUDA/Vulkan/Metal); OpenAI-compatible, MOSA-compliant, BYOM | Fielded · active IL-6 IATT |
| **Custom Models (Light / Medium / Heavy)** | Models | Military-specific models on open-weight foundations, sized to the mission's hardware; GPT-5 task parity at the edge (published research) | Fielded · TRL 8 |
| **Automated LoRA & Fine-Tuning Platform** | Adapters | Self-service LoRA creation and fine-tuning at the GCC level without vendor involvement; per-MOS/AFSC adapters delivered in 30–60 days | Proven |
| **WarClaw** | Agentic orchestration | On-device mission-workflow orchestration — tradecraft as versioned, validated, auditable software (Tool→Skill→Role→Mission Workflow); human-gated; first-class execution record. Orchestration, not autonomy | Built · TRL 7 (NGC2 demo) |
| **Ground Truth (eng. "Warrant")** | Governance | Model-agnostic verification layer — grounds each AI claim (and, at the frontier, each agent action) in a human-approved evidence ledger; pass/flag/block gate; portable signed WBOM receipt; attribution, not truth | Proven / Built |
| **EVELYN** | Machine vision / data labeling | Edge machine vision — live target ID and training-ready dataset labeling from a handful of seeds (seeded, not trained); COCO/YOLO/Pascal VOC exports | TRL 7 · Tradewinds Awardable (Jul 2026) |
| **DORIS** | Learning loop | On-device, offline document→dataset→LoRA fine-tune→GGUF export pipeline with a judge-LLM quality gate; adapts the reasoning model where the mission is | Proof-of-concept |
| **Edge Platform** | Cross-cutting | Connects edge to GCC and enterprise levels — model delivery, data return, and continuous improvement across all tiers | Fielded |

## Services
| Component | Description |
|-----------|-------------|
| **MOS-Specific LoRAs** | EdgeRunner AI research team builds Military Occupational Specialty-specific LoRA adapters at the GCC level |
| **LLM Mid-Training & Post-Training** | Custom LLM mid-training and post-training for mission-specific use cases at the GCC or enterprise level |

## LoRA Definition (for first use in proposals)
> EdgeRunner's research team builds mission-specific LoRA adapters — lightweight model extensions trained on MOS-level tasks and operational patterns at the GCC level. LoRAs allow rapid specialization of base models for specific roles and missions without full retraining, delivering tailored AI capability at a fraction of the compute and timeline cost.

## Operational Capabilities (for summary graphics)
| Capability | Description |
|------------|-------------|
| Operational Now | Mission-ready AI already implemented and operational with real SOF users |
| No New Infrastructure | Runs on existing systems; integrates with current platforms |
| DDIL Ready | Operates fully disconnected with no network required |
| Scalable | Single devices, enterprise environments, or cloud-hosted with web access |
| Measurable Impact | Improves speed, reduces workload, accelerates adaptation |
| Non-Disruptive | Complements Enterprise Frontier AI rather than replacing it |
| Cost-Efficient | No token-based or external API dependencies |
