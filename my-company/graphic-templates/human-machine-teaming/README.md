# Human-Machine Teaming

## When to use
5-step left-to-right workflow showing human-AI interaction loop. Step 3 (center) gets hero treatment. Includes feedback arc and 3 principle callout boxes at the bottom. Steps 1 and 5 can have top icons (operator/decision).

## Required fields
- `title`, `subtitle` — canvas header
- `steps` — exactly 5, each with `name`, `sub`, `lines[]` (1–5 body lines), `bottom_note`
  - Optional: `top_icon` (emoji), `top_label`, `hero` (boolean for step 3)
- `feedback` — `{label}` for bottom arc
- `principles` — exactly 3: `[{title, sub}]`
- `footer` — `{brand, tagline, website}`

## Anti-patterns
- Only step 3 (index 2) should have `hero: true`.
- Keep lines to 4 words max per line — SVG text doesn't wrap.
- Top icons are intended for steps 1 and 5 only (operator bookends).
