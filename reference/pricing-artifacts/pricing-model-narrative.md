---
artifact_id: pricing-model-narrative
output_file: drafts/pricing-model.md
companion_file: working/pricing-inputs.md
mental_model: A scored statement of how the solution is priced, funded, and awarded, with no numbers in it
must_not_produce:
  - Rates, prices, price ranges, or totals of any kind
  - Labor categories, hours, or FTE tables
  - Wrap rates, indirect factors, fee, or margin
  - Non-public pricing (price lists, negotiated discounts, partner SKU prices)
  - A ROM, budget, milestone schedule, or cost volume
---

# Pricing Model Narrative

Used by `marketplace-video-pitch` (IARPA Solutions Marketplace, CDAO Tradewinds
Solutions Marketplace, and other open-call marketplaces with the same shape).

## Mental model
The panel scores pricing as a rubric row (10% on IARPA SM) and the announcement
prohibits rates and non-public pricing. Full credit goes to the submission whose pricing
**approach**, **funding structure**, and **award type** are each stated clearly and
completely. Being clear earns the points. Numbers can only lose them, through a
compliance bounce or a release problem.

The narrative is spoken in the video and repeated on one slide. It runs about 25
seconds, roughly 70 to 90 words, in three short paragraphs, one for each element, in
the order the announcement lists them.

Calibration: `proposals/iarpa-solutions-marketplace/drafts/video-script.md`, section
"Pricing model" (submitted August 2026).

## Required inputs (ask the user)

### 1. Pricing approach
- Pricing basis: commercial pricing, cost basis, or both, and for which parts of the offer
- Unit of sale: per node, per device, per seat, per deployment, enterprise, fixed-scope engagement
- Tiering dimension, if any (deployment scale, model tier, support level)
- Price comparison: what a buyer compares this against (a commercial category or the
  status-quo alternative), stated qualitatively
- Which parts are licensed and which are services (adaptation, integration, accreditation support)

### 2. Funding structure
- One of the announcement's categories: Government-funded / mixed / private investment / cost-share / revenue-share
- What private investment has already paid for (the built product), and what
  Government funding would pay for

### 3. Award type
- One of the announcement's categories: fixed-price / cost-reimbursable / T&M / incentive-based
- Which award type applies to which part of the offer (licenses versus defined work)
- Willingness to use a specific instrument (OT with milestone payments, existing vehicle),
  only if the user confirms it

## What NOT to ask
- Any dollar figure, rate, or range
- Internal cost structure or margin
- Teaming-partner pricing

If the user offers numbers, keep them in `working/pricing-inputs.md` (INTERNAL ONLY) and
leave them out of the draft.

## Calculation approach
There is no calculation. The method is classification: put each part of the offer
into the announcement's own categories for funding structure and award type, using the
announcement's words, so the assessor can tick the row without interpreting.

## Output structure (`drafts/pricing-model.md`)

```markdown
# Pricing Model

## Pricing approach
[Pricing basis + unit of sale + tiering, one to two sentences. Services priced separately,
one sentence. Price comparison against a named category or the status-quo alternative,
one sentence, qualitative.]

## Funding structure
[Announcement category, stated first. What private investment built; what Government
funding would cover.]

## Award type
[Announcement category, stated first, mapped to each part of the offer. Instrument
preference if confirmed.]
```

Slide version: three labelled lines on one card (approach, funding structure, award type), no numbers.

## Pitfalls
- **Any number on screen or spoken.** It breaks the no-rates prohibition and can bounce the submission at the compliance screen.
- **Using categories the announcement doesn't use.** Write "mixed," not "hybrid-funded." The assessor matches words.
- **Leaving out the price comparison.** It is named in the pricing-approach element, and it is the part most vendors skip.
- **Describing value instead of pricing.** Mission impact has its own row. Spending this row's time on value loses its points.
- **Claiming a vehicle or instrument the company doesn't hold.** Check `my-company/contract-vehicles.md` and `my-company/claim-envelope.md` first.
- **Drifting into a ROM.** If the customer later asks for a price, that is a different artifact (`rom` or `cso-commercial`).
