# Mission-Effect Translation: fitting the "five things" into the pipeline

**Date:** 2026-09-09 · **Status:** adopted by Bill 2026-09-09. Stage one implemented the same day: `reference/methodology/mission-effect-translation.md`; the Mission Effect block in the spine; the storyboard's "Mission Effect Advanced" field; Red Team category 12 and the Gold Team Mission Effect Check (Bill's addition: the review itself asks whether the mission impact is clearly articulated); the `operational-user` persona seated on every type; the editor's fifth Final Pass question; Pattern 5. Stages two to six (preflight script, matrix column and bind translation rule, pricing line, quick-look and capture-intent, prose-lint advisory) remain.
**Trigger:** Paul Van Slett's LinkedIn post of 8 September, relaying Omar Pimentel's SpaceNews essay ("I saw more than 1,000 pitches to the Pentagon ... and a clear pattern for success", early September 2026; Pimentel spent three years at DIU). The post text is captured in full at the end of this file; the essay itself is paywalled and was not read.
**Bill's instruction:** translate the guidance into how we write and structure proposals without discarding what the pipeline already does well; every proposal review asks "what operational outcomes does this proposal enable or support?"

---

## 1. What the post actually says

Two arguments, and they matter differently to us.

**Pimentel's pattern (the pitch side).** Of more than a thousand DIU pitches, the companies that won were the ones who could align a whole room, operators, acquisition officials, and technical experts, around five things: the problem, the mission effect, the capability, the cost, and the timeline. Winning was not about better technology. It was about translation. Van Slett's gloss: translating a company's technology "into how it solves the mission problem or improves a required capability is key. It is the 'why' that drives everything else."

**Van Slett's point (the requirements side).** He has written requirements for twenty years. A company was excluded from a demonstration for never having operated at one orbital altitude, although it had proven a harder version of the capability elsewhere. The requirement was written narrowly enough to filter out the answer it was looking for. The move from JCIDS to the Joint Force Requirements Process shifts emphasis from system performance requirements to capability requirements, which describe the effect the warfighter needs and leave room for how industry gets there. He has seen systems meet every line item and still not deliver the capability the mission needed.

For a bidder the two arguments combine into one rule. **Answer the line item, and say what effect the line item exists to produce.** When the solicitation is written as effects (the JFRP direction, and already the norm in CSO areas of interest and prize challenges), the effect is the scored object and a capability tour fails outright. When it is written as performance specs, the effect is the thing the spec is reaching for, and a response that names it reads as understanding while a response that only ticks the spec reads as compliance. And when our evidence does not match a narrow spec literally but proves the effect under a harder condition, the honest translation is to state the effect achieved, the condition, and why it transfers, without claiming the spec.

## 2. Where the pipeline already does this, and where it does not

The survey below is verified against the tree, not remembered.

**Already enforced, keep as is.**

| Granularity | Mechanism | Where |
|---|---|---|
| Per discriminator | Feature, Advantage, Benefit escalation; "aim for Benefit-level" statements that address a customer-stated issue | `reference/proposal-writing-patterns.md` Pattern 2 |
| Per section opener | Theme statement with three elements: what, why it matters to the Government, proof hook | Pattern 1 |
| Per graphic | Action caption: what the graphic proves, not what it shows; "if you cannot write one, the graphic has no evaluative point" | `proposal-graphics` skill |
| Per Strength | Gold Team requires "Benefit to Government" for every Strength; a Strength must be advantageous to be a Strength | `red-team-review`, `reference/evaluator-rubrics/strengths-weaknesses-deficiencies.md` |
| Readability | Cold-reader persona: "the so what" findable after page one; capability tours are a structural finding | `reference/adversarial-personas.md` |
| Voice | "Ties the point to proof, risk reduction, or mission value"; solution-brief mode explains the solution as a customer outcome before naming components | `reference/editorial-voice-guide.md`, `reference/narrative-operating-modes.md` |
| Spine | Every movement traceable to a customer-stated problem; "capability-tour proposals" named as an anti-pattern | `narrative-spine` skill |

**Not enforced, and this is the gap the post names.**

