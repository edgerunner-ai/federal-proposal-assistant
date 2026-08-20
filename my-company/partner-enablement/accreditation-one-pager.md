# EdgeRunner AI — Compliance & Accreditation Summary
*The "can your buyer say yes" doc.*

**Distribution Statement C** · Distribution authorized to U.S. Government agencies and their contractors; Administrative/Operational Use; 2026-05-07. **CUI // FEDCON.**
**Version:** v2026-05-07 · CAGE 9Z176 · UEI SLZTJUA8DBD3 · NAICS 541511

---

## Page 1 — At a glance

### Security model

EdgeRunner AI is an air-gapped, on-device inference platform. The runtime executes locally on customer hardware. There is no cloud connectivity required during operation: no telemetry beacon, no model-update heartbeat, no licensing callback, no per-token external billing. Every inference is local. Every operator artifact stays on the customer's enclave unless explicitly returned to the GCC by an authorized data-flow path.

This design is not a configuration option — it is the architectural premise. (See `capabilities.md` §Secure Deployment & IL Architecture; evidence-ledger EV-040, EV-044.)

### Authorities to Operate (ATO) currently held

| ATO | Authorizing Official | Program | Status | Source |
|---|---|---|---|---|
| **IL-5** | U.S. Space Force / SSC | Space-domain AI agents | Active | `capabilities.md` §Secure Deployment |
| **IL-6** | Navy ICOP / NIWC Atlantic / PMW 120 | Integrated Common Operating Picture | Active. EdgeRunner is on the Navy approved-applications list. | EV-022 |

> **Important framing.** An ATO is granted by an Authorizing Official for a specific program. Holding an IL-6 ATO from the Navy ICOP AO does not automatically transfer that authorization to a different command's AO — each AO issues their own. The credibility weight of these ATOs is that EdgeRunner has been authorized at IL-5 and IL-6 by federal AOs, evidencing the application's compliance posture and security architecture. Each new program writes its own ATO package; we provide the artifacts.

### Risk Management Framework posture

- RMF-aligned architecture.
- NIST AI RMF flywheel architecture (designed and documented as part of the Mystic Depot CSO LOE1 evaluation harness).
- Traceable, auditable AI outputs with local data control.
- Cross-domain deployment patterns supported.
- IL-2 through IL-6 multi-domain operation supported (per `proposals/akamai-gcds/` white paper §3.1).
- SECRET / TS spaces supported (per Application Arsenal capability brief).

### Identity, network, and data handling

- **CAC-enabled access** to secure DoD networks.
- **OpenAI-compatible API** for integration; drop-in replacement for cloud OpenAI / Azure OpenAI calls (EV-045).
- **Bring Your Own Model** architecture; customer can ship the model and the runtime separately.
- **Local data control.** Operator data does not leave the enclave unless an explicit authorized path returns it to the GCC.

### Distribution markings

EdgeRunner AI uses the standard DoD Distribution Statement set (per `my-company/distribution-statements.md`):
- **Statement A** — public release.
- **Statement B** — U.S. Government only.
- **Statement C** — Government + contractors. *Recommended default for partner-shared technical material.*
- **Statement D** — DoD + DoD contractors only. *Recommended default for SOCPAC-class submissions.*
- **Statement F** — directed only.
- **CUI // FEDCON** — when proprietary capabilities, pricing, or sensitive technical detail is included.

### Procurement vehicles

| Vehicle | Status | Effect |
|---|---|---|
| CDAO Tradewinds Marketplace | Awardable (EV-020) | Direct procurement via the Marketplace without re-competing |
| CDAO Tradewinds CSO | Direct Award holder (USSF, EV-023) | Closed contract via CSO Direct Award; vehicle is distinct from Marketplace |
| SAM.gov | Active (EV-021) | Required registration current |
| GSA Schedule (MAS) | [CONFIRM: not held per current sources] | — |
| Other IDIQs / consortia (SOSSEC, NSTXL, TReX, etc.) | [CONFIRM: not listed in repo] | — |

### Identifiers

```
CAGE 9Z176 · UEI SLZTJUA8DBD3 · NAICS 541511 · SAM.gov Active
ATOs: IL-5 (USSF SSC) · IL-6 (Navy ICOP / NIWC Atlantic)
Vehicles: CDAO Tradewinds Marketplace (Awardable) · Tradewinds CSO Direct Award holder
```

