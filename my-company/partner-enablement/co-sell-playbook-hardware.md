# Co-Sell Playbook — Hardware Integrators & Silicon Partners
**EdgeRunner AI joint-motion guide for HP, AMD, Panasonic, Intel, Akamai — and the cleared-prime pattern (Lockheed Martin, BigBear.ai, Armada, Anduril, Safran Federal Systems).**
[CONFIRM: Armada, Anduril, Safran Federal Systems are not yet logged in `my-company/evidence-ledger.json`. References below assume the partnerships are in place; remove or restate before publishing externally.]

**Distribution Statement C** · Distribution authorized to U.S. Government agencies and their contractors; Administrative/Operational Use; 2026-05-07.
**Audience:** Partner BD / channel manager + partner SE.
**Length:** ~5 pages including the joint-pursuit checklist tear-out.
**Version:** v2026-05-07.

---

## 1. The three patterns we co-sell with

EdgeRunner AI's federal motions don't fit a single channel template. Pick the pattern first; the rest of this playbook keys off it.

### Pattern A — Sub on payload (we ship inside your platform)

**The shape:** Your hardware (a ruggedized laptop, an edge server, a fly-away kit, a domain-specific appliance) is the customer-facing platform; EdgeRunner AI is the on-device AI runtime inside it. Customer sees one bill of materials; you are the prime relationship. We deliver the runtime, the military-tuned models, and the MOS/AFSC adapters as a software payload.

**When this fits:** HP ruggedized laptops (EV-050), Panasonic Toughbook-class (EV-051), Akamai distributed edge (EV-054), AMD/Intel reference designs at the edge (EV-052, EV-053), and any cleared-prime platform offering AI-on-edge (Armada / TitanCore [CONFIRM]; Anduril / NGC2 [CONFIRM]; Safran Federal Systems / NGA GrandCanyon [CONFIRM]).

**Customer perception:** "I'm buying [partner platform]. EdgeRunner is the AI capability that comes with it." Single procurement vehicle. Your contract.

### Pattern B — Joint co-sell (parallel software line item)

**The shape:** Your hardware is one line item; EdgeRunner AI is a separate, parallel software line item on the same opportunity. Customer can procure either alone; the *value* is in deploying them together. Joint discovery, joint demo, separate POs.

**When this fits:** AMD joint demo motion (e.g., a customer evaluating AMD MI-class silicon for AI inference and EdgeRunner for the runtime / model layer). HP joint hardware play where the customer wants line-item visibility. Lockheed Martin / BigBear.ai opportunities where both companies are named subs but procurement runs separately (Mystic Depot pattern, EV-055, EV-056).

**Customer perception:** "I'm buying [partner] *and* EdgeRunner. Two procurement actions, one operational outcome."

### Pattern C — Teaming on a competitive bid

**The shape:** A solicitation is open. Your company is the prime (or a different sub). EdgeRunner AI is named in the proposal as a teaming partner with a specific scope of work, written into the SOW. Award flows through the prime; we operate as a sub.

