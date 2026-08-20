# Contracting Paths — Internal BD Guide

**INTERNAL USE ONLY. Do not send to customers.** The customer-facing version is
[`contracting-paths-leave-behind.md`](contracting-paths-leave-behind.md).

Purpose: stop losing funded work because nobody opened a contracting path before the funding
decision. Written after the FY27 ACC/BDA loss, where ACC funded a vendor that already had a
contract in place while we were six months into a 128-day BAA path.

---

## 1. Ask these four questions in every first meeting

This is the whole point of the document. Everything else is reference.

1. **Whose money is it?** The office that wants the capability is often not the office that holds
   the funds. AFRL wanted the BDA work; ACC held the money. We optimized the wrong customer.
2. **What color and what year?** See Section 2. This determines what they can legally buy and how
   long they have to spend it.
3. **Which contracting office supports you, and who is the contracting officer?** Get a name. A
   program manager cannot put you on contract and will usually overestimate how long it takes.
4. **Do you already have a contract or vehicle we could ride?** Theirs, a sister office's, or a
   prime already performing for them. This is the fastest path in existence and almost nobody
   volunteers it.

If you get no further than these four questions in a first meeting, the meeting was a success.

## 2. Color of money, in sixty seconds

Federal funds are not fungible. Using the wrong appropriation is a violation, so a contracting
officer will refuse rather than improvise.

| Appropriation | What it buys | Available for |
|---|---|---|
| **3600 RDT&E** | Research, development, test, prototypes. Budget Activity 6.1 basic, 6.2 applied, 6.3 advanced, 6.4 demo. | 2 years |
| **3400 O&M** | Operations, sustainment, services, software subscriptions, training | 1 year |
| **3080 Procurement** | Production quantities, fielded systems | 3 years |

Two consequences worth internalizing:

- **O&M expires at the end of the fiscal year.** Every August and September there is 3400 money
  looking for a home. Ask for it explicitly.
- **6.2 applied research money cannot buy licenses, and O&M cannot fund research.** When a customer
  says "I have money," the follow-up is always "what color."

AFRL's guidance to us in January named the target precisely: PE# 62788F, 3600 funds, Budget
Activity 6.2. That was a real constraint, not a stall.

## 3. The paths

Timelines are realistic ranges from "customer decides" to "we can start work." The dominant
variable is almost always the customer's contracting office workload, not the instrument.

