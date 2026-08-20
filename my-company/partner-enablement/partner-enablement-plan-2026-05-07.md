# EdgeRunner AI — Partner & Reseller Enablement Plan
**Date:** 2026-05-07
**Owner:** Bill (with EdgeRunner AI partner team)
**Scope:** Federal/defense channel only. Direct-sale enablement is out of scope.
**Maintained alongside:** `my-company/edgerunner-profile-2026-05-08.md`, `my-company/evidence-ledger.json`

---

## 1. Why this plan exists

EdgeRunner AI's federal channel is a mix of patterns that look nothing like a SaaS reseller motion:

- **Sub-on-payload to a hardware integrator** (HP joint hardware play; the Armada / TitanCore prime pattern; the Safran Federal Systems / NGA GrandCanyon pattern). [CONFIRM: Armada and Safran relationships not yet in `my-company/evidence-ledger.json`. HP is logged as EV-050 — commercial OEM only — not as a co-sell partner. Bill to confirm scope before any of these are referenced in partner-facing material.]
- **Software co-sell with silicon/OEM partners** (HP, AMD, Intel, Panasonic). EV-050 through EV-053. AMD joint demo and HP joint hardware play map here.
- **Teaming partner on a competitive bid** (Lockheed Martin and BigBear.ai on Mystic Depot — EV-055 / EV-056 — and Anduril on NGC2; the latter is not in the ledger and needs confirmation).
- **Sub on cleared-prime program work** (Project Maven, Project ARIA, NIWC NGC2, DIU prototypes). [CONFIRM: Anduril NGC2 sub role, Project Maven and Project ARIA partner mappings.]

Three things follow from the pattern:

1. **The partner field doesn't pitch us cold** — partners discover us through a customer ask, an integrator conversation, or a teaming RFI. Enablement has to make us easy to *position, qualify, and pull in*, not easy to prospect.
2. **Federal deals die on accreditation, not features** — the IL-5 / IL-6 ATO posture, NIST RMF alignment, distribution-statement handling, and CAC integration are the questions that close or kill a deal, and partner reps need to be able to answer those without calling us.
3. **Voice and provenance matter** — claims about deployments (USASOC, 4th ID NGC2, Navy ICOP, USSF Tradewinds CSO Direct Award) carry real weight in a federal evaluation, and a partner repeating a fabricated claim is a credibility blast radius event. Every enablement asset must trace to `my-company/evidence-ledger.json`.

---

## 2. Inventory of what exists today

| Asset | Path | Use for partner enablement |
|---|---|---|
| Consolidated company profile (the one-stop fact sheet) | `my-company/edgerunner-profile-2026-05-08.md` | Source-of-truth for every battlecard, brief, and one-pager |
| Capability detail | `my-company/capabilities.md` | Source for technical solution briefs |
| Components & services table | `my-company/components-table.md` | Source for product-level talk tracks |
| Past-performance table | `my-company/past-performance.md` | Source for proof-point citations |
| Published research (MilDeflect, EdgeRunner 20B) | `my-company/published-research.md` + PDFs in `my-company/capability-papers/` | High-credibility differentiator evidence; printable PDFs already exist |
| Distribution statements | `my-company/distribution-statements.md` | Required header on every partner-shared brief |
| Brand design system | `my-company/branding/brand-design-system.md`, `brand-palette.md` | Voice and visuals for any new asset |
| Evidence ledger | `my-company/evidence-ledger.json` | The "is this fact citeable?" check for every claim |
| Reusable graphic templates | `my-company/graphic-templates/*` | Architecture, customer-map, deployment-spectrum, comparison templates |
| Past-proposal write-ups | `my-company/past-proposals/jadpact-mash-baa-2026/`, `mystic-depot-cso-2026/` | Mineable for proof points and joint-pursuit storyboards |
| Product PDFs | `my-company/capability-papers/edgerunner-20b/EdgeRunner_20B.pdf`, `mil-deflect/mil_deflect.pdf` | Already partner-shareable as discriminator evidence |
| Logo + colors | `my-company/branding/edgerunner-logo.png`, `colors_and_type.css` | Co-branded layout consistency |

