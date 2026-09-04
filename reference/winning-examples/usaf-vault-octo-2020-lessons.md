# Winning Example: Octo, USAF SAF/CO VAULT Technical Approach (Dec 2020)

**Source:** `D:\OneDrive\Desktop\Winning Proposal Examples\Air Force VAULT\VAULT tech volume white glove.pdf` (52 pp; Bill ran this proposal, it won).
**What it is:** Step 2 Technical Approach for solicitation FA701421R0005, a large multi-award IDIQ (data engineering / AI-ML SME support to the Air Force Chief Data Office). Prime: Octo Consulting Group (1,100 staff) with 12 teammates.
**Why it is here:** Bill asked for the three things this document does that our final products should emulate: graphics (frequency, quality, layout), callout boxes (what they are used for), and prose tone. This file records what the document actually does, with numbers, and what to change in our pipeline to reproduce it. Section 6 maps each recommendation to the skill, script, or reference file that owns it.

**Read this alongside:** `reference/graphic-templates/illustrator-conventions.md` (calibrated on this same document in April 2026; layout taxonomy, sidebar format, density table, Pink-team checklist), `reference/proposal-writing-patterns.md` (the four winning patterns), `reference/style-guide.md` (register by type), `my-company/branding/brand-design-system.md` (palette and caption rule). This file does not repeat the layout taxonomy; it adds the measured numbers, the callout content rule, the tone analysis, and the wiring plan that the April file never got.

---

## 1. Document anatomy

| Part | Pages | Notes |
|---|---|---|
| Title page | 1 | POC block, "Prepared for" block with named Government recipients, data-restriction legend, program name spelled out (Visible Accessible Understandable Linked Trusted). |
| TOC, List of Figures, List of Tables | 2 | Every heading carries its PWS reference: "2.2.1.1 Data Acquisition [PWS 2.1.1]". |
| Glossary of acronyms | 4 | About 190 entries, two-column table. |
| Executive Summary | 4 | Own page numbering (1 to 4). One figure, four tables. |
| Technical Approach | 21 | Page numbering restarts at 1. Fourteen figures, six tables, eight callout boxes. |
| Appendix A, "Proposal without Graphics/Tables" | ~20 | The same narrative with every figure and table stripped out. Bill confirmed (2026-09-04) this was a proposal requirement, not insurance. It is cheap to generate mechanically; see section 7. |

**Page furniture.** Letter, roughly 1-inch margins. Header: company mark left, program name and solicitation number right, in the blue accent. Footer: "Step 2: Technical Approach", date and page number, and the data-restriction legend in italic. Body text is Times New Roman 12 pt; every table, callout, caption, and figure label is Arial Narrow 9.8 pt. Section headings are blue; run-in lead-ins alternate blue and orange. Two accent colours plus navy and grey, used identically in prose, tables, callouts, and figures. That consistency is most of what reads as "polished".

**Known defects that survived to submission** (evaluators forgave them; our lints would not): four "Error! Reference source not found." field errors on pages 1, 6 and 20 of the technical approach; a callout header ("Data/AI/ML Training Success") reused on page 8 above an unrelated story about PEO partnerships; a missing space in the heading "[PWS 2.2.3]Expertise and Administration". Polish is relative. Density of proof mattered more than zero defects.

---

## 2. Graphics: frequency, quality, layout

### 2.1 Frequency (the headline number)

| Measure | Value |
|---|---|
| Body pages (exec summary + technical approach) | 25 |
| Figures | 15 |
| Tables | 10 |
| Callout boxes | 8 (7 unique) |
| Non-prose elements per page | 1.3 |
| Pages with no figure, table, or callout | 2 of 25 (page 1 of the technical approach, which is the numbered-principles page, and page 18) |
| Words per page | about 490 (range 310 to 750) |

The operating rule the document follows: **every page carries at least one thing an evaluator can score without reading a paragraph.** A figure, a table, or a proof-point box. The prose is there to connect them.

### 2.2 Inventory and archetypes