| Path | Who can use it | What it can buy | What it cannot buy | Realistic timeline |
|---|---|---|---|---|
| **CDAO Tradewinds** (we hold Awardable status) | Any DoD component | AI/ML capability, services, prototypes. CSO-based direct award, competition requirements already satisfied, no further competition needed | Non-AI scope. Civilian agencies | 30 to 90 days |
| **Ride an existing contract** (theirs or a sister office's) | Anyone with a vehicle and in-scope work | Anything within the existing statement of work and ceiling | Anything out of scope. See the CICA trap in Section 5 | Days to weeks. **Fastest path that exists** |
| **Subcontract to an incumbent prime** | Any prime already performing | Whatever the prime's scope covers | Nothing, if the prime says no. This is their decision, not the government's | 2 to 8 weeks. See Section 6 |
| **Component CSO** (e.g. ACC/AMIC, AFWERX) | The issuing component | Innovative commercial solutions against a published area of interest. 10 U.S.C. 3458. Direct award | Scope outside the published AOI | 60 to 120 days |
| **SEWP** (via Carahsoft as distributor, Gov't Acquisitions Inc. as VAR) | Any federal agency | Software licenses, hardware, and closely associated product services: install, config, training, maintenance | **Research. Custom development. Standalone services.** SEWP is a products vehicle | 2 to 6 weeks once a quote is in hand |
| **Simplified acquisition / commercial items** | Any contracting officer | Commercial products and services. Micro-purchase at $10K, simplified acquisition threshold at $250K, FAR 13.5 commercial procedures well above that | Anything requiring full development | 2 to 6 weeks. Genuinely fast under the SAT |
| **Prototype OT** | Components with OT authority, directly or through a consortium | Prototypes. 10 U.S.C. 4022. Carries a **4022(f) sole-source follow-on production award**, which is the strategic prize | Sustainment or production without first completing a prototype | 1 to 4 months, faster inside a consortium |
| **SBIR/STTR Phase III** | Any agency, if we hold prior SBIR/STTR work | Anything deriving from the earlier SBIR work. **Sole source, no competition, no dollar ceiling** | Applies only if we hold qualifying prior SBIR/STTR. **Confirm whether we do** | 30 to 90 days. Largest single unlock if we qualify |
| **BAA** (e.g. AFRL AFAR) | The issuing lab | Basic and applied research, on the lab's topics and timeline | Speed | AFRL told us **128 days** from white paper to contract, plus the funding wait |
| **CRADA** | Federal laboratories only | Their personnel, facilities, equipment, data, and 5-year data protection under 15 U.S.C. 3710a(c)(7)(B) | **Money. A CRADA legally cannot pay us** (15 U.S.C. 3710a(d)(1)) | Months to execute, and it produces no revenue |

## 4. Which one do I ask for

- Customer wants **software, licenses, or devices** and has O&M → SEWP through Carahsoft or GAI.
- Customer wants **AI capability or services** and is DoD → Tradewinds direct award. Lead here.
- Customer is an **Air Force or ACC organization** → ask whether their component CSO covers it
  before assuming a lab BAA is the only route.
- Customer's money is **under $250K** → simplified acquisition, commercial items. Weeks.
- Customer wants **research and has 6.2 money next fiscal year** → BAA or prototype OT. Slow.
  Start now and manage expectations.
- **Someone else already holds the contract** → subcontract. Fastest, lowest margin.
- Customer wants to **collaborate but has no money** → CRADA or bailment. Understand that this is
  relationship investment, not revenue.
- **It is August or September and they have expiring O&M** → simplified acquisition or Tradewinds.
  Move immediately.

## 5. Traps

**The "$1 contract" does not work.** You cannot park a nominal contract and add money later.
Loading substantial new work onto it is an out-of-scope modification, which is a competition
violation under CICA, and a contracting officer will refuse it. What actually holds a place open:
an IDIQ with a nominal guaranteed minimum and a real ceiling, a BPA or BOA with pre-negotiated
rates, a prototype OT with priced option CLINs, or standing pre-qualification like Tradewinds
awardable status. Ask for "an instrument with a ceiling and priced options."

**Do not oversell SEWP.** We are not a SEWP prime. Our products ride resellers' contracts. SEWP is
a products vehicle and cannot fund research or standalone services. Saying "we're on SEWP" to a
customer who needs R&D wastes their time and costs us credibility when their CO says no.

**A CRADA is not a funding path.** It cannot transfer money to us in either direction except
company to lab. Useful for access, data, and IP protection. Never cite it as a contract.

**Never overstate accreditation.** Verified and sayable: active IL-6 IATT, IL-5 ATO with the Space
Force. Not held and never claimable: FedRAMP, SOC 2, ISO 27001, and any "full ATO" phrasing. A
partner asked the Navy for reciprocity in June and got told we did not hold what our press release
claimed. That cost us more than any contract vehicle would have earned.

**The government generally will not direct a prime to use us.** See Section 6.

## 6. Teaming and subcontracting, realistically

A BAA does not have "primes" in the integrator sense. Each BAA award is a separate contract to a
separate performer for that performer's own proposed scope. There is no large integrator with
subcontract slots to fill, which changes how teaming works.

**What a government PM can do:**

- Make an informal introduction to an awardee once the award is public.
- Point us at an industry day, proposers' day, or published teaming list.
- Encourage teaming in general terms.

**What they cannot do:**

- Direct a prime to subcontract to us. Subcontractor selection is the prime's decision.
- Share proposal content, pricing, or source-selection information. Procurement Integrity Act,
  41 U.S.C. 2101 to 2107.
- Steer work while a related procurement is still open.

**What we can do without asking anyone:** award data is public. Contract actions above the
micro-purchase reporting threshold appear in FPDS and USAspending, and BAA selections are usually
announced. Look the awardee up first, then ask for a warm introduction to a specific company
rather than a general "who won."

**Timing is the real lesson.** For BAAs, teaming has to happen *before* submission, because each
awardee's scope is fixed by its own proposal. Adding us after award requires the prime to want us,
a contract modification, and government consent to subcontract. That is a slow, low-leverage path.
Get on a team before the white paper goes in, not after the award comes out.

## 7. "They have money but only use their own vehicles." Now what?

This is the most common blocker we hit, and subcontracting is not the only answer. Options, roughly
in order of how often they work.

**First, test the premise.** "We only use our own vehicles" is almost always a workload and
preference statement, not a legal constraint. A contracting officer *can* buy from us directly if
someone wants it badly enough. The question to ask is not "can you?" but "**what would it take?**"

### Ways in that are not subcontracting

**1. Reseller or distributor, which is not the same as being a sub.** For product sales this is the
single most underrated path. The government buys EdgeRunner licenses through Carahsoft's or
Government Acquisitions Inc.'s contract. We are the named manufacturer, it is our product being
bought, we keep the customer relationship, and we give up only a modest reseller margin rather than
a prime's fee and G&A on our labor. **Treat this as close to a direct sale, not as teaming.** It
only works for products and closely associated services, not research.

**2. Sole source with a Justification and Approval.** Under FAR 6.302 a contracting officer can
award without competition. The bases we would realistically use are 6.302-1 (only one responsible
source, meaning a genuinely unique capability) and 6.302-2 (unusual and compelling urgency). Below
the simplified acquisition threshold this is much lighter, since FAR 13 permits soliciting a single
source with far less documentation. **Our job is to make it easy to say yes:** hand the customer a
written technical justification their CO can lift, naming what is unique and why an alternative
will not meet the requirement. Most companies ask for a sole source and never supply the paperwork
that would let one happen.

**3. Join a vehicle they already use.** Many instruments have on-ramps.
   - **GSA Multiple Award Schedule is continuously open to new offers.** Anyone can apply at any
     time. It takes months, but it is permanent and it answers "we buy off GSA" forever.
   - **OT consortia** accept members on a rolling basis, usually cheaply and quickly, and
     membership gives access to a vehicle the government is already using.
   - GWACs like SEWP recompete periodically. Track the windows.

**4. Assisted acquisition.** If the blocker is that *their* contracting shop is slow, they can send
the money to a contracting shop that is fast. Under the Economy Act, or through GSA's assisted
acquisition services, the customer keeps the requirement and the funds but borrows another agency's
contracting capacity, including shops that can buy off SEWP or GSA MAS where we already sit. This
solves the exact problem of "we have money and no path" without asking their CO to do anything new.

**5. SBIR/STTR Phase III.** Congress designed Phase III precisely for this problem. A Phase III
award may be **sole source, by any agency, at any dollar value, with no further competition**, if
the work derives from earlier SBIR or STTR work. It is the purpose-built answer to "we have money
but no vehicle." **We still have not confirmed whether EdgeRunner holds any qualifying prior SBIR
or STTR award.** If we do not, winning one becomes strategically valuable less for its own dollars
than as a permanent sole-source on-ramp to every other agency.

**6. A CSO the customer already has access to.** Tradewinds is DoD-wide. When a DoD customer says
"our own vehicles," Tradewinds may already be one of theirs and they may not know it. Say so.

### The strategic conclusion

**Vehicles are a standing asset, not a per-deal problem.** The pattern that keeps costing us is
arriving at a funded requirement with no place to put the money, then trying to solve it inside
that deal's timeline. It never works, because every path above takes longer than the customer's
patience.

The fix is to hold the vehicles before the requirement appears. Concretely, in priority order:

1. **Resolve the SBIR question.** Highest leverage on this list, and it is a one-question answer.
2. **Pursue GSA MAS if we do not hold it.** Continuously open, months to obtain, permanent once
   held.
3. **Join the OT consortia** covering our mission areas.
4. **Use Tradewinds far more aggressively.** We hold it, it is DoD-wide, and it is underused.
5. **Keep the reseller path warm** for every product sale, and stop describing it as teaming.

## 8. What EdgeRunner already holds

Confirm current status before citing any of these to a customer.

- **CDAO Tradewinds** Awardable status. Strongest genuine direct-award path for DoD AI work.
- **SEWP** through Carahsoft (distributor) and Gov't Acquisitions Inc. (VAR). *Confirm V vs VI
  transition status with the resellers before quoting.*
- **ITES-SW2** through resellers. Army software vehicle. Not usable by the Air Force.
- **CRADAs** with AFRL and ARL, plus an ARL Joint Work Statement. Research partnerships with AI2C
  and NIWC Atlantic. Not funding paths.
- **USSF** on contract.
- **SBIR/STTR history: unconfirmed.** Somebody needs to answer this. If we hold any qualifying
  prior award, Phase III is the single most powerful instrument on this list.
- Identifiers: CAGE 9Z176, UEI SLZTJUA8DBD3, primary NAICS 541511.