### What does *not* exist (the gap inventory)

- **No `my-company/partnerships.md`.** EV-050 through EV-056 cite this file; the file does not exist on disk. This is the single most consequential gap because it means the canonical statement of "who our partners are and what each one does with us" is scattered across the ledger only.
- **No partner-facing assets at all.** No battlecards, no one-pagers, no co-sell playbooks, no demo scripts, no objection handling, no FAQs, no certification path, no recorded demos, no joint-pursuit checklists, no deal registration template. The partner channel is currently being run from emails and slide decks built per-partner.
- **No accreditation summary as a stand-alone artifact.** Accreditation language is buried inside `capabilities.md` §Secure Deployment & IL Architecture and inside the consolidated profile §4. A partner SE asking "can your buyer say yes" needs a one-pager, not an archaeological dig through internal docs.
- **No War Claw source brief.** [CONFIRM: customer, scope, status, contract type, role, period of performance. Zero source content in repo as of 2026-05-08.]
- **`past-performance.md` is out of sync with the ledger.** Navy ICOP (EV-014), IL-6 ATO (EV-022), and the USSF Tradewinds CSO Direct Award (EV-023) were added to the ledger 2026-05-05 but have not propagated into the human-readable past-performance file. Any partner asset built off `past-performance.md` alone will *understate* current proof.

---

## 3. Prioritized category list

Twelve categories, ranked. Don't ship more than three at once — partners ignore a content dump and use it to delay calling you. Four shipped well beats twelve shipped sloppily.

### P0 — ship this month

#### P0-1. Partner Battlecard (1-page)

| Field | Value |
|---|---|
| **Audience** | Partner sales rep, partner BD lead. Not a technical role. |
| **Problem it solves** | "I need to know in 30 seconds what EdgeRunner AI is, when to mention them in front of a federal customer, and when *not* to." |
| **Format** | 1-page PDF (front and back acceptable). Markdown source, exported to docx → PDF for distribution. |
| **Length** | 1 page. Hard cap. |
| **Delivery vehicle** | PDF in partner portal, attached to first partner email, embedded in QBR deck appendix. |
| **Refresh cadence** | Quarterly, or after any IL-level / contract-vehicle change. |

**Content outline:**
1. **Who we are in one sentence.** ("EdgeRunner AI provides on-device AI execution, agentic workflows, and operational data capture for disconnected tactical environments.")
2. **Top 3 differentiators with proof.** Each differentiator is a one-line claim plus one line of evidence-ledger-grade proof (e.g., "GPT-5 parity at the edge — published research (arXiv), 95%+ statistical significance, EV-031").
3. **Top 3 proof points.** Real customer logos: USASOC (1st/7th/10th SFG + JFK SWCS), 4th ID NGC2, Navy ICOP / IL-6 ATO, USSF Tradewinds CSO Direct Award. EV-001 through EV-023.
4. **When to bring us in.** Trigger-event language — air-gap requirement, DDIL operational tempo, refusal/safety-tuning failure, edge LLM compute, MOS-specific specialization.
5. **When NOT to bring us in.** Pure-cloud SaaS LLM use cases, OCONUS commercial cloud, problems where the customer has no edge hardware footprint, IL-2 unclassified web-app workloads where commercial GPT does the job.
6. **Top 3 objections and responses.** ("You're a small company" / "We already have Azure OpenAI" / "Why not just use a commercial open model directly").
7. **Procurement footer.** CAGE / UEI / NAICS / Tradewinds Awardable / IL-5 ATO / IL-6 ATO via Navy ICOP / SAM.gov active.

**Voice:** No buzzwords. Sentence case headlines. Banned words list applies (`brand-design-system.md` §10).

---

#### P0-2. Co-Sell Playbook for Hardware Integrators (4–6 pages)