| Fig | Title | Archetype | Width | What it argues |
|---|---|---|---|---|
| 1 | Current Support across the AF Data Enterprise | 6-tile past-performance grid (program name, 3-line scope, icon) | Full | "We are already inside the customer's enterprise in six places." |
| 2 | DataOps | 6-step process, icon diamonds on chevrons, bullet column under each step | Full | Their methodology, named, with the customer's end state (Exploit) in orange. |
| 3 | Data Acquisition and Preparation | Three linked cycle diagrams, each with a one-sentence summary band beneath | Full | Three PWS sub-tasks answered in one figure. |
| 4 | Agile Algorithm Development | Flow of boxes with annotations above and below each node | Full | Engineering process with decision inputs visible. |
| 5 | Technology Insertion Model | Three chevrons, bullets under each | Full | Identify, evaluate, qualify. |
| 6 | Phased Approach to DOC Establishment | Composite: org chart on top, three-phase chevron plan, milestone timeline with diamonds, strategic-imperative box | Full, tall | The single most information-dense graphic; answers "who, in what order, gated by what." |
| 7 | Encapsulating Controls within Layers | Layered stack (Applications to Networking) with inheritable-controls and continuous-monitoring rails, three discipline panels on the left | Full | The cATO argument: inherited controls reduce recertification. |
| 8 | RRAD | Dashboard screenshot | Full | "This exists." Weakest figure; screenshot with no annotation. |
| 9 | Data Governance Components | Four horizontal bands (What, Who, Why/How/When, Tools) with icon and chips | Full | Taxonomy the customer can adopt. |
| 10 | 13-Point Data Maturity Assessment | Numbered ladder | Half, text wraps left | A proprietary assessment instrument, shown rather than described. |
| 11 | Gartner Maturity Curve | Curve with named stages and a "chasm" marker | Full | Borrowed analyst frame, relabelled with their positioning. |
| 12 | PADDLS | 2x4 imagery grid: pre, post, mask, classification | Full | Model output as proof. |
| 13 | Applied R&D Approach | Four-phase chevrons with bullet columns | Full | Phase 0 to 3. |
| 14 | Streamlined ML | List of eleven algorithm classes as a figure, with an "average implementation time" footer | Half, text wraps left | A capability list turned into an artefact. |
| 15 | OPAL | Hub-and-spoke process wheel with eight labelled satellites | Full | Their PM system, named. |

Archetypes used more than once: **chevron phase plan with bullet columns** (Figs 2, 5, 6, 13), **cycle or flow** (3, 4, 15), **layered stack** (7), **ladder or list-as-figure** (10, 14), **evidence imagery** (8, 12), **tile grid** (1, and Table 1).

### 2.3 What makes them read as high quality

1. **One visual grammar for the whole volume.** Same rounded rectangles, same chevrons, same four colours (navy, blue, orange, green) with grey for neutral, same icon style. Orange is reserved for the end state or the customer-facing outcome in every figure (Exploit in Fig 2, Phase 3 FOC in Fig 6, "Deploy to any Infrastructure" in Fig 7). An evaluator learns the grammar on page 2 and reads every later figure faster.
2. **Every figure is a self-contained argument.** Each one carries enough text that it could be pulled out and still make its point: step names, two to four bullets per step, and in Fig 3 a one-sentence summary band under each panel. Nobody has to read the paragraph to understand the figure.
3. **Figures answer PWS structure.** Fig 3's three panels are PWS 2.1.1, 2.1.2 and the data model; Fig 6 is PWS 2.2.2 end to end. The figure is placed on the page where that PWS reference is discussed, never deferred to an appendix.
4. **Composite figures where the requirement is composite.** Fig 6 combines org chart, phase plan, milestones and outcome because the PWS task is "stand up and operate a centre." One figure, one task.
5. **Label sizes hold.** Labels in the full-width figures render at roughly 8 to 9 pt; the bullet text inside Fig 2 is about 9 pt. That is the floor our `lint-rendered-artifact.py` enforces (7 pt HIGH, 7 to 9 pt advisory), so their convention and our gate agree.
6. **Every figure has a version tag** (for example `20_USAF_VAULT_011-R4`) in 4-pt grey in the corner. Their graphics were a managed library with revision control, not one-off drawings.
7. **Captions are two-part and mostly action captions.** Bold "Figure N: Title." then an italic sentence stating what the figure proves ("Data becomes actionable information through acquisition and preparation."). Three of fifteen are title-only or weak (Figs 6, 8, 10); the rest follow the rule we already have in `my-company/branding/brand-design-system.md` section 10.

