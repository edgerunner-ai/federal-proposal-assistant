# Deployment Spectrum

## When to use
Horizontal 3–4 column layout showing deployment environments from connected (left) to autonomous (right). Rightmost columns get hero red treatment. Each column has deployment details, use cases, and connectivity badge.

## Required fields
- `title`, `subtitle` — canvas header
- `spectrum` — `{left_label, right_label}` for the gradient bar endpoints
- `columns` — 3–4 columns, each with `name`, `sub`, `hero` (boolean), `deployment[]`, `use_cases[]`, `connectivity`, `connectivity_badge`
- `tagline` — bottom tagline inside the SVG
- `footer` — `{brand, tagline, website}`

## Anti-patterns
- Keep use case lists to 3–4 items max per column — text overflows at 5+.
- The SVG layout uses fixed x-coordinates; 3 columns will leave a gap on the right. For 3-column use, adjust column widths in the template.