| Field | Value |
|---|---|
| **Audience** | Partner BD / channel manager + partner SE at HP, AMD, Panasonic, Intel — and the same role at Armada, Anduril, Safran Federal Systems, Lockheed Martin, BigBear.ai when EdgeRunner is the software payload on their hardware/integration platform. [CONFIRM: Armada, Anduril, Safran roles before naming.] |
| **Problem it solves** | "We have a customer asking for AI on the edge of our hardware. How does the joint motion actually work — who owns what, how is the deal registered, what's the comp impact for my rep, and what do we put in front of the customer first?" |
| **Format** | 4–6 page PDF, markdown source. Includes a one-page joint-pursuit checklist as a tear-out. |
| **Delivery vehicle** | Reviewed live in a 30-minute joint-team kickoff with each named partner; PDF is the leave-behind. Hosted in a partner-shared Notion or Box folder per partnership. |
| **Refresh cadence** | Per-partner customization quarterly; master template revised when comp model changes. |

**Content outline:**
1. **Pattern selection.** Three named patterns — *sub on payload* (we ship inside their platform), *joint co-sell* (we are a parallel software line item to their hardware), *teaming on a competitive bid* (we are a named subcontractor in their proposal). One paragraph each on when each applies.
2. **RACI by phase.** Discovery → Qualification → Demo → Pricing → Proposal/Contract → Deployment → Renewal. Who-leads / who-supports for each phase by pattern.
3. **Deal registration.** What constitutes a registered joint deal, how to register (form link or email-to address), what protection registration provides, and what disqualifies a registration.
4. **Compensation implications.** Whose number gets credit on a joint deal. Net-new vs. renewal treatment. (Bill: this section needs your input — current comp policy is not in the repo.) [CONFIRM: comp policy.]
5. **Joint-pursuit checklist (the tear-out).** 12 yes/no items: Is the customer's IL requirement compatible? Is there a hardware footprint that fits 16GB VRAM? Is the timeline compatible with a 90-day fielding loop? Is past performance citation cleared? Are distribution markings agreed? Has a joint architecture diagram been drafted? Etc.
6. **First 30 days.** What the partner SE should ask the customer in week 1, what we will provide in week 2, what the joint demo looks like in week 3, what the proposal artifact set looks like in week 4.
7. **Escalation contacts.** Named EdgeRunner POCs by function (BD, SE, contracts).

**Voice:** Direct, RACI-style. Use tables for ownership; prose only where context is needed.

---

#### P0-3. Compliance & Accreditation One-Pager (1–2 pages)

| Field | Value |
|---|---|
| **Audience** | Partner SE *and* the customer's contracting / cyber officer. The doc is dual-use: a partner SE answers questions with it; the partner can hand the same PDF to the customer. |
| **Problem it solves** | "Can our buyer actually say yes to this software? What is the security posture, what ATOs are in hand, what compliance artifacts can we provide, and what does it take to deploy on a customer enclave?" |
| **Format** | 1-page front (the summary table), 1-page back (the detail / FAQ). PDF, markdown source. CUI/FEDCON marking optional based on detail level. |
| **Delivery vehicle** | Linked from the battlecard. Required attachment in any RFI/RFP response a partner submits with us. Mirrored as the "Compliance" tab in the partner portal. |
| **Refresh cadence** | Whenever any ATO grant, renewal, or scope change occurs. **High-stakes accuracy** — every claim must trace to the evidence ledger by ID. |

**Content outline (front):**
- Security model summary (air-gapped, on-device, no cloud telemetry, no licensing callback).
- Authorities-to-Operate: IL-5 (USSF SSC), IL-6 (Navy ICOP / NIWC Atlantic). Plain-English framing of what a per-program ATO does and does not transfer to a new command.
- RMF posture: NIST AI RMF flywheel architecture; traceable, auditable outputs; local data control.
- Identity / network: CAC-enabled access; cross-domain deployment patterns supported.
- Distribution markings: Statement A through F + CUI/FEDCON usage guidance.
- Procurement vehicles: CDAO Tradewinds Marketplace (Awardable) + Tradewinds CSO (Direct Award holder, USSF).
- Identifiers: CAGE 9Z176, UEI SLZTJUA8DBD3, NAICS 541511, SAM.gov active.

