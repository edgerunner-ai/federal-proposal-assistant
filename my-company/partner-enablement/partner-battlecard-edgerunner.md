# EdgeRunner AI — Partner Battlecard

**Distribution Statement A** · Approved for public release; distribution unlimited.
**Audience:** Partner sales / BD. Read in 2 minutes; carry in your back pocket.
**Version:** v2026-05-07 · CAGE 9Z176 · UEI SLZTJUA8DBD3

---

## What we are, in 30 seconds

EdgeRunner AI provides on-device AI execution, agentic workflows, and operational data capture for disconnected tactical environments. Our platform runs military-tuned open-weight LLMs — fully air-gapped — on government laptops, fly-away kits, edge servers, ATAK devices, and Toughbook-class hardware. We turn real-world operator use into structured training-ready data and feed it back to the GCC and enterprise tiers. We are the **operational layer** that connects enterprise AI investments to warfighters at the edge.

> If a customer says "we need this to work without the network," that is a partner-trigger to bring us in.

---

## Three things that make us different

| Differentiator | One-line proof | Source |
|---|---|---|
| **GPT-5 parity at the edge** | EdgeRunner 20B matches or exceeds GPT-5 on military tasks at 95%+ statistical significance — published research (arXiv), on-device, no cloud. | Paper: *EdgeRunner 20B*, `published-research.md` · EV-031 |
| **Refusal problem solved** | Commercial LLMs refuse up to 98.2% of legitimate military queries. MilDeflect (published research, arXiv) eliminates this — 66.5-point answer-rate gain with 2% average regression on other tasks. | Paper: *MilDeflect*, `published-research.md` · EV-030 |
| **DDIL by design, not by retrofit** | Zero cloud, zero telemetry, zero licensing callback. The platform is engineered for Denied / Disrupted / Intermittent / Limited operation as the operating assumption. | `capabilities.md` §Secure Deployment · EV-040, EV-044 |

---

## Three proof points to lead with

| Customer / program | What it proves |
|---|---|
| **USASOC** — 1st, 7th, and 10th Special Forces Groups, plus JFK Special Warfare Center & School | Operational at the tip of the spear. Multi-SFG breadth, not a single pilot. EV-001, EV-002, EV-003, EV-004. |
| **U.S. Navy ICOP** (NIWC Atlantic / PMW 120) — IL-6 ATO granted, on Navy approved-applications list | Navy production substantiation at IL-6. The ATO is from the ICOP Authorizing Official; per-AO posture, but the credibility of an IL-6 grant remains. EV-014, EV-022. |
| **U.S. Space Force** — active production contract via TradeWinds CSO Direct Award | Closed contract under a CSO Direct Award vehicle, transitioned from prior research collaboration. Distinct from CDAO Tradewinds Marketplace Awardable status. EV-013, EV-023. |

Plus: **4th Infantry Division** (NGC2) for conventional-force scale (EV-005); **AFRL CRADA** and **ARL JWS** for research depth (EV-010, EV-011); two published papers (arXiv) as research-velocity evidence (EV-030, EV-031).

---

## When to bring us in

A federal customer says any of these — bring EdgeRunner AI into the conversation:

- "We need AI on the **edge** / on a **laptop** / on a **boat** / **forward-deployed** / **without internet**."
- "We can't send our data to the cloud" / "it has to stay on the enclave" / "it has to run in the SCIF."
- "Commercial GPT keeps refusing the questions our analysts actually need to ask."
- "We want a tactical model that knows our **MOS** / **AFSC** / domain doctrine."
- "We need to feed operator usage back into model improvement, but our data can't leave the GCC."
- "We need to deploy on a **GFE laptop** / **Toughbook** / **fly-away kit** / **ATAK** device."
- The integration target is **OpenAI-compatible API** — drop-in replacement for cloud OpenAI / Azure OpenAI calls.
- The customer is a **JADC2** / NGC2 program, a SOF unit, or an IC analytic shop with DDIL operational tempo.

---

## When NOT to bring us in

