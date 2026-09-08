# Readiness Levels Quick Reference (TRL, IRL, SRL, MRL)

Government definitions only, for use while drafting and checking proposals. TRL tables and terms are the wording of the DoD *Technology Readiness Assessment Guidebook*, February 2025 (Tables 2-1, 2-2, 2-3, 6-1). IRL and SRL are the scales GAO-20-48G adapted from Sauser and that the DoD Guidebook adopts (Guidebook Figure 6-1 and 6-2; GAO Tables 14 and 15). House rules for making a claim live in `reference/trl-irl-reference.md`, section 4.

## 1. Technology Readiness Levels, hardware and software

| TRL | Hardware definition | Software definition | Software: what the level means | Evidence that supports the level (software) |
|---|---|---|---|---|
| 1 | Basic principles observed and reported. | Basic principles observed and reported. | A new software domain under basic research: basic use, basic properties of software architecture, mathematical formulations, general algorithms. | Basic research activities, research articles, peer-reviewed white papers, point papers, early lab model of basic concept. |
| 2 | Technology concept and/or application formulated. | Technology concept and/or application formulated. | Practical applications invented but speculative; no proof or detailed analysis. Analytic studies using synthetic data. | Applied research activities, analytic studies, small code units, papers comparing competing technologies. |
| 3 | Analytical and experimental critical function and/or characteristic proof of concept. | Analytical and experimental critical function and/or characteristic proof of concept. | Scientific feasibility shown through analytical and laboratory studies; limited-functionality environments validate critical properties, including cybersecurity, with non-integrated components and partially representative data. | Algorithms on a surrogate processor in a laboratory; instrumented components in a laboratory; laboratory results validating critical properties. |
| 4 | Component and/or breadboard validation in a laboratory environment. | Module and/or subsystem validation in a laboratory environment (software prototype development environment). | Basic software components integrated to show they work together; primitive in efficiency and robustness. Architecture work begins (interoperability, reliability, maintainability, extensibility, scalability, security). Emulation with legacy elements. | Advanced technology development; stand-alone prototype solving a synthetic full-scale problem; stand-alone prototype processing fully representative data sets. |
| 5 | Component and/or breadboard validation in a relevant environment. | Module and/or subsystem validation in a relevant environment. | Ready to start integration with existing systems. Prototype conforms to target environment and interfaces; realistic problems; simulated interfaces to existing systems; system software architecture established; algorithms on processors with expected operational characteristics. | System architecture diagram with critical performance requirements; processor selection analysis; Sim/Stim laboratory build-up plan; software under configuration management; COTS/GOTS components identified. |
| 6 | System/subsystem model or prototype demonstration in a relevant environment. | Module and/or subsystem validation in a relevant end-to-end environment. | Engineering feasibility demonstrated: laboratory prototype on full-scale realistic problems, partially integrated with existing hardware and software; cybersecurity verification included in testing. | Laboratory test results for a prototype near the desired configuration, including physical, logical, data, and security interfaces; tested-versus-operational difference analytically understood; measured throughput, scalability, reliability contribution; human-computer analysis begun. |
| 7 | System prototype demonstration in an operational environment. | System prototype demonstration in an operational, high-fidelity environment. | Program feasibility demonstrated: operational-environment prototype, critical technical-risk functionality available for demonstration and test, well integrated with operational hardware and software. | Critical technological properties, including cybersecurity, measured against requirements in an operational environment. |
| 8 | Actual system completed and qualified through test and demonstration. | Actual system completed and mission qualified through test and demonstration in an operational environment. | Fully integrated with operational hardware and software; development documentation complete; all functionality and cybersecurity measures tested in simulated and operational scenarios. | Published documentation and technology-refresh build schedule; software resource reserve measured and tracked; all severity 1 and 2 defects resolved, low severity 3 backlog. |
| 9 | Actual system proven through successful mission operations. | Actual system proven through successful mission-proven operational capabilities. | Readily repeatable and reusable; fully integrated; all documentation verified; successful operational experience; sustaining engineering in place. | Production configuration-management reports; defect resolution system and process in place for deployed software. |

