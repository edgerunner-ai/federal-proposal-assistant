# Claude Design vs. Current Proposal-Graphics Workflow — Evaluation

**Author:** Claude (Opus 4.7) | **Date:** 2026-04-30
**Question:** Would adopting Anthropic's "Claude Design" meaningfully improve the federal proposal graphics this repo produces vs. the current `/proposal-graphics` workflow?

**One-line answer:** No — keep the current workflow for proposal graphics. Adopt Claude Design selectively for **adjacent** artifacts (pitch decks, one-pagers, capture briefs) where it actually plays to its strengths.

---

## 1. What "Claude Design" actually is

Anthropic Labs launched Claude Design on **April 17, 2026** — a Claude Opus 4.7-powered product for generating "designs, prototypes, slides, one-pagers, and more" from natural-language prompts and refining them through inline comments / direct edits / sliders.

Confirmed facts (from Anthropic, TechCrunch, MacRumors, VentureBeat, and a hands-on review by Victor Dibia):

| Aspect | What it does |
|---|---|
| **Output types** | Interactive prototypes, mockups, pitch decks, one-pagers, marketing collateral, code-powered prototypes (voice/video/3D) |
| **Export formats** | Canva, PDF, **PPTX**, standalone HTML, internal org-scoped URLs |
| **Design-system** | At setup, "Claude builds a design system for your team by reading your codebase and design files. Every project after that uses your colors, typography, and components automatically" |
| **Code handoff** | "When a design is ready to build, Claude packages everything into a handoff bundle that you can pass to Claude Code with a single instruction" |
| **Access** | Research preview — Pro / Max / Team / Enterprise (Enterprise requires admin enablement). Uses subscription limits with optional extra-usage. |
| **Positioning** | Anthropic explicitly aims it at **"founders and product managers without a design background"** (TechCrunch); positions it as complementary to Canva, not Figma |
| **Honest weakness** (Dibia review) | "Initial outputs prioritize visual interest over clarity" — first prototypes look appealing but mis-map to underlying data; humans must validate that visuals communicate truth |

**It is *not*** the same thing as the **Claude Code → Figma** integration (a separate Feb 2026 product that captures running UIs into Figma frames; UI-only, not for diagrams or slides). And it is not a built-in Claude Code feature — it's a separate web product with a Code-handoff path.

**Caveat I want to flag.** No public review I found tested Claude Design on **technical architecture diagrams** specifically. Marketing demos showcase a meditation-app prototype and an interactive globe. Federal proposal graphics — three-tier architectures with DDIL boundaries, capability-to-evidence matrices, swim-lane timelines with go/no-go gates — are not the use case Anthropic markets it for.

---

## 2. Current implementation — what's actually in this repo

The `/proposal-graphics` skill ([.claude/skills/proposal-graphics/SKILL.md](.claude/skills/proposal-graphics/SKILL.md)) and its supporting infrastructure is already a mature, opinionated graphics pipeline tuned for the specific failure modes of federal proposals:

### Pipeline

```
working/graphics-brief.md  (spec — wireframe, components, action caption, "what this proves")
       ↓
graphics/fig<N>-<pattern>.html  (deterministic fill of parametric template OR free-form HTML)
       ↓
graphics/rendered/fig<N>-<pattern>.png  (headless Chrome at 2× DPI, 2400×1600 for full-column embed)
       ↓
final/docx/  (Word embed at 6.5" width)
```

### Components

- **Parametric templates** in [reference/graphic-templates/](reference/graphic-templates/) — `three-tier-architecture` and `capability-matrix` shipped today, four more (`swim-lane-timeline`, `lifecycle-loop`, `objectives-split`, `differentiator-comparison`) defined in the framework but deferred until next use.
- **Deterministic renderer** [scripts/render-graphic.py](scripts/render-graphic.py) — `{{field}}` / `{{a.b.c}}` / `<!-- REPEAT:items -->` substitution with `--strict` mode; no template engine, no dependencies.
- **Schema-validated input** — every template has a `schema.json` with `maxLength`, `minItems`/`maxItems` constraints derived from what fits the SVG layout.
- **Brand palette codified** in [my-company/brand-palette.md](my-company/brand-palette.md) — EdgeRunner dark/red plus a darker `#C8102E` slide variant for dense layouts; tier-specific fill/stroke/text rules.
- **Override path** — `my-company/graphic-templates/<pattern>/` takes precedence over `reference/graphic-templates/<pattern>/`, so per-customer or per-program palettes don't fork the framework.
- **Print-legibility math** — pixel-to-point formula `(E × 72) ÷ W`, with a binding minimum (≥10pt body / ≥12pt heading / ≥18pt title) on a 1200×800 canvas embedded at 6.5" wide. This rule was burned in after an earlier default produced 5.4pt text on paper.
- **Action-caption discipline** (Pattern 3 from `reference/proposal-writing-patterns.md`) — captions live in the Word doc text, not in the graphic; every figure asserts what it *proves*, not what it shows; if you can't write an action caption, the graphic shouldn't exist.
- **Anti-patterns documented** — no emojis, no IL-level badges inside boxes, no figure numbers in the graphic title, no off-brand accents, no key-metric taglines at the bottom. These came out of SOCPAC lessons-learned.
- **Production usage** — graphics are rendered for `mystic-depot`, `nato-diana`, `socpac`, `dod-openweight-whitepaper`, `extic-26-2`, `senate-*`, `ngb-enterprise-data-ai`, `ae-mmp`, `ITDX26-AI-Analyst` (8+ active proposals). Confirmed PNG outputs exist in e.g. [proposals/dod-openweight-whitepaper/graphics/](proposals/dod-openweight-whitepaper/graphics/).