---

## Page 2 — FAQ for the customer's contracting / cyber officer

### Is the IL-6 ATO transferable to my command?

No, and any vendor who tells you otherwise is overclaiming. Each Authorizing Official issues their own ATO based on their program's mission, system boundary, and risk posture. The Navy ICOP ATO is evidence that EdgeRunner has been ATO'd at IL-6 by a federal AO — that evidences the application's compliance posture and security architecture. Your AO will issue their own ATO. We provide:
- Architecture and data-flow diagrams.
- NIST 800-53 control mappings.
- Test artifacts and evidence packages from prior ATO work.
- Direct support to your ATO sprint (cyber lead engagement, SE walkthrough, RMF artifact tailoring).

### What does a typical ATO sprint look like for a new customer?

[CONFIRM: end-to-end timeline TBD. Common envelope is 60–120 days for an inheriting program at IL-5 and 90–180 days at IL-6, but actual depends on the AO's package requirements and the customer's reciprocity practices. Bill / cyber lead to provide a canonical answer.]

The shape of an EdgeRunner-supported ATO sprint:
1. **Kickoff with the customer's ISSM/ISSO** — system boundary definition, mission needs, classification level.
2. **Artifact handoff** — architecture diagrams, control mappings, prior ATO package (with appropriate distribution markings).
3. **Tailoring** — adjustments to satisfy customer-specific overlays.
4. **Evidence collection** — test artifacts, vulnerability scans, configuration baseline.
5. **AO review and authorization** — customer-led; we support.

### What artifacts can EdgeRunner provide for an RMF package?

- Three-tier architecture diagram (enterprise → GCC → edge).
- Data-flow diagram, including any return-to-GCC path.
- NIST 800-53 control mapping (IL-5 baseline, with IL-6 overlay where applicable).
- Boundary diagram and component inventory.
- Vulnerability disclosure history. [CONFIRM: VDP and SLA details — not currently in repo.]
- NIST 800-171 questionnaire response. (A version exists for the JADPACT/MASH submission and can be tailored. Source: `my-company/past-proposals/jadpact-mash-baa-2026/security-questionnaire.md`.)
- AI-system-specific NIST AI RMF flywheel architecture documentation.

### Can EdgeRunner run in a SCIF or on a classified enclave?

Yes. The Navy ICOP deployment is an example (EV-014). SECRET and TS spaces are supported per the Application Arsenal capability brief. The runtime is air-gapped by design — no cloud dependency means there is no exfiltration path to remediate, which is the architectural property the customer's cyber officer is most often verifying.

### What about CMMC / SPRS / FedRAMP / SOC 2 / ISO 27001?

[CONFIRM: status of each. Per `my-company/edgerunner-profile-2026-05-08.md` §4, these are flagged as TODO. Bill / cyber lead to provide the canonical status. Do NOT publish a partner-shared version of this one-pager with these items unanswered. Suggested response shape:]
- **CMMC level:** [CONFIRM]
- **NIST SP 800-171 / SPRS score:** [CONFIRM — JADPACT security questionnaire was answered using NIST 800-171 framework throughout, but no published SPRS score is in the repo]
- **FedRAMP:** **Not held.** EdgeRunner has not pursued FedRAMP authorization for its application; the requirement has not arisen, because the product deploys on-premises and air-gapped inside the customer's own accredited boundary rather than as a cloud service. Do not claim any FedRAMP status. (Confirmed by Bill, 2026-07-26; consistent with `edgerunner-profile.md` §4 "Not held — do not claim.") Where a FedRAMP-authorized environment is relevant, it belongs to the hosting platform or a partner, and must be attributed to them.
- **SOC 2:** [CONFIRM]
- **ISO 27001:** [CONFIRM]

### Are EdgeRunner personnel cleared?

[CONFIRM: clearance roster is not in repo. If "cleared personnel" is part of the security posture answer, the canonical statement needs to come from Bill before this section is partner-shared. The current evidence ledger does not document personnel clearance levels.]

### How does EdgeRunner handle vulnerability disclosure?