**When this fits:** AFRL JADPACT/MASH (EdgeRunner prime; subs are different shape — informational here only). DIU Mystic Depot CSO with Lockheed Martin and BigBear.ai (EV-055, EV-056). Project Maven / Project ARIA / NGC2 sub-positions on cleared primes [CONFIRM: each opportunity's prime relationship before naming].

**Customer perception:** "I awarded [prime]. EdgeRunner is named in their proposal." One contract, multiple companies on it.

---

## 2. RACI by phase

The phases and ownership patterns differ by motion. Use the table that matches your pattern.

### Pattern A — Sub on payload

| Phase | Lead | Support | Notes |
|---|---|---|---|
| Discovery | Partner BD | EdgeRunner BD | Partner owns the relationship; loops EdgeRunner in once edge-AI is in scope |
| Qualification | Partner BD | EdgeRunner BD + SE | Use the trigger-event guide; qualify against IL/clearance/hardware footprint fit |
| Demo | Joint | — | Partner SE owns hardware demo; EdgeRunner SE owns the AI capability portion. Single joint session preferred over two separate ones |
| Pricing | Partner | EdgeRunner provides software list / OEM pricing | Bill participates on first deal of each new motion |
| Proposal / Contract | Partner | EdgeRunner provides past-performance citations + capability brief | Use the proof-point library, evidence-ledger-cited |
| Deployment | Partner | EdgeRunner SE | EdgeRunner SE on the install for first deployment per partner; partner SE for subsequent |
| Renewal | Partner | EdgeRunner BD | EdgeRunner BD attends renewal QBR |

### Pattern B — Joint co-sell

| Phase | Lead | Support | Notes |
|---|---|---|---|
| Discovery | Either | The other | Whichever team finds the deal opens it for both; deal-registration step formalizes this |
| Qualification | Joint | — | Trigger-event guide on the partner side; evidence-ledger qualification on the EdgeRunner side |
| Demo | Joint | — | Two-act joint demo: partner hardware first, EdgeRunner runtime second, joint Q&A |
| Pricing | Each owns their line | The other reviews | Pricing alignment review before submission to customer |
| Proposal | Each owns their volume | Joint architecture diagram | Use shared architecture brief; cite each other's past performance only with permission |
| Contract | Each | — | Two procurement actions in customer's system; coordinate award timing |
| Deployment | Joint | — | Joint kickoff; partner-SE-led for hardware, EdgeRunner-SE-led for runtime |
| Renewal | Each | The other | Attend each other's renewals when joint solution is in production |

### Pattern C — Teaming on competitive bid

| Phase | Lead | Support | Notes |
|---|---|---|---|
| RFI / pre-RFP | Prime | All teammates | Prime decides team composition; EdgeRunner contributes capability brief and past-performance citations |
| Capture | Prime | EdgeRunner BD | Capture intent, ghosting strategy, win themes — prime owns; EdgeRunner contributes |
| Proposal | Prime | EdgeRunner authors named scope sections | EdgeRunner owns the scope-of-work it will execute, signed off by prime |
| Pricing | Prime aggregates | EdgeRunner provides line-item pricing | Pricing per `reference/pricing-artifacts/` template that matches the contract type |
| Award | Prime | EdgeRunner | Subcontract terms negotiated post-award |
| Performance | EdgeRunner on its scope | Prime PM | EdgeRunner reports to prime PM; prime reports to customer |

---

## 3. Deal registration

We're standing this up as a process, not a portal-driven workflow yet. As the channel scales we will move to a form (Pattern B is most affected); for now the protocol is:

**To register a deal:**
1. Email the EdgeRunner partner alias [CONFIRM: partner-deals@edgerunnerai.com or equivalent — Bill to confirm]
2. Include: customer name, program name, expected fiscal action, expected vehicle, your role, EdgeRunner role, expected timeline, IL level, key competitive context.
3. Acknowledgement within 1 business day. Registration is "active" once acknowledged.

**What registration provides:**
- 90-day exclusivity on EdgeRunner-side joint pursuit support for that customer/program. We will not engage another partner on the same opportunity during the window.
- Priority technical-SE allocation for the demo and proposal phases.
- Past-performance citation clearance in expedited form.

**What disqualifies:**
- The customer has an existing direct EdgeRunner engagement on the same program.
- Another partner registered the same opportunity earlier (we'll surface this in the acknowledgement).
- The opportunity has already been awarded.
- Information provided is materially incomplete (no IL level, no fiscal year, no role definition).

---

## 4. Compensation implications

[CONFIRM: this section is a placeholder. EdgeRunner AI does not have a published partner comp policy in the repo. Bill to provide canonical language before this playbook ships externally. Suggested fields below — replace with policy text once approved.]

- **Net-new vs. renewal credit treatment:** [CONFIRM]
- **Number-credit on a joint deal:** [CONFIRM]
- **Margin / discount stack:** [CONFIRM]
- **Spiff or accelerator program (if any):** [CONFIRM]

In the absence of a published policy, the working rule is: economics are negotiated per deal at registration, with the partner BD lead and EdgeRunner BD lead documenting the split in the registration acknowledgement.

---

## 5. Joint-pursuit checklist (the tear-out)

Print this as page 1 of the playbook. Walk it before the first joint customer meeting.

- [ ] **Pattern selected.** A (sub on payload) / B (joint co-sell) / C (teaming on competitive bid).
- [ ] **IL level confirmed.** Customer's required IL level is documented (IL-2, IL-4, IL-5, IL-6, on-prem only). EdgeRunner has IL-5 (USSF SSC) and IL-6 (Navy ICOP) ATOs in hand. Compatible? If not, we plan an ATO sprint with the customer's AO.
- [ ] **Hardware footprint fits.** 16GB VRAM recommended (8GB minimum for 4B model; 16GB for 20B/26B). Cross-OS (Windows / Linux / macOS). Hardware-agnostic silicon (Intel, AMD, NVIDIA). Customer's GFE or partner's platform meets this?
- [ ] **Timeline compatible.** Customer's required fielding date allows for runtime install + adapter delivery. 90-day fielding loop committed for SF (18-series) / PSYOP (37-series) / CA (38-series) adapters; existing five MOS adapters (Logistics / Combat Medic / Combat Arms / Acquisitions / Cyber) are operational today.
- [ ] **Past-performance citations cleared.** Which EV-references will appear in the proposal (e.g., USASOC EV-001/2/3/4, Navy ICOP EV-014, USSF Tradewinds CSO EV-023). Distribution markings reviewed.
- [ ] **Distribution markings agreed.** Statement A (public) / B (Government only) / C (Government + contractors) / D (DoD + DoD contractors) / F (directed only) / CUI//FEDCON. Header on every artifact.
- [ ] **Joint architecture diagram drafted.** Three-tier (enterprise → GCC → edge) topology, integration surface (OpenAI-compatible API), deployment mode (binary / container / web-hosted), and data flow including any return-to-GCC structured data.
- [ ] **Compliance posture artifacts ready.** Compliance & Accreditation One-Pager attached. Customer's ATO officer briefed.
- [ ] **Deal registered.** Email sent, acknowledgement received, 90-day window active.
- [ ] **POCs named.** Partner BD, partner SE, EdgeRunner BD, EdgeRunner SE — names + emails on a single line.
- [ ] **Pricing alignment.** Each side's pricing reviewed. Patterns A/B: line items align. Pattern C: subcontract pricing structure consistent with prime's response.
- [ ] **Risk / disqualifiers reviewed.** No conflicting registration, no IL incompatibility, no excluded models, no lapsed customer ATO, no clearance gap on customer site visits.

---

## 6. The first 30 days of a joint pursuit

A reference cadence for Patterns A and B. Pattern C runs against the prime's capture timeline.

**Week 1 — Discovery alignment**
- Joint discovery call with the customer. Partner SE + EdgeRunner SE both present.
- Partner SE asks the trigger-event questions (see *Trigger-Event Guide*, P1). EdgeRunner SE asks the qualifying technical questions: what hardware footprint, what IL level, what data classifications, what existing AI investments are in place, what's the operational tempo, what does "success" look like in 90 days.
- Output: a shared one-page customer-context summary with current architecture, target architecture, and EdgeRunner-relevant decision points.

**Week 2 — Joint solution shaping**
- EdgeRunner SE drafts a joint architecture diagram (using `graphic-templates/03-platform-architecture/`).
- Partner SE confirms hardware fit and any platform-specific constraints.
- Joint review with partner BD lead; edits before showing the customer.

**Week 3 — Joint demo**
- Two-act demo. Partner hardware in act one, EdgeRunner runtime + a relevant scenario in act two, joint Q&A in act three.
- Recommended scenarios (pick the one closest to the customer's mission): SOF intel summarization (USASOC pattern); NGC2-style C2 query (4th ID pattern); MOS-specific Q&A on a tactical task (Combat Arms / Combat Medic); refusal contrast vs. commercial model (MilDeflect demo).
- Output: a customer-shareable demo recording and a list of the customer's follow-up questions.

**Week 4 — Proposal artifact set**
- Joint architecture brief (PDF, distribution-marked).
- EdgeRunner past-performance citations (proof-point library, evidence-ledger-cited).
- Compliance & Accreditation One-Pager attached.
- Pricing artifact per pattern (line item, separate proposals, or sub on the prime).
- Joint-pursuit checklist re-walked; any open items flagged for resolution before submission.

---

## 7. Escalation contacts

| Function | Contact | Channel |
|---|---|---|
| Partner deals registration | [CONFIRM: partner-deals alias] | Email |
| Partner BD lead | [CONFIRM: name + email] | Email + Slack |
| Partner SE lead | [CONFIRM: name + email] | Email + Slack |
| Past-performance / proposal support | [CONFIRM: contact — likely Bill or designated proposal lead] | Email |
| Security / accreditation | [CONFIRM: cyber lead] | Email; CUI-marked threads only |
| Executive escalation | [CONFIRM: CEO / Founder — likely Tyler Saltsman per `published-research.md` author lists, role unconfirmed] | Direct email; reserved for stuck deals or partnership-policy questions |

---

## 8. Appendix — pattern-specific notes per named partner

[CONFIRM: each partner block below should be reviewed and customized by Bill before being sent to that specific partner. The structure is canonical; the per-partner specifics need confirmation against the evidence ledger and any partner-specific MoUs.]

### HP (EV-050)
- Pattern: A (sub on payload) and B (joint co-sell). Ruggedized laptop platforms fielded across the Department of War. EdgeRunner runtime is engineered for HP ruggedized hardware.
- Joint motion: customer asks for AI on an HP ZBook / EliteBook ruggedized — EdgeRunner is the runtime answer.

### AMD (EV-052)
- Pattern: B (joint co-sell). x86 silicon at the edge.
- Joint motion: AMD joint demo with EdgeRunner runtime on AMD-powered platforms; customer evaluates inference performance on AMD silicon vs. alternatives.

### Panasonic (EV-051)
- Pattern: A (sub on payload). Toughbook-class ruggedized laptops.
- Joint motion: same shape as HP; tactical-laptop deployments with the runtime as software payload.

### Intel (EV-053)
- Pattern: B (joint co-sell). x86 silicon at the edge; complement to AMD motion when the customer is Intel-platform.

### Akamai (EV-054)
- Pattern: A (sub on payload) for distributed edge infrastructure use cases. Defense integrator relationship — Akamai operates as integrator/infrastructure for defense workloads.
- Joint motion: customer wants distributed edge inference with multi-domain (IL-2 through IL-6) compatibility; EdgeRunner runtime is hosted on Akamai distributed-edge infrastructure.

### Lockheed Martin (EV-055)
- Pattern: C (teaming on competitive bid). Active teaming on Mystic Depot CSO. Provides large-prime integration capability and access to defense program-of-record customers.
- Joint motion: cleared-prime opportunities where Lockheed is prime and EdgeRunner is named sub for the AI / TEVV / adversarial-testing scope.

### BigBear.ai (EV-056)
- Pattern: C (teaming on competitive bid). Active teaming on Mystic Depot CSO. AI / decision-intelligence integration.
- Joint motion: opportunities where decision-intelligence + on-device AI runtime are both required; BigBear.ai prime, EdgeRunner sub.

### Armada (TitanCore prime) — [CONFIRM]
- Pattern: A (sub on payload) suspected. Armada as prime on TitanCore platform; EdgeRunner as on-device AI software payload.
- [CONFIRM: scope of partnership, nature of software payload role, contract vehicle, timeline.]

### Anduril (NGC2 sub) — [CONFIRM]
- Pattern: C (teaming on competitive bid) suspected. Anduril as a sub or prime in NGC2; EdgeRunner as an AI runtime sub or software payload.
- [CONFIRM: NGC2 program structure, who-is-prime, EdgeRunner's named scope.]

### Safran Federal Systems (NGA GrandCanyon) — [CONFIRM]
- Pattern: A (sub on payload) or C (teaming) — depends on the GrandCanyon program structure.
- [CONFIRM: NGA GrandCanyon scope, contract vehicle, role assignments.]

### WebAI — [CONFIRM]
- [CONFIRM: scope of partnership being scoped per Bill's notes. Not in evidence ledger.]

---

*Source: every claim above traces to `my-company/evidence-ledger.json` where evidence-ledger IDs (EV-NNN) are noted. Partner roster items not yet logged in the ledger are marked [CONFIRM] and must be resolved before publishing externally. Distribution-statement compliance: this document is marked Statement C; do not redistribute to commercial / non-cleared parties without remarking.*