### 2.4 Layout rules they follow

- **Full width is the default.** Twelve of fifteen figures span the text column at 2.5 to 3.5 inches tall. Nothing is pushed to a page of its own; a figure sits between the paragraph that introduces it ("Figure 3 addresses...") and the paragraph that walks it.
- **Half width with text wrap** for tall narrow figures (Fig 10 ladder, Fig 14 list) and for every callout box. The wrapped column is about 55 to 60 percent of the text width; the graphic or box takes 35 to 45 percent and sits flush right (twice flush left for variety, page 9 of the technical approach).
- **Figure, then table, then prose** is the common page rhythm: page 7 of the technical approach has Table 5, Figure 4, and Table 6 with three short prose bridges. No page has two full-width figures stacked.
- **Tables are styled as graphics.** Dark navy title band across the top ("Table 6: Team Octo's Approach to Test and Evaluation by ORL."), orange-tinted header row, Arial Narrow body, first column bold. A table and a figure look like siblings.
- **Tables carry the argument as often as figures do.** Table 3 is a two-column "Qualification | USAF SAF/CO Benefit" table (feature and benefit, with run-in bold lead-ins in each cell). Table 4 is a quantified experience snapshot (customer, cloud, users, two key metrics, data types, overview). Table 10 is a requirement-by-requirement response to PWS 6.0, three columns: PWS number, requirement, our plan.

---

## 3. Callout boxes: what they are used for

### 3.1 The format

A single-cell box about 2.6 inches wide, thin navy border, **navy header bar with a white bold title**, white body in Arial Narrow 9.8 pt, 60 to 90 words. Text wraps around it. It is placed beside the paragraph whose claim it substantiates, on the same page, never on the next.

### 3.2 The seven unique boxes

| Page (TA) | Header | Content type | The number in it |
|---|---|---|---|
| 2 | Data Acquisition for AF DCGS | Past performance | Seven DCGS Programs of Record at U, S, and TS/SCI |
| 4 | Architecture at Kessel Run | Past performance | 22 clusters, three AWS regions, over 1 billion transactions per month |
| 5 | Data/AI/ML Training Success | Past performance | 200 instructor-led classes, 3,000+ students, 56,000 self-paced enrolments |
| 8 | (header reused by mistake) | Past performance | PEO / requirements-owner partnerships, machine-to-machine tasking to weapon |
| 9 | Technology Assessment, US Army | Past performance with result | Integration time cut by 40 percent |
| 9 | Ability to Secure and Retain SMEs | Corporate proof | 86 percent retention over 10 years, 11 points above the industry average of 75 |
| 11 | RMF Support to SMC Kobayashi Maru | Past performance with result | 55 days from start to first deployment on SIPR; cATO SME co-founded Kessel Run |
| 13 | Data Governance at HHS | Past performance | Program spans all HHS operating divisions; Covid-19 dashboards as visible result |

### 3.3 The rule they follow, stated plainly

**A callout box is one past-performance proof point: a named customer or program, a number, and a result, placed beside the approach paragraph it proves.** Nothing else goes in a box. Not definitions, not quotations from the solicitation, not warnings, not win-theme slogans, not "why this matters" commentary.

This division of labour is the thing to copy. The body prose stays in the approach register ("Team Octo will...", "our SMEs will...") and does not stop every third sentence to say "as we did at X." The sidebar carries the evidence in a form an evaluator can score by skimming: header names the customer, body gives the metric. An evaluator writing a Strength can lift the box almost verbatim into the evaluation notice.

Corollaries:

