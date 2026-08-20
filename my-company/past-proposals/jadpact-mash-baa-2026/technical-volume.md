# Vol 1. Technical Proposal — JADPACT II MASH
**FA238426SB005 (Call 01) | EdgeRunner AI, Inc.**
**Title:** Mission-Trained Edge AI for Battle Management Decision Support
**Date:** 14 March 2026 | **POC:** Dave Anderson | Dave@edgerunnerai.com

---

## Technical Approach

### Nature and Scope of Research

The Department of the Air Force (DAF) is pursuing Joint All-Domain Command and Control (JADC2) capabilities that enable commanders and battle managers to maintain decision advantage in contested, dynamic, and data-rich operational environments. EdgeRunner AI proposes a Battle Management AI Teammate designed to augment Air Force battle managers during operational planning and execution. The proposed solution interprets operational information, assists in generating and sequencing Courses of Action (COAs), highlights operational dependencies, and evaluates operational outcomes.

The capability will be delivered as a containerized microservice integrated into the government-provided digital assistant environment during the Multi-Decision Advantage Sprint (MASH) event conducted under the JADPACT II program.

EdgeRunner's approach is built on three core innovations:
1. **Mission-trained operational AI models** optimized for military decision support tasks based on curated defense datasets
2. **Secure runtime environment** capable of operating within government infrastructure
3. **Battle management reasoning workflows** aligned with the Transformational Model–Battle Management (TM-BM) framework

These capabilities enable AI-assisted decision support while preserving full human authority over operational decisions.

### Technical Program Summary

EdgeRunner AI introduces an AI Battle Management Teammate that augments battle managers throughout the battle management decision cycle. The EdgeRunner system functions as an intelligent assistant containing an agentic framework that unifies diverse input data, continuously interpreting operational context and providing decision support across multiple battle management functions.

The system ingests operational data streams — including mission plans, operational orders, intelligence updates, and simulation environment outputs. Using mission-trained AI models, the system synthesizes this information to maintain an evolving representation of the operational environment.

Based on this understanding of mission context and operational conditions, the system assists battle managers in developing and evaluating candidate COAs — particularly by its ability to search operational domains and discern operational significance by highlighting events or entities that may affect mission execution. The system can propose operational options, identify dependencies across operational tasks, highlight potential coordination requirements between operational elements, and evaluate the potential impacts of alternative actions.

The system is designed to preserve human decision authority. AI recommendations are presented with transparent reasoning and supporting information, allowing battle managers to evaluate the system's suggestions and incorporate them into their decision-making process.

### Unique Technical Innovations

- **Mission-trained operational models** optimized for military decision support tasks based on curated defense datasets
- **Secure AI runtime for operational environments** allowing our capabilities to operate directly within government networks and computing environments, eliminating reliance on external cloud services or token-based AI platforms
- **Battle management reasoning workflows** specifically structured around the TM-BM framework

### Technology Features

EdgeRunner implements its Battle Management AI capability as a modular, containerized microservice architecture designed to integrate with the government-provided digital assistant environment used during the MASH event. The system operates within a containerized environment provided by the government and exposes a stable API that allows the government-owned digital assistant orchestrator to interact with the system.

The EdgeRunner architecture consists of four functional components:

1. **Data Ingestion Layer** — Processes incoming operational data streams from the simulation environment. These streams may include mission plans, operational updates, intelligence reports, and sensor information. The ingestion layer converts these inputs into structured representations that can be processed by the AI models.

2. **Mission AI Model Layer** — Contains the core mission-trained models responsible for interpreting operational information and generating recommendations. These models analyze operational context, identify relevant entities or events, and generate candidate courses of action based on mission objectives and operational constraints.

3. **Battle Management Reasoning Engine** — Coordinates the analysis performed by the AI models and organizes the outputs into structured decision support outputs. This engine applies reasoning workflows aligned with TM-BM battle management processes.

4. **Integration Layer** — Exposes system outputs through a stable API that allows the government digital assistant orchestrator to retrieve recommendations and analysis results. This design allows the system to operate independently while still contributing to the overall decision-support environment.

### Technical Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| **Data interface variability** — simulation environment may generate data in formats varying from expected schemas | Flexible data ingestion layer with configurable parsers and schema mapping tools allowing rapid adaptation to input formats |
| **Latency constraints in real-time decision support** — systems must produce recommendations quickly enough to support human decision-making cycles | Models are optimized for edge execution, running locally without cloud dependence, significantly reducing latency |
| **Multi-system interoperability** — multiple contractor-developed services may operate simultaneously during MASH | EdgeRunner delivered as a self-contained containerized microservice with well-defined API interface; operates independently while interoperating with the government-provided orchestration layer |

---

## Prior Applications and Testing

