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

| Attribute | Public Marketing (edgerunnerai.com) | Federal Proposal (graphics/slides) |
|---|---|---|
| Background | `#000000` (jet black) | `#191c20` (near-black) |
| Brand red | `#EE2525` | `#ee2929` |
| Dense red (slides) | — | `#C8102E` |
| Font | Inter | Segoe UI (sub: Inter + Saira) |
| Border radius | `0px` everywhere | 6/10/12px stack |
| Button style | Notched/chamfered via clip-path | Rectangular, 6px radius |
| Headline casing | Sentence case, often ends with period | UPPERCASE, letter-spacing 0.5px |
| Word documents | — | Times New Roman 12pt |

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
- **Dark canvas dominant.** No light backgrounds on branded surfaces (exception: internal dashboard).
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
| `branding/proposal-graphics.css` | Proposal-specific component classes (canvas, tier, pill, boundary, tile, comparison) |
| `branding/edgerunner-logo.png` | White-on-transparent wordmark |
| `branding/brand-design-system.md` | This file |
| `branding/components/` | Reusable JSX component snippets (Canvas, TierBlock, etc.) |
| `graphic-templates/` | Parametric templates (template.html + schema.json + example-data.json) |