- **Header is a noun phrase naming the work, not a slogan.** "Architecture at Kessel Run", not "Proven Cloud Expertise".
- **One box per proof point.** Two boxes on the same page when two different claims each need one (page 9).
- **The box answers the paragraph next to it.** Data Acquisition paragraph, DCGS data-acquisition box. Architecture paragraph, Kessel Run architecture box. Certification and accreditation paragraph, Kobayashi Maru RMF box.
- **Roughly one box per three pages.** Eight in 25 pages. More would dilute; they are used where the claim is a scored discriminator.
- **In our vocabulary, a callout box is one evidence-ledger item rendered as a sidebar.** Every box above would be one `EV-` record in `my-company/evidence-ledger.json`: customer, metric, outcome, citation. That is the operational hook for section 6.

---

## 4. Tone and prose

### 4.1 Measured properties of the body text

| Property | VAULT | Our current doctrine | Note |
|---|---|---|---|
| Mean sentence length | 31 words (median 25) | about 20 words | Theirs is long by our standard. It reads fine because sentences are noun-dense, not clause-dense. |
| Bullet lines as share of all lines | 4.6 percent | 10 to 35 percent advisory | Prose-dominant; bullets appear only inside tables and figures and in three short lists. |
| Lines containing bold inside a body sentence | 98 of about 1,400 | White-paper register bans it | Run-in lead-ins and bolded key phrases are a deliberate scanning device. |
| "Team Octo will" / "Team Octo SMEs will" / "We will" / "Our SMEs will" | 48 occurrences in 12,300 words | "we will" stacking is an advisory | One per 250 words. Every future commitment is paired with a named past instance. |
| Marketing adjectives | proven 9, leading 9, robust 4, innovative 2, world-class 1, cutting edge 2 | Banned list | Present but sparse: about one per 400 words, and usually attached to a named thing ("proven TRL9 open source and COTS products"). |
| Solicitation language mirrored | "utilize data as a strategic asset" quoted five times; every heading carries "[PWS x.y]"; VAULT expansion used as a sentence in the governance section | Style guide principle 3 | They mirror harder than we do. |

### 4.2 The paragraph pattern

Nearly every paragraph in the technical approach has the same skeleton:

1. **Approach commitment, future tense, named actor.** "Team Octo SMEs will analyze functional and non-functional business requirements and translate them into technical data requirements..."
2. **Specific mechanism.** Tool names, standards, networks: NiFi, Kylo, Talend, Hadolint, Anchore, DoDAF, ITIL, RMF, DoD 8570.01-M, NIPR/SIPR/JWICS/CENTRIXS/DREN, Iron Bank, Platform One.
3. **Named past instance, often with a number**, either inline ("at GSA, we are transforming nine federal acquisition systems into a single portal") or offloaded to the adjacent callout box.
4. **Benefit to the customer, in the customer's words.** "...to enable the USAF to meet its mission objective to 'utilize data as a strategic asset.'"

Where a section has several sub-requirements, each gets a **run-in bold lead-in in the accent colour** followed by a colon or full stop: "Service Enablement:", "Issue Management:", "Functionality.", "Scalability.", "Classification and Security.", "Data Stewardship:", "Policy Development and Dissemination:". An evaluator scanning for the PWS sub-bullet finds the lead-in, reads one paragraph, scores it. This is the mechanism that makes 31-word sentences survivable.

### 4.3 Register

Confident, declarative, first-person plural with the team name as subject. It is not restrained in our "almost understated" sense; it asserts constantly. What keeps it from reading as marketing is that **assertions are about mechanisms and named instances, not about qualities.** "Team Octo has delivered over 200 instructor-led classes" rather than "Team Octo is an experienced training provider." When an adjective does appear it is immediately followed by the noun that earns it.

Other register features worth naming:

- **Numbered principles at the top of the approach** (five, each beginning "Team Octo SMEs will...", each with one bolded phrase). A one-page frame the evaluator can hold the rest of the volume against.
- **Recommendations in the customer's interest, not only commitments.** "Team Octo recommends preparing data at the lowest possible classification level and using cross-domain solutions..." Reads as advisory partnership rather than vendor pitch, and it is scorable as understanding.
- **Explicit compliance sentences where the PWS is administrative.** "Team Octo acknowledges that the government will not be furnishing property or services..." One sentence, no elaboration.
- **Almost no hedging and no self-narration.** No "in this section we describe"; no "it should be noted." Transitions are a figure or table reference ("Figure 3 addresses...", "as described in Table 6").