EdgeRunner capabilities are currently being piloted and operationally evaluated across multiple Department of the Air Force (DAF) organizations, including the Air Force Research Laboratory (AFRL), the Enterprise and IT End User Services Group (HNI-ES), and the Office of the Assistant Secretary of the Air Force for Space Acquisition and Integration (SAF/SQ).

Within HNI-ES, EdgeRunner is piloting several Air Force Specialty Code (AFSC)-specific AI models operating directly on standard government laptops to support acquisitions and logistics workflows. These deployments demonstrate that mission-trained models can operate fully offline while still providing procedural guidance and decision support to Air Force personnel.

EdgeRunner also provides a containerized AI runtime capable of operating within government cloud or private infrastructure. An IL5 deployment is currently underway with the SAF/SQ office under Maj Gen Purdy to evaluate mission-trained AI models supporting Department of the Air Force acquisitions workflows. In this environment, EdgeRunner provides an acquisitions-trained AI container accessible through an Azure IL5 portal.

EdgeRunner maintains a Cooperative Research and Development Agreement (CRADA) with the AFRL Information Directorate (AFRL-RI) to develop and evaluate AFSC-specific on-device AI models. This research focuses on validating how edge-resident AI can mitigate cloud dependency, cross-domain data movement constraints, and operational cost while maintaining effective decision support.

In recent internal research, EdgeRunner trained a 20-billion-parameter mission-specialized model on more than 1.6 million curated military data artifacts. The resulting model demonstrated performance comparable to frontier models while operating entirely within a local computing environment without reliance on external cloud services.

---

## Statement of Work (SOW)

### 1.0 Objective

The objective of this effort is to deploy and demonstrate the EdgeRunner Battle Management AI capability as a containerized microservice operating within the government-provided execution environment during the Multi-Decision Advantage Sprint (MASH) event under the JADPACT II program.

The system will ingest operational data generated by the MASH simulation environment and provide real-time AI-assisted decision support to battle managers participating in simulated operational scenarios. The demonstration will evaluate how mission-trained AI can enhance human decision-making across key battle management functions defined in the TM-BM framework.

### 2.0 Scope

The system will support three primary decision-support functions during the demonstration:
1. Interpretation of operational context and mission plans
2. Generation and sequencing of candidate battle courses of action
3. Evaluation of operational outcomes and impacts

The system will operate within a containerized runtime environment provided by the government, expose a stable API to the government digital assistant orchestrator, and ingest real-time data streams from the simulation environment.

### 3.0 Background

The Department of the Air Force faces an increasingly complex operational environment in which commanders must make rapid decisions across multiple operational domains while managing large volumes of data from distributed sensors, intelligence systems, and operational reporting channels.

The Transformational Model–Battle Management (TM-BM) framework defines thirteen subfunctions that collectively describe the cognitive processes required for effective battle management. This effort proposes an AI-enabled battle management capability to support these functions — particularly understanding the battlespace, interpreting operational context, generating and sequencing courses of action, coordinating operational activities, and assessing operational outcomes.

### 4.0 Tasks

**Task 1: Deployment of Containerized Service**
Capability packaged as a Docker-compatible containerized service compatible with the government's runtime environment. Container encapsulates mission-trained AI models, data ingestion services, reasoning workflows, and API interface components.

**Task 2: API-Based Integration with Government Orchestrator**
Service exposes a stable API endpoint for the government digital assistant orchestrator. Supports structured requests and responses for operational context, mission updates, and decision-support queries. Returns candidate COAs, operational analysis, coordination alerts, and mission execution assessments.

**Task 3: Processing of Dynamic Simulation Data**
Ingest and process structured and semi-structured operational data streams (sensor observations, force movements, mission status changes, operational events). Continuously update operational context model and AI analysis in near real time.

**Task 4: Delivery and Presentation of Demonstration Outputs**
Generate and deliver decision-support outputs through the API interface including: (i) identification of relevant operational events or entities, (ii) candidate battle COAs, (iii) sequencing of operational actions and timelines, (iv) assessments of potential impacts or risks.

**Task 5: Post-Event Analysis and Reporting**
Compile and analyze demonstration results. Prepare presentation and Scientific and Technical Report Summary (CDRL DI-MISC-80048) documenting technical approach, scenarios addressed, observed system performance, lessons learned, and follow-on recommendations.

### 5.0 Deliverables

| Technical Artifact | Description |
|--------------------|-------------|
| **Containerized AI Micro-Service** | Docker-compatible container hosting mission-trained AI models, reasoning engine, and secure API interface |
| **Integration Interface Specification** | API documentation describing endpoints, request/response structures, and integration procedures |
| **Demonstration Support** | On-site technical support during the MASH event |
| **Technical Presentation** | Briefing summarizing system architecture, demonstration results, and operational implications |
| **Scientific & Technical Report Summary** | CDRL DI-MISC-80048 — delivered end of period of performance |
