# Keeping the evidence ledger current — diagnosis and proposal

Written 2026-08-27, prompted by finding that the ARL CRADA robotics result — arguably our strongest
technical asset — had no ledger entry despite having been submitted to the Government eight days
earlier.

## The diagnosis

The ledger is not out of date because nobody maintains it. It is out of date because of **where it
sits in the flow**.

Evidence is created when a paper is written, a demo is run, a contract is signed, a customer says
something quotable, or a proposal is submitted. Evidence enters the ledger only when a proposal
author needs a citation and discovers the entry is missing. So the ledger records **what we have
cited**, not **what we can prove** — and those are very different sets. Anything we can prove but
have not yet needed to cite is invisible.

Three symptoms of the same cause:

1. **The CRADA robotics gap.** The Warthog / Phoenix demonstration, the two-platform heterogeneity
   result, the runtime-portability observation, and a public customer quote from Phil Osteen all
   went into a Government submission on 19 Aug. None had a ledger entry on 27 Aug. Fixed today as
   EV-124 through EV-128, but only because this pursuit happened to need them.
2. **Concept papers are largely absent.** Spot-check of 16 known company assets:

   | Asset | In ledger? |
   |---|---|
   | SPOTTER concept paper | **No** |
   | Dead Reckoning (EdgeRunner x Lucenia) | **No** |
   | Ecosystem Slick / Edge Mission Loop | **No** |
   | Machine Vision Workflow slick | **No** |
   | Capable Isn't Fieldable | **No** |
   | Ground Truth zero-trust enablement plan | **No** |
   | Ground Truth capability readout | **No** |
   | Warrant Relay / Task-Pack Foundry | **No** |
   | Growth Playbook | **No** |
   | Fielding AI is a Stack | yes |
   | WarClaw / DORIS / EVELYN briefings | yes |
   | Compression paper | yes |
   | Power BI integration (Army 1st Corps) | yes |
   | Discipline-as-Software paper | yes |

   Roughly half the published body of work is unrepresented. The ones present are present because a
   proposal cited them.
3. **Almost nothing cites it.** Exactly **one** draft file across all 50+ proposal workspaces
   carries `[EV-...]` citations. A register that is rarely read gets rarely fed.

There is also a **durability** problem, separate from the currency problem: the 2026-07-24 overwrite
lost ~49 entries because the file had not been committed. The `_comment` header already records the
prevention rule — commit after every append — but nothing enforces it.

## What good looks like

The ledger should be fed **at the moment evidence is created**, by whoever created it, in under two
minutes — not reconstructed months later by a proposal author who wasn't there.

Two moments produce nearly all of our evidence, and both are already points where someone stops and
does something deliberate:

- **A proposal is submitted.** Everything it asserted has survived review and gone to the
  Government. That is the highest-confidence evidence moment we have, and it is exactly where the
  Warthog claims were sitting, already written and already vetted.
- **A paper, briefing, or slick is published.** The claims are made, the numbers are fixed, and
  someone decided they were defensible enough to put a logo on.

## Proposal

### 1. A `/ledger-harvest` skill

Point it at a source — a submitted proposal, a paper, a contract, a call note — and it proposes
candidate entries with provenance filled in, for approval before anything is written.

The pattern already exists in this repo. `capture-demand-signals` does precisely this shape for the
demand-signal register: mine a source, propose typed rows, confirm, append. `/ledger-harvest` is
that skill pointed at a different register.

Mechanics it must respect, all of which we already know:

- **Allocate IDs above the current max, never into a historical gap.** Gaps are the scars of the
  July overwrite; reusing one silently re-points every historical citation.
- **Append-only. Retire, never delete.**
- **Preserve file formatting** — `indent=2`, LF, `ensure_ascii=False`. Writing it any other way
  produces a 1,800-line diff that hides the actual change. (I did this today and had to undo it.)
- **Nothing enters without a `source_file` and `source_anchor`.** An entry that cannot be traced is
  worse than no entry, because it reads as verified.
- **Proposed, not written.** A human approves each entry. The ledger's value is that it is trusted.

### 2. Wire it into the two moments

- Add a harvest step to `/capture-submission`, which already runs at submission and already
  snapshots the final document. It is the natural place: the claims are in hand and freshly
  reviewed.
- Add it to whatever step publishes a paper or briefing in `edgerunner-papers`.

### 3. One-time backfill

Run the harvest over the unledgered assets in the table above, plus the last several submitted
proposals. Best done in batches by product line — Ground Truth, WarClaw, DORIS, EVELYN — because
the claims cluster and duplicates surface within a batch rather than across.

Rough scale: 15 to 25 new entries. A couple of hours with a human approving, not a project.

### 4. Close the durability hole

Two candidates, cheap:

- A pre-commit or post-write check that fails if `evidence-ledger.json` has uncommitted changes
  older than one session.
- Have the harvest skill commit the ledger itself as its final step, so an append is never left
  dangling.

The existing pre-commit guard on the ledger means commits already need deliberate handling; worth
reading that guard before adding anything that assumes a plain commit will work.

## What I would not do

- **Auto-extraction without approval.** An unreviewed ledger stops being usable as a citation
  source, which destroys the thing that makes it worth maintaining.
- **A separate database or new tool.** The JSON file with a schema works; the problem is inputs,
  not storage.
- **Backfilling everything at once.** The July overwrite is a standing reminder that bulk rewrites
  of this file are the risky operation. Batch, commit, verify.

## Open question for Bill

Is the ledger meant to be **the company's evidence register** or **the proposal system's citation
store**? Today it is built as the second and used as if it were the first. If it is the first, it
should also carry the marketing and partnership claims that never appear in a proposal — the
Ecosystem Slick, the Growth Playbook, partner collateral — and the harvest should run over those
too. That is a scope call, not a technical one.

## Status

Nothing here is built. This is a proposal for how to proceed, plus today's tactical fix
(EV-124..EV-128) already applied.