### 4.4 What does not transfer

Octo bid a 1,100-person prime with 12 teammates on an IDIQ where breadth of past performance was the scored factor. Half the executive summary is a roll call of programs and headcount ("3,300+ engineers... 2,200+ hold clearances... 225+ have PhDs"). EdgeRunner cannot and should not write that paragraph. What transfers is the **shape**: each claim carrying a named instance and a number, whatever the number is. Our equivalents are named deployments (USASOC, 4th ID, 101st, Navy ICOP PMW 120), named agreements (AFRL CRADA, ARL CRADA), the IL-5 ATO and IL-6 IATT, measured benchmarks from the two papers, and the demo and trial results in the evidence ledger.

The white-paper register in `reference/style-guide.md` (flat, no bold in body, no rhetorical devices) stays as it is. The VAULT patterns belong to the **far-rfp, ota-proposal, and cso-full register**, where the style guide already says "assertive, plain, evaluation-criterion-aware." The run-in lead-in and the sidebar proof box are exactly how an assertive register stays scannable.

---

## 5. The transferable rules, in priority order

1. **Every page carries one scorable non-prose element.** A figure, a styled table, or a proof-point box. Two prose-only pages in 25 is the ceiling. Plan this at storyboard time, not at export.
2. **Proof lives beside the prose, not inside it.** Body paragraphs commit to the approach; a sidebar box carries the named-customer, numbered proof point. Each box is one evidence-ledger item.
3. **Figures are self-contained arguments.** Step names, two to four bullets per step, a one-line summary band where the figure has panels, and an action caption. Orange (or our red) reserved for the customer-facing end state.
4. **One visual grammar per volume.** Same shapes, same four-colour palette, same icon style, same caption format, and tables styled to match the figures (dark title band, tinted header row, condensed sans body).
5. **Headings mirror the solicitation.** Section heading carries the PWS or evaluation-factor reference; sub-requirements get run-in bold lead-ins in the accent colour.
6. **Every future-tense commitment is paired with a named past instance.** Inline if short, in a callout if it needs a number and a customer name.
7. **Full width by default, half width with wrap for tall narrow figures and for every callout.** No figure gets its own page. No two full-width figures stacked.
8. **Ship a graphics-free twin of the narrative** when the page limit excludes figures and tables, or when a plain-text reading is plausible. Mechanical to produce.

---

## 6. Where each rule lands in our pipeline

### 6.1 The finding that matters most: this was captured once already, and nothing reads it

`reference/graphic-templates/illustrator-conventions.md` was calibrated on this same document ("Air Force IDIQ technical volume, 52 pages, 2026-04-23"). It already describes the right-floating sidebar (section 3.2), the lead-in label pattern (section 1.3), a per-page density table (section 8), a Pink-team graphics checklist (section 9), and a proposed `callout-sidebar/` template (section 10, item 2). It is referenced by three other reference files and by **no skill and no script**. The writer, editor, graphics skill, and the Word renderer never consult it. The April capture produced a document; it did not change what the pipeline emits. This file exists to close that gap, so the rest of section 6 is a wiring plan rather than new doctrine.

### 6.2 Rule-by-rule: what exists, what is missing, where the change goes

