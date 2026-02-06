# COMMAND INTERFACE - Standard Prompts

**Purpose:** Course-agnostic commands for consistent AI interactions across all 5 courses.

---

## Usage

Use these commands verbatim (or close to verbatim). The goal is that you never need to write a bespoke prompt to get consistent outputs.

**How to use:**
- Prepend command with course name: "CrimLaw: prep for class 5"
- Or specify course in command: "prep for Property class 3"

---

## Core References

**Universal system specs:**
- `00_SYSTEM/FOLDER_STRUCTURE_SPEC.md` - Folder structure for all courses
- `01_WORKFLOWS/` - All workflow documentation

**Templates:**
- `03_TEMPLATES/audio_prep_template.md`
- `03_TEMPLATES/text_prep_template.md`
- `03_TEMPLATES/review_template.md`
- `03_TEMPLATES/master_log_template.md`
- `03_TEMPLATES/prewrite_doctrinal_template.md`
- `03_TEMPLATES/prewrite_policy_template.md`
- `03_TEMPLATES/qc_checklist_template.md`

**Style guides:**
- `02_STYLE_GUIDES/WRITING_FOUNDATIONS.md` - Universal writing standards
- `00_ADMIN/course_style_guide.md` - Course-specific standards

---

## Commands

### `prep for [COURSE] class [NN]`

**Aliases:** `prep [COURSE] class NN`, `generate prep for [COURSE] class NN`

**What it means:** Create both audio and text preps for the specified class.

**Agent procedure:**
1. Open course folder: `[COURSE]/`
2. Check `00_ADMIN/MASTER_LOG.md` for class NN details
3. Open assignment file: `01_SOURCES/syllabus/assignments/YYYY-MM-DD_classNN.md`
4. Create text prep: `02_PREP/text/YYYY-MM-DD_classNN_text.md`
   - Use template: `03_TEMPLATES/text_prep_template.md`
   - **REQUIRED sections**: QUICK NAVIGATION, BOOK NAVIGATION, CORE DOCTRINE, DEFINITIONS TO HAVE READY, EXPECTED QUESTIONS, CASE BRIEFS, POLICY/THEORY, QUICK HYPOS, SEARCH TERMS, EXAM SIGNALS, PROFESSOR'S SPECIAL PROMPTS
   - Include: Core doctrine, expected questions, case briefs, policy, 5+ hypos
   - **Integrate past exam spec**: Check `00_ADMIN/exam_spec.md` for how this topic was tested in past years
   - **Integrate syllabus prompts**: If professor highlighted special questions/exercises for this class, include them
   - **Integrate past outlines**: Reference how past students organized this topic
5. Create audio prep: `02_PREP/audio/YYYY-MM-DD_classNN_audio.md`
   - Use template: `03_TEMPLATES/audio_prep_template.md`
   - Transform text prep into conversational format
   - Target: 4,000-5,000 words (~25-30 min at 1.5x)
6. QC both documents against `03_TEMPLATES/qc_checklist_template.md`
7. Update `00_ADMIN/MASTER_LOG.md`:
   - Mark `Prep` as "Done"
   - Mark `Audio?` as ✅
   - Update `Next Action`

---

### `prep for next [COURSE] class`

**Aliases:** `prep next [COURSE]`, `make prep for next [COURSE] class`, `create prep for next [COURSE]`

**What it means:** Create both audio and text preps for the next upcoming class.

