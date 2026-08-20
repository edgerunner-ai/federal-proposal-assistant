# Government Acquisition & Cost Guidance Catalog

**Purpose.** This is the authoritative-source register for EdgeRunner federal work. It tells the
drafting skills *which* government documents govern *which* claims, so that proposals, ROMs,
white papers, and cost artifacts are written against the customer's actual acquisition and
cost-estimating rules — not against generic vendor marketing. Cite these the way an evaluator
expects them cited: by document number and the specific provision, not by vibe.

**How to use it.**
- The **Applicability Matrix** (bottom) maps proposal type → the guidance that applies.
- Each entry states: what it governs, current ID/date/status, EdgeRunner relevance, and the
  concrete drafting move it forces.
- Treat every status line as point-in-time (verified June 2026). Re-verify the issuance date and
  whether a newer change/version exists before asserting "current" in a customer-facing document.
- **Masthead note.** DoD issuances reissued in/after 2025 carry the "Department of War (DoW)"
  masthead and "DoWI" labeling; the *instruction numbers are unchanged* (e.g., DoDI/DoWI 5000.02).
  Match the customer's own usage in the solicitation. Do not editorialize the rename in prose.

This file is a local FPA reference (not a workbench-synced doctrine file) — it may be hand-edited
here. Keep it factual; it is a citation map, not a sales sheet.

---

## Tier 1 — Cost estimating & pricing (governs ROMs, cost volumes, BOEs, OTA milestone schedules)

### GAO Cost Estimating and Assessment Guide — GAO-20-195G (March 2020)
- **Governs:** what makes a cost estimate *defensible*. The canonical reference DoD cost analysts,
  DCAPE, and GAO auditors grade estimates against.
- **The four characteristics** every credible estimate must show: **comprehensive, well-documented,
  accurate, credible.** The **12-step process** maps to those four. (See Table 3 in the guide.)
- **EdgeRunner move:** even a one-page ROM should *visibly* satisfy the four characteristics in
  miniature — state the method (analogous / parametric / engineering build-up), document the
  basis and assumptions, show a range with uncertainty (credible), and tie scope to cost
  (comprehensive). A ROM that reads as a single point number with no basis fails the credibility
  test the moment a trained reviewer sees it.
- **Source:** https://www.gao.gov/products/gao-20-195g (PDF: gao.gov/assets/gao-20-195g.pdf)

### DoDI 5000.73 — Cost Analysis Guidance and Procedures (reissued **24 Oct 2024**)
- **Governs:** how DoD conducts cost estimation, cost analysis, and cost-data collection; roles of
  DCAPE/DDCA; when an Independent Cost Estimate (ICE) is required; Cost and Software Data Reporting
  (CSDR), including **Software Resources Data Reports (SRDR)**.
- **This is the document DoDI 5000.87 points to** for Software Acquisition Pathway cost estimates
  ("the cost estimate will be developed in accordance with DoDI 5000.73").
- **EdgeRunner move:** when a solicitation is on the Software or MTA pathway and asks for a cost
  estimate, frame the basis in 5000.73 terms (analogous/parametric/engineering, with CSDR/SRDR
  awareness for larger efforts). For small OTAs/CSOs this is context, not a deliverable — don't
  manufacture a CSDR plan nobody asked for.
- **Source:** https://www.esd.whs.mil/portals/54/documents/dd/issuances/dodi/500073p.pdf

### GAO Agile Assessment Guide — GAO-24-105506 (reissued w/ revisions 15 Dec 2023)
- **Governs:** cost estimating, scheduling, WBS, and EVM *in an Agile/iterative software context* —
  i.e., how to estimate when you're delivering capability in increments rather than against a fixed
  spec. Directly relevant to any EdgeRunner software/AI effort using a DevSecOps cadence.
- **EdgeRunner move:** when pricing iterative delivery (sprints, capability releases, MVP→MVCR),
  estimate by **capacity/throughput over time** (team × cadence × duration), not by pretending a
  waterfall WBS exists. This is the defensible way to cost a SWP-pathway effort and it aligns the
  pricing artifact with the technical narrative.
