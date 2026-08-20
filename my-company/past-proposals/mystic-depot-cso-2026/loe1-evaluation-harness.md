# LOE1: Vendor-Agnostic AI Evaluation Harness for Mission Environments
**Team EdgeRunner AI** — EdgeRunner AI, Inc. + BigBear.ai + Lockheed Martin
**Submitted:** March 24, 2026 | **AOI:** LOE 1: Evaluation Harness
**CAGE:** 9Z176 | **UEI:** SLZTJUA8DBD3

---

## 1.0 Executive Summary

The Department of War (DoW) is rapidly adopting AI systems that function as multi-step, tool-using agents operating in mission environments. However, current evaluation approaches remain fragmented, non-reproducible, and tightly coupled to specific vendors and environments — limiting the DoW's ability to make fast, risk-informed decisions about mission readiness. There is no consistent, government-controlled capability to evaluate models and agent workflows, compare performance, or generate auditable results across environments at scale.

Team EdgeRunner AI — EdgeRunner AI, BigBear.ai, and Lockheed Martin — proposes a vendor-agnostic AI Evaluation Harness that establishes a standardized, government-owned capability for executing and managing AI evaluations across mission systems. This approach shifts AI evaluation from tool-driven execution to a standardized, protocol-governed system, enabling consistent, decision-ready results across all environments.

Key features include:

- **Protocol-Governed Evaluation:** Enforces standardized execution and scoring across models and tools
- **Cross-Environment Consistency:** Runs identical evaluations across cloud, classified, and DDIL environments
- **Agentic Workflow Evaluation:** Assesses multi-step workflows, tool use, and decision-making
- **Vendor-Agnostic, Government-Owned Architecture:** Separates external benchmarks (LOE2) from standardized execution (LOE1)
- **Auditable Results:** Captures full execution traces for reproducible, defensible evaluation

The team integrates complementary capabilities: EdgeRunner AI provides the evaluation harness and secure runtime; BigBear.ai enables agentic workflow execution and human-in-the-loop assessment; and Lockheed Martin contributes deep experience in adversarial testing, evaluation frameworks, and audit/provenance aligned to DoW evaluation best practices.

---

## 2.0 Technology Concept

### 2.1 Overview and Problem Framing

Current evaluation approaches do not adequately assess multi-step, tool-using agents operating in mission conditions, particularly within classified and disconnected (DDIL) environments. Existing methods are typically tied to specific tools or infrastructure and lack the ability to evaluate end-to-end workflows under realistic operational constraints.

The Evaluation Harness builds on EdgeRunner's TRL7+ secure runtime, enabling consistent execution and evaluation of AI models across cloud, classified, and DDIL environments. It supports commercial APIs, government-hosted, and locally deployed models through a unified Evaluation Protocol Layer that governs configuration, tool access, agent behavior, logging, and scoring.

### 2.2 Architecture and Technical Approach

The Evaluation Harness operates as a control plane that decouples evaluation logic from models, tools, and infrastructure, providing the government flexibility in choice of evaluation tools, models, and infrastructure. It separates evaluation definition, execution, and scoring into modular layers. At its core, the system consists of:

**Evaluation Protocol Layer:** Governs model configuration, tool access, agent behavior, and scoring. This ensures evaluations are executed consistently across runs, prevents benchmark contamination, and enables direct comparison between models and systems.

**Model Abstraction Layer:** Decouples evaluation logic from model implementation, enabling seamless integration of commercial APIs, government-hosted models, and local/edge-deployed models.

**Execution Environment Layer:** Runs evaluations identically across cloud (IL4/5/6), air-gapped, classified, and DDIL environments, ensuring results reflect real-world operational conditions.

**Benchmark Repository Integration Interface:** Integrates government-owned, versioned benchmark content while maintaining strict separation.

A benchmark scenario defined in an external benchmark repository is ingested by the Evaluation Harness and executed under a protocol-governed model. The protocol layer controls how the model interacts with tools, executes tasks, and is scored, while capturing all intermediate steps and outputs. The result is a structured evaluation record that is directly comparable across models and environments. Benchmark content remains externally managed and versioned, ensuring that evaluation execution remains independent of benchmark development.

### 2.3 Key Technical Differentiators

**Protocol-Centric Control Plane:** Evaluation behavior is governed by a unified protocol layer, separating execution logic from models, tools, and infrastructure to ensure consistency and prevent benchmark contamination.

**Decoupled Benchmark and Execution Model:** External, versioned benchmark content is executed independently of the harness, preserving government ownership and enabling flexible evaluation at scale.

**Environment-Agnostic Execution:** Identical evaluation logic is applied across cloud, classified, and DDIL environments without modification, ensuring operationally relevant results.

**Framework-Orchestrated, Not Framework-Dependent:** Evaluation frameworks (e.g., HELM, Inspect, Garak) operate under harness control, enabling consistent configuration, logging, and scoring across tools.

**Full Execution Traceability:** All evaluation steps — including intermediate actions and tool interactions — are captured as structured records to support audit, analysis, and reproducibility.