**Agent procedure:**
1. Open `00_ADMIN/MASTER_LOG.md`
2. **Find next class:** Look for the first class where EITHER:
   - `Prep` column is empty OR "Not Started"
   - `Class?` is NOT ✅ (class hasn't happened yet)
3. Extract class number, date, and assignment path from that row
4. Execute `prep for [COURSE] class [NN]` procedure with that class number

**If all classes have prep or have already happened:** Report "No upcoming classes need prep" and show next 2 scheduled classes.

---

### `text prep for [COURSE] class [NN]`

**What it means:** Create only the text prep (comprehensive reference).

**Agent procedure:**
1. Open course folder and MASTER_LOG
2. Open assignment file for class NN
3. Create text prep: `02_PREP/text/YYYY-MM-DD_classNN_text.md`
   - Use template: `03_TEMPLATES/text_prep_template.md`
   - **REQUIRED sections**: QUICK NAVIGATION, BOOK NAVIGATION, CORE DOCTRINE, DEFINITIONS TO HAVE READY, EXPECTED QUESTIONS, CASE BRIEFS, POLICY/THEORY, QUICK HYPOS, SEARCH TERMS, EXAM SIGNALS, PROFESSOR'S SPECIAL PROMPTS
   - **READ INDEX FILES FIRST** (efficient lookup):
     - `01_SOURCES/past_outlines/INDEX.md` → Find topic → get file + line range
     - `01_SOURCES/past_exams/INDEX.md` → Find topic → see exam history + model answers
   - **Integrate past exam spec**: Check `00_ADMIN/exam_spec.md` for how this topic was tested
   - **Integrate syllabus prompts**: If professor highlighted special questions/exercises, include them
   - **Integrate past outlines**: Read ONLY the relevant lines from the recommended outline
4. QC against checklist
5. Update MASTER_LOG

---

### `audio prep for [COURSE] class [NN]`

**What it means:** Create only the audio prep (TTS-friendly script).

**Agent procedure:**
1. Open course folder and MASTER_LOG
2. Open assignment file for class NN
3. If text prep exists, use it as source
4. Create audio prep: `02_PREP/audio/YYYY-MM-DD_classNN_audio.md`
   - Use template: `03_TEMPLATES/audio_prep_template.md`
   - Conversational tone, TTS-friendly formatting
   - Target: 4,000-5,000 words
5. QC against checklist
6. Update MASTER_LOG

---

### `ingest transcripts [COURSE]`

**Aliases:** `scan transcripts [COURSE]`, `register transcripts [COURSE]`

**What it means:** Scan for new transcripts and register them in the review tracking system.

**Agent procedure:**
1. Scan `03_TRANSCRIPTS/raw/` for all `.txt` files
2. Check each against `00_ADMIN/REVIEW_INDEX.md` to find unregistered files
3. For each new transcript:
   - Extract date from filename (preferred: `{CourseName}-transcript-MM-DD.txt`; also supports `YYYY-MM-DD_*.txt`, `MM-DD-YYYY_*.txt`, `YYYY-MM-DD_CourseName.txt`)
   - Match date to class in `00_ADMIN/MASTER_LOG.md`
   - If match found: add to REVIEW_INDEX "Pending Queue" with status `pending`
   - If no match: add to REVIEW_INDEX "Unmatched Transcripts" for manual resolution
4. Update REVIEW_INDEX Quick Stats
5. Report: "Found X new transcripts, Y matched, Z need manual matching"

**If REVIEW_INDEX.md doesn't exist:** Create from template `03_TEMPLATES/review_index_template.md`

---

### `review [COURSE]`

**Aliases:** `review for [COURSE]`, `process transcript [COURSE]`, `create review [COURSE]`

**What it means:** Process the next pending transcript (oldest first) and create a review document.

**Agent procedure:**
1. Check `00_ADMIN/REVIEW_INDEX.md` for pending transcripts
2. Select oldest pending transcript
3. Locate inputs:
   - **Transcript:** Check in order:
     - First: `03_TRANSCRIPTS/processed/YYYY-MM-DD_classNN_diarized.md` (if exists—especially valuable for CrimLaw/discussion classes)
     - Second: `03_TRANSCRIPTS/processed/YYYY-MM-DD_classNN_clean.md` (if exists)
     - Fallback: `03_TRANSCRIPTS/raw/{CourseName}-transcript-MM-DD.txt`
   - **Text prep:** `02_PREP/text/YYYY-MM-DD_classNN_text.md`
   - **Assignment:** `01_SOURCES/syllabus/assignments/YYYY-MM-DD_classNN.md`
   - **Class notes:** `07_NOTES/YYYY-MM-DD.md` or `07_NOTES/[date].md` (check for student's in-class notes with observations not in prep docs or transcripts)
   - **Past year outline:** Check `01_SOURCES/past_outlines/*.{md,txt}` for relevant topic coverage (DO NOT try to read PDFs/DOCX—those live in `01_SOURCES/original_sources/`)
4. Create review: `04_REVIEWS/YYYY-MM-DD_classNN_review.md`
   - Use template: `03_TEMPLATES/review_template.md`
   - **Section 1:** Prep vs. reality comparison
   - **Section 2:** Exam signals (tag with #EXAM_SIGNAL)
   - **Section 3:** Corrections to prep
   - **Section 4:** Doctrinal insights (professor's exact formulations)
   - **Section 5:** Policy arguments (what professor rewarded)
   - **Section 6:** Outline inserts (copy-paste ready)
   - **Section 7:** Source extraction (cases, statutes, readings)
   - **Section 8:** Prewrite opportunities identified
   - **Section 9:** Transcript QC flags (if any errors detected)
5. Score prediction accuracy (0/1/2) in frontmatter
6. QC against `03_TEMPLATES/qc_checklist_template.md`
7. Update REVIEW_INDEX: move to "Completed Reviews", status = `review_done`
8. Update MASTER_LOG:
   - Mark `Transcript?` as ✅
   - Mark `Review?` as ✅
   - Mark `Review_QC` as 1
   - Record signal count
   - Update `Next Action`

**If no pending transcripts:** Run `ingest transcripts [COURSE]` first, or report "No pending transcripts."

---

### `review [COURSE] class [NN]`

**Aliases:** `create review [COURSE] class NN`, `process transcript [COURSE] class NN`

**What it means:** Create review document for a specific class.

**Agent procedure:** Same as `review [COURSE]` but:
- Skip REVIEW_INDEX queue check
- Find transcript matching class NN by date from MASTER_LOG
- Process that specific transcript

---

### `review [COURSE] all`

**Aliases:** `batch review [COURSE]`, `process all transcripts [COURSE]`

**What it means:** Process ALL pending transcripts in order.

**Agent procedure:**
1. Run `ingest transcripts [COURSE]` to ensure all transcripts registered
2. Get Pending Queue from REVIEW_INDEX (sorted by date, oldest first)
3. For each pending transcript:
   - Execute `review [COURSE]` procedure
   - Execute `integrate review [COURSE] class [NN]` procedure
   - Update tracking before proceeding to next
4. Report summary: "Processed X reviews, added Y sources, created Z prewrite fragments"

---

### `integrate review [COURSE] class [NN]`

**Aliases:** `integrate [COURSE] class NN`, `push review [COURSE] class NN`

**What it means:** Push review extractions into SOURCES_TABLE, outline, and prewrite bank.

**Agent procedure:**
1. Open review document: `04_REVIEWS/YYYY-MM-DD_classNN_review.md`
2. **Update SOURCES_TABLE** (`05_OUTLINE/SOURCES_TABLE.md`):
   - For each case mentioned: add/update Cases section
   - For each statute: add/update Statutes section
   - For each reading: add/update Readings section
   - For each scholar: add/update Scholars section
   - Update "Classes Referenced" for existing sources
3. **Update Outline** (`05_OUTLINE/[relevant sections]`):
   - Paste outline inserts from review
   - Integrate professor's language
   - Add #EXAM_SIGNAL tags
4. **Create Prewrite Fragments** (if identified in review):
   - Doctrinal: `06_PREWRITES/DOCTRINAL/[topic]/[doctrine]_analysis.md`
   - Policy: `06_PREWRITES/POLICY/[topic].md`
   - Use templates, extract professor's formulations
5. Update REVIEW_INDEX: status = `integrated`
6. Update MASTER_LOG: Mark `Outline?` as ✅

**If SOURCES_TABLE.md doesn't exist:** Create from template `03_TEMPLATES/sources_table_template.md`

---

### `review status [COURSE]`

**Aliases:** `transcript status [COURSE]`, `review progress [COURSE]`

**What it means:** Show current review workflow status.

**Agent procedure:**
1. Open `00_ADMIN/REVIEW_INDEX.md`
2. Display:
   - Pending transcripts (count and list)
   - Completed reviews (count)
   - Reviews needing integration
   - Unmatched transcripts needing attention
3. Show recommendations for next action

---

### `update outline [COURSE] [section]`

**What it means:** Integrate review inserts into outline section.

**Agent procedure:**
1. Open review document for relevant class
2. Identify relevant outline section(s)
3. Paste outline inserts into `05_OUTLINE/[section]/`
   - Update existing sections or create new ones
   - Integrate professor's language
   - Add exam signal tags
4. Update MASTER_LOG:
   - Mark `Outline?` as ✅
   - Mark `Outline_QC` as 1
   - Update `Next Action`

---

### `prewrite [COURSE] [doctrine]`

**What it means:** Create doctrinal prewrite for specific doctrine.

**Agent procedure:**
1. Identify doctrine and relevant course
2. Determine which folder: `06_PREWRITES/DOCTRINAL/[topic_folder]/`
3. Create prewrite: `[doctrine]_analysis.md`
   - Use template: `03_TEMPLATES/prewrite_doctrinal_template.md`
   - PREWRITE section (copy-paste ready IRAC)
   - TRIGGERS (when to use)
   - FRAMEWORK (element-by-element breakdown)
   - EXAMPLE APPLICATIONS (2-3 worked examples)
4. QC against checklist
5. Update MASTER_LOG: Mark `Doctrinal?` as ✅

---

### `policy prewrite [COURSE] [topic]`

**What it means:** Create policy prewrite for specific topic.

**Agent procedure:**
1. Identify policy topic and relevant course
2. Create prewrite: `06_PREWRITES/POLICY/[topic].md`
   - Use template: `03_TEMPLATES/prewrite_policy_template.md`
   - OVERVIEW (one-paragraph description)
   - POSITIONS (2-3 positions with arguments)
   - EXAM-READY PARAGRAPHS for each position
   - COMPARATIVE ANALYSIS (table)
   - PROFESSOR'S ANGLE (what they reward)
3. QC against checklist
4. Update MASTER_LOG: Mark `Policy?` as ✅

---

### `status [COURSE]`

**What it means:** Show MASTER_LOG summary and current status.

**Agent procedure:**
1. Open `00_ADMIN/MASTER_LOG.md`
2. Display:
   - Classes with incomplete prep
   - Classes missing reviews
   - Classes with outstanding outline updates
   - Overall completion metrics
3. Highlight:
   - Urgent items (next class prep)
   - Backlog items
   - QC issues

---

### `qc [document path]`

**What it means:** Quality control check for specific document.

**Agent procedure:**
1. Open target document
2. Open relevant QC checklist from `03_TEMPLATES/qc_checklist_template.md`
3. Run through checklist:
   - Audio prep: Structure, formatting, content, length
   - Text prep: Structure, content, completeness
   - Review: Structure, content, exam signals
   - Outline: Structure, content, coherence
   - Prewrite: Structure, content, usability
4. Edit document in place to fix issues
5. Update frontmatter: Set `qc_iteration: [1|2|✓]`
6. Update MASTER_LOG if applicable

---

### `next prep [COURSE]`

**What it means:** Create prep for next upcoming class (earliest with Prep = "Not Started").

**Agent procedure:**
1. Open `00_ADMIN/MASTER_LOG.md`
2. Find first row where `Prep = "Not Started"`
3. Run `prep for [COURSE] class [NN]` for that class

---

### `exam spec [COURSE]`

**What it means:** Analyze past exams to create exam specification document.

**Agent procedure:**
1. Review `01_SOURCES/past_exams/`
2. Create `00_ADMIN/exam_spec.md`
   - Use template: `03_TEMPLATES/exam_spec_template.md`
   - Analyze: Format, question types, topic weighting, hypo patterns
   - Document: What's rewarded, what's tested, professor patterns
3. Update MASTER_LOG with exam analysis

---

### `init course [COURSE]`

**What it means:** Initialize folder structure for new course.

**Agent procedure:**
1. Create standard folder structure:
   - `00_ADMIN/` (with README, MASTER_LOG, course_style_guide)
   - `01_SOURCES/` (syllabus/, past_exams/, past_outlines/)
   - `02_PREP/` (audio/, text/)
   - `03_TRANSCRIPTS/` (raw/, processed/)
   - `04_REVIEWS/`
   - `05_OUTLINE/` (with INDEX.md)
   - `06_PREWRITES/` (DOCTRINAL/, POLICY/)
   - `99_EXAM_DAY/`
2. Create MASTER_LOG from template
3. Create course_style_guide from template
4. Copy exam_spec_template

---

## Naming Conventions

**Preps:**
- Audio: `YYYY-MM-DD_classNN_audio.md`
- Text: `YYYY-MM-DD_classNN_text.md`

**Transcripts:**
- Raw (downloaded; keep original filename): `{CourseName}-transcript-MM-DD.txt` (e.g., `Criminal Law-transcript-01-22.txt`)
- Processed: `YYYY-MM-DD_classNN_clean.md`

**Reviews:**
- `YYYY-MM-DD_classNN_review.md`

**Prewrites:**
- Doctrinal: `[doctrine]_analysis.md`
- Policy: `[topic].md`

---

## Course-Specific Modifications

Each course's `00_ADMIN/course_style_guide.md` includes:
- Course priorities (MPC focus, policy weight, case depth)
- Professor patterns (what they emphasize)
- Prep format preferences
- Exam answer style

**When generating course-specific content, reference these guides.**

---

## Error Handling

**If assignment file is missing:**
- Flag explicitly in document
- Use past outlines as priors
- Note: "Assignment file not found, using past outlines"

**If supplement is missing:**
- Flag explicitly: "Supplement X not available locally"
- Rely on past outlines and known themes
- Don't fake quotes or pretend to have source

**If MASTER_LOG doesn't exist:**
- Create from template: `03_TEMPLATES/master_log_template.md`
- Populate with course schedule if available

---

## Integration Points

**Workflows:**
- `01_WORKFLOWS/PRE_CLASS_WORKFLOW.md` - Full prep generation workflow
- `01_WORKFLOWS/POST_CLASS_WORKFLOW.md` - Full review workflow
- `01_WORKFLOWS/EXAM_PREP_WORKFLOW.md` - Prewrite building workflow
- `01_WORKFLOWS/QC_WORKFLOW.md` - Quality control workflow

**Templates:**
- All in `03_TEMPLATES/`

**Style guides:**
- `02_STYLE_GUIDES/WRITING_FOUNDATIONS.md` (universal)
- Course-specific guides (in each course's `00_ADMIN/`)

---

*Last Updated: 2026-01-19*
