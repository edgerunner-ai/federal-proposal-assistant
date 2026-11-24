---
name: opportunity-quick-look
description: Use this skill to rapidly vet a new opportunity before committing to full proposal analysis. Produces a one-page triage report covering opportunity fit, funded/unfunded status, size/scope, customer alignment, and go/no-go signal. Reads the solicitation from inputs/00_priority/ and inputs/01_customer/, and assesses fit against the company capability register in my-company/evidence-ledger.json rather than against a hardcoded list of past work. Writes to working/quick-look.md.
phase: capture
composes: [ledger-harvest]  # consumes the company capability/application/expertise register that ledger-harvest maintains; still runs cold on the solicitation itself
conflicts_with: [capture-scorecard]  # this is raw-solicitation triage; once proposal-manager has run, use capture-scorecard
---

# Opportunity Quick Look Skill

## Purpose
A 5–10 minute triage that tells you whether an opportunity is worth pursuing before investing in full capture analysis. This is not a technical review. It is a business-sense filter — does the shape of this opportunity fit your company's profile, capacity, and priorities?

Run this first. Kill bad opportunities fast. Save full analysis for the ones that pass.

## When to Use
- A new solicitation, BAA, CSO, or white paper task drops
- You need a rapid fit assessment before briefing leadership on a new opportunity
- You are evaluating multiple opportunities in parallel and need to prioritize
- You are unsure whether to invest in `/proposal-manager` and downstream analysis