[CONFIRM: VDP policy and SLA are not currently in the repo. The pattern customers expect is: a published VDP, a triage SLA, and a maintained changelog of resolved CVEs. Bill / cyber lead to provide.]

### Where can the customer's cyber team find prior compliance evidence?

By distribution marking and request:
- **Statement A (public):** the two published papers (arXiv preprints) in `my-company/capability-papers/` — `edgerunner-20b/EdgeRunner_20B.pdf` and `mil-deflect/mil_deflect.pdf`.
- **Statement C (Government + contractors):** this one-pager, the architecture brief, the past-performance citations.
- **Statement B / D / F:** prior ATO packages, JSOC pilot details (EV-061, restricted), and any program-specific compliance evidence — request through the EdgeRunner cyber lead.

### What is your guidance if my AO asks for an "IL-6 ATL"?

The repo source consistently uses **IL-6 ATO** (Authority to Operate). If a customer or partner is using "ATL," it may be a regional acronym or a typo — clarify the term before responding. EdgeRunner has Authority to Operate at IL-6, granted by the Navy ICOP AO (EV-022). [CONFIRM: confirm the customer's intended term to avoid mismatched expectations.]

---

## Page 3 — Companion data (for the cyber officer's package)

### Hardware compatibility profile

- **VRAM:** 8 GB minimum (4B model); 16 GB recommended (20B / 26B models).
- **OS:** Windows, Linux, macOS.
- **Silicon:** Hardware-agnostic — Intel, AMD, NVIDIA. Validated platforms include HP ruggedized laptops (EV-050), Panasonic Toughbook (EV-051), AMD x86 (EV-052), Intel x86 (EV-053).
- **Form factors:** GFE laptop, edge server, fly-away kit, ATAK / TAK device, tablet.
- **Deployment options:** binary install or containerized web-hosted application.

### Data architecture

- Local-first inference. No cloud dependency. No mandatory telemetry.
- Optional structured operational data return to the GCC for model refinement (EVELYN platform; EV-070).
- BYOM (Bring Your Own Model) architecture: customer can supply model weights or use EdgeRunner's military-tuned models (EdgeRunner 20B, MOS/AFSC LoRA adapters).

### Contract / vehicle reference

- **CDAO Tradewinds Marketplace Awardable** — direct procurement, no re-compete (EV-020).
- **CDAO Tradewinds CSO Direct Award** — closed USSF contract (EV-023). Vehicle distinct from the Marketplace.
- **SAM.gov:** Active (EV-021).
- **Nontraditional Defense Contractor:** Yes — material to OTA submissions (per `my-company/edgerunner-profile-2026-05-08.md` §2).

### Past performance — production / deployed

(For full distribution-marked citations, see the Proof-Point Library, P1.)

| Customer | Program | Evidence ID |
|---|---|---|
| USASOC — 1st SFG | SOF AI Pilot | EV-001 |
| USASOC — 7th SFG | SOF AI Pilot | EV-002 |
| USASOC — 10th SFG | SOF AI Pilot | EV-003 |
| JFK Special Warfare Center & School | SOF Training Integration | EV-004 |
| 4th Infantry Division | NGC2 | EV-005 |
| U.S. Navy ICOP (NIWC Atlantic / PMW 120) | Integrated Common Operating Picture | EV-014 |
| U.S. Space Force | TradeWinds CSO Direct Award contract | EV-023 |
| AFRL CRADA | Research collaboration | EV-010 |
| ARL JWS | AI agents for drones / robotics / CV | EV-011 |
| JSOC pilot | Restricted — Distribution B+ environments only | EV-061 |

---

*Source: every claim traces to `my-company/evidence-ledger.json` (EV-NNN). Items marked [CONFIRM] must be resolved by Bill or the cyber lead before this document is shared with a partner or customer. The CMMC / SPRS / FedRAMP / SOC 2 / ISO 27001 line is the most consequential gap; do not ship this one-pager externally until those answers are filled in.*

*Document is marked **Distribution Statement C, CUI // FEDCON**. Do not redistribute outside Government + cleared contractor channels. For a Statement A version (public release), strip the proof-point table, the JSOC reference, and the back-page detail; keep only the at-a-glance summary on Page 1.*
