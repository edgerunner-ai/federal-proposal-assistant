# EdgeRunner AI — Brand Design System
*Extracted from edgerunnerai.com · May 2026*

> **Superseded.** Use `my-company/branding/brand-design-system.md` — it covers both the marketing-site surface and the Federal Proposal surface, and is the source of truth for all visual artifacts. This file documents the marketing-site surface only.

---

## Brand Identity

**Company:** EdgeRunner AI  
**Tagline:** Domain-specific AI for the warfighter  
**Personality:** Military-precision, tactical, high-contrast, no-nonsense

---

## Color Palette

### Primary Colors

| Role | Name | Hex | RGB | Usage |
|------|------|-----|-----|-------|
| Brand Red | EdgeRunner Red | `#EE2525` | rgb(238, 37, 37) | CTA buttons, announcement bar, icons, accents |
| Background | Jet Black | `#000000` | rgb(0, 0, 0) | Page background, nav background, hero |
| Surface | Gunmetal | `#393939` | rgb(57, 57, 57) | Cards, panels, newsroom card |
| Primary Text | White | `#FFFFFF` | rgb(255, 255, 255) | All headings, body text on dark bg |

### Secondary / Utility Colors

| Role | Name | Hex | Notes |
|------|------|-----|-------|
| Muted Border | Dark Mist | `rgba(31, 30, 29, 0.4)` | Subtle element borders |
| Subtle Border | Gray Ghost | `rgba(159, 159, 159, 0.376)` | Dividers, input outlines |
| Link / Highlight | Mantine Blue | `#228BE6` | rgb(34, 139, 230) — inline links only |
| Footer surface | Charcoal | `#1A1A1A` (approx) | Footer background, slightly lighter than black |

### Color Rules
- Dark-mode-first: all sections are black or near-black
- Red is the **only** warm color; never use orange or yellow
- No gradients except the red-to-transparent sweep in the hero section
- White text on black/dark surfaces only — never dark text on dark background
- Partner/customer logos displayed in white/grayscale monochrome on dark bg

---

## Typography

### Font Family
- **Primary:** `Inter` (all weights)
- **Fallback stack:** `Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial`
- **Monospace:** `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas`

### Type Scale

| Element | Size | Weight | Color | Notes |
|---------|------|--------|-------|-------|
| H1 Hero | ~64–72px | 700 (Bold) | `#FFFFFF` | Two-line hero headline, line-height ~1.1 |
| H2 Section | ~40–48px | 700 (Bold) | `#FFFFFF` | Often ends with a period: "Key Benefits." |
| H3 Subhead | ~24px | 600 (SemiBold) | `#FFFFFF` | Feature names, card titles |
| Body | 16px | 400 | `#FFFFFF` (70% opacity) | Descriptive text, muted gray-white |
| Small / Caption | 13–14px | 400–500 | `#FFFFFF` (60% opacity) | Metadata, secondary info |
| Nav Links | 16px | 400 | `#FFFFFF` | Prefixed with "/" slash character |
| CTA Button | 14px | 500 | See buttons | |

### Typography Style Rules
- Headings: ALL caps is **not** used — sentence case with capital first word
- Section headings frequently end with a **period** (e.g., "Key Benefits.")
- Navigation items are prefixed with a `/` slash: "/ Product", "/ Industries"
- No italic usage observed — strong, upright type throughout
- Letter-spacing: normal for most; no tight tracking

---

## Buttons & CTAs

### Button System — "Notched" Style
EdgeRunner uses a **custom notched/chamfered button design** — no rounded corners. Buttons have a diagonal cut at one or both corners, creating a tactical/angular aesthetic. This is implemented via a custom `NotchedButton` CSS module.

| Variant | Background | Text | Border | Usage |
|---------|-----------|------|--------|-------|
| **Primary** (Contact us) | `#EE2525` | `#FFFFFF` | none | Main CTA |
| **Secondary** (Try Now) | `#FFFFFF` | `#000000` | subtle | Secondary CTA |
| **Outline / Ghost** | transparent | `#FFFFFF` | `#FFFFFF` | Tertiary actions |
| **Red Filled** (Read more) | `#EE2525` | `#FFFFFF` | none | Section CTAs |

### Button Anatomy
- Border radius: **0px** (sharp, angular)
- Chamfered/notched corners — diagonal cut bottom-left or top-right
- Padding: ~12px 25px
- Chevron arrow `›` or `>` suffix on most buttons
- Font: 14px, weight 500
- Text transform: none (sentence case)

---

## Logo

### Wordmark
- **Format:** Icon + wordmark horizontal lockup
- **Icon:** Stylized angular "R" mark — red/dark red geometric shape
- **Wordmark:** "edge**runner**AI" — "edge" and "runner" in white, "AI" in lighter weight/color
- **Typography:** Inter, custom weight — "edgerunner" lowercase, "AI" slightly smaller