- **Source:** https://www.gao.gov/products/gao-24-105506

### Companion GAO guides (cite when the solicitation raises the topic)
- **GAO Schedule Assessment Guide (GAO-16-89G)** — the 10 best practices for a credible integrated
  master schedule. Use when a white paper or proposal commits to a delivery timeline that an
  evaluator will test for realism.
- **GAO Technology Readiness Assessment Guide (GAO-20-48G)** — TRL methodology. EdgeRunner cites
  *operational* TRL 8 deployments (USASOC, 4th ID, 101st, Navy ICOP); use this guide's vocabulary
  so the TRL claim reads as a methodology-grounded assessment, not a self-awarded badge.

### Basis of Estimate (BOE) — practice, not a single regulation
- **Governs:** the narrative that justifies each cost element in a FAR cost volume or detailed OTA
  proposal — labor hours, mix, materials, ODCs, with the rationale (analogy, parametric, vendor
  quote, engineering judgment) and traceability to the SOW/WBS.
- **EdgeRunner move:** only triggered for `far-cost-volume` and detailed `ota-milestones` artifacts.
  For ROM/CSO/SBIR it is explicitly **out of scope** — see `pricing-artifacts/rom.md` "must_not_produce."

---

## Tier 2 — Acquisition pathway framing (tells you what kind of response the customer can even accept)

### DoDI 5000.02 — Operation of the Adaptive Acquisition Framework (23 Jan 2020, Ch.1 2022; DoW reissues 2025+)
- **Governs:** the six pathways — **Urgent Capability, Middle Tier of Acquisition (MTA), Major
  Capability, Software Acquisition, Defense Business Systems, Acquisition of Services.** Each has a
  different artifact set, cadence, and evaluation logic.
- **EdgeRunner move:** identify the pathway *before* deciding what to write. The same capability is
  pitched differently under MTA (rapid prototyping/fielding, ≤5 yr) vs. SWP (continuous delivery) vs.
  Services. Naming the pathway correctly signals acquisition literacy to the evaluator.
- **Source:** https://www.esd.whs.mil/Portals/54/Documents/DD/issuances/dodi/500002p.PDF

### DoDI 5000.87 — Operation of the Software Acquisition Pathway (2 Oct 2020) — **local copy: `500087p.pdf`**
- **Governs:** the preferred pathway for software-intensive capability. As of **March 2025 the SecDef
  directed SWP as the preferred pathway for all DoD software development** — a strong tailwind to cite.
- **Two paths:** applications (commercial HW/cloud) and embedded (mil-unique HW). **Two phases:**
  Planning → Execution. **Entry-to-execution artifacts:** CNS, User Agreement, Acquisition Strategy,
  Test Strategy, Cost Estimate.
- **Load-bearing concepts for EdgeRunner prose:**
  - **MVP / MVCR** — Minimum Viable Product, Minimum Viable Capability Release. **MVCR for the
    applications path must reach an operational environment ≤1 year from first funds obligated**
    (congressional/OSD bias is 6 months or less), then deliver **at least annually** thereafter.
  - **Value assessments** at least annually after fielding.
  - **DevSecOps / continuous testing / cybersecurity as persistent requirements**, MOSA, max automation.
  - Cost estimate **per DoDI 5000.73**; IP strategy **per DoDI 5010.44**.
- **EdgeRunner move:** when responding to an SWP effort, structure the technical approach around
  MVP→MVCR with an explicit ≤12-month (ideally faster) first-delivery commitment and an annual
  cadence. This is the customer's own success criterion — answering it directly is a discriminator.
  Edge AI's offline/on-device posture is the credible enabler for delivering into DDIL operational
  environments on that cadence.

