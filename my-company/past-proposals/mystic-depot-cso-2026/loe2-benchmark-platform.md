# LOE2: Vendor-Agnostic Framework for Mission-Specific AI Evaluation
**Team EdgeRunner AI** — EdgeRunner AI, Inc. + BigBear.ai + Lockheed Martin
**Submitted:** March 24, 2026 | **AOI:** LOE 2: Benchmark Development and Methodology
**CAGE:** 9Z176 | **UEI:** SLZTJUA8DBD3

---

## 1.0 Executive Summary

The Department of War (DoW) and Intelligence Community (IC) lack a defensible, government-owned standard for evaluating AI systems in mission contexts. Existing benchmarks are static, vendor-controlled, and increasingly unreliable due to dataset saturation.

Team EdgeRunner AI — EdgeRunner AI, BigBear.ai, and Lockheed Martin — proposes a Vendor-Agnostic Benchmark Development and Methodology Platform that establishes a government-owned evaluation protocol layer — defining how AI systems are measured, validated, and compared across mission environments.

This solution enables the DoW and IC to:

- Define mission-specific evaluation criteria aligned to real operational workflows
- Generate reproducible, versioned benchmark datasets
- Execute evaluations consistently across environments
- Maintain independence from vendors and models
- Continuously evolve benchmarks as models and mission needs change

The platform delivers a government-owned evaluation system that transforms benchmarking from static datasets into a governed, continuously evolving capability.

Phase I delivers a fully functional benchmark development pipeline and evaluation protocol within 180 days, demonstrating mission-specific benchmark generation, reproducibility, and cross-environment execution.

This solution defines the evaluation standard that AI systems must meet, enabling consistent comparison, procurement decisions, and operational trust across DoW programs.

---

## 2.0 Technology Concept

### 2.1 Overview

The DoW requires a repeatable, government-owned method to define what constitutes effective AI performance in mission contexts. Current approaches measure general capability rather than mission-specific performance, are susceptible to dataset saturation and gaming, and lack consistency across environments and programs.

Team EdgeRunner AI delivers a Benchmark Development Platform and Evaluation Protocol Layer that enables the government to define, generate, validate, and maintain mission-specific benchmarks independent of any vendor, model, or execution system.

### 2.2 Architecture & Evaluation Control Framework

The architecture separates benchmark definition from execution while maintaining a unified evaluation standard across environments.

#### 2.2.1 Benchmark Development Pipeline (LOE2 Core)

The Benchmark Development Pipeline implements a NIST AI RMF-aligned lifecycle that enables the government to create and sustain mission-specific benchmarks as versioned, governed assets.

Benchmarks are derived from mission workflows through mission-informed scenario design and SME input, ensuring evaluation reflects real operational tasks. Data is generated and curated using a tiered approach (Bronze, Silver, Gold) that balances scale and fidelity, combining synthetic generation, SME validation, and adversarial augmentation to prevent dataset saturation and gaming.

A key differentiator is a production-proven Bronze dataset workflow refined through operational use at EdgeRunner. This workflow transforms raw source data into structured benchmark artifacts through:
- Document ingestion and tokenization (including OCR)
- Subdivision into semantically coherent sections
- Multi-level summarization to capture both local and global context
- Benchmark example generation: question–answer pairs, reasoning tasks, and agentic workflows aligned to mission objectives

Automated quality control and testing evaluate dataset consistency, difficulty, and coverage, while integrated feedback identifies strengths and gaps in each benchmark iteration. This feedback loop informs subsequent dataset generation, enabling continuous refinement of benchmark fidelity and alignment with evolving mission requirements.

All benchmark artifacts are semantically versioned, cryptographically signed, and validated through statistical testing, bias analysis, and SME review. Validated benchmarks are published as secure, versioned packages accessible via API and deployable across unclassified, classified, and air-gapped environments.

#### 2.2.2 Evaluation Protocol Layer (Control Plane)

The Evaluation Protocol Layer defines how benchmarks are executed, scored, and interpreted. It standardizes task structure, scoring logic, and result aggregation, ensuring consistent evaluation across models, vendors, and environments.

This layer is decoupled from both benchmark content and execution infrastructure, enabling portability and long-term stability while preventing inconsistencies in evaluation methodology. It establishes a consistent evaluation standard that can be applied across any execution environment or system. This layer acts as the authoritative control point for evaluation, ensuring that all systems are measured against a consistent standard regardless of where or how they are executed.

#### 2.2.3 Execution Interface (Integration Layer)

The LOE2 platform delivers benchmark packages and evaluation protocols through standardized interfaces that can be consumed by any evaluation system, including government-developed or third-party execution environments.

Benchmarks are delivered via API and executed using the defined protocol, ensuring consistent scoring and reproducibility regardless of the underlying system. This allows benchmark development and evaluation standards to evolve independently of execution infrastructure.

#### 2.2.4 Operationalization & Validation (Trust Layer)

Team EdgeRunner AI provides full lifecycle evaluation capability:

- **EdgeRunner AI** defines benchmark methodology and evaluation protocol
- **BigBear.ai** contributes operational scenarios and human-AI teaming environments grounded in real mission workflows
- **Lockheed Martin** provides test, evaluation, verification, and validation (TEVV), adversarial testing, and continuous monitoring to validate performance and detect drift over time

Together, these capabilities ensure benchmarks are operationally relevant, technically valid, and defensible for decision-making.

#### 2.2.5 Benchmark API & Delivery

Benchmark artifacts are distributed as standardized, versioned packages via a secure API that governs publication, discovery, and access. Each release includes structured metadata describing provenance, scope, and intended use, ensuring reproducibility and traceability.

