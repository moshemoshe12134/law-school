# QC Checklists (Operational Standards)

This file defines what “done” means so prep/review outputs are consistent without bespoke prompting.

## Prep Packet QC (must-pass)
- File name matches: `Lectures/Prep/Packets/YYYY-MM-DD_classNN_prep.md`
- YAML frontmatter exists and has: `doc_type`, `class_number`, `date`, `title`, `status`, `inputs.syllabus_assignment`
- Contains all required headings (exact or near-exact):
  - `## 1) Assignment Snapshot`
  - `## 2) MPC Parsing Sheet (primary)`
  - `## 3) Policy / Theory Brief (co-primary; ~50% exam)`
  - `## 4) Minimal Case Cards (tertiary)`
  - `## 5) Cold Call / Co‑Counsel Script (2 minutes)`
  - `## 6) Predictions (explicit + falsifiable)`
  - `## 7) TA / Office Hours Questions (if any)`
- MPC section list is explicit (even if short): at least one `### MPC § ___` block when MPC is assigned.
- Policy brief has:
  - 1-sentence thesis
  - 3 claims
  - 2 quotes (or a placeholder if quotes unavailable in the source file)
- Predictions are falsifiable (not generic): “likely cover X, likely skip Y, likely cold-call Z”.
- Length/time check:
  - Fits within the configured `time_budget_minutes` (default 90); if longer, the doc starts with a triage plan.

## Review Doc QC (must-pass)
- File name matches: `Lectures/Reviews/YYYY-MM-DD_classNN_review.md`
- YAML frontmatter exists and has: `doc_type`, `class_number`, `date`, `title`, `inputs.prep_packet`, `inputs.class_notes_raw`
- Contains all required headings:
  - `## 1) What Actually Happened (5 bullets max)`
  - `## 2) Deltas vs Prep Packet`
  - `## 3) MPC “Moves” Harcourt Modeled`
  - `## 4) Policy / Theory Integration`
  - `## 5) Exam Signals`
  - `## 6) Outline Inserts (copy-ready)`
  - `## 7) Spaced Reinforcement (10–15 minutes later)`
- Has at least one concrete “delta” and at least one outline insert (or explicitly says “no changes needed”).
- Prediction accuracy is scored in frontmatter (`metrics.prediction_accuracy: 0|1|2`).

## Audio Prep QC (must-pass)
- File name matches: `Lectures/Prep/Audio/YYYY-MM-DD_classNN_audio_prep.md`
- YAML frontmatter exists and has: `doc_type`, `class_number`, `date`, `title`, `status`
- Contains (at least) these headings:
  - `## INTRO`
  - `## COLD CALL PREP`
  - `## CLOSING`
- TTS-friendly formatting: short paragraphs, no tables, minimal inline citations.
- Includes explicit cold-call questions with answer starters (not just summaries).

## Class Reference QC (must-pass)
- File name matches: `Lectures/Prep/Reference/YYYY-MM-DD_classNN_class_reference.md`
- YAML frontmatter exists and has: `doc_type`, `class_number`, `date`, `title`, `status`, `inputs.syllabus_assignment`
- Contains (at least) these headings:
  - `## QUICK NAVIGATION`
  - `## CORE DOCTRINE`
  - `## EXPECTED HARCOURT QUESTIONS (Q→A)`
  - `## CASE BRIEFS`
  - `## POLICY / THEORY`
  - `## QUICK HYPOS`
  - `## SEARCH TERMS`
- Hypos include both‑side arguments (prosecution + defense) and a likely Harcourt push.
- Missing/unstored assigned supplements are explicitly flagged (no silent guessing).
