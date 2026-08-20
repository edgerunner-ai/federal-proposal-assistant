# Differentiator Comparison

## When to use
3-column comparison showing your solution against two alternative approaches. Columns progress from weakest (left) to strongest (right/hero). Each row is a dimension with per-cell icon state (✗/~/✓), label, and sublabel.

## Required fields
- `title` — main heading (uppercase applied by CSS)
- `subtitle` — one-line positioning sentence
- `columns` — exactly 3: `[{name, sub}]`. Column 0 = weakest, column 2 = hero (red treatment)
- `rows` — 1–12 dimension rows, each with `dimension`, `dimension_sub`, and `cells[3]`
- `cells` — each has `state` ("no"/"partial"/"yes"), `label`, `sub`
- `footer` — `{brand, tagline, website}`

## Anti-patterns
- **Never name competitors directly.** Use category labels ("Proprietary / Closed-Weight") not company names.
- Don't exceed 8 rows — the graphic gets too dense for Word embed at half-page width.
- Cell icon states in the template use fixed glyphs per column position (✗/~/✓). If you need per-cell state variation, use the reference example `06-differentiator-comparison.html` as a starting point instead.