### 2.4 Phase I Prototype Approach

Phase I delivers a functional Evaluation Harness through integration and demonstration of existing, fielded capabilities, reducing technical risk and enabling rapid deployment.

The effort begins with deployment of the harness within EdgeRunner AI's secure runtime, establishing a unified control plane with protocol control, model abstraction, and execution layers. The system then integrates representative models and government-relevant benchmark scenarios via any external Benchmark Repository.

The Evaluation Protocol Layer governs execution by defining model configuration, tool access, agent behavior, constraints, logging, and scoring. Models and agents execute under these controlled conditions across cloud, classified, and DDIL environments.

BigBear.ai enables agentic workflow execution and human-in-the-loop assessment, leveraging operational deployments (e.g., Ask Sage) to evaluate multi-step task performance, tool use, and decision-making. Lockheed Martin contributes adversarial testing, robustness assessment, and continuous monitoring, supported by mature evaluation frameworks (e.g., Scouter, ASTERisk, OMEGA) used in operational environments.

Evaluations leverage established frameworks (e.g., HELM, Inspect Evals, Garak) under protocol-governed execution. The harness — not the frameworks — controls execution and captures complete records, including inputs, intermediate steps, tool interactions, outputs, and scoring artifacts, producing structured, comparable results.

By the end of Phase I, the government receives an operational Evaluation Harness capable of executing standardized, reproducible evaluations across models and environments, with auditable outputs and a demonstrated end-to-end evaluation producing consistent results across heterogeneous systems.

### 2.5 Deliverables and Success Criteria

**Deliverables:**
- Containerized modular Evaluation Harness with protocol control and model abstraction
- Configured evaluation workflows for agentic and multi-model execution
- Structured outputs including scoring, logs, and audit artifacts
- Demonstration of cross-environment execution
- Access controls protecting sensitive data according to classification requirements

**Success will be demonstrated by:**
- Evaluation of multiple models without reconfiguration
- Reproducible and comparable results across runs
- Execution of agentic workflows and human-in-the-loop evaluation
- Capability demonstrated across cloud, classified, and DDIL environments

At the conclusion of Phase I, the government will observe a complete evaluation run executed across multiple models and environments, with identical protocols producing directly comparable, auditable results.

---

## 3.0 Company Viability

### 3.1 Company Overview and Traction

Founded in 2024, EdgeRunner AI delivers mission-tailored AI for air-gapped, classified, and disconnected/DDIL environments. The company is actively supporting USASOC, Air Force Research Laboratory (AFRL), U.S. Army 4th Infantry Division / U.S. Army Artificial Intelligence Integration Center (AI2C), Army Research Laboratory (ARL), U.S. Space Force, and NIWC Atlantic, demonstrating operational relevance. EdgeRunner AI has raised $17.5M and projects $5M in 2026 operating income, providing a strong foundation for scaling deployment.

### 3.2 Technical Expertise in AI Evaluation and Benchmarking

The team brings demonstrated expertise across AI evaluation, benchmarking, and robustness testing, including ongoing engagement with NIST and the Center for AI Standards and Innovation:

- **EdgeRunner AI:** Protocol-driven evaluation, model performance assessment, and mission-aligned benchmarking, including on-device and edge model evaluation
- **BigBear.ai:** Large-scale AI deployment and orchestration, including multi-model integration and agentic workflows in operational DoW environments (e.g., Ask Sage)
- **Lockheed Martin:** End-to-end AI TEVV and assurance, including benchmark execution, adversarial testing, continuous monitoring, and automated evaluation pipelines (e.g., Scouter, ASTERisk, OMEGA)

### 3.3 Secure Deployment and Operational Experience

Our team has extensive experience deploying AI systems across IL5/IL6, JWICS, and DDIL environments, combining enterprise-scale platforms (BigBear.ai, Lockheed Martin) with EdgeRunner's edge-optimized runtime.

### 3.4 Human-in-the-Loop and Agentic Evaluation

The team provides integrated capabilities for evaluating agentic systems and human-AI teaming:

- **BigBear.ai:** Human-in-the-loop workflows and operational feedback integration across deployed systems
- **Lockheed Martin:** Structured evaluation, audit trails, and performance measurement for agent behavior and system outputs
- **EdgeRunner AI:** Protocol-driven evaluation of multi-step agent workflows and mission-level performance within the evaluation harness

### 3.5 Commercialization and Transition

EdgeRunner AI operates a commercial-first deployment model, delivering software capabilities directly to mission users and integrating with primes and platform providers. The Evaluation Harness aligns with existing demand for vendor-agnostic, secure AI evaluation and will transition through:

- Current operational users (e.g., USASOC, NIWC Atlantic)
- Integration with prime contractor ecosystems
- Expansion into broader DoW, IC, and national security programs

This capability builds directly on deployments already in use with operational units, enabling immediate transition into existing mission environments without additional development. As a Nontraditional Defense Contractor, EdgeRunner AI will perform a substantial portion of the work, ensuring compliance with OTA requirements while maintaining commercial speed and flexibility.
