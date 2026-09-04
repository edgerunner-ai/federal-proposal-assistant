#!/usr/bin/env python3
"""prose-lint.py — deterministic AI-smell / prose-quality lint for proposal drafts.

This is NOT a beauty judge. It catches mechanical patterns that reliably make
proposal prose feel artificial or leak internal process vocabulary into
customer-facing text. Run it before /export-proposal.

Two severities:
  HIGH     — must not ship: the section-sign glyph, dashes used as sentence
             punctuation, internal process vocabulary leaking into
             customer-facing prose. Exit code 1.
  ADVISORY — worth a look: banned marketing words, self-narration /
             performative-honesty commentary, prohibited-claim diction without a
             ledger cite, forbidden absolutes, self-limiting capability
             statements and claim withdrawals, "we will" stacking, repeated
             paragraph openings. Exit code 0 (informational).

Usage:
  python scripts/prose-lint.py --proposal <slug>     # scans proposals/<slug>/drafts/*.md
  python scripts/prose-lint.py path/to/file.md ...   # scans the given files

Scope: top-level drafts/*.md only. drafts/loose/ (pre-bind Pass 1 drafts) is
skipped — loose drafts are allowed to be rough.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# --- Rule set. The rule CONTENT lives in reference/prose-lint-rules.json (a shared,
# syncable data file — see tools/sync-voice-anchors.sh); this script is only the harness.
# A rule added to the JSON propagates here with no code edit, and to the sibling apps
# (federal-proposal-copilot, proposal-workbench) on their next sync.
#
# prose-lint is an export gate, so it FAILS CLOSED: if the rules file is missing or
# malformed, error out (exit 2) rather than silently passing with no rules.
RULES_PATH = REPO_ROOT / "reference" / "prose-lint-rules.json"


def _load_rules() -> dict:
    try:
        return json.loads(RULES_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"prose-lint: rules file not found: {RULES_PATH}", file=sys.stderr)
        raise SystemExit(2)
    except (OSError, ValueError) as exc:
        print(f"prose-lint: could not parse rules file {RULES_PATH}: {exc}", file=sys.stderr)
        raise SystemExit(2)


_RULES = _load_rules()
_TERMS = _RULES.get("term_lists", {})
_PATTERNS = _RULES.get("patterns", {})
_THRESHOLDS = _RULES.get("thresholds", {})

# HIGH: internal process vocabulary that must never reach customer-facing prose.
PROCESS_TERMS = _TERMS.get("process_terms", [])
# ADVISORY: marketing words (mirrors reference/editorial-voice-guide.md).
BANNED_WORDS = _TERMS.get("banned_words", [])
# ADVISORY: self-referential / performative-honesty commentary.
META_COMMENTARY = _TERMS.get("meta_commentary", [])
# ADVISORY: prohibited-claim diction needing an evidence-ledger cite.
PROHIBITED_CLAIM_TERMS = _TERMS.get("prohibited_claim_terms", [])
# ADVISORY: implicit-superiority absolutes.
FORBIDDEN_ABSOLUTES = _TERMS.get("forbidden_absolutes", [])
# ADVISORY: AI-proposalese — reasoning narration and abstract-subject openers
# (adopted 2026-07-30 from the army-brevity-companion voice retrospective: prose
# that explains its own significance instead of stating what the actor does).
AI_PROPOSALESE = _TERMS.get("ai_proposalese", [])

# HIGH: em-/en-dash or "--" as sentence punctuation. "---" rules and "|---|" separators
# do not match because the double-hyphen forms require surrounding whitespace/word chars.
_NEVER = r"(?!x)x"  # never-matches, if a pattern is absent from the rules file
EM_DASH = re.compile(_PATTERNS.get("em_dash", _NEVER))
# ADVISORY: "leverage" in any form — prefer use/apply/extend.
LEVERAGE = re.compile(_PATTERNS.get("leverage", _NEVER), re.IGNORECASE)
# ADVISORY: trailing explainer clause (", which is/means/allows/makes ...") —
# the claim-then-annotation tail that reads as narrated reasoning. State the
# point as its own sentence or fold it into the verb.
EXPLAINER_TAIL = re.compile(_PATTERNS.get("explainer_tail", _NEVER), re.IGNORECASE)
# ADVISORY: negation-stacked dismissal — a sentence whose payload is a non-event
# ("...collects no performance data on human operators, so no IRB review is required").
# The reader decodes two negations to reach one fact. State the affirmative fact and let
# the negative be the consequence, not the subject. Checked per SENTENCE, not per line,
# because drafts are hard-wrapped and these constructions routinely span two lines.
NEGATION_DISMISSAL = re.compile(_PATTERNS.get("negation_dismissal", _NEVER), re.IGNORECASE)
# ADVISORY: raise-then-permit — "X is not required ... and Y is acceptable". Same family as
# negation_dismissal: the sentence spends its subject on something that does not happen.
# Requires BOTH halves, so a bare scope limit ("no VLA is proposed in Phase I") is not flagged.
RAISE_THEN_PERMIT = re.compile(_PATTERNS.get("raise_then_permit", _NEVER), re.IGNORECASE)
# ADVISORY: self-limiting capability statement — telling the customer what we do not have or
# have not measured ("masking is not a current capability", "the 30 W target has not been
# measured", "asserts no module of its own"). A proposal states how it meets a requirement, or
# how it will meet it. Convert, do not delete. Deliberately does NOT match negatives that carry
# a positive claim ("No model participates in the verification check", "no telemetry egress").
CAPABILITY_DENIAL = re.compile(_PATTERNS.get("capability_denial", _NEVER), re.IGNORECASE)
# ADVISORY: claim withdrawal — prose that pulls a claim back after making it ("not claimed at
# TRL 7", "a demonstration rather than a contract delivery", "does not guarantee"). State the
# maturation path or the delivery path instead.
CLAIM_WITHDRAWAL = re.compile(_PATTERNS.get("claim_withdrawal", _NEVER), re.IGNORECASE)

# ADVISORY: contrast-construction DENSITY — "not X but Y", ", not Y.", "rather than", "instead
# of". One is fine and often load-bearing; a density of them reads as a debate brief. Counted per
# 1,000 words. Adopted 2026-09-02: the NAVWAR brief carried 18 in 3,600 words, and a blind
# reviewer flagged the pattern before anyone in-house did.
CONTRAST = re.compile(_PATTERNS.get("contrast_construction", _NEVER), re.IGNORECASE)
CONTRAST_PER_1000 = _THRESHOLDS.get("contrast_per_1000_words", 3.0)
# ADVISORY: bullet-to-prose word ratio. Below the low mark is a wall of prose nobody can skim;
# above the high mark is a paper rewritten as bullets. The same brief went 0% -> 53% -> 20%
# with nothing measuring it.
BULLET_RATIO_LOW = _THRESHOLDS.get("bullet_ratio_low", 0.10)
BULLET_RATIO_HIGH = _THRESHOLDS.get("bullet_ratio_high", 0.35)
# ADVISORY: phrases a reviewer has explicitly called an AI tell. Seeded from NAVWAR EPSS.
AI_TELL_TERMS = _TERMS.get("ai_tell_terms", [])
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")

WE_WILL_THRESHOLD = _THRESHOLDS.get("we_will", 8)  # occurrences before it reads as a wall
REPEATED_OPENING_THRESHOLD = _THRESHOLDS.get("repeated_opening", 3)

HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def strip_noise(text: str) -> list[tuple[int, str]]:
    """Return [(line_number, line)] with HTML comments blanked and fenced code
    blocks dropped. Line numbers are 1-based and refer to the original file."""
    out: list[tuple[int, str]] = []
    in_fence = False
    in_callout = False
    for i, raw in enumerate(text.splitlines(), start=1):
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = raw.strip()
        # Callout sidebar fences and their key lines (tools/md_to_docx.py) are
        # structure, not prose; the box body is linted like any paragraph.
        if s.startswith(":::"):
            in_callout = s.lower().startswith(":::callout") or s.startswith("::: callout")
            continue
        if in_callout and re.match(r"^(evidence|align)\s*:", s, re.IGNORECASE):
            continue
        out.append((i, HTML_COMMENT.sub("", raw)))
    return out


def lint_file(path: Path) -> list[tuple[str, int, str]]:
    """Return findings as (severity, line_no, message)."""
    findings: list[tuple[str, int, str]] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = strip_noise(text)

    we_will = 0
    for ln, line in lines:
        low = line.lower()

        if "§" in line:
            findings.append(("HIGH", ln, "section-sign glyph (§) — spell out 'Section'"))

        if EM_DASH.search(line):
            findings.append(("HIGH", ln, "em-dash/en-dash/'--' as sentence punctuation — rewrite with a period, comma, colon, or parentheses"))

        for term in PROCESS_TERMS:
            if re.search(r"\b" + re.escape(term) + r"\b", low):
                findings.append(("HIGH", ln, f"internal process vocabulary leaked: '{term}'"))

        for w in BANNED_WORDS:
            if re.search(r"\b" + re.escape(w) + r"\b", low):
                findings.append(("ADVISORY", ln, f"marketing word: '{w}'"))
        if LEVERAGE.search(line):
            findings.append(("ADVISORY", ln, "'leverage' — use 'use', 'apply', or 'extend'"))
        for term in AI_TELL_TERMS:
            if term.lower() in low:
                findings.append(("ADVISORY", ln, f"AI tell: '{term}' — a reviewer has flagged this phrase as machine-written; say the plain thing"))

        meta_hit = next((phrase for phrase in META_COMMENTARY if phrase in low), None)
        if meta_hit:
            findings.append(("ADVISORY", ln, f"self-referential / performative-honesty commentary: '{meta_hit}' — state the capability and its boundary plainly"))

        for term in PROHIBITED_CLAIM_TERMS:
            if re.search(r"\b" + re.escape(term) + r"\b", low):
                findings.append(("ADVISORY", ln, f"prohibited claim term without verified citation: '{term}' — confirm an evidence-ledger cite or move to a Gaps note"))

        for phrase in FORBIDDEN_ABSOLUTES:
            if phrase in low:
                findings.append(("ADVISORY", ln, f"forbidden absolute: '{phrase}' — replace with a quantified, sourced comparison"))

        if EXPLAINER_TAIL.search(line):
            findings.append(("ADVISORY", ln, "explainer tail (', which is/means/allows...') — state the point as its own sentence with an actor, or fold it into the verb"))
        for phrase in AI_PROPOSALESE:
            if phrase in low:
                findings.append(("ADVISORY", ln, f"AI-proposalese: '{phrase}' — lead with the actor (EdgeRunner / the Army / staff) and a strong verb; do not narrate the reasoning"))

        we_will += len(re.findall(r"\bwe will\b", low))

    if we_will > WE_WILL_THRESHOLD:
        findings.append(("ADVISORY", 0, f"'we will' appears {we_will}x — vary commitment phrasing"))

    # Repeated paragraph openings: first 3 words of each body paragraph.
    blob = "\n".join(l for _, l in lines)
    # Sentence-level check. Rejoin hard-wrapped lines, then map each hit back to the line
    # the sentence starts on so the report stays actionable.
    starts, off = [], 0
    for ln, line in lines:
        starts.append((off, ln))
        off += len(line) + 1
    flat = " ".join(line for _, line in lines)

    def _line_of(pos: int) -> int:
        best = starts[0][1] if starts else 0
        for o, ln in starts:
            if o <= pos:
                best = ln
            else:
                break
        return best

    for m in RAISE_THEN_PERMIT.finditer(flat):
        findings.append((
            "ADVISORY", _line_of(m.start()),
            "raise-then-permit ('X is not required ... Y is acceptable') — lead with what the "
            "approach does and what the customer accepts, not with what is absent",
        ))

    for m in NEGATION_DISMISSAL.finditer(flat):
        findings.append((
            "ADVISORY", _line_of(m.start()),
            "negation-stacked dismissal ('...so no X is required') — the sentence's payload is a "
            "non-event; state the affirmative fact and let the negative be the consequence",
        ))

    for m in CAPABILITY_DENIAL.finditer(flat):
        findings.append((
            "ADVISORY", _line_of(m.start()),
            f"self-limiting capability statement: '{m.group(0).strip()}' — state how the solution "
            "meets the requirement, or how it will meet it under the effort; do not enumerate what "
            "is missing",
        ))

    for m in CLAIM_WITHDRAWAL.finditer(flat):
        findings.append((
            "ADVISORY", _line_of(m.start()),
            f"claim withdrawal: '{m.group(0).strip()}' — give the maturation or delivery path "
            "instead of retracting the claim (accreditation scope: restate as what the effort "
            "delivers, not as a denial)",
        ))

    # Contrast-construction density, whole document.
    total_words = len(re.findall(r"[A-Za-z][\w'-]*", flat))
    contrasts = list(CONTRAST.finditer(flat))
    if total_words >= 200 and contrasts:
        per_1000 = len(contrasts) * 1000.0 / total_words
        if per_1000 > CONTRAST_PER_1000:
            sample = "; ".join(m.group(0).strip()[:40] for m in contrasts[:3])
            findings.append(("ADVISORY", 0,
                             f"contrast constructions: {len(contrasts)} in {total_words} words "
                             f"({per_1000:.1f} per 1,000; threshold {CONTRAST_PER_1000:g}) — reads as a "
                             f"debate brief; keep the load-bearing ones, e.g. '{sample}'"))

    # Bullet-to-prose word ratio, whole document. Headings, tables, and comments excluded.
    bullet_w = prose_w = 0
    for para in re.split(r"\n\s*\n", blob):
        p = para.strip()
        if not p or p.startswith(("#", "|", ">", "!")):
            continue
        n = len(re.findall(r"[A-Za-z][\w'-]*", p))
        if LIST_ITEM.match(p):
            bullet_w += n
        else:
            prose_w += n
    body_w = bullet_w + prose_w
    if body_w >= 300:
        ratio = bullet_w / body_w
        if ratio > BULLET_RATIO_HIGH:
            findings.append(("ADVISORY", 0,
                             f"bullet ratio {ratio:.0%} of body words (high mark {BULLET_RATIO_HIGH:.0%}) — "
                             "the document is a paper rewritten as bullets; keep bullets for enumerable "
                             "items and return arguments to prose"))
        elif ratio < BULLET_RATIO_LOW:
            findings.append(("ADVISORY", 0,
                             f"bullet ratio {ratio:.0%} of body words (low mark {BULLET_RATIO_LOW:.0%}) — "
                             "a wall of prose; a reviewer triaging a dozen of these will skim, so give the "
                             "enumerable content (capabilities, deliverables, criteria) a list"))

    openers: dict[str, int] = {}
    for para in re.split(r"\n\s*\n", blob):
        p = para.strip()
        if not p or p.startswith(("#", "|", "-", "*", ">", "1.", "2.", "3.")):
            continue
        words = re.findall(r"[A-Za-z][\w'-]*", p)
        if len(words) >= 3:
            key = " ".join(w.lower() for w in words[:3])
            openers[key] = openers.get(key, 0) + 1
    for key, count in openers.items():
        if count >= REPEATED_OPENING_THRESHOLD:
            findings.append(("ADVISORY", 0, f"{count} paragraphs open with '{key}...' — vary openings"))

    return findings


def resolve_files(args: argparse.Namespace) -> list[Path]:
    if args.proposal:
        drafts = REPO_ROOT / "proposals" / args.proposal / "drafts"
        if not drafts.is_dir():
            sys.exit(f"prose-lint: no drafts directory at {drafts}")
        return sorted(drafts.glob("*.md"))
    return [Path(f) for f in args.files]


def main() -> int:
    ap = argparse.ArgumentParser(description="AI-smell / prose-quality lint for proposal drafts.")
    ap.add_argument("--proposal", help="proposal slug — scans proposals/<slug>/drafts/*.md")
    ap.add_argument("files", nargs="*", help="explicit markdown files to scan")
    args = ap.parse_args()

    files = resolve_files(args)
    if not files:
        sys.exit("prose-lint: nothing to scan (give --proposal <slug> or file paths)")

    high_total = 0
    adv_total = 0
    for path in files:
        if not path.is_file():
            print(f"  skip (not found): {path}")
            continue
        findings = lint_file(path)
        high = [f for f in findings if f[0] == "HIGH"]
        adv = [f for f in findings if f[0] == "ADVISORY"]
        high_total += len(high)
        adv_total += len(adv)
        if not findings:
            print(f"OK    {path.name}")
            continue
        print(f"{'FAIL' if high else 'warn'}  {path.name}  ({len(high)} high, {len(adv)} advisory)")
        for sev, ln, msg in findings:
            loc = f"L{ln}" if ln else "file"
            print(f"        [{sev:8}] {loc}: {msg}")

    print()
    print(f"prose-lint: {high_total} HIGH, {adv_total} ADVISORY across {len(files)} file(s)")
    if high_total:
        print("HIGH findings must be resolved before export.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
