# EdgeRunner AI — Brand Design System (Complete Reference)
*Exported from the EdgeRunner AI Design System project · May 2026*

> **Purpose.** This is the single source of truth for any AI agent or human
> producing branded visual artifacts for EdgeRunner AI. Import this file
> and `colors_and_type.css` into your workspace to enable on-brand output.

---

## 1. Brand Identity

- **Company:** EdgeRunner AI
- **Tagline:** Domain-specific AI for the warfighter
- **Founded:** 2024, Bellevue, WA
- **Identifiers:** CAGE 9Z176 · UEI SLZTJUA8DBD3 · NAICS 541511
- **Personality:** Military-precision, tactical, high-contrast, no-nonsense

---

## 2. Two Canonical Surfaces

EdgeRunner has two visual surfaces that share DNA but diverge on spec.
**Pick the surface first, then build with the matching conventions. Do not blend.**

| Attribute | Public Marketing (edgerunnerai.com) | Federal Proposal, dark (slides / HTML review) | Federal Proposal, light page (Word figures, added 2026-09-04) |
|---|---|---|---|
| Background | `#000000` (jet black) | `#191c20` (near-black) | `#ffffff` (the page); panels `#f2f3f5` |
| Brand red | `#EE2525` | `#ee2929` | `#c8102e` (dense red; `#ee2929` washes out on white) |
| Dense red (slides) | — | `#C8102E` | — |
| Structure | — | white text, `#393939` borders | `#191c20` bars and hero outlines, `#393939` strong borders, `#c8c8c8` hairlines |
| Font | Inter | Segoe UI (sub: Inter + Saira) | Segoe UI (sub: Inter) |
| Border radius | `0px` everywhere | 6/10/12px stack | 4/6/8px, no 12px slab |
| Canvas shadow | — | `0 8px 32px rgba(0,0,0,.4)` | none; 1px `#c8c8c8` hairline edge |
| Button style | Notched/chamfered via clip-path | Rectangular, 6px radius | n/a |
| Headline casing | Sentence case, often ends with period | UPPERCASE, letter-spacing 0.5px | UPPERCASE on bars and labels; sentence case in node text |
| Word documents | — | Times New Roman 12pt | Times New Roman 12pt |

**Which surface.** A figure that will be embedded in a `.docx` uses the **light page** surface: it sits on white paper next to tables and callout sidebars and must look like their sibling, not like a screenshot of a dashboard. Slides, pitch decks, the HTML review copy, and the website stay dark. Never mix the two in one document.

### 2a. Light page surface: rules

Calibrated on the Octo USAF VAULT technical volume (`reference/winning-examples/usaf-vault-octo-2020-lessons.md`, section 2.3). CSS: `branding/proposal-graphics-light.css` (load after `proposal-graphics.css`). Template presets: `branding/surfaces.json`, applied with `scripts/render-graphic.py --surface light`.

1. **One accent, reserved for the end state.** Brand red marks the customer-facing outcome in a figure (the delivered answer, the FOC phase, the deployed capability) and nothing else. EdgeRunner components are drawn as strong dark outlines (`#393939` on white), not in red. This is the VAULT orange rule with our colour.
2. **Structure is dark and grey.** Header bars and summary bands are `#191c20` with white bold uppercase text, the same treatment as the callout sidebar header, so figures, tables, and callouts share one grammar on the page.
3. **The middle state is amber, the pass state is green, both muted.** Text `#8a6a00` on `rgba(200,162,0,.12)`; text `#2e6b3a` on `rgba(46,107,58,.10)`. Never saturated.
4. **No canvas slab, no shadow, no glow.** The figure's edge is a 1px hairline. Depth comes from panel fill against the page.
5. **Every figure is a self-contained argument.** Named steps, two to four bullets or one line per step, and for multi-panel figures a one-line summary band under each panel stating what the panel proves. An action caption below the figure in the document.
6. **Label floor stays.** 24px on a 1200px canvas at a 6.5-inch embed is 9.4pt; nothing smaller.
7. **Known gap.** The parametric templates still carry a few hard-coded dark fills (input pills `#1e2124`, footer bars, `rgba(238,41,41,.04)` washes) that the preset cannot reach. Fix them in the template the first time it is rendered for the light page, replacing each with a `{{theme.*}}` token; `platform-architecture` is the first candidate.
8. **Tokens.** `--pg-canvas #ffffff`, `--pg-card #f2f3f5`, `--pg-border #c8c8c8`, `--pg-border-strong #393939`, `--pg-ink #191c20`, `--pg-red #c8102e`, `--pg-fg-1 #191c20`, `--pg-fg-2 #393939`, `--pg-fg-3 #6f6f6f`.