| Rule (section 5) | Exists today | Gap | Change and owner file |
|---|---|---|---|
| 1. One scorable non-prose element per page | Density norm "1 to 2 figures per body page" in `reference/proposal-conventions/far-rfp.md` (line 99) and `reference/section-patterns/full-proposal.md` (line 62). | `proposal-storyboard` plans a "Graphic Argument" per section but not per page; nothing checks the rendered page count against figure plus table plus callout count. | Add a **page-budget row** to the storyboard (target pages, planned figures, planned tables, planned callouts) and a `visual-density` check to `scripts/lint-rendered-artifact.py`: ADVISORY when more than 2 consecutive rendered pages carry no figure, table, or shaded box. |
| 2. Proof beside the prose (callout = one ledger item) | Sidebar format and uses in `illustrator-conventions.md` section 3.2; evidence records with customer, metric, outcome in `my-company/evidence-ledger.json`. | No markdown syntax for a callout; `tools/md_to_docx.py` (syntax list at lines 24 to 34) has no admonition or shaded-box construct; `proposal-writer` and `proposal-editor` never mention sidebars. | Define one fenced block in the drafts, for example `:::callout Architecture at Kessel Run` with an `evidence: EV-###` line, render it in `md_to_docx.py` as a one-cell table with a navy header row and a light-fill body, floated right at 40 percent width (python-docx supports floating tables through `tblpPr`). Have `proposal-writer` bind pass emit one callout per section whose storyboard lists a discriminator with a numbered ledger item. Have `evidence-check` verify the `evidence:` line the same way it verifies inline cites. |
| 3. Figures as self-contained arguments with action captions | Action caption rule in `.claude/skills/proposal-graphics/SKILL.md` (lines 38 to 57) and `reference/proposal-writing-patterns.md` Pattern 3; caption format in `my-company/branding/brand-design-system.md` section 10. | Renderer flattens the caption: `md_to_docx.py` lines 452 to 473 render the blockquote uniformly italic with no bold figure number and no auto-numbering. The graphics skill has no "summary band under each panel" or "2 to 4 bullets per step" rule. | In `md_to_docx.py`, render a blockquote that begins `Figure N:` or `Table N:` as bold label plus italic sentence, 9.5 pt, centred, keep-with-previous. Add to the graphics skill: every panel or step carries 2 to 4 bullets and, for multi-panel figures, a one-line summary band. |
| 4. One visual grammar per volume, tables styled like figures | Palette and type scale in `my-company/branding/brand-design-system.md`; five parametric templates plus eight exemplars in `my-company/graphic-templates/`. | `md_to_docx.py` `process_table` (lines 135 to 167) applies plain `Table Grid` with a bold first row: no title band, no tinted header, no condensed body font. The design system is dark-first (near-black canvas), which is right for slides and wrong for a white Word page. | Add a **light-page figure variant** to the design system (white canvas, navy and grey structure, brand red reserved for the end state) and make it the default for `--target docx`. Extend `process_table` to emit a title band row and a tinted header row when the table is preceded by a `Table N:` line. |
| 5. Headings mirror the solicitation; run-in lead-ins for sub-requirements | Lead-in label pattern in `illustrator-conventions.md` section 1.3 (line 111); style guide principle 3. | Not stated in `proposal-writer` or `proposal-editor`; no convention for putting the PWS or factor reference in the heading text. | Add to `proposal-writer` bind pass: heading text carries the solicitation reference in brackets when the type is far-rfp, ota-proposal, or cso-full; each sub-requirement under a heading opens with a bold run-in lead-in that names it. Add the same as an editor preservation rule so the editor does not strip them. |
| 6. Every commitment paired with a named instance | Pattern 2 (discriminator proof points) in `proposal-writing-patterns.md`; `prose-lint.py` counts "we will" (threshold 8, `reference/prose-lint-rules.json` lines 134 to 140). | No "Company will" stacking rule (only the paragraph-opener repeat at 3). No check that a future-tense commitment paragraph contains a past-tense named instance or a callout. | Extend the `we_will` counter to include "EdgeRunner AI will" and "our engineers will". Add an ADVISORY `unpaired-commitment`: a paragraph with two or more future-tense commitments and no ledger cite, no past-tense customer name, and no adjacent callout. |
| 7. Full width default, half width with wrap for tall figures and callouts | Sizing table in the graphics skill (lines 263 to 264) lists a 5-inch half-column size. | `md_to_docx.py` `add_figure` (lines 212 to 239) always centres at full text width; no float, no wrap. | Add a `width=half` attribute on the figure comment (`<!-- figure: NAME width=half -->`) that anchors the image in a floating one-cell table at 40 percent width, right-aligned, text wrapping. Same mechanism as the callout. |
| 8. Graphics-free twin of the narrative | Nothing. | Nothing. | `export-proposal --no-graphics` flag that runs the same conversion with figures, tables, and callouts stripped and a note line where each stood. Only when the type's page-limit rule excludes graphics, or on request. |