Hardware descriptions for the levels that are most often argued: TRL 5, high-fidelity laboratory integration of components; TRL 6, a prototype tested in a high-fidelity laboratory or simulated operational environment; TRL 7, an actual system prototype demonstrated in an operational environment (in an aircraft, in a vehicle, in space); TRL 8, developmental test and evaluation in the intended weapon system; TRL 9, operational test and evaluation.

## 2. Environment and fidelity terms (Guidebook Table 2-3)

| Term | Definition |
|---|---|
| Relevant environment | Testing environment that simulates both the most important and most stressing aspects of the operational environment. |
| Simulated operational environment | Either a real environment that can simulate all the operational requirements and specifications required of the final system, or a simulated environment that allows testing of a virtual prototype. Used to determine whether a developmental system meets the operational requirements and specifications of the final system. |
| Operational environment | Environment that addresses user operational requirements and specifications required of the final system, including platform and packaging. |
| High fidelity | Addresses form, fit, and function. A high-fidelity laboratory environment can simulate and validate all system specifications within a laboratory setting; high-fidelity models are accredited to represent the system for their defined purpose. |
| Low fidelity | A representation with limited ability to provide anything but first-order information about the end product; used for trend analysis. |
| Breadboard | Integrated components representing a system or subsystem, used to determine concept feasibility and develop technical data; laboratory-configured; may resemble the final system in function only. |
| Model | A functional form of a system, generally reduced in scale, near or at operational specification, hardened enough to demonstrate the required technical and operational capabilities. |
| Prototype | A physical or virtual model used to evaluate the technical or manufacturing feasibility or military utility of a technology, process, concept, end item, or system. |

**The Guidebook's test for a relevant environment.** A set of stressing conditions, representative of the full spectrum of intended operational employments, applied to the technology as part of a component (TRL 5) or system/subsystem (TRL 6). One or a few demonstrations under favorable conditions do not meet it. The demonstration must either validate the required functionality across the full spectrum of intended employments, or validate it for the important employments and extend confidence across the rest with accepted analytical techniques.

## 3. Reading TRL 6, 7, and 8 in an assessment

| Level | The assessor's question | Meets it | Does not meet it |
|---|---|---|---|
| 6 | Did a near-final prototype run end to end on a full-scale realistic problem, in conditions that simulate the stressing parts of the mission, partially integrated with the real systems around it? | A laboratory or field exercise with representative data, representative hardware class, real interfaces stubbed or partially live, cybersecurity verified. | A demonstration on a curated dataset; a component running alone; favorable conditions only. |
| 7 | Did the system prototype run in the operational environment, integrated with the operational hardware and software, with the risky functions exercised and measured against requirements? | A user's own data on the user's own systems in a field event or deployment, with an assessment record. | A relevant environment, however good; a demonstration where the risky function was not exercised. |
| 8 | Is the actual system complete and qualified in that environment, documented, with severity 1 and 2 defects closed? | Program-of-record fielding with acceptance testing and a refresh schedule. | A prototype, however well it ran. |

## 4. Integration Readiness Levels (GAO-20-48G Table 14, adopted by the DoD Guidebook, Figure 6-1)

IRL measures the maturity of the integration between two or more components. It is scored per integration point; a system with several integrations has several IRLs.