### Authorities to recognize by name (frame the vehicle correctly)
- **OTAs — 10 U.S.C. § 4022** (prototype OTs) and **§ 4021** (research OTs); production follow-on
  under § 4022(f). EdgeRunner's Vulcan JATF / Mystic Depot-style work lives here. OTAs are *not*
  FAR contracts — do not import FAR/DCAA cost-volume expectations into an OTA milestone proposal.
- **Commercial Solutions Opening (CSO) — 10 U.S.C. § 3458** + DFARS/class deviations. Commercial
  pricing logic, not certified cost & pricing data. See `pricing-artifacts/cso-commercial.md`.
- **SBIR/STTR** — phase-gated, statutory data rights (see Tier 5). See `pricing-artifacts/sbir-budget.md`.
- **EdgeRunner move:** the pricing artifact and the prohibited-claims posture are *dictated by the
  vehicle.* `working/proposal-type.md` already encodes this; this catalog explains the "why."

---

## Tier 3 — Software delivery, security & authorization (governs every ATO / cyber / DevSecOps claim)

### RAISE 2.0 — Rapid Assess and Incorporate Software Engineering Implementation Guide (Navy, v1.0, 4 Oct 2022) — **local copy: `RAISE2.0ImplementationGuide1Nov2022.pdf`**
- **Governs (Navy/DON):** how a containerized application inherits an existing **RAISE Platform of
  Choice (RPOC)** ATO instead of obtaining its own — the Navy's operational mechanism for cATO-style
  rapid fielding. **Highly relevant to EdgeRunner given the Navy ICOP / PMW 120 program-of-record
  relationship and the IL-6 ATO held via that program.**