| Gap | Evidence |
|---|---|
| No proposal-level statement of the mission effect | The narrative spine has Positioning, Argument, Through-Line, and Must-Not-Become. None is "the effect on the mission." The storyboard's per-section fields (Purpose, Evaluator Question, Required Answer, Reader Movement, Strength to Earn) have no mission-effect field. |
| No artifact carries the five elements as one aligned statement | The white-paper exec-summary pattern has outcome and timeline but no cost. The OTA pattern has no effect and no cost. The only place all five appear in order is the marketplace video pitch, and that is the customer's mandated content list, not ours. |
| The requirement matrix has no "effect served" column | `proposal-solution-architect` columns: Requirement, Source, Explicit/Implicit, Response Approach, Capability Source, Gap/Risk. Nothing asks what the requirement is for. This is exactly where Van Slett's translation has to happen, because it is where a performance spec gets read. |
| Cost is never tied to an outcome | `pricing-analyst` prices "to win on merit"; the only linkage anywhere is the price rubric's "are the benefits asserted in the technical volume funded in the cost volume?" |
| No reviewer persona reads as an operator | The seven adversarial personas ask about verifiability, readability, competitive attack, compliance, register, accreditation, and friendliness. Pimentel's room had operators in it; ours does not. |
| Gold Team has no mission-impact dimension | It scores Strengths, Weaknesses, Deficiencies, win-theme visibility, discriminator proof, ghosting. The benefit field is per finding; nothing asks whether the proposal as a whole names an effect an operator would recognise. |
| No mechanical check | `prose-lint` has no capability-tour detection; `check-strengths.py` verifies a benefit phrase survives edits but does not test that it is operational rather than technical. |

**The pattern.** We enforce outcome language at three fine granularities and never at the top. A proposal can pass every gate we have with a theme statement per section, a Benefit-level discriminator per section, and an action caption per figure, and still never say in one place what changes for the unit when this is fielded. That is the thirty-minute failure Pimentel describes: everything true, nothing aligned.

## 3. Reconciling with the bid-maturity rule

Our strongest standing doctrine says every bid is a graded test against the customer's published rubric, and the recurring failure is demoing the product instead of answering the requirement (the Mystic Depot Phase II lesson). A mission-effect lens could read as pulling away from the rubric. It does not, for two reasons.

First, the rubric is scored through Strengths, and a Strength by definition names a benefit to the Government. The effect statement is how a scored answer becomes a Strength instead of a met requirement. Second, the solicitations we actually chase (CSO areas of interest, OTA white papers, prize challenges, BAAs) already score mission impact, operational relevance, or transition value by name. The effect is not a competing frame; it is the rubric's own top row, which our pipeline currently treats as one factor among many.

The order of precedence stays: **the rubric decides what is scored; the mission effect decides how each scored answer is framed; the capability is the evidence, never the headline.**

## 4. The proposal: one statement, carried end to end

Introduce a **Mission Effect Statement**: the five elements as one aligned paragraph, written once, signed off with the spine, and then carried by every downstream artifact and checked by every review.

```
Problem        [customer's words, cited to the solicitation or a named conversation]
Mission effect [what changes for the operator or unit when this is fielded, in their terms:
                time, decisions, risk, availability, what no longer has to happen]
Capability     [what we deliver that produces the effect; named, evidenced]
Cost           [the pricing artifact's headline: ROM range, milestone total, or unit price]
Timeline       [when the effect arrives: pilot, IOC, first delivery; the gates in between]
```

A worked instance from the brief we shipped last week, to show the frame fits what we already write:

> **Problem.** PMW 160's Sailors maintain tactical-network software that changes faster than schoolhouse training, often disconnected, with no second source to check an answer against. **Mission effect.** A technician at the console gets the right procedure, with its source, faster than a manual or a help desk, and a wrong answer is stopped before it is executed at sea. **Capability.** EdgeRunner Mentor: local retrieval, grounded answers, a verification gate outside the model, on the workstation with no network. **Cost.** Phase 2 rough order of magnitude, submitted with the pitch. **Timeline.** Four workstreams over fifteen months; fleet pilot from month twelve on Government authorization.

