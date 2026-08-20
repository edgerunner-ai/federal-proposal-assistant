# EdgeRunner AI: Approved Language for Partner Submissions

**For partners naming EdgeRunner AI in a proposal, RFI response, white paper, or capability
statement where the partner is prime.**

Version 1 · 12 August 2026 · Owner: Bill Bal, VP Growth, bill@edgerunnerai.com

Everything below is cleared for use as written. Paste it. The wording carries legal and
accreditation risk controls, so please use it verbatim rather than paraphrasing, and send us
anything that departs from it before the document goes out.

If your response needs a claim this document does not cover, ask. A same-day answer is almost
always possible, and it is far cheaper than a correction after submission.

---

## 1. How to refer to us

EdgeRunner AI is a separate company and your teaming partner. Please avoid possessive
constructions such as "our AI layer" or "our small-language-model layer," which read as though
EdgeRunner is your product. That misattribution follows the document into any follow-on
competitive solicitation, where it becomes a problem for both of us.

**Use at first mention:**

> EdgeRunner AI, our teaming partner, provides the small-language-model layer. EdgeRunner AI is a
> U.S. company (CAGE 9Z176, UEI SLZTJUA8DBD3, NAICS 541511) whose military-specific language models
> run on-premises and fully air-gapped on commodity hardware.

After that, "EdgeRunner AI" or "EdgeRunner" on its own is fine.

## 2. Company identification

| Field | Value |
|---|---|
| Legal name | EdgeRunner AI |
| CAGE | 9Z176 |
| UEI | SLZTJUA8DBD3 |
| NAICS | 541511 |
| Founded | February 2024 |
| Headquarters | 11011 NE 9th St, Unit 218, Bellevue, WA 98004 |
| Business size | Small business |
| Contract vehicles | NASA SEWP V, ITES-SW2, CDAO Tradewinds (Awardable status and CSO Direct Award). Carahsoft distributor; Government Acquisitions Inc. VAR |

## 3. What EdgeRunner does

Use whichever of these fits the space you have.

**One sentence:**

> EdgeRunner AI builds military-specific language models and a hardware-agnostic runtime that
> executes them on-device, air-gapped, in disconnected, degraded, intermittent, and
> low-bandwidth environments, with no cloud in the critical path.

**One paragraph:**

> EdgeRunner AI delivers secure local inference on customer-owned hardware. Its models are trained
> on military data and its runtime executes them air-gapped and containerized across Intel, AMD,
> NVIDIA, Qualcomm, and Apple silicon, exposing an OpenAI-compatible, MOSA-compliant interface that
> supports bring-your-own-model. The result is that AI capability reaches operators regardless of
> connectivity, inside the customer's own accredited boundary, without sending data to a commercial
> cloud service.

**By component**, if your response benefits from naming them separately:

| Component | One-line description | Maturity, state it plainly |
|---|---|---|
| Models and adapters | Military-specialized language models in three tiers (Light, Medium, Heavy), plus mission-specific adapters | Fielded |
| EdgeRunner AI Runtime | Hardware-agnostic, air-gapped, containerized on-device inference; OpenAI-compatible; bring-your-own-model | Fielded |
| WarClaw | Agentic orchestration. Mission workflows as versioned, validated, auditable software, human-gated, with a first-class execution record. Orchestration, not autonomy | Built |
| Ground Truth | Model-agnostic verification layer. Checks each AI claim against a human-approved evidence ledger, gates pass, flag, or block with no model in the verification loop, and emits a portable signed receipt. Built to ICD 203/206. Attribution, not truth | Built |

Do not assign a TRL to Ground Truth. Do not describe WarClaw as autonomous.

## 4. Accreditation: use this wording exactly

> EdgeRunner AI holds an active Interim Authority to Test (IATT) at Impact Level 6 covering the
> EdgeRunner AI Runtime and models. An IL-5 Authority to Operate with the U.S. Space Force is in
> progress. The platform deploys inside the customer's own accredited boundary rather than as a
> cloud service.

**Do not write any of the following:**

- "IL-6 ATO," "IL-6 accredited," or "ATO granted." It is an Interim Authority to Test, and the
  distinction is material to an accreditation reviewer.