## What This Skill Does NOT Do
- Build a capability matrix (that's `/proposal-solution-architect`)
- Analyze evaluation criteria in depth (that's `/proposal-manager`)
- Assess capture readiness (that's `/capture-scorecard`)
- Research the customer in depth (that's `/customer-intel`)

---

## Inputs

Read only what exists. Do not ask for files that aren't there yet — work with what's available.

1. `inputs/00_priority/` — solicitation, BAA, CSO, white paper task, RFI (any available)
2. `inputs/01_customer/` — customer context, mission notes, any prior intel
3. **`my-company/evidence-ledger.json` — the company capability register.** Read it every time. See below.

If the first two folders have no content, ask the user to paste or describe the opportunity before proceeding. A URL, email, or paragraph description is sufficient to run this skill.

### Reading the ledger for triage

Structure and record classes are defined in `docs/CAPABILITY-LEDGER-STRUCTURE-2026-08-27.md`. Four classes matter here, and **triage reads all of them at every `evidentiary_tier`**:

| Class | Prefix | What it tells triage |
|---|---|---|
| `capability` | `CAP-##` | What we can actually do, and at what maturity |
| `application` | `APP-###` | Missions and customers our capabilities have been, or could be, pointed at |
| `expertise` | `EXP-##` | Which customer and mission spaces we have people who know |
| `evidence` | `EV-###` | What we could prove if we bid |

**This is the one place in the workspace that deliberately reads `designed` and `adjacent` records as first-class.** A concept paper that was never built, or a capability that plainly transfers to a mission we have never served, is a legitimate reason to look harder at an opportunity. It is *not* a reason to claim experience — see the Rules.

**Why this matters more than it looks.** Before 2026-08-27 this skill scored Mission Fit against a hardcoded list of early use cases (edge AI, DDIL, chatbots) and Customer Fit against a hardcoded list of early customers (Army, USAF, SOCOM). That encoded our history as our boundary and quietly filtered out everything in the Department and the IC we had not yet served. Reading the register instead means the boundary moves as the company does.

If the ledger is missing or has no `capability` records, fall back to `my-company/capabilities.md` and say so in the output.

---

## The 8 Quick Look Factors

Assess each factor on a **GREEN / YELLOW / RED** basis. Keep each assessment to 1–2 sentences. This is judgment, not deep research.

### 1. Mission Fit
Does the stated requirement map to capabilities we hold?

**Assess against `capability` records, not against a list of past use-cases.** Name the specific `CAP-##` records the requirement would exercise. Then check `application` records for whether this mission problem, or one structurally like it, already has a mapping — at any tier.

| Signal | Assessment |
|--------|-----------|
| 🟢 | Maps cleanly to one or more `CAP-##` records at `Fielded` or `Proven` maturity, and the requirement is the kind of problem those capabilities address |
| 🟡 | Maps to capabilities at `Built`, `Demonstrated`, or `Proof-of-concept` maturity; **or** maps to mature capabilities but through an `application` we have only `designed` or judged `adjacent` — the capability transfers, the mission is new to us |
| 🔴 | No `CAP-##` record covers the core of the requirement, and none plausibly transfers. Hardware-only, facilities, logistics, non-AI services |

A 🟡 here is a normal and healthy result for a mission space we have not served. It means "new application of a real capability," which is exactly the class of opportunity the register exists to surface. Do not treat unfamiliarity as a weakness — treat an absent capability as one.

Name the maturity label from the record (`Fielded` / `Proven` / `Built` / `Demonstrated` / `Proof-of-concept`) rather than inventing a looser one.

### 2. Customer Fit
Can we credibly reach this customer?

**Assess against `expertise` records first, then relationship evidence.** Credibility with an unfamiliar customer usually comes from a person who knows that space, not from prior contracts in it.

| Signal | Assessment |
|--------|-----------|
| 🟢 | An `EXP-##` record covers this customer or mission space at real depth and is current; **or** we hold `contracted` evidence with this customer |
| 🟡 | No direct expertise record, but an adjacent one applies (same Service, related mission, shared acquisition pathway); **or** we have `demonstrated` work with this customer that is not contracted |
| 🔴 | No expertise, no relationship, no adjacent record — **and** no realistic route to one before the response is due. Or a stated incumbent preference, or an OCI |

**Do not score 🔴 merely because the customer is unfamiliar.** The Department and the IC are the whole addressable space; an unserved customer with a matching capability and a person who knows the domain is a 🟡, not a 🔴. Reserve 🔴 for a customer we have no credible route into at all.

If no `expertise` records exist yet, say so in the output rather than guessing — that gap is itself worth surfacing.

### 3. Funding Status
Is there money behind this, and is it real?

| Signal | Assessment |
|--------|-----------|
| 🟢 | Funded: contract type specified, CLIN structure present, ceiling value stated, award expected within 12 months |
| 🟡 | Partially funded or TBD: BAA with flexible ceilings, OTA with task order structure, funding subject to congressional action |
| 🔴 | Unfunded: white paper only (no follow-on stated), exploratory RFI with no solicitation planned, budget not identified |

**Note:** Unfunded (RED) is not automatically a no-go — some white papers and BAAs are strategic positioning plays. Flag it and let the user decide.

### 4. Size and Scope Fit
Is the contract size and work scope a match for a small company?

| Signal | Assessment |
|--------|-----------|
| 🟢 | $500K–$10M, clear set-aside (SBIR, 8(a), small business), or explicitly structured for small business participation |
| 🟡 | $10M–$50M — possible as sub or in a strong team; limited set-aside language; scope may exceed current capacity without partners |
| 🔴 | $50M+ unrestricted, large integrator territory, or requires facilities/clearances/capacity your company does not have and cannot acquire for this effort |

### 5. Schedule Fit
Can we respond in time and execute if we win?

| Signal | Assessment |
|--------|-----------|
| 🟢 | Response deadline 3+ weeks out; performance period aligns to current bandwidth; no unusual mobilization requirements |
| 🟡 | Response deadline 1–3 weeks out (tight but possible); performance start is immediate with unclear ramp time |
| 🔴 | Response deadline under 1 week; requires personnel or resources you cannot staff by award; OR no deadline stated and unclear when solicitation will formalize |

### 6. Competitive Position
Do we have a credible reason to win this — and can we *prove* it?

This is where the `evidentiary_tier` gate bites. Factors 1 and 2 may read across the whole register; this one asks what survives contact with an evaluator.

| Signal | Assessment |
|--------|-----------|
| 🟢 | A discriminating capability backed by `contracted` or `measured` evidence that fits the requirement; or prior relationship; or a set-aside with limited competition |
| 🟡 | Capability match is real but the supporting evidence is `demonstrated` only, or the field is unknown, or the match is reasonable but undifferentiated |
| 🔴 | Strong incumbent with years of performance; large-prime territory entered as an unknown sub; **or** every supporting record is `designed` or `adjacent`, meaning we would be bidding on a capability we cannot yet evidence |

**The trap this catches:** an opportunity can score 🟢 on Mission Fit because a capability genuinely transfers, and still be a poor bid because nothing we could cite proves it. Count the citable evidence separately from the capability match, and say plainly in the Bottom Line when the two diverge.

### 7. Common Sense Barriers
Are there any immediate disqualifiers — legal, ethical, logistical, or strategic?

Examples to check:
- Clearance requirements you cannot meet by award
- Organizational conflict of interest (OCI) with existing work
- Work scope that conflicts with your ethics or customer commitments
- Geographic or facility requirements (SCIF, specific installation)
- Teaming restrictions that exclude you
- Explicitly prohibited from small business participation

| Signal | Assessment |
|--------|-----------|
| 🟢 | No significant barriers identified |
| 🟡 | One barrier exists but is resolvable (e.g., clearance can be sponsored, facility can be leased) |
| 🔴 | Hard barrier that cannot be resolved in time — disqualifying |

### 8. Submission Mechanism
Where does the proposal physically go, and is the submission format fully knowable right now?

This factor exists to catch the failure mode we learned the expensive way on NATO DIANA: the *opportunity* is visible on the public site, but the *submission format* (section labels, hard character/word limits, metadata fields) is hidden behind portal registration. Drafting starts on assumptions; the real limits surface late; 40% of the token/time budget goes to compression and restructure.

Identify the submission mechanism and act accordingly:

| Mechanism | Signal | What it means |
|--------|-----------|---------|
| **Email to CO / POC** | 🟢 | Attach what the solicitation asks for. Format authority = the solicitation. Proceed normally. |
| **SAM.gov or agency PDF upload** | 🟢 | Format authority = Section L of the solicitation. `/proposal-manager` extracts it reliably. Proceed normally. |
| **Portal you already have an account on, format viewable** | 🟢 | Note the portal name and any surprising limits; proceed. |
| **Agency portal requiring registration before format is visible** | 🟡 | **STOP drafting.** Register first, then run `/capture-portal-structure`. |
| **Third-party challenge platform (DIANA, Challenge.gov, Valid Evaluation, AFWERX Open Topic, xTech, NSIN)** | 🟡 | **STOP drafting.** Register first, then run `/capture-portal-structure`. If the portal already has an entry in `reference/portal-formats/`, that skill inherits it — fast. |
| **Unknown — can't tell from the solicitation where it goes** | 🔴 | Do not start any drafting work until resolved. Email the POC if needed. |

**Why 🟡 (not 🔴) for registration-gated portals:** these are often the highest-pWin opportunities (DIU, DIANA, AFWERX), so they are *worth pursuing* — the issue is sequencing, not fit. The yellow signals the user to register and capture format *before* `/proposal-manager`, not to pass on the opportunity.

A 🔴 here is reserved for genuinely unknowable submission mechanics (rare — usually a POC call resolves it in 5 minutes).

---

## Output Format

Write the following to `working/quick-look.md`. Always write to disk — do not just display in chat.

```markdown
# Opportunity Quick Look — [Opportunity Name]
**Date:** [today]
**Source:** [BAA / CSO / RFP / RFI / White Paper Task / Other]
**Program:** [Program name or "Unknown"]
**Customer:** [Agency / Command / Program Office]
**Ceiling Value:** [$ if known, or "Not stated"]
**Response Deadline:** [Date or "Not stated"]
**Contract Type:** [SBIR / OTA / IDIQ / FFP / Cost / Unknown]

---

## Quick Look Scorecard

| # | Factor | Status | Assessment |
|---|--------|--------|------------|
| 1 | Mission Fit | 🟢/🟡/🔴 | [1–2 sentences] |
| 2 | Customer Fit | 🟢/🟡/🔴 | [1–2 sentences] |
| 3 | Funding Status | 🟢/🟡/🔴 | [1–2 sentences] |
| 4 | Size and Scope Fit | 🟢/🟡/🔴 | [1–2 sentences] |
| 5 | Schedule Fit | 🟢/🟡/🔴 | [1–2 sentences] |
| 6 | Competitive Position | 🟢/🟡/🔴 | [1–2 sentences] |
| 7 | Common Sense Barriers | 🟢/🟡/🔴 | [1–2 sentences] |
| 8 | Submission Mechanism | 🟢/🟡/🔴 | [email / document-upload / web-form + portal name if known + whether registration required] |

**Score:** X Green / X Yellow / X Red

---

## Capability and Evidence Basis

What in the register this read rests on. Cite record IDs so the next person can check the reasoning
rather than re-deriving it.

**Capabilities exercised**

| Record | Capability | Maturity | How the requirement uses it |
|---|---|---|---|
| CAP-## | [name] | [Fielded / Proven / Built / Demonstrated / Proof-of-concept] | [one line] |

**Applications** — prior or conceptual mappings to this mission problem

| Record | Application | Tier | Relevance |
|---|---|---|---|
| APP-### | [name] | [contracted / measured / demonstrated / designed / adjacent] | [one line] |

**Expertise** — who gives us credibility with this customer

| Record | Person | Space | Depth / currency |
|---|---|---|---|
| EXP-## | [name] | [customer or mission space] | [one line] |

**Citable evidence if we bid** — `contracted`, `measured`, or `demonstrated` only

| Record | Summary | Tier |
|---|---|---|
| EV-### | [summary] | [tier] |

**Register gaps this surfaced:** [capabilities, applications, or expertise the opportunity implies we should hold but that have no record — or "none". This list is a feed for `/ledger-harvest`.]

---

## Bottom Line
[2–3 sentences: what kind of opportunity is this, why it does or doesn't fit, and what the single biggest risk or opportunity is]

## Recommendation
**[PURSUE / PASS / HOLD]**

- **PURSUE** — Fits well enough to invest in `/proposal-manager` and downstream analysis. At least 5 Green, no Red in Mission Fit, Customer Fit, or Common Sense Barriers. If Factor 8 is 🟡 (registration-gated portal), PURSUE still applies — but the first action is `/capture-portal-structure`, not `/proposal-manager`.
- **PASS** — Does not fit. Do not invest further unless circumstances change.
- **HOLD** — Interesting but missing information or a resolvable barrier. Identify what needs to happen before re-evaluating. Also use HOLD when Factor 8 is 🔴 (submission mechanism genuinely unknown) — hold until a POC call or portal page resolves the question.

[1–2 sentence rationale]

## If PURSUE: Recommended Next Steps
1. [First action — e.g., run `/proposal-manager` to extract eval criteria and page limits]
2. [Second action — e.g., check clearance requirement with security officer before proceeding]
3. [Third action — e.g., identify teaming partner for [specific gap] before kickoff]

## If HOLD: What Would Change This
- [Condition 1 — e.g., "Confirm funding is in FY26 POM before investing"]
- [Condition 2 — e.g., "Wait for draft RFP to confirm small business set-aside"]
```

---

## Rules
- Do not invent funding, clearance, or customer details — state "not stated" if unknown
- An unfunded opportunity is not automatically a PASS — some are worth strategic positioning
- A single RED in Mission Fit, Customer Fit, or Common Sense Barriers is normally a PASS unless there is an explicit strategic reason to override
- Keep all factor assessments to 1–2 sentences — this is a triage, not an analysis
- If key information is absent, default to YELLOW with a note on what's missing
- Do not run this skill and then immediately pivot to full analysis in the same session — let the user confirm PURSUE before proceeding

### Ledger rules
- **Cite record IDs, do not paraphrase the register.** "CAP-03 at Built maturity" is checkable; "we do orchestration" is not.
- **Never invent a record.** If the capability is not in the register, the honest finding is that we do not hold it — log it under Register gaps.
- **`designed` and `adjacent` records justify interest, never experience.** They may raise Mission Fit; they may not raise Competitive Position, and nothing sourced from them may be described as work we have performed. This distinction is the whole reason the tiers exist.
- **Use the register's maturity vocabulary verbatim** — `Fielded`, `Proven`, `Built`, `Demonstrated`, `Proof-of-concept`. Do not upgrade a label.
- **Respect the standing honesty constraints** carried on the records: the IL-6 posture is an IATT and not an ATO and is not attributed to a named unit; no FedRAMP, SOC 2, or ISO 27001; unfunded pilots are relevant experience and never past performance; no TRL is claimed for Ground Truth.
- **Unfamiliar is not unfit.** An unserved customer plus a matching capability plus a person who knows the space is a 🟡. Reserve 🔴 for the absence of a capability or of any route to the customer.
- **Surface register gaps every run.** They are how the register learns, and they feed `/ledger-harvest`.

---

## After Running This Skill
Tell the user:
1. Score (X Green / X Yellow / X Red)
2. Recommendation (PURSUE / PASS / HOLD) with one-sentence rationale
3. If PURSUE with Factor 8 🟢: confirm they want to proceed to `/proposal-manager` before starting
4. If PURSUE with Factor 8 🟡 (registration-gated web-form portal): tell them to register for the portal first, then run `/capture-portal-structure` — `/proposal-manager` comes after portal format is captured
5. If HOLD with Factor 8 🔴: tell them what needs to resolve (POC call, portal page visit, etc.) before the mechanism is knowable

---

## Lessons Learned

### On Unfunded Opportunities
DARPA BAAs, DIU CSOs, and SOCOM white paper tasks are often "unfunded" at the quick-look stage but represent genuine pipeline. Do not reflexively score these RED on funding — look for language about follow-on contracts, transition pathways, or OTA authority. Flag it YELLOW with a note.

### On Schedule
The highest-risk response failures come from underestimating proposal burden on a compressed timeline, not from capability gaps. If the deadline is under 2 weeks and the proposal requires more than 10 pages, flag schedule RED regardless of other factors.

### On Scope Creep in Requirements
Watch for requirements that look like your lane but contain embedded scope that isn't — e.g., "AI analytics with full system integration and facility build-out." The AI portion may fit; the rest may not. Flag this in Common Sense Barriers rather than failing Mission Fit entirely.

### On the register replacing hardcoded fit lists (2026-08-27)
This skill previously scored Mission Fit against a fixed list of early use-cases and Customer Fit against a fixed list of early customers. Both were accurate descriptions of where EdgeRunner had been and both were wrong as filters, because they made the company's history its boundary. Any opportunity outside chatbot/DDIL for Army, USAF, or SOCOM scored down on shape alone, regardless of whether the underlying capability transferred.

The register fixes this only if it is read the way it is meant to be. The failure mode to avoid now is the opposite one: reading `designed` and `adjacent` records as though they were experience, and producing a PURSUE on an opportunity we cannot evidence. Factors 1 and 2 read wide; Factor 6 reads strict. When they disagree, say so — "capability fits, evidence does not yet" is a genuinely useful triage result and usually points at a teaming decision rather than a pass.

### On a thin register
An empty or thin register produces cautious triage, not wrong triage. If `expertise` records do not exist, say Customer Fit could not be assessed from the register rather than defaulting to the old hardcoded assumptions. Surfacing that gap is more valuable than guessing around it.