### What this stack is good at

- Architecture diagrams that need exact tier coding and DDIL boundary semantics
- Reproducible re-renders when content edits land late in a proposal cycle
- Brand consistency across 14 active proposals over months
- Print-legible output sized for Word embed at federal page sizes
- Cheap iteration — templated graphics cost ~200–500 tokens for the data layer instead of regenerating HTML every run

### Gaps (visible in code, regardless of the Claude Design question)

- Only 2 of 6 templates the framework calls out are actually shipped. SOCPAC lessons-learned describe `swim-lane-timeline` as a pattern that **worked**, but it isn't shipped as a template — meaning every new swim-lane diagram falls back to free-form HTML generation (5–10k tokens, variable quality).
- `my-company/capabilities.md` is flagged in CLAUDE.md as incomplete — content quality of any capability-matrix graphic depends on it.
- No Figma round-trip exists. If you ever want a human designer (or yourself in Figma) to polish a graphic post-render, you'd export PNG and lose the structure.
- HTML is the editable master, but there's no live preview server — you re-render to PNG, open the file, eyeball it. The `dashboard` skill exists but is portfolio-state, not graphic preview.

---

## 3. Side-by-side comparison

| Dimension | Claude Design | Current `/proposal-graphics` |
|---|---|---|
| **Primary user** | Founders / PMs without design background | A senior solution architect rendering evaluator-graded artifacts |
| **Output formats** | Canva, PDF, PPTX, HTML, web URL | HTML → PNG @ 2× DPI for Word embed; optional PPTX via `/export-proposal` |
| **Federal print legibility (≥10pt body @ 6.5" embed)** | Not a tuned target | Hard rule with pixel-to-point math |
| **Brand application** | Reads codebase + design files at setup; generative every time | Palette codified; parametric templates pre-tested; override path; no drift |
| **Reproducibility** | Generative — varies run to run | Deterministic placeholder fill — identical pixels every render |
| **Token cost per graphic** | One full generation per refinement | ~200–500 tokens (data only) when a template matches; ~5–10k for free-form fallback |
| **Action-caption discipline** | Not a concept the tool understands | Mandatory; enforced by Gold Team review |
| **Federal vocabulary** (DDIL, tier accents, registry pills, IL badges) | None | Built into templates, schema, and palette |
| **Iteration UX** | Inline comments / direct edits / sliders in a web UI | Edit JSON data, re-run renderer; or edit HTML directly |
| **Code handoff** | Packages a "handoff bundle" for Claude Code | Already inside Claude Code; nothing to hand off |
| **Data-handling for CUI / sensitive content** | Cloud product; check Anthropic Enterprise terms before any CUI graphic | Local files only; nothing leaves the workspace |
| **Maturity** | Research preview, ~2 weeks old | Used in production across 14 active proposals |

### Where Claude Design would actually help in this workspace

1. **PPTX briefings outside the proposal volume itself** — OTA kickoff decks, capture review briefings, executive summaries to internal stakeholders. These are exactly the "polished slides for a non-design audience" use case Claude Design is built for, and `/export-proposal` already calls `anthropic-skills:pptx` — Claude Design could produce a richer first cut.
2. **One-pagers for BD / capture** — partner-ask sheets, capability briefs, teaming summaries for events. Federal-grade legibility math doesn't apply; speed and polish do.
3. **Pitch decks for non-government audiences** — investor updates, board materials, partner pitches. Different audience, different rules.
4. **First-pass exploration of a new graphic pattern before promoting it to a parametric template** — let Claude Design generate 3–4 visual concepts, pick the strongest layout, then codify it as a `reference/graphic-templates/<pattern>/`.

### Where it would *not* help — and could actively hurt

1. **Hero architecture figures inside proposal volumes.** The 8.5×11 print legibility rule, action-caption discipline, brand-tier semantics, and anti-pattern list (no emojis, no badge clutter, etc.) are codified in your skill specifically because earlier ad-hoc generation produced graphics that failed White Glove review. A generative tool that "prioritizes visual interest over clarity" (Dibia's words) is the wrong tool for a graphic an evaluator scores.
2. **Anything CUI-touching.** Any architecture diagram tied to a classified or CUI program shouldn't be uploaded to a research-preview cloud product without a clear data-handling answer.
3. **Compliance-sensitive figures** like the compliance matrix or capability-to-evidence table — these are deterministic translations of `working/compliance-matrix.json` and `my-company/evidence-ledger.json`. Generative styling adds nothing and risks visual drift between proposals.

---

## 4. Recommendation

**Keep `/proposal-graphics` as-is for proposal volumes.** Don't migrate. The current stack is purpose-built for the failure modes Claude Design isn't tuned for, and it's been validated across 14 proposals.

**Adopt Claude Design as a peer tool for adjacent artifacts**, not a replacement. Specifically:

| Use Claude Design for | Use `/proposal-graphics` for |
|---|---|
| Capture/BD one-pagers | Hero architecture figures (three-tier, etc.) |
| Pitch decks to non-government audiences | Capability-to-evidence matrices |
| Internal exec briefings | Swim-lane timelines with go/no-go gates |
| Partner-ask leave-behinds | Lifecycle / process loop graphics |
| First-pass design exploration of a new pattern | Anything embedded in the proposal Word doc |

### Higher-leverage improvements you could make to the existing workflow regardless

These would help more, faster, than swapping in Claude Design:

1. **Promote the four deferred templates** (`swim-lane-timeline`, `lifecycle-loop`, `objectives-split`, `differentiator-comparison`) into shipped templates. SOCPAC already proved swim-lane-timeline works as a pattern — codifying it cuts ~5–10k tokens per future swim-lane graphic and locks in the visual.
2. **Resolve `my-company/capabilities.md`** (flagged incomplete in CLAUDE.md). Any capability-matrix graphic is only as strong as that source.
3. **Add a Figma round-trip path** — wire the **Figma MCP** so a finalized graphic can be opened in Figma for hand polish or for a human designer's review. This is the genuinely useful Anthropic+design tooling for this workflow, separate from Claude Design itself. (Your Cowork plugins already include `figma:figma-implement-design` and friends — they just aren't part of `/proposal-graphics` yet.)
4. **Try `anthropic-skills:canvas-design` as the free-form fallback** — when no parametric template matches, today the skill regenerates HTML from scratch. The `canvas-design` skill (already in your installed Cowork plugins) is built around design-philosophy principles and could produce a stronger free-form draft than ad-hoc generation, while still landing in your `graphics/` HTML pipeline.

### Risks / unknowns

- **Claude Design is research preview.** Features, limits, and pricing can shift. Don't anchor a workflow on it.
- **Output quality on technical/architecture diagrams is unverified by independent reviewers.** Anthropic's marketing demos are a meditation app and an interactive globe; the one third-party evaluation I found (Victor Dibia) tested a marketing analytics widget, not architecture.
- **Data residency.** No public statement on where Claude Design renders or stores design system files. Treat as cloud until confirmed otherwise — relevant for any program with CUI handling restrictions.
- **The Figma MCP is a separate offering** with its own setup cost and is UI-screen-oriented (per Figma's blog: "captures a real, functioning UI from a browser"). It's not a clean fit for static architecture diagrams either, but it's the right shape for a hand-polish round-trip if you ever want one.

---

## Sources

- [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs)
- [Anthropic launches Claude Design (TechCrunch, 2026-04-17)](https://techcrunch.com/2026/04/17/anthropic-launches-claude-design-a-new-product-for-creating-quick-visuals/)
- [How Good is Anthropic's Claude Design? — Victor Dibia, *Designing with AI*](https://newsletter.victordibia.com/p/how-good-is-anthropics-claude-design)
- [Anthropic Debuts Claude Design (MacRumors)](https://www.macrumors.com/2026/04/17/anthropic-claude-design/)
- [Anthropic just launched Claude Design (VentureBeat)](https://venturebeat.com/technology/anthropic-just-launched-claude-design-an-ai-tool-that-turns-prompts-into-prototypes-and-challenges-figma)
- [From Claude Code to Figma (Figma Blog)](https://www.figma.com/blog/introducing-claude-code-to-figma/)
- [Claude Code and Figma: Set up the MCP server (Figma Help Center)](https://help.figma.com/hc/en-us/articles/39888612464151-Claude-Code-and-Figma-Set-up-the-MCP-server)
- Repo files reviewed: [.claude/skills/proposal-graphics/SKILL.md](.claude/skills/proposal-graphics/SKILL.md), [reference/graphic-templates/README.md](reference/graphic-templates/README.md), [reference/graphic-templates/three-tier-architecture/](reference/graphic-templates/three-tier-architecture/), [scripts/render-graphic.py](scripts/render-graphic.py), [my-company/brand-palette.md](my-company/brand-palette.md), [CLAUDE.md](CLAUDE.md)