**Content outline (back / FAQ):**
- "Is the IL-6 ATO transferable to my command?" (No — each AO issues their own. The ATO is evidence of compliance posture and architecture, not blanket cross-command authority. EV-022.)
- "What about FedRAMP / SOC 2 / ISO 27001 / CMMC level / SPRS score?" [CONFIRM: status of each. Currently flagged as TODO in `edgerunner-profile-2026-05-08.md` §4.]
- "What does a typical ATO sprint look like for a new customer?"
- "What artifacts can you provide for an RMF package?" (Architecture diagram, control mappings, NIST 800-171 questionnaire — JADPACT version exists in repo, EV-references TBD.)
- "Can EdgeRunner run in a SCIF / on a classified enclave?" (Yes — Navy ICOP example; SECRET/TS spaces supported per Application Arsenal capability brief.)
- "Are personnel cleared?" [CONFIRM: clearance roster is not in repo. Bill to provide.]
- "What is your response to a vulnerability disclosure?" [CONFIRM: VDP and SLA — not in repo.]

**Voice:** Plain English. Federal acquisition vocabulary used precisely. *Especially* careful on the IL-6 framing — overclaiming "EdgeRunner has IL-6" without qualifying which AO granted it is a credibility risk for the partner repeating it.

---

### P1 — next quarter

#### P1-4. Solution Architecture Brief (4–6 pages)

| Audience | Partner SE, customer technical evaluator |
|---|---|
| **Problem solved** | The partner SE can pitch but loses technical credibility on the second question. They need a printable architecture brief that shows the three-tier (enterprise / GCC / edge) topology, the integration surface (OpenAI-compatible API, BYOM, container vs. binary), the deployment models (GFE laptop, fly-away kit, ATAK, edge server), and the data flow including the EVELYN edge-to-enterprise feedback loop. |
| **Format** | 4–6 page PDF; reuses `graphic-templates/03-platform-architecture/`, `02-deployment-spectrum/`, `04-human-machine-teaming/`. |
| **Delivery vehicle** | Partner portal; pre-read for any joint customer technical conversation. |
| **Outline** | 1) Three-tier architecture; 2) Integration surface; 3) Deployment models with the platform constraints (16GB VRAM, OS support, hardware-agnostic silicon); 4) Data flow + telemetry posture; 5) MOS/AFSC adapter delivery loop; 6) Reference deployments by pattern. |

#### P1-5. Trigger-Event / "When To Bring Us In" Guide (2 pages)

| Audience | Partner sales rep |
|---|---|
| **Problem solved** | "I don't know which conversations should turn into a joint pitch." The current channel attaches us late — after the architect has already designed the solution around a cloud LLM. |
| **Format** | 2-page PDF. Front: 8 trigger phrases the customer says. Back: the qualifying questions to ask next, plus the EdgeRunner POC to ping. |
| **Delivery vehicle** | Battlecard companion. Lives in the partner portal. |
| **Outline** | 8 customer-said triggers (e.g., "we need this to work on the boat / in the SCIF / forward-deployed / without internet / on a Toughbook / in a SCIF with a GFE laptop / with CAC / with our existing ATO posture"). Disqualifiers. Two qualifying questions per trigger. Named POC. |

#### P1-6. Demo Script + Recorded Demo (script: 3 pages; video: 8–12 minutes)

| Audience | Partner SE |
|---|---|
| **Problem solved** | A partner SE can't credibly demo a system they've used twice. A scripted, recorded demo with a click-by-click partner-SE-runnable version means we can be in 5 deals at once. |
| **Format** | 3-page demo script (markdown → PDF) + recorded screencast hosted on partner portal. |
| **Delivery vehicle** | Partner portal video page; script PDF as leave-behind. Live shadow runs in the first two joint demos per partner. |
| **Outline** | Setup (offline laptop, 16GB GPU, no network); 4 scripted scenarios (SOF intel summarization, NGC2-style C2 query, MOS-specific Q&A, refusal contrast vs. commercial model); call to action. |

#### P1-7. Past-Performance / Proof-Point Library (rolling)