The v10 brief contains all five, spread across the executive summary, section 2.5, and section 4. Nowhere does it say them together. An evaluator assembling that paragraph does our work for us; one who does not, scores what is in front of them.

### 4.1 Changes by stage, with what stays

| Stage | Change | What is preserved |
|---|---|---|
| `/opportunity-quick-look` | Add one triage question: can we state the effect the customer wants and the effect we can prove, each in one sentence? Note whether the solicitation is written as effects or as performance specs; the second carries a translation burden and a Q&A opportunity. | The eight-factor triage is untouched; this is a ninth line. |
| `/capture-intent` | The first customer belief becomes the mission effect ("PMW 160 must believe a Sailor gets a right answer at the console when disconnected"). Add a capture action: where a spec is narrower than the effect it serves, ask the Q&A to confirm the effect, using the JFRP shift as the reason. | Beliefs, prohibited claims, posture, ghosting stay. |
| `/proposal-solution-architect` | Add one column to the requirement matrix: **Effect served**, the operational outcome the requirement exists to produce, taken from the solicitation's purpose language where it exists and marked inferred otherwise. The response approach must then answer the requirement and name the effect. | Every existing column stays. Sequencing stays requirement-first; this makes the requirement mean something before it is answered. |
| `/narrative-spine` | The Mission Effect Statement becomes the first block of the spine, above Positioning, and is part of the human sign-off. The Through-Line must be a consequence of the effect. | Positioning, Argument, Through-Line, Must-Not-Become stay. The sign-off gate already exists; nothing new to run. |
| `/proposal-storyboard` | Per-section field **Mission effect advanced** (which part of the statement this section moves, or "none"); sections that advance none are flagged the way factor-less sections are today. Exec summary storyboard requires the five-element paragraph verbatim or near it. | Evaluator Question, Required Answer, Reader Movement, Strength to Earn stay. |
| `/pricing-analyst` | The pricing artifact's headline is written as "cost for effect by date": what the number buys, in the effect's terms, and when. Adds the effect line to `working/pricing-inputs.md`. | Every template in `reference/pricing-artifacts/` stays; this is a required sentence, not a new artifact. |
| `/proposal-writer` bind | Step 2 gains an **outcome check**: each scoring section states the effect in operator terms (time, decision, risk, availability) at Benefit level, and the exec summary carries the five elements. Step 2d (constrained claims) gains the translation rule: where we do not meet a spec literally but have proven the effect under a harder or adjacent condition, state the effect, the condition, and the transfer, never the spec. | Draft-loose is untouched, by design: the effect is composed freely, then checked. |
| `/proposal-editor` | First editorial test per scoring section: does the opening name what changes for the operator? Capability-tour paragraphs (features listed, no effect sentence) are collapsed into problem, answer, proof; that instruction exists in Mode 5 and becomes a standing rule for all modes. | Everything else in the editor stays. |
| `/red-team-review` Gold Team | New table, **Mission Effect Check**: can the evaluator state all five elements from the draft alone, with paragraph cites; is the effect one an operator would recognise; is every Strength's "Benefit to Government" operational rather than technical (rewrite test: "so the operator can ..."). A missing or technical-only effect is a Weakness at the proposal level. | S/W/D scoring, win-theme visibility, discriminator proof, ghosting stay. |
| `/adversarial-review` | New blind persona, **operational-user**: a former operator now writing requirements, who reads only for what changes for the unit when this is fielded and what happens when it is not; a Material finding when the effect cannot be stated after page one or is not something a user would recognise. Added to the default panel for CSO, OTA, prize-challenge, and white-paper types. | The seven existing personas stay. |
| `/export-proposal` preflight | New deterministic script, `check-mission-effect.py`, modelled on `check-strengths.py`: verifies the spine carries the five elements, that the exec summary carries the effect phrase, and that the pricing artifact carries the cost line. Exit 1 when the spine has no statement; advisory when the exec summary drops it. | Existing preflight gates stay. |
| `prose-lint` | Last and advisory only: a capability-tour density signal (paragraphs in scoring sections with several capability verbs and no outcome marker). Heuristic; never blocks. | Rule lists stay. |
| `/status` | Shows whether the Mission Effect Statement exists and is signed off. | Read-only, as now. |