### Logo Color Variants
1. **Full color** — Red icon + white wordmark (on dark backgrounds)
2. **White** — All white (for dark overlays)
3. **Dark** — Not observed; primary version is for dark backgrounds

### Logo Clear Space
- Maintain clear space equal to height of the "R" icon on all sides
- Minimum size: approximately 120px wide for digital

---

## Iconography

- **Style:** Outlined/stroke icons (not filled)
- **Color:** `#EE2525` (red) for feature icons; white for UI icons
- **Weight:** Medium stroke (~1.5–2px)
- **Shape language:** Geometric, angular — circles, shields, clocks, grids
- **Size:** ~32–40px in feature lists

---

## Layout & Spacing

### Grid
- Full-width sections, edge-to-edge dark backgrounds
- Content max-width: ~1200px centered
- Two-column layouts: 50/50 or 40/60 (text | visual)
- Spacing system (Mantine): xs=8px, sm=12px, md=16px, lg=24px, xl=32px

### Section Patterns
1. **Hero** — Full viewport, grayscale photo bg with dark overlay, white headline left-aligned, red accent line graphic
2. **Feature list** — Icon + heading + body text left column, diagram/visual right column
3. **Announcement/News card** — Dark gray card (`#393939`) floating over black bg
4. **Logo strip** — White logos on black, horizontal scroll
5. **Video section** — Dark bg, left text + right video thumbnail with centered play button
6. **Industries tabs** — Left sidebar nav with red left-border active state
7. **Footer** — Dark charcoal, multi-column sitemap, red icon row, email subscribe with red submit button

### Announcement Bar
- Full-width red strip (`#EE2525`) at top of page below nav
- White text, centered
- Links styled with underline

---

## UI Components

### Navigation Bar
- **Background:** Near-black / very dark (transparent over hero, solid black below)
- **Logo:** Left-aligned
- **Nav links:** Center-aligned, "/" prefix, 16px Inter Regular, white
- **CTAs:** Right-aligned — "Try Now" (white/notched) + "Contact us" (red/notched)
- **Sticky:** Yes — fixed to top on scroll

### Cards
- Background: `#393939`
- Border: subtle dark outline
- No border radius (0px)
- Sharp corners consistent with button language

### Form Inputs
- Background: dark
- Border: white (`#FFFFFF`)
- Text: white
- Submit button: red, notched

### Dividers
- `rgba(159, 159, 159, 0.376)` — very subtle, almost invisible on dark bg

---

## Motion & Imagery

### Imagery Style
- Grayscale / desaturated military photography
- Subjects: fighter cockpits, military vehicles, Pentagon, aircraft carriers, soldiers
- Treatment: dark overlay to blend into black background
- Never: stock corporate imagery, people in offices, generic tech

### Motion
- Subtle fade-in on scroll for sections
- Logo strip: horizontal auto-scroll (marquee)
- CTA buttons: hover state with slight brightness increase

### Graphic Elements
- **Red diagonal line** — hero section lower-left, suggests speed/trajectory
- **Wireframe globe/sphere** — represents edge network / distributed AI
- **Node diagram** — Command-and-control tree structure, white stroke on black
- **"EDGERUNNER" ghost text** — large, faded, uppercase watermark behind product visuals

---

## Voice & Tone (Design Reflection)

- **Direct:** No adjectives without evidence
- **Technical:** Feature names are precise (not marketing-speak)
- **Military-aligned:** Terminology resonates with warfighter context
- **Minimal:** White space used generously; sections breathe

---

## Design Do's and Don'ts

### Do
- Use `#EE2525` red as the **only** accent color
- Use Inter exclusively
- Keep all text on dark backgrounds (black or `#393939`)
- Use angular/notched button shapes — no rounded corners
- Prefix nav items with `/`
- End section headings with a period
- Use grayscale military imagery

### Don't
- Use gradients (except the hero overlay)
- Use rounded corners on buttons or cards
- Use colors outside the defined palette
- Use light backgrounds on any section
- Use italic text
- Use decorative fonts or mixed typefaces

---

## Component Quick Reference

```
Background:     #000000
Surface/Card:   #393939
Accent Red:     #EE2525
Text Primary:   #FFFFFF
Text Muted:     rgba(255,255,255,0.6)
Border Subtle:  rgba(159,159,159,0.376)
Link Blue:      #228BE6 (inline links only)

Font:           Inter
H1:             700, ~68px
H2:             700, ~44px
H3:             600, ~24px
Body:           400, 16px
Button:         500, 14px

Border Radius:  0px (notched buttons)
Button Style:   Chamfered corners, sharp edges
```
