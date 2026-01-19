# Command Interface (Standard Prompts → Standard Procedure)

Use the commands below verbatim (or close to verbatim). The goal is that you never need to write a bespoke prompt to get consistent outputs.

## Two‑Doc System (What You Actually Use)
- System spec: `Admin/Two_Doc_Prep_System.md`
- Per‑class blueprint: `Admin/Per_Class_Prep_Blueprint.md`
- Audio prep style: `Lectures/Prep/Style_Guides/AUDIO_PREP_STYLE_GUIDE.md`
- Class reference style: `Lectures/Prep/Style_Guides/CLASS_REFERENCE_STYLE_GUIDE.md`

## Canonical State File
- Backbone: `Admin/Master_Log.md`
- Assignments: `Admin/Syllabus/Assignments/`
- Standards: `Admin/Templates/QC_Checklists.md`
- Templates: `Admin/Templates/Audio_Prep_TEMPLATE.md`, `Admin/Templates/Class_Reference_TEMPLATE.md`, `Admin/Templates/Prep_Packet_TEMPLATE.md`, `Admin/Templates/Review_Doc_TEMPLATE.md`
  
## Optional Helper Scripts (for determinism)
- “What’s next?”: `python3 Admin/Scripts/next_class.py prep|review|outline`
- QC: `python3 Admin/Scripts/qc_doc.py path/to/doc.md`

## Naming Conventions (so automation is possible)
- Prep (scaffolding): `Lectures/Prep/Packets/YYYY-MM-DD_classNN_prep.md`
- Audio prep: `Lectures/Prep/Audio/YYYY-MM-DD_classNN_audio_prep.md`
- Class reference: `Lectures/Prep/Reference/YYYY-MM-DD_classNN_class_reference.md`
- Transcript: `Lectures/Transcripts/raw/YYYY-MM-DD_classNN_notes.md`
- Review: `Lectures/Reviews/YYYY-MM-DD_classNN_review.md`

## Course Priorities (Harcourt-tuned)
1. **MPC close reading** (syntax, structure, defined terms, element breakdown).
2. **Policy/theory supplements** (expect ~50% policy on the exam).
3. **Cases** as vehicles/hypos (often not exam-central).
4. Hornbook (Dressler) as fast scaffolding; Kadish only as needed for assigned items.

---

# Commands

## A) `audio prep for YYYY-MM-DD` (or `audio prep for class NN`)
**What it means**: Create the TTS-friendly script you’ll listen to before class.

**Agent procedure**
1. Open the matching `Admin/Syllabus/Assignments/...` file.
2. Create `Lectures/Prep/Audio/YYYY-MM-DD_classNN_audio_prep.md` using `Admin/Templates/Audio_Prep_TEMPLATE.md`.
3. Use `Admin/Per_Class_Prep_Blueprint.md` for “must cover” items + likely cold calls.
4. If an assigned supplement is not stored locally, flag it explicitly (don’t fake quotes).
5. QC using `python3 Admin/Scripts/qc_doc.py --type audio path/to/audio.md`.

## B) `class reference for YYYY-MM-DD` (or `class reference for class NN`)
**What it means**: Create the in-class searchable Q&A reference for cold calls.

**Agent procedure**
1. Open the matching `Admin/Syllabus/Assignments/...` file.
2. Create `Lectures/Prep/Reference/YYYY-MM-DD_classNN_class_reference.md` using `Admin/Templates/Class_Reference_TEMPLATE.md`.
3. Prefer these priors unless you specify otherwise:
   - `Admin/Sources/Past_Outlines/Crim_Spring 2025_Harcourt_Full.docx.md`
   - `Admin/Sources/Past_Outlines/Criminal Law_Spring 2023_Harcourt_Exam Outline - Tanisha Gupta.docx.md`
   - `Admin/Sources/Past_Outlines/Crim Policy Notes.docx.md`
   - `Admin/Sources/Past_Outlines/MPC Supplement.docx.md`
4. Populate: expected Harcourt Q→A, doctrine, case briefs, policy frames, ≥5 hypos, search terms.
5. QC using `python3 Admin/Scripts/qc_doc.py --type class_reference path/to/reference.md`.

## 1) `next prep doc`
**What it means**: Create the prep packet for the *earliest* class whose `Prep Status` is `todo` in `Admin/Master_Log.md`.