- **Mechanics EdgeRunner should speak fluently:**
  - **RPOC** = a DevSecOps Platform (DSOP) whose inheritable security controls are AO-approved and
    whose CI/CD tools are TA-certified. Apps onboarded via RAISE deploy under the RPOC's ATO.
  - **Security Gates (8):** SAST (custom source), SBOM/dependency list, secrets/keys detection,
    container security scan (CSS), DAST, RPOC-ISSM review, **container image signing**, store signed
    image in artifact repo. (SAST not required for COTS; signing is mandatory to deploy.)
  - **Acceptable residual risk:** all findings mitigated to **not exceeding Moderate**; High-risk apps
    fall *outside* RAISE and revert to standard RMF. **High-and-above raw findings in production:
    remediate/mitigate within 21 calendar days** or the workload is isolated/removed.
  - **Edge environments** (ships, subs, planes, vehicles, tactical — *EdgeRunner's home turf*): when
    the app can't do live ConMon at the edge, the requirement is met at the **Staging/Pre-Prod**
    environment, and the edge node **synchronizes logs/updates when the mission allows.**
  - **Application Owner obligations:** SLA with RPOC Owner, registration in DADMS/DITPRDON, complete
    SRG/STIG, vulnerability management plan, SBOM, pass all gates every release.
- **EdgeRunner move:** for any Navy software effort, position EdgeRunner as a **container-native,
  RAISE-onboardable application** that meets the security gates and the Moderate residual-risk bar,
  and explicitly address **edge ConMon via stage-sync** — turning the disconnected/air-gapped
  deployment from a compliance liability into a designed-for behavior the Navy guide already
  anticipates. **Do not** claim an inherited ATO for a platform that isn't the actual RPOC; the
  IL-6 ATO is program-scoped (ICOP/PMW 120), per company doctrine — keep product-ATO and
  internal-ops compliance separate.
- **Key references inside RAISE 2.0:** NIST SP 800-190 (container security), DevSecOps CI/CD
  Assessment Guidebook, DoD Enterprise DevSecOps Reference Design, DevSecOps Fundamentals Guidebook.

### Continuous ATO (cATO) — DepSecDef/DoD CIO memo (3–4 Feb 2022) + DoD CIO *DevSecOps Continuous Authorization Implementation Guide*
- **Governs:** the enterprise standard RAISE 2.0 operationalizes for the Navy. **Three required
  competencies:** (1) ongoing visibility / continuous RMF-control monitoring inside the boundary,
  (2) active cyber defense, (3) an approved DevSecOps reference design. **A cATO has no expiration**
  while the real-time risk posture is maintained.
- **EdgeRunner move:** when the customer isn't Navy-specific, frame the same story in cATO terms
  rather than RPOC terms. Match the customer's vocabulary.
- **Sources:** https://media.defense.gov/2022/Feb/03/2002932852/-1/-1/0/CONTINUOUS-AUTHORIZATION-TO-OPERATE.PDF
  · https://dodcio.defense.gov/Portals/0/Documents/Library/DoDCIO-ContinuousAuthorizationImplementationGuide.pdf

### Supporting security baselines (cite by name when claims touch them)
- **DoD Enterprise DevSecOps Reference Design** + **DevSecOps Fundamentals Guidebook** — the
  "approved reference design" cATO competency #3 requires.
- **NIST SP 800-190** — Application Container Security Guide (the residual-risk basis behind RAISE gates).
- **RMF:** **DoDI 8510.01** + **NIST SP 800-37** (process) and **NIST SP 800-53 Rev 5** (controls).
  The DoD CC SRG completed its move to **Rev 5** in 2024 — use Rev 5 control language.
- **DoD Cloud Computing SRG — Impact Levels:** **IL2** (public), **IL4** (CUI), **IL5** (higher-
  sensitivity CUI / mission-critical / NSS-adjacent), **IL6** (SECRET / SIPRNet). CC SRG updated
  **June 2024**; FedRAMP↔IL reciprocity is defined for IL4/5/6.
  - **EdgeRunner guardrail:** cite **IL-6 only in the ICOP/PMW-120 program context** where it is the
    actual posture. Per `prohibited-claims-doctrine.md`, FedRAMP/CMMC/IL claims are categorical
    no-gos without a direct evidence-ledger citation. Edge/on-prem inference often sidesteps the
    cloud-IL framing entirely — say so plainly rather than over-claiming a level.

---

## Tier 4 — AI-specific governance (governs every "responsible/trustworthy AI" claim)

### DoD AI Ethical Principles (adopted Feb 2020) + DoD Responsible AI (RAI) Strategy & Implementation Pathway + **RAI Toolkit** (CDAO, 2023)
- **Governs:** the five principles — **Responsible, Equitable, Traceable, Reliable, Governable** —
  and the CDAO toolkit/worksheets that operationalize them (built on DIU's RAI Guidelines and the
  **NIST AI RMF**). Available via Tradewind (tradewindai.com/rai-toolkit).
- **EdgeRunner move:** when a solicitation invokes responsible/ethical/trustworthy AI, answer in the
  five-principle vocabulary and point to concrete design facts (auditability/traceability of a
  mil-specific model, governable on-device controls, reliability evidence from the EdgeRunner 20B /
  Mil-Deflect papers). Don't assert "responsible AI" as an adjective — map it to the principles.

### OMB AI memoranda (national-security and civilian acquisition framing)
- **M-25-21** — *Accelerating Federal Use of AI through Innovation, Governance, and Public Trust*
  (3 Apr 2025). **M-25-22** — *Driving Efficient Acquisition of AI in Government* (3 Apr 2025).
  (Superseded the 2024 M-24-10 / M-24-18 line.) **M-26-04** (Dec 2025) — unbiased-AI principles.
- **EdgeRunner move:** for civil-agency or cross-government AI work, frame procurement-readiness and
  governance in the current OMB-memo vocabulary. Re-verify which memo is operative for the specific
  customer at bid time — this line moves fast.
- **NIST AI RMF (AI 100-1)** + Generative AI Profile — the cross-government risk vocabulary under all
  of the above.

---

## Tier 5 — Cross-cutting: IP / data rights & open systems

### DoDI 5010.44 — Intellectual Property Acquisition & Licensing (the IP strategy DoDI 5000.87 requires)
- **Governs:** the program's IP strategy — delivery and license rights for software, source, build/
  automation scripts, data sets, SBOM, third-party components.
- **EdgeRunner move:** this is where the **two-bucket data-rights pattern** lives (Government Purpose
  Rights on funded deliverables / commercial license retained on the core product & harness — see
  project memory `reference_data_rights_two_bucket`). State the split explicitly; SWP evaluators are
  trained to look for it.

### DFARS 252.227-7013/-7014 — rights in technical data / noncommercial software; FAR/DFARS commercial-item licensing
- **Governs:** the contractual mechanics behind the two-bucket pattern. Cite when an OTA/FAR effort
  asks for a data-rights assertions table.

### MOSA — Modular Open Systems Approach (10 U.S.C. § 4401; required by DoDI 5000.02/.87)
- **Governs:** the statutory expectation of modular, open-interface design. EdgeRunner's documented
  open interfaces / model-tier modularity answer this directly.

---

## Applicability Matrix — which guidance the drafting skills should pull per proposal type

| Proposal type (`type_id`) | Tier 1 (cost) | Tier 2 (pathway) | Tier 3 (ATO/sec) | Tier 4 (AI) | Tier 5 (IP) |
|---|---|---|---|---|---|
| `rom` | GAO-20-195G (4 characteristics, in miniature) | name the likely vehicle | only if cyber is a cost driver | if AI claim made | — |
| `cso-brief` / `cso-full` | GAO-20-195G + commercial pricing logic | CSO §3458 | cATO/RAISE if fielding claim | RAI principles + OMB M-25-22 | two-bucket if deliverable |
| `ota-proposal` / `ota-white-paper` | 5000.73 framing; milestone basis (not BOE) | OTA §4022/§4021 | RAISE 2.0 / cATO | RAI + NIST AI RMF | DoDI 5010.44 + DFARS-7014 |
| `sbir-phase1/2` | SBIR budget rules | SBIR statute | proportionate | RAI if applicable | SBIR data rights |
| `far-rfp` / `idiq-to` | GAO-20-195G + **full BOE** + 5000.73 | 5000.02 pathway | RMF/SRG + IL (evidence-cited) | RAI + OMB memos | DFARS-7013/-7014 |
| `white-paper` (Navy/software) | Agile cost basis if costed | **5000.87 (MVP/MVCR/≤1yr)** | **RAISE 2.0 (gates, edge ConMon, ≤Moderate)** | DoD AI principles | DoDI 5010.44 + MOSA |
| `gsa-mas-task-order` | MAS pricing | Services / 5000.74 | RMF/SRG as required | RAI if applicable | commercial license |

---

## Integration notes (wired 2026-06-26)

The catalog is enforced by the framework, not just available for reference:

1. **`pricing-artifacts/rom.md` & `far-cost-volume.md`** — mental-model sections now state the
   GAO-20-195G four-characteristics / DoDI 5000.73 (and GAO-24-105506 for iterative) defensibility bar. ✅
2. **`proposal-types/*.md`** — every type body carries an **Acquisition guidance** section keyed to
   its matrix row; `proposal-types/README.md` documents the catalog-wide contract. ✅
3. **`red-team-review` Gold Team (step 5c)** — checks that every ATO/IL/FedRAMP/CMMC claim carries an
   evidence-ledger cite, that SWP efforts answer the MVP/MVCR cadence, that Navy efforts address RAISE
   2.0 edge-ConMon, and that costed responses meet the GAO-20-195G bar. ✅
4. **`proposal-storyboard`** — reads this catalog and adds an **Acquisition Anchor** field per section,
   so RAISE 2.0 edge-ConMon and the ≤1-year MVCR commitment surface as section-level discriminators. ✅

Re-verify dates/IDs in this file before each bid cycle; the OMB-AI-memo and CC-SRG lines move fastest.

**Local source PDFs:** `reference/doctrine/500087p.pdf` (DoDI 5000.87) ·
`reference/doctrine/RAISE2.0ImplementationGuide1Nov2022.pdf` (RAISE 2.0).