### 6.3 Two lint rules that currently fight this style

`scripts/lint-rendered-artifact.py` fires HIGH on any bold run after the first inside a sentence (rule `mid-bold`, lines 149 to 167) and on **any** non-black text run (rule `text-colour`). Both were added on 2 September from the NAVWAR EPSS lessons, and both are right for the white-paper register. They also make the VAULT page unrepresentable: the blue section headings, the coloured run-in lead-ins, and the white-on-navy callout headers would all fire.

Recommendation: keep both rules as written for `white-paper`, and make them **register-aware** by reading `working/proposal-type.md`. For far-rfp, ota-proposal, and cso-full: `text-colour` allows the two brand accent colours in heading styles, run-in lead-ins, and table or callout header rows, and still fires on coloured body text; `mid-bold` allows a bold run that is a defined key phrase (under six words) at most once per paragraph, and still fires on bold sentences. The lint should never be the reason a proposal looks less like the winning example.

### 6.4 Suggested order of work

1. **Callout block end to end** (syntax, renderer, writer bind rule, evidence-check). This is the highest-value single change: it moves proof out of the prose and gives the evidence ledger a visible output. One day of work.
2. **Caption and table rendering** in `md_to_docx.py` (bold figure label, title band, tinted header, condensed font). Half a day; every existing proposal benefits on the next export.
3. **Register-aware lint** for `mid-bold` and `text-colour`. Two hours, and it must land before 1 and 2 or every render fails the gate.
4. **Light-page figure variant** in the design system and templates. One to two days; needed before we can embed our HTML figures on a white page without them reading as screenshots of a dark dashboard.
5. **Writer and editor rules** for solicitation-mirroring headings and run-in lead-ins. Prompt changes only.
6. **Storyboard page budget and density advisory.** Small.
7. **Half-width figure wrap and the graphics-free export.** Nice to have; do when a solicitation calls for either.

None of these change the white-paper register. All of them apply to the three registers where the style guide already asks for "assertive, plain, evaluation-criterion-aware" prose.

---

## 7. Questions for Bill, answered 2026-09-04

1. **Appendix A was a proposal requirement.** The graphics-free twin is therefore a real export case, not insurance: build `export-proposal --no-graphics` (rule 8) when the next solicitation with a graphics-excluded page limit arrives, or earlier if convenient.
2. **The figures were built with a graphics artist at Bill's side.** The composite figures (Fig 6 class) are designer work; the HTML templates should cover the chevron, cycle, stack, ladder, and tile archetypes, and the graphics brief should say when a figure needs a designer.
3. **Light-page variant approved.** Build a light-page variant of the red-on-black design system for Word-embedded figures: white canvas, navy and grey structure, brand red reserved for the customer-facing end state. Next item after the callout block and register-aware lint.

## 8. Implementation status

| Item (section 6.4) | Status | Where |
|---|---|---|
| 1. Callout block end to end | Done 2026-09-04 | `tools/md_to_docx.py` (`:::callout` syntax, floating tagged table), `scripts/evidence_check_core.py` (audits the `evidence:` key line), `scripts/prose-lint.py` (fences and key lines are not prose), `proposal-writer` Step 2e, `proposal-editor` preservation rule, `evidence-check` skill note |
| 3. Register-aware lint and polish | Done 2026-09-04 | `tools/register.py` (type_id to register), `scripts/lint-rendered-artifact.py --proposal/--register`, `tools/polish_docx.py --proposal/--register`; `export-proposal` passes `--proposal` to both |
| 2. Caption and table rendering | Not started | `tools/md_to_docx.py` |
| 4. Light-page figure variant | Approved, not started | `my-company/branding/`, `my-company/graphic-templates/` |
| 5. Writer and editor heading and lead-in rules | Not started | skills |
| 6. Storyboard page budget and density advisory | Not started | `proposal-storyboard`, `lint-rendered-artifact.py` |
| 7. Half-width figure wrap; graphics-free export | Not started (export now confirmed as a real requirement) | `tools/md_to_docx.py`, `export-proposal` |
