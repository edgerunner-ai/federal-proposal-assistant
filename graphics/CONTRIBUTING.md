# Contributing to the Graphics Library

The library only stays valuable if the bar for what gets promoted into it is held high. This doc describes that bar and the promotion flow.

**Librarian:** Bill Bal. Bill is the single point of decision for what enters `_library/`. This isn't gatekeeping for its own sake — it's so the canonical set doesn't drift into "every figure ever made," which would defeat the point.

---

## What makes a graphic library-worthy

The promotion bar is one question: **would another EdgeRunner team member, in a different context, reach for this graphic?**

If yes → library candidate.
If no → keep it with the originating deck/paper/proposal; it doesn't belong in the library.

Concrete signals of yes:

- **Abstract enough to fit multiple contexts.** "Three-tier architecture" — yes. "JATF system architecture with EVELYN-specific labels" — no (that's proposal-specific, useful as a fork starting point but not as a canonical pattern).
- **Solves a recurring proposal/deck need.** Architecture diagrams, capability matrices, lifecycle loops, comparison tables, schedule swimlanes, deployment spectrums.
- **Already polished.** Brand-aligned, legible at 8.5×11 column width, no placeholder text, no figure-number embedded in the graphic.
- **Used or reusable across ≥2 distinct contexts.** If it only ever made sense in one bid, it's proposal-specific.

Concrete signals of no:

- Customer-specific labels baked in (program names, contract numbers, specific personnel).
- One-off comparison against a specific named competitor (these go in `_proposal-specific/` so the structure is forkable but the labels are clearly tied to that context).
- Decorative or illustrative graphics that don't make an evaluative point. The library is for figures that *prove something*, not figures that fill space.

---

## How to propose a contribution

**For proposal-team members** (capture, BD, writers using `/proposal-graphics`):

The skill already flags promotion candidates in `working/graphics-brief.md` — each figure has a `library-promotion candidate? yes/no` field. Bill reviews these during periodic library refreshes. No action needed from you beyond setting the flag honestly.

**For everyone else** (engineering, sales, leadership, partnerships):

1. Send Bill the graphic you'd like to contribute, in the format you built it (PowerPoint slide, HTML, Figma frame, sketched concept — anything).
2. Include 1-3 sentences on:
   - What evaluative point the graphic makes
   - What contexts you imagine it being reused in
   - Whether you already had to customize it (suggests it's a forkable pattern)
3. Bill assesses against the bar above and replies with one of:
   - **Promote** — Bill will rebuild it as a brand-aligned `source.html` + `preview.png` and add it to `_library/` on the next refresh.
   - **Park in `_proposal-specific/`** — it's interesting but not abstract enough for the canonical set; lives in the proposal-specific bucket as a fork starting point.
   - **Out of scope** — doesn't belong in the library at all; that's fine, keep using it in your own work.

---

## What Bill does on promotion

This is documented for transparency, not because anyone else needs to do it.

For each promoted graphic:

1. Rebuild from the contributor's source into the standard library structure: `_library/<slug>/source.html` + `_library/<slug>/preview.png` + `_library/<slug>/README.md` (with frontmatter).
2. Apply brand palette consistently (sometimes contributors use off-brand colors; the canonical version always matches the EdgeRunner palette).
3. Verify legibility at 8.5×11 column-width embed (≥10pt rendered body text at the default canvas + embed ratio — see the proposal-graphics skill for the math).
4. Strip customer-specific labels — replace with generic placeholders that are obvious to customize.
5. Write the README frontmatter (pattern, tags, canonical source, used_in, dimensions, last_updated).
6. Update `CATALOG.md` and re-run `build-gallery.py` to regenerate `index.html`.
7. Re-upload to Drive.

The contributor is credited in the README's body text and in the refresh announcement.

---

## Refresh cadence

The Drive copy refreshes when there are enough new entries to justify a re-upload — roughly monthly during active proposal periods, less frequently otherwise. Bill announces refreshes in the team chat.

If you have something time-sensitive (e.g., a contribution that another teammate needs *this week*), ping Bill directly and he'll push the single entry without waiting for a full refresh.

---

## Questions

Ask in the team chat or DM Bill. There's no formal review board — this is a small library for a small company, and keeping the process lightweight is part of why it works.
