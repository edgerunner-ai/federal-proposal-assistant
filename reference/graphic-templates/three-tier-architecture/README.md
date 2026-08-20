# three-tier-architecture

Parametric graphic template for three-band architecture diagrams. The most common proposal graphic pattern in EdgeRunner's library and in federal AI / edge-compute proposals generally.

## Visual

- **Dark canvas** (1200 × 612 logical), red accent.
- **Three horizontal tiers**, top to bottom: `tiers[0]`, `tiers[1]`, `tiers[2]`.
- Each tier has a name, subtitle, 4 component labels (4 columns), and a "registry pill" callout at the bottom.
- **Two boundaries** between tiers. Each has a badge label, a downward arrow (flow from upper → lower) with a label, and an upward arrow (lower → upper) with its own label.
- The **bottom tier gets accent treatment** — red border, red fill tint, red component lines. This is where EdgeRunner's own capability lives; the accent draws the evaluator's eye.
- **Footer strip** with brand, tagline, and optional website.

Preview: open [example.html](example.html) in a browser. It renders without any external resources.

## When to use

- **Enterprise / GCC / Tactical Edge** architecture narrative
- Any three-band architecture where bands have a **clear ordering / flow** (top to bottom) and **security/DDIL/classification boundaries** between them
- Positioning graphics where your capability lives at one specific layer and everything else is context

## When NOT to use

- **Two-tier** or **N-tier (N ≥ 4)** architectures — structure is fixed at 3. Use a different pattern or generate free-form HTML.
- Flow diagrams with arrows between specific components (not band-to-band) — use a flow / sequence template instead.
- "Ecosystem" maps where relationships are networked rather than hierarchical — use a network / node graph.
- Customer journey / lifecycle with phases — use the `lifecycle-loop` template (when shipped).

## Required data fields

See `schema.json` for the full contract. Summary:

- `title` (string) — top title, ~8-12 words
- `subtitle` (string) — positioning sentence under title
- `tiers` (array of exactly 3) — each with `name`, `subtitle`, 4 `components`, `pill`
- `boundaries` (array of exactly 2) — each with `label`, `down_arrow_label`, `up_arrow_label`
- `footer` — `brand`, `tagline`, optional `website`
- `theme` (optional) — color overrides; defaults to EdgeRunner dark/red palette

## How `/proposal-graphics` uses this

1. User asks for "three-tier architecture" (or the skill infers from `working/graphics-brief.md`)
2. Skill resolves to this template (prefers `my-company/graphic-templates/three-tier-architecture/` if present)
3. Skill assembles data matching `schema.json` — pulls from win themes, discriminators, architecture notes, company capability docs
4. Skill validates data against schema
5. Skill calls `scripts/render-graphic.py <template> <data> <output>` to fill placeholders
6. Output lands at `graphics/fig<N>-architecture.html`
7. Skill renders to PNG via headless Chrome → `graphics/rendered/fig<N>-architecture.png`

## Anti-patterns

- **Don't exceed 4-5 word component labels.** They overflow the column spacing. "Secure On-Device Inference" fits; "Secure On-Device Inference with Integrated Policy Engine" does not.
- **Don't put the proposal's core capability in the middle tier.** The bottom tier has accent treatment. Put the center-of-gravity there.
- **Don't use technical acronyms in the pill without glossary support.** Pills are short and visually dominant; if the evaluator doesn't know the acronym, they're confused by the most visible element.
- **Don't embed the action caption in the graphic.** Captions live in Word doc text per `reference/proposal-writing-patterns.md` Pattern 3.

## Customization

To override the color palette, pass a `theme` object in the data JSON. Example for a blue/gold palette:

```json
"theme": {
  "bg": "#0a1f44",
  "accent": "#ffb300",
  "panel": "#122a5e",
  "panel_border": "#2a3a6e",
  "text": "#ffffff",
  "muted": "#c5c9d6"
}
```

Defaults (EdgeRunner): bg `#191c20`, accent `#ee2929`, panel `#2a2d31`.

## Rendering

```bash
python scripts/render-graphic.py \
  reference/graphic-templates/three-tier-architecture/template.html \
  reference/graphic-templates/three-tier-architecture/example-data.json \
  reference/graphic-templates/three-tier-architecture/example.html \
  --strict
```

Zero unresolved placeholders is the pass condition. The `--strict` flag exits non-zero on any unresolved `{{field}}` — useful in CI / smoke testing.

For PNG output after HTML renders correctly:

```bash
chrome --headless --disable-gpu \
  --screenshot="example.png" \
  --window-size=1240,640 \
  --device-scale-factor=2 \
  "file:///absolute/path/to/example.html"
```

## File inventory

| File | Purpose |
|---|---|
| [template.html](template.html) | Parameterized HTML/SVG with `{{placeholder}}` markers |
| [schema.json](schema.json) | JSON Schema defining required data fields |
| [example-data.json](example-data.json) | Real data that fills every placeholder — starting point for new proposals |
| [example.html](example.html) | Rendered output (open in browser to preview) |
| README.md | This file |
