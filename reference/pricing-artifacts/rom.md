---
artifact_id: rom
output_file: drafts/rom.md
companion_file: working/pricing-inputs.md
mental_model: Directional range with stated assumptions — not a cost buildup
must_not_produce:
  - CLIN structure
  - DCAA-auditable labor hour tables
  - Line-item BOE narratives
  - Indirect rate buildups (fringe / overhead / G&A percentages shown separately)
  - Fee/profit as a separate line item
---

# ROM (Rough Order of Magnitude)

## Mental model
The reader is deciding whether this is a $50K effort or a $5M effort. They care about the **range**, the **assumptions that drive it**, and the **validity window**. They do NOT want a cost volume.

A ROM shows confidence via stated uncertainty, not hidden false precision. "$1.2M-$1.8M over 18 months, ±30%, assumes GFE cloud access" beats "$1,487,293.22" every time.

**Defensibility bar.** Even a one-page ROM is graded (by anyone acquisition-literate) against **GAO-20-195G**'s four characteristics — *comprehensive, well-documented, accurate, credible* — in miniature: name the method, document the basis and assumptions, show a range with uncertainty, tie scope to cost. For DoD software/MTA efforts the cost-estimate framing is **DoDI 5000.73**. See `reference/doctrine/acquisition-guidance-catalog.md` (Tier 1).

**Validated default shape (calibration: DIA DMA ROM, submitted 2026-07-24 with ZERO human edits).** For teamed FFP prototype ROMs, the submit-grade structure is:
1. **Cost table with the price in it** — labor as one line plus itemized ODC lines (travel, cloud compute *if beyond GFE*, hardware *if beyond GFE*, media/security/incidentals), each a range, ending in a bolded total range. The customer never hunts through prose for the number.
2. **Milestone allocation table** — M1..Mn with primary output and ~% share of total, summing to 100%.
3. **Level of Effort in FTE-equivalents only** — no hours column, no rates. The blended fully-burdened rate stays in `working/pricing-inputs.md` (INTERNAL ONLY); publishing FTEs without hours means no `$/hr` is derivable from the published data. The only teammate input required is each sub's *share of effort*, never a rate card.
4. **Basis of estimate** — engineering build-up by workstream; one short paragraph.
5. **Optional priced items** (not in the base) + **numbered key assumptions** + validity window.

## Required inputs (ask the user)

Keep it short. If the user is in a hurry (common for ROMs), accept approximations.

- **Scope summary** — one paragraph, what's in, what's out
- **Duration** — rough month or quarter range
- **Basis** — one of: *analogous* ("we did X for $Y"), *parametric* ("rule of thumb: $Z/seat/year"), or *expert judgment* ("architect estimate based on decomposition")
- **Key cost drivers** — 3-5 things that dominate the number (team size, compute, travel, subs)
- **Key assumptions** — 3-5 things that if false, change the range materially (GFE available, no SCIF required, existing contract vehicle, etc.)
- **Validity window** — "good for 30 days pending scope clarification" is standard

## What NOT to ask
- Labor category rates
- Fringe / overhead / G&A rates
- CLIN structure
- Per-trip travel estimates
- Subcontract markup percentages

If the user starts offering DCAA-level detail, steer them back: "That's more detail than a ROM needs. Save it for the cost volume if this progresses to a full proposal."

## Calculation approach

Pick one method (state it explicitly in the output):

| Method | When to use | How |
|---|---|---|
| Analogous | You've done a similar project | Start with prior total, adjust ±% for scope delta |
| Parametric | Repeatable unit (seats, endpoints, cores) | Rate × units, show both |
| Expert judgment | Novel scope, architect breakdown | Decompose to 3-5 workstreams, estimate each |

Always produce a **range**, not a point estimate. Minimum width ±20% (tighter signals false precision for a ROM).

## Output structure (`drafts/rom.md`)

```markdown
# Rough Order of Magnitude — [Project / Opportunity Name]

**To:** [Customer / POC]
**From:** [Your Company]
**Date:** [YYYY-MM-DD]
**Validity:** This ROM is valid for [30] days from the date above.

## Scope
[One paragraph. What we'd deliver. What's in. What's explicitly out.]

## Estimated Investment
**$[Low] – $[High]** over **[N] months**
*(±[X]% based on [method])*

## Basis of Estimate
Method: [Analogous / Parametric / Expert judgment]
[One paragraph explaining how the range was derived.]

## Key Cost Drivers
1. [Driver — what it is and roughly its contribution to the range]
2. [Driver]
3. [Driver]

## Key Assumptions
These assumptions materially affect the range. If any are false, the ROM must be revisited.

1. [Assumption and cost-swing implication if false]
2. [Assumption]
3. [Assumption]

## Risks to the Estimate
[2-4 items. Scope creep, schedule compression, dependency on third-party, etc.]

## Next Steps
[What the customer would need to provide / decide to firm this up into a full proposal or task order.]
```

## `working/pricing-inputs.md` (companion)

Short. Capture the raw numbers that drove the range so they're defensible if asked:

```markdown
# Pricing Inputs — [Project]

## Method
[Chosen method + 2-3 sentences of rationale]

## Ballpark math (internal only)
[Show the rough calculation — e.g., "2 FTE × 12 months × $250K/year blended = $500K base; +$150K compute; +$100K contingency; range 0.6M–0.9M"]

## Sensitivity
[Which inputs change the answer most? Rate, duration, headcount, compute, subs.]

## Sources
[Prior project X, parametric model Y, architect estimate Z]
```

## Pitfalls
- **Point estimate** — "It will cost $1.25M" signals false precision and invites rework. Always a range.
- **Missing validity window** — ROMs rot fast. Without a window, stakeholders treat it as a commitment.
- **Hidden precision** — "$1,487,000" is just as wrong as "$1,487,293.22." Round to significant figures appropriate to the uncertainty (e.g., $1.5M, $1.2M-$1.8M).
- **Too much structure** — If your ROM has a CLIN table, it's not a ROM.
- **No assumptions list** — The customer can't re-scope without them, and you can't defend the range without them.
