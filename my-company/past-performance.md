# Past Performance

**Source-of-truth rule.** `my-company/evidence-ledger.json` is authoritative for evidence IDs and for
what each item supports. This file is the human-readable narrative layer over it. When drafting, cite
the ID from the ledger.

> **Do not cite deployment evidence IDs from `edgerunner-profile.md` Section 6.** That table still
> maps EV-001 through EV-005 to Army and SOF deployments. Those IDs became U.S. Space Force order
> items in the 2026-07-24 ledger rebuild, and the mapping was never re-pointed. The IDs resolve, so
> `/evidence-check` passes them silently. Use the tables below or the ledger directly.
> *(Corrected here 2026-08-20; the profile table's EV column is corrected in the same pass.)*

## The distinction that governs this whole file

Confirmed by Bill 2026-08-20: **the Army and SOF deployments were not performed under any contract
vehicle. They are unsolicited, unfunded pilots.** That does not make them less real, and it does not
make them unusable. It makes them a different *kind* of evidence, and the difference is load-bearing.

| Category | What it is | What it can be offered as | What we hold |
|---|---|---|---|
| **Contracted past performance** | Work performed for the Government under a contract, order, or agreement with a number, a value, and a period of performance | A past-performance reference. Answers a scored PP factor. Supports a PPQ and CPARS lookup | **U.S. Space Force Order FA701426P0009** (documented, Section 5). **Navy ICOP / PMW 120** (real, undocumented here) |
| **Relevant experience / operational adoption** | Real fielded use with real units, at our own expense | Technical maturity (TRL), operational validation, user adoption, mission credibility, letters of support | **All Army and SOF deployments** (Section 1) |
| **Research agreements** | CRADAs and research collaborations | A research relationship and technical pedigree. Generally **not** a past-performance reference | AFRL, ARL, NIWC Atlantic (Section 4) |

> **The rule.** Never present a Section 1 deployment as past performance, as a contract, or in a
> past-performance volume, PPQ, or CPARS-referenced list. Present it as what it is: an unfunded pilot
> that a named unit chose to adopt and use operationally. Framed honestly it is persuasive evidence
> that units adopt this without being told to, which is something most competitors cannot say. Framed
> as a contract it is a finding.
>
> **When a solicitation scores past performance, we field one documented reference: a $23,000 Space
> Force order.** That is the real constraint, and it is a capture problem rather than a drafting one.
> See Section 6.

---

## 1. Operational Deployments — Army and Special Operations (Unfunded Pilots)

**None of the engagements in this section was performed under a contract vehicle.** They are
unsolicited pilots executed at EdgeRunner's expense. Read the rule above before drafting from this
table. The "Offer it as" column is the safe framing for each row.

| Customer / Unit | What EdgeRunner did | Status | Evidence | Offer it as | PP reference? |
|---|---|---|---|---|---|
| **USASOC** (1st, 7th, 10th SFG) | On-device AI fielded with mission-specific model adapters, including **Combat Medic** (TCCC guidance, injury triage, medevac COA generation, fully local) and **Logistician** (offline sustainment planning, contested-logistics COA). A custom-trained model answers unconventional-warfare queries that trip commercial model guardrails, reported 100% answer rate on that query set | Operational, TRL 8 | EV-099, EV-108, EV-059, EV-042 | Operational validation of mission-specific adapters in a SOF environment; TRL 8. USASOC naming subject to the public-release rule in EV-099 | **No — unfunded pilot** |
| **101st Airborne Division** | Deployed at **JRTC Rotation 26-06**. Used by staff in Tactical Operations Centers on laptops. Reported effect: MDMP staff processes and doctrinal research that previously took multiple days completed in a day or less | Deployed (exercise) | EV-107 | Operational validation under exercise conditions, with a measured staff-process outcome. The strongest adoption evidence we hold | **No — unfunded pilot** |
| **4th Infantry Division, 1st Stryker Brigade Combat Team** | Shortened maintenance work timelines by ingesting existing Power BI maintenance data on device, providing a single pane of glass plus a local assistant for planning and reporting | Deployed | EV-109 | Integration with existing Government data (Power BI) on device; sustainment use case | **No — unfunded pilot** |
| **4th Infantry Division** (NGC2) | First conventional-force deployment, under the Army's Next Generation Command and Control effort | Deployed, TRL 8 | EV-099 | First conventional-force adoption; TRL 8 | **No — unfunded pilot** |
| **101st Infantry Brigade** | Operational deployment | Operational, TRL 8 | EV-099 | Operational adoption; TRL 8 | **No — unfunded pilot** |
| **25th Infantry Division** (NGC2) | Participation under Army NGC2, in addition to the 4th ID activity | Engagement shape, vehicle, dates and POC **pending fact request F7** | EV-122 (*proof strength: low*) | Participation only. **Make no outcome claim** | **No — unfunded pilot** |
| **44th Medical Brigade** | In-corps adoption of on-device AI within a XVIII Airborne Corps subordinate unit | Engagement | EV-106 | Unit-level adoption. Frame as a **subordinate-unit engagement, not a corps-headquarters endorsement** | **No — unfunded pilot** |
| **Army intelligence community** | IDX26 SIGINT White Paper submitted February 2026 under Army contract **W91RUS26SFTHU** | Submitted / active engagement | EV-080 (*medium*) | A submission, not a deployment. Active Army IC engagement | **Verify.** The ledger records Army contract **W91RUS26SFTHU**. Confirm whether the white paper was submitted under that vehicle before treating it as contracted work |
| *One further SOF engagement* | Pilot | Active | EV-061 | **RESTRICTED — Government distribution only, Distribution B or more restrictive. Do not cite in public or broad-distribution documents without vetting** | **No — unfunded pilot** |

### Drop-in narratives

**Place these under a "Relevant Experience," "Operational Adoption," or "Technical Maturity" heading.
Never under "Past Performance."** Both are written to describe fielded use without implying a
contract. If a solicitation offers only a past-performance section and no relevant-experience
section, either put them in the technical volume as maturity evidence or add one sentence making the
basis explicit: *"These deployments were conducted at EdgeRunner's expense as unfunded pilots at the
invitation of the receiving unit."* That sentence costs nothing and forecloses the question.

#### Conventional force

> EdgeRunner's on-device capability is in operational use across conventional Army formations.
> EdgeRunner was deployed with the 101st Airborne Division at Joint Readiness Training Center
> Rotation 26-06, used by staff in tactical operations centers on laptops, where staff processes
> within the Military Decision-Making Process and doctrinal research reported as taking multiple days
> were completed in a day or less. With the 4th Infantry Division 1st Stryker Brigade Combat Team,
> EdgeRunner shortened maintenance planning and reporting timelines by ingesting existing structured
> maintenance data on the device and providing a local assistant over it. EdgeRunner additionally
> participates in the Army's Next Generation Command and Control effort, including a first
> conventional-force deployment with the 4th Infantry Division.
> `<!-- evidence: EV-107, EV-109, EV-099 -->`

### Drop-in narrative — special operations

> United States Army Special Operations Command elements field EdgeRunner with mission-specific model
> adapters, including Combat Medic and Logistician adapters that support casualty care decision
> guidance and contested-logistics sustainment planning entirely offline. As part of that deployment
> EdgeRunner provided a custom-trained model that answers unconventional-warfare queries which
> commercial models decline to process, at a reported 100 percent answer rate on that query set.
> `<!-- evidence: EV-059, EV-042, EV-108, EV-099 -->`

---

## 2. Operational Deployments — Navy

| Customer | Program | What EdgeRunner did | Status | Evidence | Citable |
|---|---|---|---|---|---|
| **U.S. Navy — ICOP / PMW 120** (NIWC Atlantic) | Intelligence Carry-On Program | Fielded as a Navy program-of-record capability. On the Navy approved-applications list. Full IL-6 ATO expected October 2026 at ICOP deployment | Active, program of record, TRL 8 | EV-014 (*ledger status: restricted*) | **Conditional.** Describe the program-of-record deployment freely; name **PMW 120 only when the capture lead directs**. ICOP specifics are CUI-sensitive. **Never attribute the IL-6 IATT (EV-022) to this program** |

---

## 3. Active Contracts — Space Force

| Customer | Program | Description | Status | Contract Type |
|---|---|---|---|---|
| U.S. Space Force — SAF/SQ & SSC (contracting office: Air Force District of Washington, AFDW PK) | EdgeRunner ODIN deployment + SFSC AI agents (Order FA701426P0009) | Deploy the EdgeRunner ODIN platform into the Space Force IL5 environment (containerized to Azure ILZ) for SSC and SAF/SQ users; build a domain-specific Acquisitions model (SFSC agent); perform IL5 ATO integration and ongoing engineering support | Active (PoP 2026-03-23 → 2026-09-22) | Firm-Fixed-Price (commercial, FAR 52.212-4) via CDAO Tradewinds Solutions Marketplace |

Evidence: EV-001 (order), EV-002 (IL-5 deployment), EV-102 (accreditation-integration past
performance), EV-023 (active production contract via Tradewinds Direct Award), EV-005 (Awardable
status converted to an executed order). **EV-100 is a legacy duplicate of EV-002 — cite EV-002.**

**This is the only fully documented reference in the file.** Full PPQ format at Section 5.

---

## 4. Research Agreements and Partnerships

| Partner | Agreement | Status | Evidence | Note |
|---|---|---|---|---|
| **Air Force Research Laboratory**, Information Directorate (AFRL/RI) | CRADA **25-0005284-AFRL/RI**, "Dark Saber and NIPRGPT Edge Domain Specific Generative AI". Consortium with Defense Unicorns. Authority 15 USC 3710a | **Term question — see below** | EV-121, EV-010 | 12 months from an effective date around the Air Force signature of 17 Dec 2024 / approval 6 Jan 2025. **No modification or extension is on file.** Confirm currency before describing it as active in any Government submission |
| **Army Research Laboratory** | CRADA with Joint Work Statement — AI agents for drones, robotics, computer vision | Active | EV-123, EV-011 | |
| **NIWC Atlantic** | Research collaboration | Active | EV-012 | Distinct from the Navy ICOP program. **Do not use EV-012 to substantiate ICOP claims** |
| **U.S. Space Force** | Research collaboration, transitioned to an active production contract | Transitioned | EV-013 → EV-023 | |
| **CDAO Tradewinds Solutions Marketplace** | Awardable status, executed against via FA701426P0009 | Active | EV-020, EV-005 | |
| **Lockheed Martin** | Mystic Depot teaming agreement (DIU) | Active | — | **Unrelated to NGC2.** Do not combine the two in one sentence |
| **BigBear.ai** | Mystic Depot teaming agreement (DIU) | Active | — | |

---

## 5. PPQ Reference — U.S. Space Force (Order FA701426P0009)

**Reference title:** EdgeRunner ODIN Platform Deployment & SFSC AI Agents — U.S. Space Force (SAF/SQ)

| Field | Value |
|-------|-------|
| Contract / Order number | **FA701426P0009** (DD Form 1155 delivery/purchase order) |
| Requisition / PR number | F3LFTE6076A001 |
| Date of order | 2026-03-23 (created 2026-03-20) |
| Customer (end user) | U.S. Space Force — SAF/SQ (Office of Acquisition & Integration) and Space Systems Command (SSC); place of performance / inspection & acceptance: USSF OCSO, 1670 Air Force Pentagon, Washington, DC (DoDAAC F4KF01) |
| Contracting / issuing office | Air Force District of Washington (AFDW PK), 1500 W Perimeter Rd Ste 5750, Joint Base Andrews, MD 20762 (DoDAAC FA7014) |
| Contract vehicle | CDAO Tradewinds Solutions Marketplace |
| Contract type / pricing | Firm-Fixed-Price; commercial (FAR 52.212-4); NTE on travel CLIN |
| Total value | **$23,000.00** (CLIN 0001 ODIN license $20,000; CLIN 0005 travel $3,000 NTE; CLINs 0002–0004 not separately priced) |
| Period of performance | **2026-03-23 to 2026-09-22** (6 months) |
| NAICS / Size std | 513210 (Software Publishers) / $47.0M annual receipts — small business |
| PSC | 7A21 (IT & Telecom — business application/software) |
| CAGE / UEI | 9Z176 / SLZTJUA8DBD3 |
| Contracting Officer (POC) | Robert G. Warren III, Division Chief & Contracting Officer — robert.warren.13@us.af.mil, (240) 612-6178 |
| Contract Specialist | Gwendolyn Campbell — gwendolyn.campbell.1.ctr@us.af.mil, (240) 612-6777 |
| Contractor signatory | David Anderson, Head of Partnerships, EdgeRunner AI, Inc. |
| Payment office | DFAS Columbus (DoDAAC F03000); WAWF electronic invoicing |

**Scope of work (by CLIN):**
- **CLIN 0001 — EdgeRunner ODIN Software License.** Unlimited licenses during the 6-month period of performance for SSC and SAF/SQ users. Deployed as a containerized solution into the Azure IL5 (Azure ILZ) environment. *(FFP, $20,000, funded.)*
- **CLIN 0002 — EdgeRunner Acquisitions-Specific Model.** Domain-specific model built to spec by EdgeRunner research to perform for a specified domain and environment (Space Force acquisitions / SFSC use case), deployed within the ODIN solution for all licensed users. *(FFP, not separately priced.)*
- **CLIN 0003 — Integration & IL5 ATO Support.** Up-front development to bring the solution into a new environment, including engineering support for IL5 ATO requirements. *(FFP, not separately priced.)*
- **CLIN 0004 — Ongoing Support.** Ongoing EdgeRunner engineering to keep the solution operational. *(FFP, not separately priced.)*
- **CLIN 0005 — Travel.** Kickoff meetings to review system requirements and ensure personnel are trained for use. *(FFP NTE, $3,000, funded.)*

**Relevance highlights for future bids:**
- First documented U.S. Space Force production deployment of EdgeRunner's on-device platform.
- Real IL5 deployment + ATO integration into a new accredited government environment — converts the "IL5 roadmap" claim into delivered past performance.
- Built-to-spec, mission-specific model specialization delivered under contract (not a demo).
- Executed through CDAO Tradewinds — proof the Awardable status converts to awarded, performed work.

**POC handling note:** The Government POCs above are past-performance reference contacts. Cite them only in past-performance questionnaires / volumes submitted to Government evaluators — do not publish in commercial or marketing materials.

---

## 6. Past-performance posture, and what would change it

**The honest position.** Against a solicitation that scores past performance, EdgeRunner can offer:

| Offerable today | Value | Note |
|---|---|---|
| U.S. Space Force Order FA701426P0009 | $23,000 | Fully documented, Section 5. Small in dollars, strong in content: IL-5 accreditation integration, built-to-spec model, delivered under FFP |
| Navy ICOP / PMW 120 | not held here | Real and significant, but no contract number, value, PoP, or POC is on file. Not offerable as a reference until documented |

That is the whole list. Everything in Section 1 is operational evidence, not contract performance. This is a
**capture-posture problem, not a drafting problem**, and no amount of careful wording fixes it.

**What it means in practice:**

- On a solicitation with a **scored past-performance factor** and a dollar-magnitude or
  similarity-of-scope test, we will rate Neutral or Limited Confidence on our own. Plan for it:
  either team with a prime carrying the reference weight, or target vehicles and pathways where past
  performance is not the discriminator.
- On **SBIR, BAA, CSO, OTA, and unsolicited** pathways, relevant experience and technical maturity
  are usually what is actually asked for. Our Section 1 evidence is strong there, and TRL 8 operational
  adoption by named units is a genuinely good answer.
- The Section 1 deployments are still **the most persuasive material we own** for any evaluator asking
  whether this works in the field. Units adopted it without a contract obliging them to. Say that
  plainly; it is a stronger signal than a small contract would be.

**Three things that would move the posture, in order of leverage:**

1. **Document the Navy ICOP engagement.** It is the only other real contract relationship. Contract
   or agreement number, value, PoP, and a Government POC would roughly double our offerable
   references and add a program-of-record reference at TRL 8. Owner: capture lead.
2. **Convert one pilot into a funded follow-on.** A single small order against any of the units in
   Section 1 turns a pilot into contract performance and gives us a second reference with real mission
   scope. The 101st Airborne JRTC result and the 4th ID sustainment result are the two with a
   measured outcome to build a follow-on around.
3. **Collect letters of appreciation or support** from the Section 1 units. These are not past-performance
   references and must never be presented as such, but they are legitimate, citable corroboration
   that the adoption and the reported outcomes are real, and they are obtainable now at no cost.
   Owner: Dave Anderson.

**One open verification:** the IDX26 SIGINT white paper (EV-080) is recorded against Army contract
W91RUS26SFTHU. Confirm whether that was a submission under someone else's vehicle or work we
performed under contract. If the latter, it is a second offerable reference and should be documented
in PPQ format alongside Section 5.

---

## 7. Past Performance Summary

EdgeRunner AI holds a current, named U.S. Space Force production engagement (Order FA701426P0009)
deploying its on-device ODIN platform into an IL5 accredited environment and building Space Force
Specialty Code (SFSC)-specific AI agents, including an acquisitions agent for SAF/SQ. The work
demonstrates operational maturity across the full delivery path: IL5 ATO integration into a new
government environment, containerized deployment to Azure ILZ, mission-specific model specialization
built to spec, and sustained engineering support, executed as a commercial firm-fixed-price order
through the CDAO Tradewinds Solutions Marketplace.

That contract sits alongside a Navy program-of-record capability at TRL 8, and federal research
relationships with AFRL and ARL that support the underlying model and agent work.

Separately from contract performance, EdgeRunner's capability has been adopted operationally by Army
special operations and conventional formations — USASOC with mission-specific adapters, the 101st
Airborne Division at Joint Readiness Training Center Rotation 26-06, the 4th Infantry Division under
NGC2 and in sustainment, and a XVIII Airborne Corps subordinate unit. **These were unfunded pilots
conducted at EdgeRunner's expense, not contract performance**, and they are offered as evidence of
operational maturity and user adoption rather than as past-performance references. That distinction
is worth stating openly rather than eliding: units chose to field this without a contract obliging
them to, and several reported measured improvements while doing so.
