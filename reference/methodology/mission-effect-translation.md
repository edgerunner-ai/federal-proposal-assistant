# Mission-Effect Translation

**Adopted 2026-09-09** from the assessment in `docs/MISSION-EFFECT-TRANSLATION-2026-09-09.md` (Pimentel's five elements, relayed by Paul Van Slett). This file is house methodology. It is read by `narrative-spine`, `proposal-storyboard`, `proposal-editor`, `red-team-review`, and the `operational-user` adversarial persona.

## The rule

Every proposal states, in one place and in one paragraph, the five things a Pentagon room has to agree on before it buys anything: **the problem, the mission effect, the capability, the cost, and the timeline.** The mission effect is the pivot. It is the "why" that the other four serve, and it is the thing an operator in the room would repeat back.

The pipeline already forces outcome language per discriminator (Feature, Advantage, Benefit), per section (the theme statement), per graphic (the action caption), and per Strength (benefit to the Government). This rule adds the proposal level, so those pieces align instead of merely coexisting.

**Precedence.** The rubric decides what is scored. The mission effect decides how each scored answer is framed. The capability is the evidence, never the headline. This sits inside the bid-maturity rule (every bid is a graded test), not beside it: a Strength by definition names a benefit to the Government, and the effect statement is how a met requirement becomes a Strength.

## The Mission Effect Statement

Written once, in `working/narrative-spine.md`, as the first block, signed off with the spine. Five labelled lines, then the same content as one paragraph that can be dropped into the executive summary.

| Element | What it must contain | Test |
|---|---|---|
| Problem | The customer's problem in the customer's words, cited to the solicitation, a Q&A answer, or a named conversation | Would the customer recognise it as theirs? |
| Mission effect | What changes for the operator or unit when this is fielded, in operational terms | See the operator-terms test below |
| Capability | What we deliver that produces the effect, named, with the ledger items that prove it | Does every capability named have an `EV-` record? |
| Cost | The pricing artifact's headline: ROM range, milestone total, or unit price, stated as what it buys | Could the acquisition officer say what the number purchases? |
| Timeline | When the effect arrives: pilot, IOC, first delivery, and the gates between | Does each date name who controls the gate? |

**The operator-terms test for the effect.** A mission effect is stated in terms of at least one of: time (to a decision, to a task, to restoration), decisions (made, made earlier, made with evidence), risk (reduced, bounded, detected before harm), availability (works when the network or the expert is absent), or what no longer has to happen (a wrong procedure executed, a retraining cycle, a call to a help desk). "Improves readiness" and "enables decision superiority" fail the test. "A technician at the console gets the right procedure, with its source, faster than a manual, and a wrong answer is stopped before it is executed at sea" passes.

**Length.** About 100 words. It replaces prose in the executive summary; it does not add to it.

## Reading the solicitation: effects or specs

Before the requirement matrix is built, classify the solicitation's requirements:

- **Capability requirements** describe the effect the user needs and leave room for how. Common in CSO areas of interest, prize challenges, OTA white-paper calls, and increasingly in JFRP-shaped documents. Here the effect is the scored object. A capability tour fails outright; the response must argue effect first and mechanism second.
- **Performance specifications** fix a technical characteristic (a threshold, an altitude, a footprint, a protocol). Here the response answers the line item and names the effect the line item exists to produce. A response that only ticks the spec reads as compliance; one that names the effect reads as understanding.

The requirement matrix carries an **Effect served** column so this translation happens once, when the requirement is read, and every downstream artifact inherits it.

## The translation rule for narrow specs

When we do not meet a specification literally but have proven the effect it serves under a harder or adjacent condition (Van Slett's orbital-altitude case; our own component-versus-integrated TRL cases), the response states three things and nothing more:

1. The effect achieved, in operator terms, with its evidence.
2. The condition it was achieved under, named honestly.
3. Why it transfers to the specified condition, as an argument the evaluator can check.

It never claims the spec. It never hides the gap. Where the Q&A window is still open, capture-intent asks the Government to confirm the effect behind the spec, using the JFRP shift toward capability requirements as the reason. This is the constrained-claim discipline of `proposal-writer` bind Step 2d applied to translation.

## What every review asks first

**"What operational outcomes does this proposal enable or support, and can I state them from the draft alone?"**

- `proposal-editor`: first test per scoring section, and the fifth question of the Final Pass.
- `red-team-review --mode=red`: review category 12, mission-effect clarity.
- `red-team-review` Gold Team: the Mission Effect Check table, before Win Theme Visibility. A missing, technical-only, or unassembleable effect is a Weakness at the proposal level, not a note.
- Lightweight Reader Response: "mission effect" replaces the generic "so what".
- `adversarial-review`: the `operational-user` persona, seated by default on CSO, OTA, prize-challenge, and white-paper types.

## Worked instance (NAVWAR GenAI EPSS, v10, 2026-09)

**Problem.** PMW 160's Sailors maintain tactical-network software that changes faster than schoolhouse training, often disconnected, with no second source to check an answer against. **Mission effect.** A technician at the console gets the right procedure, with its source, faster than a manual or a help desk, and a wrong answer is stopped before it is executed at sea. **Capability.** EdgeRunner Mentor: local retrieval, grounded answers, a verification gate outside the model, on the workstation with no network (EV-073, EV-130, EV-131). **Cost.** Phase 2 rough order of magnitude, submitted with the pitch. **Timeline.** Four workstreams over fifteen months; fleet pilot from month twelve on Government authorization.

The v10 brief contained all five spread across three sections. The statement assembles them.

## Failure modes this rule exists to catch

- **The capability tour.** A paragraph that lists what the product does with no sentence about what changes for the user. Collapse to problem, answer, proof.
- **The technical benefit.** "Benefit to the Government: deterministic verification with no model in the loop." That is a mechanism. The benefit is "a wrong answer is caught before a Sailor acts on it."
- **The unpriced effect.** An effect with no cost line beside it invites the room to price it themselves.
- **The undated effect.** An effect with no arrival date is a research statement.
- **The borrowed effect.** An effect stated in the vendor's terms ("decision superiority", "AI-enabled readiness") rather than the customer's. If the phrase is not in the solicitation or a customer conversation, it is ours, and it fails the operator-terms test.

## What this rule does not change

The rubric-first spine; the evidence ledger and citation protocol (an effect cites the same ledger a capability does); the TRL rules; Track B ordering for white papers; page budgets.