**Agent procedure**
1. Open `Admin/Master_Log.md` → **Class Pipeline** table.
2. Select the first row where `Prep Status = todo` and not `skip`.
3. Open the row’s `Assignment` file in `Admin/Syllabus/Assignments/`.
4. Create `Prep Doc` at the path listed in the row using `Admin/Templates/Prep_Packet_TEMPLATE.md`:
   - Fill metadata (class/date/title, link to assignment).
   - Extract assigned MPC sections from the assignment file (if any) and create MPC parsing subsections.
   - Build a 1‑page policy/theory brief for any assigned supplements.
   - Keep cases minimalist; focus on hypo usefulness + MPC/policy hooks.
   - Write falsifiable predictions (what will be covered/skipped, likely questions).
5. QC the prep doc against `Admin/Templates/QC_Checklists.md`:
   - If pass → set doc `status: final` and set `Prep Status = final` in `Admin/Master_Log.md`.
   - If fail → set doc `status: draft`, note gaps at top of doc, and keep `Prep Status = draft`.
6. Update that row in `Admin/Master_Log.md`: `Last Touched = now`, `Next Action = (usually) Class`.

## 2) `prep doc for YYYY-MM-DD`
**What it means**: Create (or regenerate) the prep packet for that date.

**Agent procedure**
- Same as `next prep doc`, but select the matching `Date` row. If the prep doc already exists and is `final`, run `qc prep doc YYYY-MM-DD` instead unless you ask for a rewrite.

## 3) `prep doc for class NN`
Same as above, selecting by `Class#`.

---

## 4) `qc prep doc YYYY-MM-DD` (or a file path)
**What it means**: Verify the prep packet conforms to the required structure and Harcourt priorities.

**Agent procedure**
1. Open the target prep doc and `Admin/Templates/QC_Checklists.md`.
2. Check required sections + frontmatter + MPC/policy coverage + falsifiable predictions.
3. If issues:
   - Fix the doc in-place (preferred) and re-run QC.
   - If major ambiguity remains, list the exact missing inputs.
4. Update `Admin/Master_Log.md` row: set `Prep Status` to `final` if it passes.

---

## 5) `add class notes YYYY-MM-DD`
**What it means**: You will paste notes/transcript; the agent will store them in the canonical notes path from the row.

**Agent procedure**
1. Locate the row by date in `Admin/Master_Log.md`.
2. Write your pasted notes to the `Notes` path in that row (create folders if needed).
3. Set `Last Touched = now`, `Next Action = Review`.

*(If you already have a file, use `link class notes YYYY-MM-DD path/to/file`.)*

## 6) `create review doc YYYY-MM-DD`
**What it means**: Generate post-class review by comparing notes/transcript to the prep packet, then create outline inserts.

**Agent procedure**
1. Locate row by date in `Admin/Master_Log.md`; open `Prep Doc` + `Notes`.
2. Create `Review Doc` using `Admin/Templates/Review_Doc_TEMPLATE.md`.
3. Produce deltas vs prep; extract MPC interpretive moves; extract policy takeaways; create copy-ready outline inserts.
4. Score prediction accuracy (`0/1/2`) in review doc frontmatter.
5. QC review doc against `Admin/Templates/QC_Checklists.md`.
6. Update row: `Review Status`, `Pred Acc`, `Next Action = Outline`.

## 7) `qc review doc YYYY-MM-DD` (or a file path)
Same idea as `qc prep doc`, using the Review QC checklist.

---

## 8) `update outline YYYY-MM-DD`
**What it means**: Integrate the review doc’s “Outline Inserts” into `Exams/Outline/Cumulative_Outline.md` (and/or `Exams/Outline/Policy_Bank.md`).

**Agent procedure**
1. Open the review doc for that date.
2. Insert/update only the relevant sections in `Exams/Outline/` (no full rewrite).
3. Mark `Outline Updated = Y` in `Admin/Master_Log.md` and set `Next Action = Prep` for the next class.

---

## 9) `index past exams`
**What it means**: Summarize the available past exams to build an “Exam Spec” (question types + what gets rewarded).

**Agent procedure**
1. Review `Exams/Past_Exams/`.
2. Create `Exams/Exam_Spec.md` with: structure, time constraints, policy vs doctrine ratio, and a checklist of what to practice.
3. Update `Admin/Master_Log.md` → set `P-004` to `final`.

## 10) `index past outlines`
**What it means**: Build a topic-priority “priors” index from `Admin/Sources/Past_Outlines/`.

**Agent procedure**
1. Review `Admin/Sources/Past_Outlines/` (prefer `.md` files when available).
2. Create `Admin/Mapping/Past_Outlines_Index.md` with: recurring topics, recurring policy themes, and recommended weighting—flagged as “must verify in class.”
3. Update `Admin/Master_Log.md` → set `P-005` to `final`.