### 4.2 The doctrine file

One new reference, `reference/methodology/mission-effect-translation.md`, holding: the five-element definition; the operator-terms test for an effect (time, decision, risk, availability, what no longer has to happen); the translation rule for narrow specs; the effects-versus-specs reading of a solicitation; and the worked EdgeRunner examples (NAVWAR EPSS above; WarRoom; the AFAR focus area). `reference/proposal-writing-patterns.md` gains a short Pattern 5, Effect translation, that points to it. No synced doctrine file is touched.

### 4.3 What we deliberately do not change

- The rubric-first spine and the evaluation model. The effect sits inside them.
- The evidence ledger and citation protocol. An effect claim cites the same ledger a capability claim does; "so the operator can" is not a licence to assert.
- The TRL rules written this week. An effect proven at EXTiC is still a component effect until the integrated configuration ran.
- The white-paper Track B order. The statement is written in the spine, which Track B already has.
- Length budgets. The five-element paragraph replaces prose; it does not add to it. The NAVWAR instance above is 110 words and would replace about that much of the current summary.

## 5. Order of work and effort

1. Doctrine file, spine block, storyboard field, Gold Team table, operational-user persona. Prompt and template changes only. Half a day. This alone answers Bill's instruction that every review asks the question.
2. `check-mission-effect.py` with selftest, wired into export preflight and `/status`. Half a day.
3. Requirement-matrix column and the writer's translation rule in bind Step 2d. Two hours.
4. Pricing "cost for effect by date" line. One hour.
5. Quick-look triage line and capture-intent belief and Q&A action. One hour.
6. Prose-lint capability-tour advisory. Last, and only if the heuristic proves useful on two proposals.

Then apply it retroactively to one live pursuit as the test, the way the VAULT scrub was tested on NAVWAR v9: write the Mission Effect Statement for the Digital Scribe white paper (due 25 September) before drafting, and see whether the draft gets shorter and sharper.

## 6. Recommendation

Adopt. The pipeline is already good at making individual claims land; what it lacks is the one paragraph that aligns the room. The change is small in mechanism and large in effect because it inserts at the two points that already have human sign-off (the spine) and mechanical enforcement (export preflight), and it gives every reviewer, human and adversarial, the same first question.

---

## Appendix: the post, verbatim

Paul Van Slett, LinkedIn, 8 September 2026.

A company can walk into a Pentagon pitch meeting with a working prototype, credible engineers, and real investors behind them, and still lose the room in thirty minutes.

That is the argument in a recent SpaceNews piece by Omar Pimentel. In it, he stated that he sat in on more than a thousand of those meetings at the Defense Innovation Unit and that the companies who won were the ones who could align an entire room, operators, acquisition officials, technical experts, around the same five things: the problem, the mission effect, the capability, the cost, and the timeline. His conclusion was not about who had the better technology. It was about translation.

I have been writing requirements documents for twenty years now, so a different part of the piece stuck with me. Pimentel described watching a company get excluded from a demonstration because it had never operated at one specific orbital altitude, even though it had already proven a harder version of that capability elsewhere. The requirement was written narrowly enough to filter out the answer it was actually looking for.

The recent shift from JCIDS to the Joint Force Requirements Process moved emphasis away from system performance requirements and toward capability requirements. A system performance specification can lock in one specific technical characteristic that narrows available options even if there are other novel ways to solve the mission problem. A capability requirement describes the effect the warfighter needs and leaves more room for how industry gets there. Warfighters care far more about having the capability when they need it most than the manner in which it was provided.

Translating a company's superior or novel technology into how it solves the mission problem or improves a required capability is key. It is the "why" that drives everything else. And for those of us who author requirements, writing it too tightly can lead to missed opportunities to leverage the very innovations that industry excels at and improve the DoW's mission effectiveness.

I've seen performance requirements precise enough to evaluate cleanly and produce a system that met every line item without delivering the capability the mission actually needed. A performance requirement too specific eliminates real competition. One too broad does not guarantee effective capability delivery. Where do you think the balance sits? And for those of you in industry, have you seen a change this year in how these requirements are being written?
