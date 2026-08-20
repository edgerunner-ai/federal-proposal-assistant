"""Per-proposal detail view — command bar, tabbed layout, visual pipeline stepper."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st

from dashboard.config import (
    ACTIVITY_MD,
    COMPLIANCE_GAPS_MD,
    EVIDENCE_CHECK_MD,
    GOLD_TEAM_MD,
    KEY_WORKING_ARTIFACTS,
    NARRATIVE_SPINE_MD,
    PATCH_LOG_MD,
    PROPOSALS_DIR,
    RED_TEAM_NOTES_MD,
    TECHNICAL_REVIEW_APPROACH_MD,
    TECHNICAL_REVIEW_DRAFTS_MD,
    WHITE_GLOVE_MD,
)
from dashboard.loaders import (
    _parse_activity,
    _read_jsonl,
    load_proposal_summary,
)
from dashboard.views.helpers import (
    SKILL_LABELS,
    TRACK_B_STAGES,
    fmt_due,
    health_badge,
    is_track_b,
    next_action,
    pipeline_progress,
)

_STEPS_PER_ROW = 7


# ────────────────────────────────────────────────
# Pipeline stepper helpers
# ────────────────────────────────────────────────

def _render_track_b_stepper(s) -> None:
    """6-stage Track B stepper for white-paper type proposals."""
    completed_set = set(s.completed_skills)
    current_found = False

    st.markdown("**Track B Stages** (narrative-first white-paper workflow)")
    cols = st.columns(len(TRACK_B_STAGES))
    for col, (skill, label) in zip(cols, TRACK_B_STAGES):
        with col:
            if skill in completed_set:
                st.markdown(f"✅\n\n**{label}**")
            elif not current_found:
                current_found = True
                st.markdown(f"▶️\n\n**{label}**")
            else:
                st.markdown(f"○\n\n{label}")

    st.caption(
        "Track B: spine → draft-loose → bind → evidence-check → gold-team → patch → export. "
        "Skips storyboard and editor."
    )


def _render_stepper(s) -> None:
    """Full pipeline stepper: ✅ done / ▶️ current / ○ pending."""
    if not s.required_skills:
        st.caption(
            "No `working/proposal-type.md` found — cannot show pipeline. "
            "Run `/new-proposal` to set one up."
        )
        return

    if is_track_b(s.type_id):
        _render_track_b_stepper(s)
        st.divider()
        st.markdown("**Full required-skill list:**")

    completed_set = set(s.completed_skills)
    current_found = False
    steps: list[tuple[str, str]] = []

    for skill in s.required_skills:
        if skill in completed_set:
            status = "done"
        elif not current_found:
            status = "current"
            current_found = True
        else:
            status = "pending"
        steps.append((skill, status))

    for row_start in range(0, len(steps), _STEPS_PER_ROW):
        row = steps[row_start : row_start + _STEPS_PER_ROW]
        cols = st.columns(len(row))
        for col, (skill, status) in zip(cols, row):
            num = s.required_skills.index(skill) + 1
            label = SKILL_LABELS.get(skill, skill)
            with col:
                if status == "done":
                    st.markdown(f"✅ **{num}**\n\n{label}")
                elif status == "current":
                    st.markdown(f"▶️ **{num}**\n\n**{label}**")
                else:
                    st.markdown(f"○ {num}\n\n{label}")
        if row_start + _STEPS_PER_ROW < len(steps):
            st.write("")

    if s.skipped_skills:
        st.caption(
            f"Skipped for type `{s.type_id}`: "
            + ", ".join(f"`{sk}`" for sk in s.skipped_skills)
        )


# ────────────────────────────────────────────────
# Key artifacts panel
# ────────────────────────────────────────────────

def _render_key_artifacts(root: Path) -> None:
    rows = []
    for rel_path, label in KEY_WORKING_ARTIFACTS:
        p = root / rel_path
        if p.exists():
            stat = p.stat()
            modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
            size_kb = stat.st_size / 1024
            rows.append({
                "Artifact": label,
                "Status": "✅",
                "Modified": modified,
                "Size": f"{size_kb:.1f} KB",
            })
        else:
            rows.append({
                "Artifact": label,
                "Status": "○ missing",
                "Modified": "—",
                "Size": "—",
            })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


# ────────────────────────────────────────────────
# Narrative spine viewer
# ────────────────────────────────────────────────

def _render_spine_viewer(root: Path) -> None:
    spine_path = root / NARRATIVE_SPINE_MD
    if not spine_path.exists():
        st.info(
            "No narrative spine yet. Run `/narrative-spine` after `/proposal-solution-architect` "
            "to write the one-page argument — the spine is the foundation everything drafts from."
        )
        return

    try:
        content = spine_path.read_text(encoding="utf-8", errors="replace")
        stat = spine_path.stat()
        modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
        word_count = len(content.split())
    except OSError:
        st.warning("Could not read narrative-spine.md.")
        return

    col_meta, _ = st.columns([3, 1])
    col_meta.caption(f"Last modified: **{modified}** · {word_count} words")

    with st.expander("Read narrative spine (working/narrative-spine.md)", expanded=True):
        st.markdown(content)


# ────────────────────────────────────────────────
# Drafts tab
# ────────────────────────────────────────────────

def _word_count(text: str) -> int:
    return len(text.split())


def _render_drafts_tab(root: Path) -> None:
    drafts_dir = root / "drafts"
    loose_dir = drafts_dir / "loose"
    patched_dir = drafts_dir / "patched"  # future patcher output

    if not drafts_dir.exists():
        st.info(
            "No `drafts/` directory yet. Run `/proposal-writer` to generate section drafts."
        )
        return

    # Collect bound drafts (direct children of drafts/, not in subdirs)
    bound_files = sorted(
        f for f in drafts_dir.glob("*.md") if f.is_file()
    )

    if not bound_files:
        # Check for loose drafts only (writer --mode=draft-loose ran but bind hasn't)
        if loose_dir.exists():
            loose_only = sorted(loose_dir.glob("*.md"))
            if loose_only:
                st.warning(
                    "Only loose drafts found (`drafts/loose/`). "
                    "Run `/proposal-writer --mode=bind` to produce the verified bound drafts."
                )
                bound_files = []
        if not bound_files:
            st.info(
                "Draft files not found in `drafts/`. "
                "Run `/proposal-writer` (or `--mode=draft-loose` then `--mode=bind`) to generate them."
            )
            return

    # ── Summary strip
    total_words = 0
    for f in bound_files:
        try:
            total_words += _word_count(f.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            pass

    n_sections = len(bound_files)
    loose_count = len(list(loose_dir.glob("*.md"))) if loose_dir.exists() else 0
    has_loose = loose_count > 0

    c1, c2, c3 = st.columns(3)
    c1.metric("Sections", n_sections)
    c2.metric("Total words", f"{total_words:,}")
    c3.metric("Loose drafts", loose_count if has_loose else "—")

    if has_loose and loose_count < n_sections:
        st.caption(
            f"⚠️ {loose_count} loose / {n_sections} bound — some sections were re-bound "
            "after the loose draft was replaced. The loose column shows pre-bind text where available."
        )

    st.divider()

    # ── Section selector
    section_stems = [f.stem for f in bound_files]
    selected_stem = st.selectbox(
        "Section",
        options=section_stems,
        format_func=lambda s: s.replace("-", " ").title(),
        key="draft_section_selector",
    )

    bound_path = drafts_dir / f"{selected_stem}.md"
    loose_path = loose_dir / f"{selected_stem}.md" if loose_dir.exists() else None
    has_loose_for_section = loose_path is not None and loose_path.exists()

    # ── Section metadata
    try:
        bound_text = bound_path.read_text(encoding="utf-8", errors="replace")
        bound_words = _word_count(bound_text)
        bound_modified = datetime.fromtimestamp(
            bound_path.stat().st_mtime
        ).strftime("%Y-%m-%d %H:%M")
    except OSError:
        st.error(f"Could not read {bound_path.name}.")
        return

    meta_cols = st.columns(3)
    meta_cols[0].metric("Words", bound_words)
    meta_cols[1].caption(f"**Bound** modified\n\n{bound_modified}")
    if has_loose_for_section:
        try:
            loose_text = loose_path.read_text(encoding="utf-8", errors="replace")
            loose_words = _word_count(loose_text)
            loose_modified = datetime.fromtimestamp(
                loose_path.stat().st_mtime
            ).strftime("%Y-%m-%d %H:%M")
            meta_cols[2].caption(f"**Loose** modified\n\n{loose_modified} ({loose_words} words)")
        except OSError:
            loose_text = ""
            has_loose_for_section = False

    # ── Unsupported claim count
    claim_count = bound_text.count("CLAIM-UNSUPPORTED")
    if claim_count:
        st.warning(
            f"⚠️ {claim_count} `CLAIM-UNSUPPORTED` marker{'s' if claim_count > 1 else ''} in this section. "
            "Run `/evidence-check` then `/proposal-patcher` to resolve."
        )

    st.divider()

    # ── Content display
    if has_loose_for_section:
        tab_bound, tab_loose = st.tabs(["Bound draft", "Loose draft (pre-bind)"])
        with tab_bound:
            st.markdown(bound_text)
        with tab_loose:
            st.markdown(loose_text)
    else:
        st.markdown(bound_text)

    # ── All-sections word budget table
    st.divider()
    with st.expander("Word count by section"):
        wc_rows = []
        for f in bound_files:
            try:
                txt = f.read_text(encoding="utf-8", errors="replace")
                wc = _word_count(txt)
                unsupported = txt.count("CLAIM-UNSUPPORTED")
            except OSError:
                wc = 0
                unsupported = 0
            wc_rows.append({
                "Section": f.stem.replace("-", " ").title(),
                "Words": wc,
                "CLAIM-UNSUPPORTED": unsupported if unsupported else "—",
                "Loose?": "✅" if (loose_dir / f.name).exists() else "—",
            })
        wc_rows.append({
            "Section": "TOTAL",
            "Words": sum(r["Words"] for r in wc_rows),
            "CLAIM-UNSUPPORTED": "—",
            "Loose?": "—",
        })
        st.dataframe(pd.DataFrame(wc_rows), use_container_width=True, hide_index=True)


# ────────────────────────────────────────────────
# Reviews tab helpers
# ────────────────────────────────────────────────

def _render_review_file(root: Path, rel_path: str, label: str, expanded: bool = False) -> bool:
    """Render a review markdown file in an expander. Returns True if file existed."""
    p = root / rel_path
    if not p.exists():
        return False
    try:
        content = p.read_text(encoding="utf-8", errors="replace")
        stat = p.stat()
        modified = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
    except OSError:
        return False

    with st.expander(f"{label} — `{rel_path}` (modified {modified})", expanded=expanded):
        st.markdown(content)
    return True


# ────────────────────────────────────────────────
# Main render
# ────────────────────────────────────────────────

def render() -> None:
    slug = st.session_state.get("selected_proposal")
    if not slug:
        st.warning("No proposal selected. Go to **Triage** and click **Open →**.")
        return

    root = PROPOSALS_DIR / slug
    if not root.exists():
        st.error(f"Proposal `{slug}` not found under `proposals/`.")
        return

    s = load_proposal_summary(root)
    badge, _label = health_badge(s)
    cmd = next_action(s)
    track_b = is_track_b(s.type_id)

    # ── Header
    track_b_tag = " · **Track B**" if track_b else ""
    st.title(f"{badge}  {s.slug}")

    m1, m2, m3, m4 = st.columns(4)
    m1.markdown(f"**Type**\n\n{s.display_name or s.type_id or '—'}{track_b_tag}")
    m2.markdown(f"**Customer**\n\n{s.customer or '—'}")
    m3.markdown(f"**Due**\n\n{fmt_due(s.due_date)}")
    m4.markdown(f"**Pages**\n\n{s.page_target or '—'}")

    if not s.v15_migrated:
        st.warning(
            "Pre-v1.5 proposal: JSON sidecars not found. "
            "Dashboard shows what it can infer from markdown files. "
            "Run `/compliance-check` and ensure `working/proposal-type.md` exists to fully migrate."
        )

    # ── Command bar
    st.write("")
    if cmd:
        with st.container(border=True):
            st.markdown("#### What to run next")
            bar_cmd, bar_prog = st.columns([2, 3])
            with bar_cmd:
                st.code(cmd, language="bash")
                st.caption("Copy the command above and paste into Claude Code.")
            with bar_prog:
                done, total_req = pipeline_progress(s)
                if total_req:
                    st.progress(
                        done / total_req,
                        text=f"Pipeline: {done} / {total_req} skills complete",
                    )
    else:
        st.success(
            "✅ All required skills complete — ready for `/export-proposal` or a final Gold Team review."
        )

    st.divider()

    # ── Tabs
    tab_pipe, tab_drafts, tab_comp, tab_ev, tab_rev, tab_spend = st.tabs(
        ["Pipeline", "Drafts", "Compliance", "Evidence", "Reviews", "Spend"]
    )

    # ────────────────────────────────────────────────
    # Pipeline tab
    # ────────────────────────────────────────────────
    with tab_pipe:
        st.subheader("Skill Pipeline")
        _render_stepper(s)

        # ── Narrative spine
        st.divider()
        st.subheader("Narrative Spine")
        _render_spine_viewer(root)

        # ── Key artifacts
        st.divider()
        st.subheader("Key Artifacts")
        _render_key_artifacts(root)

        # ── Skill detail table
        if s.required_skills:
            st.divider()
            st.subheader("Skill detail")
            rows = []
            for skill in s.required_skills:
                done_bool = skill in s.completed_skills
                if done_bool:
                    status_str = "✅ done"
                elif cmd == f"/{skill}":
                    status_str = "▶ next"
                else:
                    status_str = "○ pending"
                rows.append({
                    "#": s.required_skills.index(skill) + 1,
                    "Skill": skill,
                    "Label": SKILL_LABELS.get(skill, skill),
                    "Status": status_str,
                })
            for skill in s.skipped_skills:
                rows.append({
                    "#": "—",
                    "Skill": skill,
                    "Label": SKILL_LABELS.get(skill, skill),
                    "Status": f"⏭ skipped ({s.type_id})",
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

        # ── Recent activity
        st.divider()
        st.subheader("Recent activity")
        entries = _parse_activity(root / ACTIVITY_MD)
        if entries:
            recent = list(reversed(entries))[:10]
            act_rows = [
                {
                    "When": (
                        e["timestamp"].strftime("%Y-%m-%d %H:%M")
                        if e["timestamp"]
                        else e["timestamp_str"]
                    ),
                    "Skill": e["skill"] + (f" [{e['mode']}]" if e["mode"] else ""),
                    "Summary": (e["summary"] or "")[:120],
                    "Output": (e["output"] or "")[:60],
                }
                for e in recent
            ]
            st.dataframe(pd.DataFrame(act_rows), use_container_width=True, hide_index=True)
        else:
            st.caption("No activity logged yet. Skills write to `working/activity.md` on completion.")

    # ────────────────────────────────────────────────
    # Drafts tab
    # ────────────────────────────────────────────────
    with tab_drafts:
        st.subheader("Draft Content")
        _render_drafts_tab(root)

    # ────────────────────────────────────────────────
    # Compliance tab
    # ────────────────────────────────────────────────
    with tab_comp:
        st.subheader("Compliance Coverage")
        if s.has_compliance_json:
            c1, c2, c3, c4, c5, c6 = st.columns(6)
            c1.metric("Total", s.compliance_total)
            c2.metric("Covered", s.compliance_covered)
            c3.metric("Drafted", s.compliance_drafted)
            c4.metric("Planned", s.compliance_planned)
            c5.metric("Partial", s.compliance_partial)
            c6.metric("Gaps", s.compliance_gap)

            if s.coverage_pct is not None:
                st.progress(
                    min(100, int(s.coverage_pct)) / 100,
                    text=f"Coverage: {s.coverage_pct:.0f}% (Covered + Drafted / Total)",
                )

            gaps_path = root / COMPLIANCE_GAPS_MD
            if gaps_path.exists():
                with st.expander("Open gaps — reviews/compliance-gaps.md"):
                    try:
                        st.markdown(gaps_path.read_text(encoding="utf-8", errors="replace"))
                    except OSError:
                        st.caption("Could not read gaps file.")
        else:
            st.info(
                "No compliance JSON yet. Run `/compliance-check` to generate it. "
                "The skill produces `working/compliance-matrix.json` which powers this view."
            )
            if s.type_id in ("white-paper",):
                st.caption(
                    "Note: white-paper type skips compliance-check (no compliance matrix). "
                    "Evidence coverage is tracked separately in the Evidence tab."
                )

    # ────────────────────────────────────────────────
    # Evidence tab
    # ────────────────────────────────────────────────
    with tab_ev:
        st.subheader("Evidence Coverage")
        if s.evidence_coverage_pct is not None:
            st.progress(
                min(100, int(s.evidence_coverage_pct)) / 100,
                text=f"Evidence: {s.evidence_coverage_pct:.0f}% of claim markers supported",
            )
        else:
            st.info(
                "No evidence coverage data. Run `/evidence-check` after drafting to compute."
            )

        _render_review_file(root, EVIDENCE_CHECK_MD, "Evidence check report", expanded=False)

    # ────────────────────────────────────────────────
    # Reviews tab
    # ────────────────────────────────────────────────
    with tab_rev:
        # ── Gold Team (primary)
        st.subheader("Gold Team")
        gt_path = root / GOLD_TEAM_MD
        if s.gold_team_exists:
            st.metric("pWin Estimate", s.gold_team_pwin or "—")
            _render_review_file(root, GOLD_TEAM_MD, "Gold Team scorecard", expanded=True)
        else:
            st.info(
                "Gold Team review not yet run. "
                "Run `/red-team-review --mode=gold` after drafting and evidence-check."
            )

        # ── Patch log
        if (root / PATCH_LOG_MD).exists():
            st.divider()
            st.subheader("Patch Log")
            _render_review_file(root, PATCH_LOG_MD, "Patch log (proposal-patcher output)", expanded=True)
        elif s.gold_team_exists:
            st.divider()
            st.caption(
                "No patch log yet. After Gold Team review, run `/proposal-patcher` to apply "
                "W/D findings surgically. Patch log will appear here."
            )

        # ── Red Team notes
        st.divider()
        st.subheader("Red Team Notes")
        if not _render_review_file(root, RED_TEAM_NOTES_MD, "Red Team notes"):
            st.info("No red-team notes yet. Run `/red-team-review --mode=red`.")

        # ── White Glove
        st.divider()
        st.subheader("White Glove")
        if not _render_review_file(root, WHITE_GLOVE_MD, "White Glove checklist"):
            st.info("No white glove checklist yet. Run `/red-team-review --mode=white-glove`.")

        # ── Technical review
        approach_exists = _render_review_file(
            root, TECHNICAL_REVIEW_APPROACH_MD, "Technical Review — Approach phase"
        )
        drafts_exists = _render_review_file(
            root, TECHNICAL_REVIEW_DRAFTS_MD, "Technical Review — Drafts phase"
        )
        if not approach_exists and not drafts_exists:
            st.divider()
            st.caption(
                "No technical review files yet. "
                "Run `/technical-review --phase=approach` before drafting or "
                "`--phase=drafts` after."
            )

    # ────────────────────────────────────────────────
    # Spend tab
    # ────────────────────────────────────────────────
    with tab_spend:
        st.subheader("AI Spend")
        if s.has_ai_runs:
            sc1, sc2 = st.columns(2)
            sc1.metric("AI runs logged", s.ai_run_count)
            sc2.metric(
                "Estimated cost",
                f"${s.ai_total_cost_usd:,.2f}" + (" *" if s.ai_cost_is_estimated else ""),
            )
            if s.ai_cost_is_estimated:
                st.caption(
                    "\\* Token counts are null in the ledger; cost shows `$0.00` "
                    "until skills log real `input_tokens_estimate` values."
                )

            runs = _read_jsonl(root / "working/ai-runs.jsonl")
            if runs:
                run_df = pd.DataFrame(runs)
                cols_keep = [
                    c for c in [
                        "timestamp", "skill", "job_type", "model",
                        "input_tokens_estimate", "output_tokens_estimate", "cost_estimate_usd",
                    ]
                    if c in run_df.columns
                ]
                st.dataframe(run_df[cols_keep], use_container_width=True, hide_index=True)
        else:
            st.info(
                "No AI runs logged. Skills append to `working/ai-runs.jsonl` per the CLAUDE.md "
                "Activity Trail convention."
            )

        st.caption(f"Proposal files: `{root}`")
