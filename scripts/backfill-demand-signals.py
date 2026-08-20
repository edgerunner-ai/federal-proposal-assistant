#!/usr/bin/env python3
"""One-time backfill of the demand signal register from existing pursuit history.

The register is worthless on its first read if it is empty: "eleven pursuits asked for a
cross-air-gap model update path" is an argument, a good schema with no rows is a chore. This
script replays the twelve requirement matrices already in the workspace through the
extractor, applies a HUMAN CURATION table, and writes signals/demand-signals.jsonl.

The curation table below is the record of judgment calls. It is checked in deliberately so the
backfill is reproducible and auditable: anyone can see which extracted rows were dropped as
submission mechanics, which keyword-suggested themes were overridden, and which statuses were
set from reading the Gap/Risk prose.

Curation rules encoded here:
  * DROP — submission mechanics, contract structure, corporate posture, deliverable and
    milestone schedules, and our own pitch framing. None of these are customer capability
    demand and each one that ships dilutes the channel.
  * THEME — override the extractor's keyword suggestion, or classify what it could not.
  * STATUS / IMPACT — set our_status and bid_impact by reading the matrix's Gap/Risk prose.
    Left as extracted where the source does not support a stronger claim; 'unknown' is honest
    and the brief's gap queue ignores it.
  * spotter is excluded whole: its "requirements" are needs WE inferred for an unsolicited
    paper, not asks a customer made. Inferred needs in a demand register are circular.

Run once. Re-running rewrites the register from scratch and will renumber signal IDs, so it
refuses to run if the register already exists unless --force is given.

BOUNDARY NOTE: the curation table below names customers and programs and records candid gap
admissions — the same class of material signals/ is gitignored to protect. This file is tracked
anyway, as a reviewed exception accepted 2026-08-01, because an auditable backfill has to show
its judgment calls. The exception holds only while the remote is private and single-user; see
README "The guard is path-based, so it cannot see content". If that changes, move the curation
table to signals/backfill-curation.json and read it from there.

Usage:
  python scripts/backfill-demand-signals.py --dry-run
  python scripts/backfill-demand-signals.py
  python scripts/backfill-demand-signals.py --selftest
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass

WORKSPACE_ROOT = Path(__file__).parent.parent
REGISTER = WORKSPACE_ROOT / "signals" / "demand-signals.jsonl"
sys.path.insert(0, str(WORKSPACE_ROOT / "scripts"))

# Proposals excluded entirely, with the reason.
EXCLUDE_PROPOSALS = {
    "spotter": "unsolicited white paper — 'requirements' are needs we inferred, not customer asks",
}

# Customer, source type, and observation date per pursuit. source_type is the kind of
# encounter that produced the ask, not the kind of document we wrote back.
PURSUITS: dict[str, dict] = {
    "ITDX26-AI-Analyst": {
        "customer": "U.S. Army Futures and Concepts Center (FCC/ICED)",
        "program": "ITDX 2026 — Intelligence Technology Discovery Experiment",
        "source_type": "rfi", "date": "2026-03-31",
    },
    "africom-jwic": {
        "customer": "USAFRICOM", "program": "JWIC Challenge LOE 1",
        "source_type": "solicitation", "date": "2026-05-27",
    },
    "army-brevity-companion": {
        "customer": "U.S. Army", "program": "ONIX Marketplace Challenge — Digital Brevity & Clarity Companion",
        "source_type": "solicitation", "date": "2026-07-21",
    },
    "cybercom-j9": {
        "customer": "USCYBERCOM J9", "program": "Decensored model ROM",
        # Requirements came out of a scope conversation and a customer-facing ROM draft,
        # not a published solicitation. That is exactly the verbal signal class.
        "source_type": "one-on-one", "date": "2026-04-22",
    },
    "daf-tactical-edge-llm": {
        "customer": "DAF AFLCMC", "program": "Tactical Edge LLM Pilot",
        "source_type": "solicitation", "date": "2026-05-26",
    },
    "dia-dma-frontier-llm": {
        "customer": "DIA", "program": "DMA Frontier-Class LLM Integration and Onboarding Challenge",
        "source_type": "solicitation", "date": "2026-07-21",
    },
    "digital-guardian-sim": {
        "customer": "U.S. Navy (USW acquisition community)", "program": "Digital Guardian Simulator MVP",
        "source_type": "solicitation", "date": "2026-05-15",
    },
    "extic-26-2": {
        "customer": "USCENTCOM / DIU AZ OnRamp Hub", "program": "EXTiC 26.2",
        "source_type": "solicitation", "date": "2026-05-01",
    },
    "nato-diana-decision-superiority": {
        "customer": "NATO DIANA", "program": "Decision Superiority for NATO Warfighters",
        "source_type": "solicitation", "date": "2026-04-23",
    },
    "tradewinds-cdao-adl-p2": {
        "customer": "CDAO", "program": "Autonomy Data Labeling Phase II",
        "source_type": "rfi", "date": "2026-07-24",
    },
    "unmanned-ground-recovery-rfi": {
        "customer": "Army Materiel Command (ACC-CTRS)", "program": "Unmanned Ground Recovery",
        "source_type": "rfi", "date": "2026-07-09",
    },
}

# (slug, row_id) -> reason. Dropped as not-capability-demand.
DROP: dict[tuple[str, str | None], str] = {}


def _split_ids(ids: str) -> list[str]:
    """Split an ID list on commas when present, whitespace otherwise.

    Some matrices use row IDs that contain spaces ('EF-1.2 (IMPL)'), which whitespace
    splitting silently mangles into two IDs that match nothing — the curation entry then
    appears to be applied while the row sails through. Comma-delimited lists are the escape
    hatch for those.
    """
    if "," in ids:
        return [part.strip() for part in ids.split(",") if part.strip()]
    return ids.split()


def _drop(slug: str, ids: str, reason: str) -> None:
    for rid in _split_ids(ids):
        DROP[(slug, None if rid == "NONE" else rid)] = reason


_drop("ITDX26-AI-Analyst", "S-03 S-04 S-05 S-06 S-07 S-08", "submission and participation mechanics")
_drop("africom-jwic", "NONE", "duplicate summary table restating the R-xx rows")
# R-07 (state current TRL/MRL/IRL) is already filtered by the extractor's internal-framing
# pattern, so it never reaches this table.
_drop("africom-jwic", "R-01 R-03 R-04 R-05 R-06 R-11 R-12 R-13 R-10",
      "solicitation framing and submission content, not capability demand")
_drop("army-brevity-companion", "**R12** **R13**", "corporate posture and pricing mechanics")
_drop("cybercom-j9", "R-05 R-08 R-12 R-13 R-14 R-15 R-16",
      "contract structure, audience definition, and pricing mechanics")
# This matrix's header says the requirements were inferred from a proposal plan and SOW summary
# with no solicitation in inputs/. The SOW.* rows trace to the customer's SOW; the EF-* rows are
# our own guess at the evaluation factors, which is inference, not demand.
_drop("daf-tactical-edge-llm", "EF-1.1 (IMPL), EF-1.2 (IMPL), EF-1.3 (IMPL), EF-2 (IMPL)",
      "evaluation factors we inferred, not requirements the customer stated")
_drop("daf-tactical-edge-llm", "SOW.2.1 SOW.2.2", "schedule and key-personnel mechanics")
_drop("dia-dma-frontier-llm", "S1 S2 S3 S4 S5 S6 S7 S8 S10", "required submission content list")
_drop("digital-guardian-sim", "D-1 D-2 D-3 D-4 MS-1 MS-2 MS-3 MS-4",
      "deliverable and milestone schedule")
_drop("digital-guardian-sim", "T-8", "our own reuse constraint, not a customer ask")
_drop("digital-guardian-sim", "T-9", "near-duplicate of SEC-1 (zero trust + audit logging)")
_drop("extic-26-2", "TR-10 TR-11 TR-12 TR-13", "maturity and framing statements")
_drop("nato-diana-decision-superiority", "EF-3 EF-4 EF-8 R-06",
      "evaluation-factor labels and outcome statements")
_drop("tradewinds-cdao-adl-p2", "R1.1.1 R1.1.3b R1.2.2",
      "delivery-model question, NDA willingness, and CAC access")
_drop("unmanned-ground-recovery-rfi", "REQ-5", "scoping option in the response instructions")

# (slug, row_id) -> capability_theme. Overrides the extractor's keyword suggestion, or
# classifies a row it could not.
THEME: dict[tuple[str, str | None], str] = {}


def _theme(slug: str, theme: str, ids: str) -> None:
    for rid in _split_ids(ids):
        THEME[(slug, rid)] = theme


# ITDX26's sixteen tasks are one coherent engineering ask: produce the MI staff product.
_theme("ITDX26-AI-Analyst", "staff-product-generation",
       "R-01 R-02 R-03 R-04 R-05 R-06 R-07 R-08 R-09 R-10 R-11 R-12 R-13 R-14 R-15 R-16")
_theme("africom-jwic", "air-gap-ddil-deployment", "R-02")
_theme("africom-jwic", "token-cost-economics", "R-08")
_theme("africom-jwic", "platform-integration-embedded", "R-09")
_theme("africom-jwic", "federation-cross-enclave", "R-14")
_theme("army-brevity-companion", "ato-accreditation-artifacts", "**R1**")
_theme("army-brevity-companion", "mission-mos-finetuning", "**R2** **R6** **R7**")
_theme("army-brevity-companion", "staff-product-generation", "**R3**")
_theme("army-brevity-companion", "platform-integration-embedded", "**R4**")
_theme("army-brevity-companion", "tevv-eval-harness", "**R5** **R11**")
_theme("army-brevity-companion", "sustainment-training-support", "**R8** **R9** **R10**")
_theme("cybercom-j9", "tevv-eval-harness", "R-02 R-03 R-04")
_theme("cybercom-j9", "mission-mos-finetuning", "R-06")
_theme("cybercom-j9", "agentic-orchestration", "R-07")
_theme("cybercom-j9", "multi-model-hosting-byom", "R-10")
_theme("cybercom-j9", "cross-domain-model-update", "R-11")
_theme("daf-tactical-edge-llm", "air-gap-ddil-deployment", "SOW.1.1")
_theme("daf-tactical-edge-llm", "cross-domain-model-update", "SOW.3.1")
_theme("digital-guardian-sim", "wargame-simulation-personas", "F-1 F-2 F-3 F-4 F-6 F-10")
_theme("digital-guardian-sim", "output-verification-attribution", "F-5 F-7 F-8")
_theme("digital-guardian-sim", "training-data-rights", "D-5")
_theme("digital-guardian-sim", "ato-accreditation-artifacts", "SEC-1")
_theme("digital-guardian-sim", "hardware-footprint-compression", "T-1 T-2 F-9")
_theme("digital-guardian-sim", "platform-integration-embedded", "T-3")
_theme("digital-guardian-sim", "air-gap-ddil-deployment", "T-4 T-7")
_theme("extic-26-2", "output-verification-attribution", "TR-2 TR-16")
_theme("extic-26-2", "platform-integration-embedded", "TR-4")
_theme("extic-26-2", "air-gap-ddil-deployment", "TR-6 TR-7")
_theme("extic-26-2", "hardware-footprint-compression", "TR-8")
_theme("extic-26-2", "multi-model-hosting-byom", "TR-17")
_theme("extic-26-2", "token-cost-economics", "TR-18")
_theme("nato-diana-decision-superiority", "wargame-simulation-personas",
       "CS-01 CS-02 CS-03 CS-04 CS-05 R-03 R-05")
_theme("nato-diana-decision-superiority", "staff-product-generation", "CS-06 CS-07 R-02 R-04")
_theme("nato-diana-decision-superiority", "retrieval-over-doctrine", "CS-09 R-07")
_theme("nato-diana-decision-superiority", "platform-integration-embedded", "CS-10")
_theme("nato-diana-decision-superiority", "multi-model-hosting-byom", "R-08")
_theme("nato-diana-decision-superiority", "federation-cross-enclave", "R-10")
_theme("tradewinds-cdao-adl-p2", "data-labeling-curation",
       "R1.1.2c R1.3.1 R1.3.2a R1.3.2b R1.3.2c R1.3.2d R1.3.4")
_theme("tradewinds-cdao-adl-p2", "platform-integration-embedded", "R1.2.4")
_theme("unmanned-ground-recovery-rfi", "robotic-autonomy-control", "REQ-1b REQ-2 REQ-3")

# (slug, row_id) -> (our_status, bid_impact). Read from the matrix's Gap/Risk prose.
STATUS: dict[tuple[str, str], tuple[str, str | None]] = {
    ("unmanned-ground-recovery-rfi", "REQ-1a"): (
        "prototype",
        "Answered as an adaptation, not a demonstrated capability — detection models are trained "
        "for drones, guns and tanks, not disabled vehicles.",
    ),
    ("unmanned-ground-recovery-rfi", "REQ-1b"): (
        "no-plan", "Question declined. No path planning, SLAM or motion control; needs a robotics partner.",
    ),
    ("unmanned-ground-recovery-rfi", "REQ-2"): (
        "no-plan", "Question declined. Physical manipulation is entirely outside the product line.",
    ),
    ("unmanned-ground-recovery-rfi", "REQ-3"): (
        "no-plan", "Question declined and heavily caveated. Same root cause as REQ-1b and REQ-2.",
    ),
    ("unmanned-ground-recovery-rfi", "REQ-4"): (
        "prototype",
        "Scoped down to the AI decision layer under DDIL — the ARL CRADA covers reasoning, not "
        "navigation or rigging actuation.",
    ),
    # T-2 (NVIDIA-optimized inference) is marked "Full" in the source — vLLM primary, DGX-native.
    # An earlier draft of this table called it a gap by reading the requirement instead of the
    # matrix. The real gap in that table is F-9, in the author's own words.
    ("digital-guardian-sim", "F-9"): (
        "gap", "Sustained 45-minute session not validated; carried as a 2-week testing sprint.",
    ),
    ("dia-dma-frontier-llm", "R3"): (
        "gap", "Bid the path, not the capability — no concrete cross-air-gap upgrade mechanism to cite.",
    ),
    ("dia-dma-frontier-llm", "R9"): (
        "prototype", "DIA-specific tuning bid as a path, not as done work.",
    ),
    ("dia-dma-frontier-llm", "R11"): (
        "prototype", "Ground Truth is TRL 7 — framed as prototype-stage, not fielded.",
    ),
    ("dia-dma-frontier-llm", "R7"): (
        "prototype", "Utilization telemetry is partly a prototype build; scoped honestly in the response.",
    ),
    ("dia-dma-frontier-llm", "R8"): (
        "prototype",
        "Written as 'support through the customer's process' — no pre-existing DIA or ICD 503 ATO "
        "to claim reciprocity from.",
    ),
    ("dia-dma-frontier-llm", "R1"): (
        "prototype", "Federated rather than tied in — the DIA hosting platform may be incumbent-controlled.",
    ),
    ("cybercom-j9", "R-01"): (
        "prototype",
        "Abliteration is less characterized on the hybrid transformer/SSM architecture the customer "
        "named.",
    ),
    ("africom-jwic", "R-02"): (
        "prototype", "No AFRICOM AOR experience — framed by DDIL analogy from SOCOM operations.",
    ),
    ("tradewinds-cdao-adl-p2", "R1.2.1"): (
        "prototype", "IL5 answered as a pathway with a timeline rather than native execution today.",
    ),
}


def parse_matrix_date(slug: str, fallback: str) -> str:
    path = WORKSPACE_ROOT / "proposals" / slug / "working" / "requirement-matrix.md"
    if path.exists():
        head = path.read_text(encoding="utf-8", errors="replace")[:600]
        m = re.search(r"(20\d\d-\d\d-\d\d)", head)
        if m:
            return m.group(1)
    return fallback


def build_records(candidates: list[dict]) -> tuple[list[dict], dict[str, int], list[str]]:
    records: list[dict] = []
    stats = {"dropped_curated": 0, "dropped_unclassified": 0, "dropped_excluded": 0, "kept": 0}
    warnings: list[str] = []
    # A curation entry that matches no candidate row is a dead rule: it reads as applied while
    # the row it was meant to catch sails through into the register. Track what actually fired.
    used: set[tuple[str, str | None]] = set()
    next_id = 1
    for cand in candidates:
        slug = cand["proposal_slug"]
        rid = cand["row_id"]
        if slug in EXCLUDE_PROPOSALS:
            stats["dropped_excluded"] += 1
            continue
        if slug not in PURSUITS:
            warnings.append(f"{slug}: no pursuit metadata; rows skipped")
            stats["dropped_unclassified"] += 1
            continue
        if (slug, rid) in DROP:
            used.add((slug, rid))
            stats["dropped_curated"] += 1
            continue
        if (slug, rid) in THEME:
            used.add((slug, rid))
        if (slug, rid) in STATUS:
            used.add((slug, rid))
        theme = THEME.get((slug, rid)) or cand["theme_suggestion"]
        if not theme:
            stats["dropped_unclassified"] += 1
            continue
        meta = PURSUITS[slug]
        status, impact = STATUS.get((slug, rid), (cand["our_status_inferred"], None))
        records.append({
            "schema_version": "demand-signal.v1",
            "signal_id": f"SIG-{next_id:04d}",
            "date_observed": parse_matrix_date(slug, meta["date"]),
            "source_type": meta["source_type"],
            "source_ref": cand["source_ref"],
            "customer": meta["customer"],
            "program": meta["program"],
            "proposal_slug": slug,
            "requirement": cand["requirement"],
            "capability_theme": theme,
            "demand_strength": cand["demand_strength_inferred"],
            "rubric_weight_pct": cand["rubric_weight_pct"],
            "pursuit_value_usd": None,
            "our_status": status,
            "bid_impact": impact,
            "evidence_id": None,
            "cto_disposition": None,
            "cto_disposition_detail": None,
            "cto_disposition_date": None,
            "cto_owner": None,
            "notes": "backfilled 2026-07-31 from requirement-matrix history",
        })
        next_id += 1
        stats["kept"] += 1

    for table_name, table in (("DROP", DROP), ("THEME", THEME), ("STATUS", STATUS)):
        for key in table:
            if key[0] in EXCLUDE_PROPOSALS or key in used:
                continue
            warnings.append(
                f"dead curation rule: {table_name}[{key[0]}, {key[1]!r}] matched no candidate row "
                "— check the row ID (IDs containing spaces need a comma-delimited list)"
            )
    return records, stats, warnings


def selftest() -> int:
    # Curation keys must not contradict each other: a dropped row cannot also be themed.
    overlap = set(DROP) & set(THEME)
    assert not overlap, f"rows both dropped and themed: {sorted(overlap)}"
    status_only = {k for k in STATUS if k in DROP}
    assert not status_only, f"rows both dropped and status-set: {sorted(status_only)}"

    valid = set(load_valid_themes())
    unknown = {t for t in THEME.values() if t not in valid}
    assert not unknown, f"curation uses themes absent from the vocabulary: {sorted(unknown)}"
    bad_status = {s for s, _ in STATUS.values()} - {
        "shipping", "prototype", "roadmap", "gap", "no-plan", "unknown"
    }
    assert not bad_status, f"invalid statuses in curation: {bad_status}"

    fake = [{
        "proposal_slug": "dia-dma-frontier-llm", "row_id": "R3",
        "source_ref": "proposals/dia-dma-frontier-llm/working/requirement-matrix.md#R3",
        "requirement": "Support progressive upgrades", "theme_suggestion": "cross-domain-model-update",
        "our_status_inferred": "unknown", "demand_strength_inferred": "mandatory-scored",
        "rubric_weight_pct": 10.0,
    }, {
        "proposal_slug": "spotter", "row_id": "R1", "source_ref": "x", "requirement": "y",
        "theme_suggestion": "agentic-orchestration", "our_status_inferred": "unknown",
        "demand_strength_inferred": "desired", "rubric_weight_pct": None,
    }, {
        "proposal_slug": "dia-dma-frontier-llm", "row_id": "S1", "source_ref": "x",
        "requirement": "Proposed Period of Performance", "theme_suggestion": "air-gap-ddil-deployment",
        "our_status_inferred": "unknown", "demand_strength_inferred": "desired", "rubric_weight_pct": None,
    }]
    recs, stats, _ = build_records(fake)
    assert stats == {"dropped_curated": 1, "dropped_unclassified": 0, "dropped_excluded": 1, "kept": 1}, stats
    assert recs[0]["our_status"] == "gap", recs[0]["our_status"]
    assert recs[0]["bid_impact"].startswith("Bid the path"), recs[0]["bid_impact"]
    assert recs[0]["customer"] == "DIA" and recs[0]["signal_id"] == "SIG-0001"
    print(f"SELFTEST PASS — {len(DROP)} drop rules, {len(THEME)} theme overrides, "
          f"{len(STATUS)} status overrides, all consistent with the vocabulary")
    return 0


def load_valid_themes() -> list[str]:
    themes_file = WORKSPACE_ROOT / "reference" / "capability-themes.md"
    return [
        m.group(1)
        for m in (re.match(r"^\|\s*`([a-z0-9-]+)`\s*\|", line)
                  for line in themes_file.read_text(encoding="utf-8", errors="replace").splitlines())
        if m
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="report without writing the register")
    parser.add_argument("--force", action="store_true", help="overwrite an existing register (renumbers IDs)")
    parser.add_argument("--candidates", help="candidate JSONL (default: regenerate with the extractor)")
    parser.add_argument("--selftest", action="store_true", help="verify the curation table is self-consistent")
    args = parser.parse_args()

    if args.selftest:
        return selftest()
    if REGISTER.exists() and not args.force and not args.dry_run:
        print(f"ERROR: {REGISTER.relative_to(WORKSPACE_ROOT).as_posix()} already exists. "
              "This is a one-time backfill; use --force only if you intend to renumber every "
              "signal_id and discard any dispositions already recorded.", file=sys.stderr)
        return 2

    if args.candidates:
        cand_path = Path(args.candidates)
    else:
        cand_path = WORKSPACE_ROOT / "signals" / "candidates" / f"{date.today().isoformat()}-candidates.jsonl"
        result = subprocess.run(
            [sys.executable, str(WORKSPACE_ROOT / "scripts" / "extract-demand-signals.py"), "--all",
             "--out", str(cand_path)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"ERROR: extractor failed: {result.stderr[-500:]}", file=sys.stderr)
            return 2
    candidates = [json.loads(l) for l in cand_path.read_text(encoding="utf-8").splitlines() if l.strip()]

    records, stats, warnings = build_records(candidates)
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)

    print(f"Candidates in:            {len(candidates)}")
    print(f"  dropped (curated)       {stats['dropped_curated']}  submission mechanics, framing, contract structure")
    print(f"  dropped (excluded)      {stats['dropped_excluded']}  " +
          "; ".join(f"{k}: {v}" for k, v in EXCLUDE_PROPOSALS.items()))
    print(f"  dropped (unclassified)  {stats['dropped_unclassified']}  no theme fit")
    print(f"  kept                    {stats['kept']}")

    themes: dict[str, set[str]] = {}
    statuses: dict[str, int] = {}
    for r in records:
        themes.setdefault(r["capability_theme"], set()).add(r["customer"])
        statuses[r["our_status"]] = statuses.get(r["our_status"], 0) + 1
    print("\nThemes by customer breadth:")
    for theme, custs in sorted(themes.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"  {len(custs)} customer(s)  {theme}")
    print("\nStatus: " + ", ".join(f"{k}={v}" for k, v in sorted(statuses.items())))

    if args.dry_run:
        print("\nDry run — nothing written.")
        return 0

    REGISTER.parent.mkdir(parents=True, exist_ok=True)
    with REGISTER.open("w", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"\nWrote {len(records)} signals -> {REGISTER.relative_to(WORKSPACE_ROOT).as_posix()}")
    print("Next: python scripts/build-demand-signal-brief.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