Packaging supports deployment across unclassified, classified, and air-gapped environments while preserving data integrity and access control. This layer provides centralized governance of benchmark assets, ensuring consistency and control independent of where evaluation is executed.

### 2.3 Key Differentiators

**Government-Owned Evaluation Standard** — The Evaluation Protocol Layer defines how benchmarks are executed, scored, and compared, ensuring consistent, defensible evaluation independent of vendors or models.

**Mission-Driven Benchmarking** — Benchmarks are derived from real operational workflows, enabling evaluation of human-AI teaming and agentic behavior in mission-relevant contexts.

**Continuous Benchmark Evolution** — Versioning, adversarial augmentation, and SME feedback ensure benchmarks remain resistant to gaming and relevant as models evolve.

**Integrated TEVV and Validation** — Lockheed Martin provides formal validation, adversarial testing, and continuous monitoring to ensure benchmarks are statistically valid and operationally defensible.

**Operational Scenario Realism** — BigBear.ai contributes mission-tested scenarios and human-AI environments derived from real DoW and IC deployments.

**Cross-Environment, Vendor-Agnostic Execution** — Benchmarks execute consistently across cloud, edge, air-gapped, and classified (IL4/5/6) systems without dependency on any specific execution platform.

### 2.4 Phase I Prototype Approach

Phase I prioritizes integration over invention, leveraging existing, field-proven capabilities from Team EdgeRunner AI to rapidly deliver a functional benchmark development and evaluation system.

Within the initial 90 days, the team will stand up a working benchmark development pipeline and deliver initial mission-specific benchmark sets (Bronze, Silver, Gold). These benchmarks will be exposed through API and executed across multiple models to demonstrate consistent evaluation.

By 180 days, the prototype will demonstrate full operational capability, including consistent scoring across models and repeatable evaluation within a defined deployment environment. The system will support human-AI teaming and agentic evaluation workflows, leveraging BigBear.ai's operational scenarios and Lockheed Martin's validation capabilities.

The prototype will operate in an unclassified environment while ensuring compatibility with classified and air-gapped deployment. Documentation and training materials will enable government personnel to independently develop and maintain benchmarks.

This approach minimizes risk by leveraging existing capabilities while delivering a scalable foundation for follow-on production.

### 2.5 Deliverables & Success Criteria

**Deliverables:**
- Benchmark Development Pipeline for generating, validating, and versioning mission-specific benchmarks
- Versioned benchmark repository with Bronze, Silver, and Gold datasets
- Benchmark API and protocol interface
- End-to-end execution across multiple AI models
- Training materials and methodology guide for government use

All deliverables are deployable in unclassified environments and designed for classified and air-gapped transition.

**Success Criteria:**
- Reproducible results across runs and environments
- Clear performance differentiation across models
- Consistent evaluation independent of model or vendor
- Benchmarks aligned to real mission workflows
- Successful execution across multiple environments
- Government ability to create and maintain benchmarks without vendor dependency

---

## 3.0 Company Viability

### 3.1 Company Overview and Traction

Founded in 2024, EdgeRunner AI delivers mission-tailored AI for air-gapped, classified, and disconnected/DDIL environments. The company is actively supporting USASOC, Air Force Research Laboratory (AFRL), U.S. Army 4th Infantry Division / U.S. Army Artificial Intelligence Integration Center (AI2C), Army Research Laboratory (ARL), U.S. Space Force, and NIWC Atlantic, demonstrating operational relevance. EdgeRunner AI has raised $17.5M and projects $5M in 2026 operating income, providing a strong foundation for scaling deployment.

### 3.2 Evaluation Expertise

Team EdgeRunner AI combines complementary capabilities across benchmark development, operational evaluation, and formal validation:

- **EdgeRunner AI:** Leads benchmark methodology, evaluation protocol design, and model evaluation, with experience developing mission-specific and agentic benchmarks aligned to multiple operational Military and National Security use cases
- **BigBear.ai:** Provides operational scenario design, mission decomposition, and human-AI teaming environments based on deployments across Joint, Army, and IC programs
- **Lockheed Martin:** Delivers AI TEVV, including adversarial testing, continuous monitoring, and performance validation frameworks used in mission-critical systems

This combination enables the team to define, execute, and validate AI evaluation in a manner that is both operationally relevant and technically defensible.

### 3.3 Secure Deployment Capability

The team has deployed AI systems across unclassified, classified (IL5/IL6), air-gapped, and DDIL environments. EdgeRunner AI focuses on edge and disconnected execution, while BigBear.ai and Lockheed Martin bring proven capability in enterprise and classified deployments, ensuring the solution can scale across environments without architectural changes.

### 3.4 Human-in-the-Loop & Agentic Evaluation

The proposed solution supports evaluation of both human-AI teaming and fully agentic workflows. BigBear.ai contributes operational experience in human-AI interaction and mission workflows, while EdgeRunner provides agentic evaluation frameworks and benchmark design. Lockheed Martin enhances this with validation methodologies and monitoring to ensure safe and reliable operation in mission contexts.

### 3.5 Transition Strategy

The solution builds on existing, field-tested capabilities and is designed for rapid transition into operational environments.

Because the architecture separates benchmark development (LOE2) from execution (LOE1) while maintaining a unified protocol, the system can be adopted across multiple programs without requiring redesign or vendor lock-in.

Following Phase I, the solution can scale through:
- Expansion of benchmark libraries across mission areas
- Deployment into classified and operational environments
- Integration with additional evaluation and decision-support systems

This positions the solution for follow-on production and broad adoption across the DoW enterprise.