---

## 3. Color Palette

### Primary
| Token | Hex | Usage |
|---|---|---|
| `--er-red` | `#EE2525` | CTA, announcement bar, accents (public) |
| `--er-red-proposal` | `#ee2929` | Proposal graphics accent |
| `--er-red-slide` | `#C8102E` | Dense dark slides where `#ee2929` is too bright |
| `--er-red-dark` | `#c81d1d` | Hover / pressed primary |

### Neutrals
| Token | Hex | Usage |
|---|---|---|
| `--er-black` | `#000000` | Public page background |
| `--er-charcoal` | `#1A1A1A` | Footer surface |
| `--er-near-black` | `#191c20` | Proposal canvas |
| `--er-gunmetal` | `#393939` | Cards, panels |
| `--er-bg-tier` | `#2a2d31` | Tier card fills |
| `--er-bg-tier-soft` | `#222528` | Boundary labels, sunken pills |
| `--er-border` | `#393939` | Tier borders, dividers |
| `--er-border-soft` | `#2a2d31` | Cell borders |
| `--er-rule` | `#4a4a4a` | Boundary dashes |
| `--er-grey-medium` | `#9f9f9f` | Subtitles, captions |
| `--er-grey-light` | `#c8c8c8` | Body text on dark |
| `--er-white` | `#ffffff` | Headings, primary labels |

### Tints
| Token | Value | Usage |
|---|---|---|
| `--er-red-tint-08` | `rgba(238,41,41,0.08)` | Subtle fills, hero tier bg |
| `--er-red-tint-12` | `rgba(238,41,41,0.12)` | Column headers, callouts |
| `--er-red-tint-15` | `rgba(238,41,41,0.15)` | Hero tier fills |
| `--er-red-tint-40` | `rgba(238,41,41,0.40)` | Commitment borders |

### Categorical / Status
| Token | Hex | Usage |
|---|---|---|
| `--er-amber` | `#c8a200` | "Partial" / middle-state indicator |
| `--er-link` | `#228BE6` | Inline links only |

### Rules
- **Single accent rule.** One red — never two warm accents.
- **Dark canvas dominant on screen.** No light backgrounds on branded screen surfaces (exception: internal dashboard). Figures embedded in a Word document use the light page surface (section 2a) instead.
- **No gradients** except the hero overlay on edgerunnerai.com.
- **Tier hierarchy via tint, not hue.** Same red at opacity stops (.08/.12/.15/.40).

---

## 4. Typography

### Families
| Role | Canon | Web Substitute |
|---|---|---|
| UI / body | Segoe UI | Inter (Google Fonts) |
| Display / wordmark | Segoe UI Bold | Saira (Google Fonts) |
| Monospace | — | JetBrains Mono |
| Documents | Times New Roman 12pt | — |

### Scale — Public Site (marketing)
| Element | Size | Weight | Notes |
|---|---|---|---|
| H1 hero | 68px | 700 | line-height 1.1 |
| H2 section | 44px | 700 | Often ends with period |
| H3 subhead | 24px | 600 | |
| Body | 16px | 400 | `rgba(255,255,255,0.70)` |
| Caption | 13px | 400 | `rgba(255,255,255,0.60)` |
| Button | 14px | 500 | |

### Scale — Proposal Graphics (1200px canvas)
| Element | Size | Weight |
|---|---|---|
| Title | 26–28px | 700 |
| Tier name | 22px | 700 |
| Body | 17px | 400 |
| Secondary | 15px | 400 |
| Caption/micro | 11–13px | 700 |

### Rules
- **Sentence case** on public site; **UPPERCASE with letter-spacing 0.5px** on proposal graphics.
- **No italic** — strong, upright type throughout.
- Public section headings frequently end with a **period**.
- Nav links prefixed with `/` slash.

---

## 5. Buttons

### Public — Notched/Chamfered
- `0px` radius with diagonal cut at bottom-left via `clip-path`.
- All CTAs end with `›` chevron.
- Variants: `er-btn-primary` (red/white), `er-btn-secondary` (white/black), `er-btn-ghost` (transparent/white outline).