| IRL | Definition | Evidence |
|---|---|---|
| 0 | No integration. | No integration between the specified components has been planned or intended. |
| 1 | A high-level concept for integration has been identified. | Principal integration technologies identified; top-level functional architecture and interface points defined; high-level concept of operations and principal use cases started. |
| 2 | Some specificity of requirements to characterize the interaction between components. | Inputs and outputs for the principal integration technologies known, characterized, and documented; principal interface requirements or specifications drafted. |
| 3 | The detailed integration design has been defined, including all interface details. | Detailed interface design documented; system interface diagrams completed; inventory of external interfaces completed with data engineering units identified. |
| 4 | Validation of interrelated functions between integrating components in a laboratory environment. | Functionality of the integrating modules, functions, or assemblies demonstrated in a laboratory or synthetic environment; data transport methods and specifications defined. |
| 5 | Validation of interrelated functions between integrating components in a relevant environment. | Individual modules tested to verify the module components work together; external interfaces well defined (source, data formats, structure, content, method of support). |
| 6 | Validation of interrelated functions between integrating components in a relevant end-to-end environment. | End-to-end functionality of the systems integration validated; data transmission tests completed successfully. |
| 7 | System prototype integration demonstration in an operational high-fidelity environment. | Fully integrated prototype demonstrated in an actual or simulated operational environment; each system and software interface tested individually under stressed and anomalous conditions. |
| 8 | System integration completed and mission qualified through test and demonstration in an operational environment. | Fully integrated system meets overall mission requirements in an operational environment; system interfaces qualified and functioning correctly there. |
| 9 | System integration proven through successful mission-proven operations capabilities. | Fully integrated system has demonstrated operational effectiveness and suitability in its intended or a representative operational environment; integration performance fully characterized and consistent with user requirements. |

The original Sauser scale (2008) uses the same nine numbers with different wording (interface, interaction, compatibility, quality assurance, control, information structuring, verification and validation, mission qualification, mission proven). Some platforms and papers still use it; when a solicitation names IRL, check which scale it cites.

## 5. System Readiness Levels (GAO-20-48G Table 15; DoD Guidebook Figure 6-2)

SRL is an index computed from the TRLs of a system's technologies and the IRLs of their integration points, mapped to the acquisition life cycle.

| SRL | Definition |
|---|---|
| 1 | System alternative materiel solutions should have been considered. |
| 2 | System materiel solution should have been identified. |
| 3 | System high-risk immature technologies should have been identified and prototyped. |
| 4 | System performance specifications and constraints should have been defined and the baseline allocated. |
| 5 | System high-risk component technology development should have been complete; low-risk system components identified. |
| 6 | System component integrability should have been validated. |
| 7 | System threshold capability should have been demonstrated at operational performance level using operational interfaces. |
| 8 | System interoperability should have been demonstrated in an operational environment. |
| 9 | System has achieved initial operational capability and can satisfy mission objectives. |

## 6. Manufacturing Readiness Levels (DoD Guidebook Table 6-1; MRL Deskbook 2022)

MRLs assess manufacturing maturity and risk for a technology, component, subsystem, or system; TRLs assess the maturity of an individual technology. DoDI 5000.88 requires program managers to manage manufacturing, producibility, and quality risk across the life cycle.

| MRL | Description |
|---|---|
| 1 | Basic manufacturing implications identified. |
| 2 | Manufacturing concepts identified. |
| 3 | Manufacturing proof of concept developed. |
| 4 | Capability to produce the technology prototype in a laboratory environment. |
| 5 | Capability to produce prototype components in a production-relevant environment. |
| 6 | Capability to produce a prototype system or subsystem in a production-relevant environment. |
| 7 | Capability to produce systems, subsystems, or components in a production-representative environment. |
| 8 | Pilot line capability demonstrated; ready to begin low-rate initial production. |
| 9 | Low-rate production demonstrated; capability in place to begin full-rate production. |
| 10 | Full-rate production demonstrated and lean production practices in place. |

## 7. Sources

- DoD, *Technology Readiness Assessment Guidebook*, February 2025, OUSD(R&E): https://www.cto.mil/wp-content/uploads/2025/03/TRA-Guide-Feb2025.v2-Cleared.pdf
- GAO, *Technology Readiness Assessment Guide*, GAO-20-48G, January 2020: https://www.gao.gov/products/gao-20-48g
- Sauser, Gove, Forbes, Ramirez-Marquez, "Integration maturity metrics: development of an Integration Readiness Level," INCOSE 2008 (original IRL wording).
- DoD *Manufacturing Readiness Level Deskbook*, 2022; DoDI 5000.88; 10 U.S.C. 4252.