- Pure-cloud, IL-2 unclassified web-app workloads where commercial GPT does the job and there is no edge or enclave constraint.
- The customer has no edge hardware footprint and no plans to acquire one — we are not a hardware play, we are the runtime.
- The deal is *only* about a model-training pipeline that lives in a hyperscaler GovCloud and never touches an operator endpoint. (We can complement it; we are not the headline.)
- The customer has explicitly forbidden open-weight models in their environment. (Rare, but it happens — usually a misunderstanding of open-weight vs. open-source. Worth a clarifying conversation before disqualifying.)

---

## Top 3 objections and responses

**1. "EdgeRunner AI is a small company. Can you support us at scale?"**
We are a small business by SBA size standard, founded 2024, $17.5M raised. We are *already* at scale on the missions that count: deployed across three Special Forces Groups, the SWCS schoolhouse, the 4th Infantry Division, the Navy ICOP program, and a USSF production contract. Procurement-ready via CDAO Tradewinds Marketplace (Awardable) and Tradewinds CSO (Direct Award). The right question isn't "are they big enough" — it's "are they fielded where my mission lives." We are.

**2. "We already have Azure OpenAI / Bedrock / a hyperscaler LLM. Why do we need this?"**
Two reasons. First, those services don't run when the network doesn't — and the missions you care about increasingly happen in DDIL conditions. Second, commercial LLMs refuse up to 98.2% of legitimate military queries, per published research (EV-030). We *complement* hyperscaler enterprise AI; we don't replace it. We are the operational layer that lets the same data and models reach the warfighter at the edge.

**3. "Why not just use a commercial open-weight model directly?"**
You can run a base open-weight model — but you'll inherit the refusal problem (98%+ on legitimate military queries), you won't have MOS/AFSC specialization (we ship five production adapters today: Logistics, Combat Medic, Combat Arms, Acquisitions, Cyber), you won't have an authorized inference runtime with an IL-5 / IL-6 ATO posture, and you won't have a structured operational-data feedback loop. EdgeRunner AI is what turns an open-weight model into a fielded military capability.

---

## Procurement footer

```
EdgeRunner AI · Bellevue WA · Founded 2024
CAGE 9Z176 · UEI SLZTJUA8DBD3 · NAICS 541511 · SAM.gov Active
CDAO Tradewinds Marketplace: Awardable · Tradewinds CSO: Direct Award holder (USSF)
ATOs in hand: IL-5 (USSF SSC) · IL-6 (Navy ICOP / NIWC Atlantic)
```

> An ATO is granted by an Authorizing Official for a specific program. EdgeRunner has been ATO'd at IL-5 and IL-6 by federal AOs; that evidences the application's compliance posture and security architecture, not blanket cross-command authority. Each new program writes its own ATO package — we provide the artifacts.

---

## Who to contact at EdgeRunner

| Need | Who | When to ping |
|---|---|---|
| Joint deal qualification / pursuit | Partner BD lead [CONFIRM: name + email] | Before the customer call |
| Technical SE / architecture review | Partner SE lead [CONFIRM: name + email] | Before a technical demo |
| Past-performance citation clearance | Bill / proposal lead [CONFIRM: contact] | Before any RFI/RFP that names EdgeRunner past performance |
| Security / accreditation questions | [CONFIRM: cyber lead] | When the customer's ATO officer engages |

---

## What's in the partner kit alongside this card

- **Compliance & Accreditation One-Pager** — the "can your buyer say yes" doc.
- **Co-Sell Playbook for Hardware Integrators** — RACI, deal registration, joint-pursuit checklist.
- **Solution Architecture Brief** *(coming P1)* — three-tier topology + integration surface.
- **Demo recording + script** *(coming P1)*.
- **Proof-Point Library** *(coming P1)* — pre-cleared past-performance citations with evidence-ledger IDs.

---

*Source: every claim above traces to `my-company/evidence-ledger.json`. If a fact cannot be cited by ID, it does not appear here. Items still requiring source confirmation are marked [CONFIRM]. Cleared partner-internal version available with EV-061 (JSOC) on request — Distribution B+ environments only.*