### Proposal — Rectangular
- `6px` radius, red fill. Buttons rare in proposal graphics.

---

## 6. Layout & Spacing

### Spacing Scale
`4 · 8 · 12 · 16 · 20 · 24 · 32 · 48 · 64` px

### Canvas
- **1200px wide** for proposal graphics, padded 18–32px.
- **Card padding:** 11–14px (cells), 18–32px (panels).

### Radii
| Context | Value |
|---|---|
| Public (all) | `0px` |
| Proposal outer canvas | `12px` |
| Proposal tier cards | `10px` |
| Proposal pills | `9999px` |
| Proposal tiles | `6px` |
| Proposal small | `4px` |

### Shadows
| Token | Value | Usage |
|---|---|---|
| `--shadow-canvas` | `0 8px 32px rgba(0,0,0,0.40)` | Lift canvas off Word page |
| `--glow-red` | `0 0 18px rgba(238,41,41,0.45)` | Emphasis on brand red |
- **No drop shadows on cards or text.** Both surfaces are flat.

---

## 7. Borders & Boundaries

- **Public:** `1px` hairlines in `rgba(159,159,159,0.30)`.
- **Proposal:** `1.5px` solid `#393939` on tier cards; `2px` solid `#ee2929` on hero tier.
- **Boundary lines:** `1.5px dashed #4a4a4a` with capsule label (`#222528` bg, `#4a4a4a` border, `9999px` radius, `11px` uppercase bold).

---

## 8. Cards

- Fill: `#2a2d31` (neutral) or `rgba(238,41,41,0.08)` (hero).
- Border: `1.5px solid #393939` (neutral) or `2px solid #ee2929` (hero).
- Radius: `10px`.
- Padding: 11–14px cells, 18–32px panels.
- **No shadow.** Depth via background contrast.

---

## 9. Imagery & Iconography

### Imagery
- **No stock photos, no AI-generated imagery, no hand-drawn illustrations.**
- All visuals are SVG/HTML geometric primitives.
- Customer logos displayed in white/greyscale monochrome on dark bg.
- Military photography (when used): grayscale, dark overlay.

### Icons
- **No custom icon set.** Recommended substitute: **Lucide** (MIT, line style).
- Icons are **categorical, not decorative** — a chip means compute, a satellite means ISR.
- **No emoji** in customer-facing artifacts (internal dashboard exception).
- **No mixing** line + filled styles in the same artifact.

### Logo
- `edgerunner-logo.png` — white-on-transparent wordmark. Only legible on dark.
- Angular red "R" mark approximated via CSS clip-path (see `colors_and_type.css`).

---

## 10. Voice & Content

### Tone
- **Direct, technically grounded, no filler.** Evaluator has 15 minutes and a red pen.
- **Problem-first.** Lead with what's broken, then present the solution.
- **Operational layer framing.** EdgeRunner *connects* enterprise AI to the edge.

### Banned Words
*robust, innovative, cutting-edge, leverage* (verb), *utilize, in order to, the fact that*

### Naming
- **EdgeRunner AI** (full name), never "EdgeRunner" alone.
- **Government**, never "Govt".

### Captions
Action captions, two-part: `Figure N: [Title]. [What the graphic proves.]`

---

## 11. Animation & Interaction

- **Proposal graphics are fully static** (rendered to PNG for Word embed).
- Hover: brighten 4–6% white tint. No scale, no shadow expansion.
- Press: drop opacity to 0.85.
- Transitions: 120–160ms ease. No bounces, no springs, no parallax.

---

## 12. File Inventory

| File | Purpose |
|---|---|
| `branding/colors_and_type.css` | All design tokens — import in every HTML graphic |
| `branding/proposal-graphics.css` | Proposal-specific component classes (canvas, tier, pill, boundary, tile, comparison), dark surface |
| `branding/proposal-graphics-light.css` | Light page surface for Word-embedded figures; loads after the dark kit and re-skins the same classes, plus `.pg-bar`, `.pg-band`, `.pg-node-*` |
| `branding/surfaces.json` | `dark` and `light` theme presets for the parametric templates (`render-graphic.py --surface`) |
| `branding/edgerunner-logo.png` | White-on-transparent wordmark |
| `branding/brand-design-system.md` | This file |
| `branding/components/` | Reusable JSX component snippets (Canvas, TierBlock, etc.) |
| `graphic-templates/` | Parametric templates (template.html + schema.json + example-data.json) |
