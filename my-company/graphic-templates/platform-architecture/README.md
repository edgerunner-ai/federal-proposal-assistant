# Platform Architecture

## When to use
Left-to-right pipeline diagram showing data flow through a multi-layer system: Inputs → Processing → Core Engine (hero) → Reasoning → Outputs, with a feedback arc at the bottom.

## Required fields
- `title`, `subtitle` — canvas header
- `layers` — exactly 5: [Inputs, Layer1, Layer2-hero, Layer3, Outputs]
  - Each has `name`, `sub`, `hero` (boolean), `section1_label`, `section1_items[]`, optional `section2_label`, `section2_items[]`
  - Layer 0 (Inputs): items rendered as individual cards
  - Layer 4 (Outputs): items rendered as red-tinted output boxes
- `feedback` — `{label}` for the bottom arc annotation
- `footer` — `{brand, tagline, website}`

## Anti-patterns
- Max 6 items per section — SVG positions are fixed vertically.
- Layer 2 always gets hero treatment (red border/fill). Don't set hero on other layers.
- The Inputs layer only uses section1 (no section2). Outputs only uses section1.