| Audience | Partner BD writing a proposal |
|---|---|
| **Problem solved** | Partners cite EdgeRunner past performance unevenly and sometimes inaccurately. A library of pre-cleared one-paragraph citations per past-performance entry — with the relevant evidence-ledger ID for every claim — turns a 3-day proposal-section ask into a copy-paste. |
| **Format** | A single markdown file per past-performance entry, mirroring `past-performance.md` table rows, plus a master index. |
| **Delivery vehicle** | Partner portal "Proof Points" tab; gated by NDA where appropriate (JSOC pilot / EV-061 — restricted). |
| **Outline** | Per entry: customer, program, our role, scope summary, outcome, distribution markings, evidence-ledger ID, contact for verification. |

#### P1-8. Joint-Pursuit Workflow + Deal Registration Form

| Audience | Partner channel manager |
|---|---|
| **Problem solved** | The pursuit process is informal today — emails between BD leads. As partner volume grows this breaks. |
| **Format** | A 1-page workflow diagram + a 12-field web form (Notion, Airtable, or Salesforce — pick one). |
| **Delivery vehicle** | Form linked from the co-sell playbook; workflow doc as a process artifact. |
| **Outline** | Trigger → Register → Qualify → Joint Plan → Pricing → Proposal → Award → Deploy. SLA per stage. |

---

### P2 — later (when scale or field feedback warrants)

| # | Category | Audience | Why P2 |
|---|---|---|---|
| 9 | Objection-Handling Guide (10–15 pages) | Partner sales / BD | The top-3 objections live in the battlecard already. A full handbook is only worth building once we have field-tested objections from 5+ joint deals. |
| 10 | Pricing Kit (commercial item / Tradewinds CSO patterns + ROM ranges by deployment shape) | Partner BD, partner pricing | Pricing patterns are still being developed. A kit before patterns stabilize will need a rewrite within a quarter. |
| 11 | Partner Onboarding & Certification Path (LMS-style) | Partner SE / channel manager | Worth building when more than ~10 partner SEs need to be ramped concurrently. Today, joint-call shadowing is faster. |
| 12 | Joint Marketing Kit (co-branded one-pagers, joint case studies, conference booth assets) | Partner marketing | Triggers when there is a joint named program worth publicly co-branding. War Claw and IL-6 ATL with the Navy are candidates if [CONFIRM] resolves and public-distribution markings are achievable. |

---

## 4. Delivery-vehicle matrix

The federal channel has *specific* delivery preferences. Don't pick a fancy LMS if a PDF in a Box folder works.

| Asset | Best vehicle | Backup vehicle | Why |
|---|---|---|---|
| Partner Battlecard | PDF, partner portal + email attach | Notion page | Reps want it printable and offline-ready (DDIL applies to *them* sometimes, ironic but true) |
| Co-Sell Playbook | PDF + 30-min joint-team kickoff | Joint shared Box folder per partnership | Pattern-specific customization is faster in a live read-through |
| Compliance & Accreditation One-Pager | PDF (CUI/FEDCON-marked when detailed) | Distribution-Statement-C version for hand-off to customer | Accreditation review is the ATO officer's primary artifact; keep it printable |
| Solution Architecture Brief | PDF with embedded diagrams | HTML one-pager from `graphic-templates/` | Federal SEs read PDFs, not browser tabs |
| Trigger-Event Guide | PDF + "cheat-sheet card" laminated for in-person | Partner portal | Reps live in calendar tools and email; long-form fails |
| Demo Script | Markdown → PDF + recorded screencast | Live joint-call shadowing on first two deals | Scripts age; recordings give reps a fallback |
| Proof-Point Library | Markdown source in repo + portal index | Per-partner Notion mirror | Single source of truth; ledger-cited |
| Deal Registration | Web form (Notion / Airtable / Salesforce) | Email-to alias | Form forces the structured fields; alias is fallback |
| Objection-Handling | PDF + searchable wiki tab | None | Search matters more for objections than skim |
| Pricing Kit | PDF + xlsx ROM templates | Bill-led pricing call | Pricing is too sensitive for self-service |
| Onboarding / Certification | LMS course (Litmos / Mindtickle / similar) | Recorded onboarding webinar | Scale requires automation; not yet justified |
| Joint Marketing Kit | Co-branded PDFs + landing page | Conference handout | Marketing-quality assets need design review beyond a markdown export |