- The IL-5 ATO as held or in hand. It is in progress.
- Any attribution of the IL-6 IATT to the Navy, PMW 120, or Navy ICOP, or to any other named
  program or unit. State the IL-6 IATT as a standalone claim. Our Navy work may be listed
  separately as a program-of-record engagement, and both statements are true, but they must not be
  joined.
- Any FedRAMP, SOC 2, or ISO 27001 status. **EdgeRunner holds none of these and is not pursuing
  them.** If a form or evaluator asks, the correct answer is that the product deploys on-premises
  and air-gapped inside the customer's own accredited boundary rather than as a cloud service, so
  FedRAMP does not apply to it. Your own or a hosting platform's FedRAMP posture may of course be
  described, attributed to you by name.
- Accreditation coverage for WarClaw, Ground Truth, or EVELYN. The IL-6 IATT covers the runtime
  and models only; the other components are not separately accredited.

An authorization from one program does not automatically transfer to another command. Each
Authorizing Official issues their own. What the IL-6 IATT evidences is security architecture and
compliance posture, not blanket cross-command authority.

## 5. Past performance: use this wording exactly

> EdgeRunner AI is fielded in operational U.S. military use, including U.S. Army Special Operations
> Command (1st, 7th, and 10th Special Forces Groups), the JFK Special Warfare Center and School,
> and the 4th Infantry Division, and is a component within a program of record with the U.S. Navy
> (Integrated Common Operating Picture, NIWC Atlantic / PMW 120). EdgeRunner holds a production
> contract with the U.S. Space Force and research agreements with the Air Force Research Laboratory
> and the Army Research Laboratory.

If you need a shorter version, cut from the end. Do not add units or programs not listed here
without asking; some of our engagements are restricted and cannot appear in a document with
unlimited distribution.

## 6. Please keep these attributed to yourselves

These are the corrections we have had to request most often. In each case the underlying statement
is true of the prime and untrue, or unconfirmed, of EdgeRunner:

| Claim | Why |
|---|---|
| CMMC Level 2, or any CMMC level | EdgeRunner holds no CMMC certification. Our internal environment is not under CMMC. Please do not write a sentence in which EdgeRunner and your platform jointly "generate CMMC-aligned controls." |
| ITAR and EAR operational controls | Same. Keep the attribution with the prime. |
| "Certified by DoD as 100% Made in the USA" | This is your certification. Our software is developed in the United States, which you are welcome to state as "incorporating U.S.-made software and AI models," but our software is not covered by your certification. |
| Foreign Ownership, Control, or Influence statements | Yours to make about your company. |
| Facility clearance level | Ours to confirm on request. Do not assume it from a deployment. |

What **can** be stated jointly, where both are true: on-premises or fully air-gapped deployment,
zero cloud dependency, role-based access control, encrypted communications, and full audit logging.

## 7. Describing a joint capability that is not built yet

When a response describes your platform and EdgeRunner working together, please write it in the
tense that matches reality. If the integration is scoped but not delivered, describe it as what the
team would stand up, not as something the combined product does today.

This is not caution for its own sake. Responses like these are usually scored partly on the
respondent's demonstrated experience, and present-tense language about an unbuilt integration
sitting next to a genuine multi-year delivery record puts the real record in question if anyone
checks. Both companies have strong, separately provable histories. Those carry the experience
criterion on their own, and the joint capability then reads as upside rather than as a claim
someone has to verify.

## 8. Quick reference: never in a customer-facing document

- IL-6 ATO, or IL-6 described as accredited
- IL-5 ATO described as held
- The IL-6 IATT tied to the Navy, PMW 120, ICOP, or any named unit
- FedRAMP, SOC 2, or ISO 27001 status for EdgeRunner
- CMMC certification or level for EdgeRunner
- Accreditation coverage extended to WarClaw, Ground Truth, or EVELYN
- The name of any open-weight model underlying an EdgeRunner model tier
- A TRL assigned to Ground Truth
- WarClaw described as autonomous

---

**Questions, or need language this document does not cover:**
Bill Bal, VP Growth, bill@edgerunnerai.com
