"""Paths and constants for the dashboard. Everything is relative to the repo root."""
from pathlib import Path

# Repo root is one level up from this file (dashboard/config.py → repo_root/dashboard/ → repo_root)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Top-level directories the dashboard reads
PROPOSALS_DIR = REPO_ROOT / "proposals"
MY_COMPANY_DIR = REPO_ROOT / "my-company"
REFERENCE_DIR = REPO_ROOT / "reference"
DOCS_DIR = REPO_ROOT / "docs"

# Per-proposal sidecar filenames
PROPOSAL_TYPE_MD = "working/proposal-type.md"
PROPOSAL_PLAN_MD = "working/proposal-plan.md"
PROPOSAL_PLAN_JSON = "working/proposal-plan.json"
COMPLIANCE_MATRIX_MD = "working/compliance-matrix.md"
COMPLIANCE_MATRIX_JSON = "working/compliance-matrix.json"
ACTIVITY_MD = "working/activity.md"
AI_RUNS_JSONL = "working/ai-runs.jsonl"
NARRATIVE_SPINE_MD = "working/narrative-spine.md"

# Review artifacts
GOLD_TEAM_MD = "reviews/gold-team-scorecard.md"
RED_TEAM_NOTES_MD = "reviews/red-team-notes.md"
WHITE_GLOVE_MD = "reviews/white-glove-checklist.md"
PATCH_LOG_MD = "reviews/patch-log.md"
TECHNICAL_REVIEW_APPROACH_MD = "reviews/technical-review-approach.md"
TECHNICAL_REVIEW_DRAFTS_MD = "reviews/technical-review-drafts.md"
COMPLIANCE_GAPS_MD = "reviews/compliance-gaps.md"
EVIDENCE_CHECK_MD = "reviews/evidence-check.md"

# Key working artifacts (for the artifact health panel)
KEY_WORKING_ARTIFACTS: list[tuple[str, str]] = [
    ("working/narrative-spine.md", "Narrative Spine"),
    ("working/proposal-plan.md", "Proposal Plan"),
    ("working/capture-intent.md", "Capture Intent"),
    ("working/solution-strategy.md", "Solution Strategy"),
    ("working/architecture-concept.md", "Architecture Concept"),
    ("working/storyboard.md", "Storyboard"),
    ("working/graphics-brief.md", "Graphics Brief"),
    ("working/compliance-matrix.md", "Compliance Matrix"),
    ("working/pricing-inputs.md", "Pricing Inputs"),
]

# Company-wide files
EVIDENCE_LEDGER_JSON = MY_COMPANY_DIR / "evidence-ledger.json"

# UI
APP_TITLE = "Federal Proposal Assistant — Dashboard"
APP_ICON = ":briefcase:"
