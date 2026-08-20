# Customer Map

## When to use
A 5-column customer/partner table with status pills and 4 summary stat cards at the bottom. Shows operational footprint across defense and IC customers.

## Required fields
- `title`, `subtitle` — canvas header
- `column_headers` — exactly 5 strings (e.g. CUSTOMER, MISSION AREA, DEPLOYMENT TYPE, ENVIRONMENT, STATUS)
- `rows` — 1–12 customer rows, each with:
  - `customer`, `customer_sub` — left column name/description
  - `cells` — exactly 3 strings for middle columns
  - `status` — pill text (e.g. "ACTIVE", "ENGAGED")
  - `status_active` — `true` = red pill, `false` = grey pill
- `stats` — exactly 4: `[{value, label}]`
- `footer` — `{brand, tagline}`

## Notes
- The template uses REPEAT blocks for rows — Claude fills one row per item.
- Status pill color varies: active rows get red, non-active get grey. The template currently renders all pills in accent red; to use grey for non-active, the filling script should substitute `{{theme.panel_border}}` for `{{theme.accent}}` in the status span when `status_active` is false.
- Keep customer names short (≤30 chars) — the left column is 220px fixed.