### Federal-channel-specific notes on delivery

- **No SaaS LMS for cleared partner reps until you have IL-2 hosting confirmed.** Most cleared-side partner BD won't load a public LMS link from a government laptop. Prefer PDF / printable for anything they will touch on a customer site.
- **CUI / FEDCON marking on every detailed asset.** If the asset names IL-6, names a customer that requires Distribution B+, or quotes pricing — mark it. The brand-system says CUI/FEDCON header is acceptable on non-public artifacts.
- **Distribution Statement on every PDF.** Distribution A for the public Battlecard; C or D for the Compliance & Accreditation back page when it details ATO scope. `my-company/distribution-statements.md` is the rulebook.
- **Logos and customer names.** Use white/greyscale logos on dark canvas only (`brand-design-system.md` §9). Never use customer logos a partner will rebroadcast without checking the originating-office permissions for that customer.

---

## 5. Validation checklist before any of this goes to a partner

These are the items Bill needs to validate first. Each is a credibility blast risk if wrong.

1. **`my-company/partnerships.md` is created or the evidence ledger source pointers are corrected.** EV-050 through EV-056 cite a file that does not exist. This is the single biggest content-gap risk to fix this week. Without it, every partner asset cites a phantom source.
2. **Partner roster confirmation.** [CONFIRM] each of: Armada (prime on TitanCore), Anduril (NGC2 sub), Safran Federal Systems (NGA GrandCanyon), WebAI scope, AMD joint demo scope. None are in the ledger today. The Battlecard, Playbook, and Plan reference them only with [CONFIRM] markers.
3. **War Claw source brief.** [CONFIRM: customer, scope, status, contract type, role, period of performance, dollar value.] No mention exists in the repo. If War Claw is a P0 talking point, treat it as a P0 ledger-update task before anything ships.
4. **"IL-6 ATL" vs. "IL-6 ATO" terminology.** Bill's request used "IL-6 ATL." All repo source consistently uses "IL-6 ATO" (Authority to Operate). The Compliance one-pager uses ATO with a footnote. If ATL is intentional (a different acronym in your context), let me know and the drafts will be updated.
5. **Sync `past-performance.md` with the evidence ledger.** Navy ICOP (EV-014), IL-6 ATO (EV-022), and USSF Tradewinds CSO Direct Award (EV-023) are in the ledger but not in the human-readable past-performance file. The Battlecard cites all three; if they don't appear in a partner-facing past-performance one-pager, partners will be confused.
6. **Comp policy for the Co-Sell Playbook.** The "compensation implications" section needs Bill's authoritative input.
7. **Cleared-personnel posture for the Compliance one-pager.** The repo doesn't have a clearance roster. If we name "cleared personnel" as part of the security posture, that claim has to be verifiable.
8. **CMMC / SPRS / FedRAMP / SOC 2 / ISO 27001.** Compliance one-pager FAQ cites these as [CONFIRM]. A partner's customer cyber officer *will* ask. The answer is fine if it's "in progress / TBD" — but it needs a real answer, not a blank.

---

## 6. Output of this engagement

| Deliverable | Path | Status |
|---|---|---|
| This plan | `my-company/partner-enablement/partner-enablement-plan-2026-05-07.md` | Drafted |
| Partner Battlecard | `my-company/partner-enablement/partner-battlecard-edgerunner.md` | Drafted (P0) |
| Co-Sell Playbook for Hardware Integrators | `my-company/partner-enablement/co-sell-playbook-hardware.md` | Drafted (P0) |
| Compliance & Accreditation One-Pager | `my-company/partner-enablement/accreditation-one-pager.md` | Drafted (P0) |
| Mirrored copies for chat-side review | `outputs/` | Mirrored |

All four files should be exported via the existing `/export-proposal` skill (or equivalent docx pipeline) before being sent to a partner — markdown is the authoring layer, PDF is the delivery layer.

---

*End of plan. Update history: 2026-05-07 — initial draft. Source-of-truth files for every fact cited above are listed in §2 inventory and `my-company/edgerunner-profile-2026-05-08.md`.*
