# System Reorganization Tracker

**Date Started:** Jan 19, 2026  
**Target Completion:** Jan 24, 2026  
**Purpose:** Track comprehensive cleanup and standardization of all 5 courses

---

## ⚠️ CRITICAL GUARDRAILS - READ FIRST ⚠️

### DO NOT DELETE These Files (Move to ARCHIVE instead):
- ❌ `elements-of-style.md` - Move to `02_STYLE_GUIDES/REFERENCES/`, DO NOT delete
- ❌ `_PREP_FORMAT_EXAMPLE.md` - Contains user's refined case brief format, MUST preserve
- ❌ `MASTER_LOG.md` files in any course - Existing tracking data, migrate don't delete
- ❌ Any file in `ACTIVE/` courses with recent content (check file modified date)

### "Consolidate" Means:
✅ READ all source files thoroughly  
✅ MERGE content into new unified file  
✅ PRESERVE all unique information  
✅ MOVE originals to ARCHIVE/ after confirming new file is complete  
❌ NOT: Copy first file and ignore others  
❌ NOT: Delete sources before verifying new file works

### Before Moving/Deleting ANY File:
1. ✅ Check file size > 0 bytes
2. ✅ Open file and verify content exists
3. ✅ Check file modified date (if recent, extra caution)
4. ✅ Confirm destination exists OR create it first
5. ✅ After move, verify file exists in new location

### Validation Checkpoint After EACH Phase:
1. List files in destination folders - confirm expected files present
2. Check file sizes - no 0-byte files
3. Spot-check 2-3 files by opening them - content intact
4. Mark phase complete ONLY after validation passes

### If Something Goes Wrong:
- STOP immediately
- Document what happened
- Check if files can be recovered from Google Drive version history
- Ask user before proceeding

---

## Reorganization Goals

1. **Unified structure** - All courses use identical 00-06 folder system
2. **Consolidated resources** - Style guides, templates, workflows in law-school-common
3. **Clear tracking** - Every course has identical MASTER_LOG format
4. **Prewrites system** - Build exam answers throughout semester
5. **No clutter** - Archive old files, delete duplicates

---

## Phase 1: law-school-common/ Consolidation

### 1.1 Create New Structure ⬜
**Task:** Build new folder structure in law-school-common/

**Folders to create:**
- [ ] `00_SYSTEM/` - AI rules, command interface, folder structure spec
- [ ] `01_WORKFLOWS/` - Pre-class, post-class, exam prep workflows
- [ ] `02_STYLE_GUIDES/` - Unified writing style guide
- [ ] `03_TEMPLATES/` - All templates (prep, review, master log, etc.)
- [ ] `04_SCRIPTS/` - Automation scripts (when built)
- [ ] `05_ARCHIVE/` - Old/obsolete files

**Status:** Not started  
**Blocking:** Nothing  
**Next:** Create folders, move existing good files

**Validation After Completion:**
- [ ] All 6 folders exist (00_SYSTEM through 05_ARCHIVE)
- [ ] Each folder has a README.md explaining its purpose
- [ ] No typos in folder names (check spelling carefully)

---

### 1.2 Consolidate Style Guides ⬜
**Task:** Create two-layer style guide system (universal + course-specific)

**Layer 1: Universal Writing Guide**
**Sources:**
- [ ] `law-school-common/elements-of-style.md` (Strunk's writing principles)
- [ ] `law-school-common/SKILL.md` (AI guardrails for applying rules)

**Output:** `law-school-common/02_STYLE_GUIDES/WRITING_FOUNDATIONS.md`

**Sections:**
- Elements of Style principles (active voice, concrete language, omit needless words)
- SKILL.md AI guardrails
- Legal writing conventions (IRAC, paragraph structure)
- Formatting standards (headings, lists, emphasis)

**Layer 2: Course-Specific Style Guides**
**Sources:**
- [ ] `CrimLaw/Lectures/Prep/Style_Guides/AUDIO_PREP_STYLE_GUIDE.md`
- [ ] `CrimLaw/Lectures/Prep/Style_Guides/CLASS_REFERENCE_STYLE_GUIDE.md`
- [ ] `Deals/Assignments/PREP-SHEET-STYLE-GUIDE.md`
- [ ] `law-school-common/_PREP_FORMAT_EXAMPLE.md` (CASE BRIEF FORMAT - user's refined structure)

**Outputs (one per course):**
- `CrimLaw/00_ADMIN/course_style_guide.md`
- `Deals/00_ADMIN/course_style_guide.md`
- `Property/00_ADMIN/course_style_guide.md`
- `Torts/00_ADMIN/course_style_guide.md`

**Content per course guide:**
- Course priorities (MPC focus, policy weight, case depth)
- Professor emphasis patterns
- Prep doc format preferences
- Exam answer style
- **CASE BRIEF FORMAT** (from _PREP_FORMAT_EXAMPLE.md - standardized structure user developed last semester)

**Also:**
- [ ] Move `elements-of-style.md` → `02_STYLE_GUIDES/REFERENCES/` (keep as reference)
- [ ] Delete `SKILL.md` standalone (integrated into WRITING_FOUNDATIONS.md)

**Status:** Not started  
**Blocking:** Folder 02_STYLE_GUIDES/ must exist  
**Estimated time:** 90 min (45 min universal + 45 min course-specific templates)

**⚠️ CRITICAL STEPS (Do in this exact order):**
1. Read ENTIRE _PREP_FORMAT_EXAMPLE.md - note case brief structure (Rule of Law → Facts + Procedural Posture → Issue → Holding & Reasoning → Dissent)
2. Read ALL source style guides completely before starting to write
3. Create WRITING_FOUNDATIONS.md by MERGING elements-of-style.md + SKILL.md (not just copying one)
4. Add case brief format section to WRITING_FOUNDATIONS.md
5. Create 4 course_style_guide.md files (one per course) - include case brief format in each
6. VERIFY all 5 new files exist and have content > 1000 characters
7. ONLY THEN move elements-of-style.md to REFERENCES/ (verify it arrived there)
8. ONLY THEN delete SKILL.md (after confirming content is in WRITING_FOUNDATIONS.md)

**Validation After Completion:**
- [ ] WRITING_FOUNDATIONS.md exists and contains content from BOTH sources
- [ ] Case brief format from _PREP_FORMAT_EXAMPLE.md is documented in WRITING_FOUNDATIONS.md
- [ ] All 4 course_style_guide.md files exist
- [ ] Each course guide includes the case brief format section
- [ ] elements-of-style.md exists in REFERENCES/ folder
- [ ] SKILL.md is deleted (content merged into WRITING_FOUNDATIONS.md)
- [ ] Open 2-3 files randomly and verify content looks correct

---

### 1.3 Consolidate Templates ⬜
**Task:** Merge templates from CrimLaw and Property into standard set

**Sources:**
- CrimLaw/Admin/Templates/ (5 files)
- Property/TEMPLATES/ (7 files)

**Output templates:**
- [ ] `audio_prep_template.md`
- [ ] `text_prep_template.md`
- [ ] `review_template.md`
- [ ] `master_log_template.md`
- [ ] `exam_spec_template.md`
- [ ] `prewrite_doctrinal_template.md` (NEW - IRAC structure)
- [ ] `prewrite_policy_template.md` (NEW - policy argument structure)
- [ ] `course_style_guide_template.md` (NEW - for Layer 2 style guides)
- [ ] `qc_checklist_template.md` (Quality control standards - from CrimLaw QC_Checklists.md)

**Status:** Not started  
**Blocking:** Folder 03_TEMPLATES/ must exist  
**Estimated time:** 30 min

**⚠️ CRITICAL STEPS:**
1. List all files in CrimLaw/Admin/Templates/ - note which ones exist
2. List all files in Property/TEMPLATES/ - note which ones exist
3. For each output template: Check if it exists in BOTH sources, ONE source, or NEITHER
4. If exists in both: MERGE unique content from both, don't just copy one
5. If exists in one: Use that version
6. If NEW template (prewrite_doctrinal, prewrite_policy, course_style_guide): CREATE from scratch using examples
7. VERIFY all 8 templates exist before marking complete

**Validation After Completion:**
- [ ] All 8 template files exist in 03_TEMPLATES/
- [ ] Each template file has content (not empty)
- [ ] prewrite_doctrinal_template.md shows case brief format from _PREP_FORMAT_EXAMPLE.md
- [ ] Spot-check 2 templates by opening them - look reasonable

---

### 1.4 Create Unified Workflows ⬜
**Task:** Document three core workflows

**Sources:**
- CrimLaw/Admin/Two_Doc_Prep_System.md
- CrimLaw/Admin/Per_Class_Prep_Blueprint.md
- law-school-common/POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md

**Output workflows:**
- [ ] `PRE_CLASS_WORKFLOW.md` - Generate preps (audio + text)
- [ ] `POST_CLASS_WORKFLOW.md` - Process transcripts, extract signals, update outline  
- [ ] `EXAM_PREP_WORKFLOW.md` - Build prewrites, daily drills, practice exams
- [ ] `QC_WORKFLOW.md` - Iterative quality control (check against standards, edit in place, track iterations)

**QC Design Principles (minimize extra docs):**
- **No separate QC documents** - QC edits the original doc directly
- **Tracking in MASTER_LOG** - Add QC columns: `Prep_QC`, `Review_QC`, `Outline_QC` (iteration count)
- **QC findings** - Brief notes in MASTER_LOG Notes column OR in doc frontmatter (no standalone files)
- **Iterative counter** - `0` (unchecked) → `1` (first pass) → `2+` (additional passes) → `✓` (final/passed)
- **Process location** - QC happens wherever the doc lives (02_PREP/, 04_REVIEWS/, 05_OUTLINE/)
- **Monitoring** - MASTER_LOG shows QC status at-a-glance for all deliverables

**QC Design Principles:**
- **No separate QC docs** - QC edits the original document in place
- **Tracking in MASTER_LOG** - Add QC columns (Prep_QC?, Review_QC?, Outline_QC?) showing iteration count
- **QC findings** - Go in MASTER_LOG Notes column or in doc frontmatter (not separate files)
- **Iterative** - QC can run multiple times: `0` (unchecked) → `1` (1st pass) → `2+` (more passes) → `✓` (final/passed)

**Status:** Not started  
**Blocking:** Folder 01_WORKFLOWS/ must exist  
**Estimated time:** 45 min

**Validation After Completion:**
- [ ] All 4 workflow files exist (PRE_CLASS, POST_CLASS, EXAM_PREP, QC)
- [ ] Each workflow has step-by-step instructions (numbered list)
- [ ] Each workflow references relevant templates from 03_TEMPLATES/
- [ ] QC_WORKFLOW.md references qc_checklist_template.md and defines iterative review process

**Status:** Not started  
**Blocking:** Folder 01_WORKFLOWS/ must exist  
**Estimated time:** 60 min

---

### 1.5 Create Command Interface ⬜
**Task:** Course-agnostic command interface for standard prompts

**Source:** CrimLaw/Admin/Command_Interface.md (adapt)

**Output:** `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md`

**Commands:**
- `prep [course] [class_num]` - Generate audio + text prep
- `review [course] [class_num]` - Process transcript, generate review
- `prewrite [course] [topic]` - Generate exam answer for topic
- `status [course]` - Show MASTER_LOG summary
- `outline [course] [section]` - Update outline section

**Status:** Not started  
**Blocking:** Folder 00_SYSTEM/ must exist  
**Estimated time:** 45 min

---

### 1.6 Archive Old Files ⬜
**Task:** Move obsolete files to law-school-common/05_ARCHIVE/

**⚠️ IMPORTANT: Do NOT delete _PREP_FORMAT_EXAMPLE.md - it contains user's refined case brief format!**

**Files to archive:**
- [ ] `_HOUSEKEEPING_REPORT_2025-10-24.md`
- [ ] `_MASTER_STRUCTURE.md` (replaced by FOLDER_STRUCTURE_SPEC.md)
- [ ] `POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md` (merged into workflows)

**Files to keep (moved to REFERENCES):**
- [ ] `elements-of-style.md` → `02_STYLE_GUIDES/REFERENCES/` (keep as reference)
- [ ] `echo360_transcript_guide.md` → `01_WORKFLOWS/REFERENCES/` (useful how-to)
- [ ] `_PREP_FORMAT_EXAMPLE.md` → `02_STYLE_GUIDES/REFERENCES/` (user's case brief format - DO NOT DELETE)

**Files to delete (integrated elsewhere):**
- [ ] `SKILL.md` (integrated into WRITING_FOUNDATIONS.md)

**Status:** Not started  
**Blocking:** Phase 1.2-1.4 complete (so files are replaced first)  
**Estimated time:** 10 min

**Validation After Completion:**
- [ ] _PREP_FORMAT_EXAMPLE.md EXISTS in 02_STYLE_GUIDES/REFERENCES/ (verify this first!)
- [ ] elements-of-style.md EXISTS in 02_STYLE_GUIDES/REFERENCES/
- [ ] 3 files moved to 05_ARCHIVE/ as expected
- [ ] SKILL.md deleted (only after verifying WRITING_FOUNDATIONS.md contains its content)

---

## Phase 2: CrimLaw Restructuring

### 2.1 Create New Folder Structure ⬜
**Task:** Create Option B (Hybrid) folder structure for CrimLaw

**New structure:**
```
CrimLaw/
├── 00_ADMIN/
│   ├── README.md                    # What's in each folder, when to use
│   ├── MASTER_LOG.md
│   ├── exam_spec.md
│   └── course_style_guide.md        # NEW: CrimLaw-specific style guide
├── 01_SOURCES/                       # [Reference throughout semester]
│   ├── syllabus/
│   ├── past_exams/
│   └── past_outlines/
├── 02_PREP/                          # [USE BEFORE CLASS]
│   ├── audio/
│   └── text/
├── 03_TRANSCRIPTS/                   # [USE AFTER CLASS]
│   ├── raw/
│   └── processed/
├── 04_REVIEWS/                       # [USE AFTER CLASS]
├── 05_OUTLINE/                       # [Build throughout semester, use on exam]
│   ├── INDEX.md
│   ├── 01_elements/
│   ├── 02_homicide/
│   ├── 03_defenses/
│   ├── 04_inchoate/
│   └── 05_theory/
├── 06_PREWRITES/                     # [Build throughout semester, use on exam]
│   ├── INDEX.md
│   ├── DOCTRINAL/                    # Black letter law IRAC analyses
│   │   ├── INDEX.md
│   │   ├── 01_elements/
│   │   ├── 02_homicide/
│   │   ├── 03_defenses/
│   │   └── 04_inchoate/
│   └── POLICY/                       # Policy arguments
│       ├── INDEX.md
│       ├── punishment_theory.md
│       ├── racial_justice.md
│       └── critical_theory.md
└── 99_EXAM_DAY/                      # [USE ONLY ON EXAM]
    ├── README.md
    ├── attack_outline.md
    ├── prewrites_index.md
    ├── checklist.md
    └── quick_reference/
```

**Status:** Not started  
**Blocking:** Nothing  
**Next:** Create folders

---

### 2.2 Migrate Admin Files ⬜
**Task:** Move/reorganize CrimLaw/Admin/ content

**Actions:**
- [ ] Keep `Master_Log.md` → move to `00_ADMIN/MASTER_LOG.md`
- [ ] Keep `Exam_Spec.md` → move to `00_ADMIN/exam_spec.md`
- [ ] Create `00_ADMIN/course_style_guide.md` (from consolidated style guides)
- [ ] Create `00_ADMIN/README.md` (explain folder structure + activity markers)
- [ ] Move `Syllabus/` → `01_SOURCES/syllabus/`
- [ ] Move `Sources/Past_Outlines/` → `01_SOURCES/past_outlines/`
- [ ] Move past exams → `01_SOURCES/past_exams/` (if they exist)
- [ ] Archive `Admin/ARCHIVE/` → delete (already archived)
- [ ] Archive `Admin/Templates/` → delete (moved to law-school-common)
- [ ] Archive `Admin/Scripts/` → review first, may keep useful scripts
- [ ] Archive `Command_Interface.md`, `Two_Doc_Prep_System.md`, `Per_Class_Prep_Blueprint.md` → delete (merged into law-school-common workflows)
- [ ] Archive `Mapping/` → review content, may integrate into exam_spec.md

**Status:** Not started  
**Blocking:** Phase 1 complete (so law-school-common has consolidated files)  
**Estimated time:** 30 min

**⚠️ CRITICAL STEPS:**
1. Before deleting ANY Admin subfolder: List its contents, verify files are moved/archived
2. Master_Log.md contains student's class tracking - DO NOT lose this data
3. course_style_guide.md must be copied from law-school-common (not created from scratch)
4. When "archiving" something: Move to CrimLaw/00_ADMIN/ARCHIVE_OLD_SYSTEM/ first, don't delete

**Validation After Completion:**
- [ ] MASTER_LOG.md exists in 00_ADMIN/ with all existing tracking data intact
- [ ] course_style_guide.md exists (copied from law-school-common templates)
- [ ] Old Admin/ folder is empty or deleted
**Validation After Completion:**
- [ ] MASTER_LOG.md exists in 00_ADMIN/ with all existing tracking data intact
- [ ] course_style_guide.md exists (copied from law-school-common templates)
- [ ] Old Admin/ folder is empty or deleted
- [ ] No files lost (check: did any files have unique content that's now gone?)

---

### 2.3 Migrate Lecture Files ⬜
**Task:** MOVE existing CrimLaw prep/transcript files into new structure

**⚠️ IMPORTANT:** CrimLaw already has ~20+ prep documents and transcripts - we are MOVING existing files, NOT generating new content.

**Actions:**
- [ ] `Lectures/Prep/Audio/` → `02_PREP/audio/` (MOVE existing audio preps)
- [ ] `Lectures/Prep/Reference/` → `02_PREP/text/` (rename from "Reference", MOVE existing text preps)
- [ ] `Lectures/Prep/Packets/` → Archive (scaffolding, not final deliverable)
- [ ] `Lectures/Prep/Style_Guides/` → Delete (moved to law-school-common)
- [ ] `Lectures/Transcripts/` → `03_TRANSCRIPTS/` (MOVE existing transcripts)

**Status:** Not started  
**Blocking:** Phase 2.2 complete  
**Estimated time:** 20 min

**⚠️ CRITICAL:** These are student's actual prep docs - DO NOT delete without confirming moved successfully

**Validation After Completion:**
- [ ] Count files in old Lectures/Prep/Audio/ vs new 02_PREP/audio/ - numbers match
- [ ] Count files in old Lectures/Prep/Reference/ vs new 02_PREP/text/ - numbers match
- [ ] Open 1-2 random files in new locations - content intact
- [ ] Old Lectures/ folder structure can be deleted (after confirming above)

---
- [ ] Count files in old Lectures/Prep/Audio/ vs new 02_PREP/audio/ - numbers match
- [ ] Count files in old Lectures/Prep/Reference/ vs new 02_PREP/text/ - numbers match
- [ ] Open 1-2 random files in new locations - content intact
- [ ] Old Lectures/ folder structure can be deleted (after confirming above)
- [ ] `Lectures/Reviews/` → `04_REVIEWS/`

**Status:** Not started  
**Blocking:** 2.1 complete  
**Estimated time:** 20 min

---

### 2.4 Restructure Outline ⬜
**Task:** Break CrimLaw outline into modular sections

**Current:** `Exams/Outline/Cumulative_Outline.md` (skeletal)

**New structure:**
```
05_OUTLINE/
├── INDEX.md
├── 01_elements/
│   ├── actus_reus.md
│   ├── mens_rea.md
│   └── causation.md
├── 02_homicide/
│   ├── murder.md
│   ├── heat_of_passion.md
│   ├── felony_murder.md
│   └── unintended_killings.md
├── 03_defenses/
│   ├── self_defense.md
│   ├── necessity.md
│   └── duress.md
├── 04_inchoate/
│   ├── attempt.md
│   ├── complicity.md
│   └── conspiracy.md
└── 05_theory/
    └── policy_arguments.md
```

**Status:** Not started  
**Blocking:** Syllabus must be available to determine logical sections  
**Estimated time:** 45 min (structure only, content comes from reviews)

---

### 2.5 Create Prewrites Structure ⬜
**Task:** Set up prewrite system for CrimLaw (Option B: DOCTRINAL + POLICY split)

**Structure:**
```
06_PREWRITES/
├── INDEX.md                          # Master list of all prewrites
│
├── DOCTRINAL/                        # Black letter law IRAC analyses
│   ├── INDEX.md
│   ├── 01_elements/
│   │   ├── actus_reus_analysis.md
│   │   ├── mens_rea_analysis.md
│   │   └── causation_analysis.md
│   ├── 02_homicide/
│   │   ├── murder_analysis.md
│   │   ├── heat_of_passion_analysis.md
│   │   └── felony_murder_analysis.md
│   ├── 03_defenses/
│   │   ├── self_defense_analysis.md
│   │   ├── necessity_analysis.md
│   │   └── duress_analysis.md
│   └── 04_inchoate/
│       ├── attempt_analysis.md
│       ├── complicity_analysis.md
│       └── conspiracy_analysis.md
│
└── POLICY/                           # Policy arguments (essay-ready paragraphs)
    ├── INDEX.md
    ├── punishment_theory.md          # Retribution vs. deterrence vs. rehab
    ├── racial_justice_criminal_law.md
    ├── death_penalty_justifications.md
    ├── legality_and_vagueness.md
    ├── foucault_discipline_critique.md
    └── critical_theory_applications.md
```

**Also create:**
```
99_EXAM_DAY/
├── README.md                         # "Open this folder on exam day"
├── attack_outline.md                 # Condensed rules (3-5 pages)
├── prewrites_index.md                # Quick index to all prewrites
├── checklist.md                      # Issue-spotting checklist
├── mpc_quick_reference.md            # All MPC sections
└── case_quick_reference.md           # Major cases (2-3 lines each)
```

**Each DOCTRINAL prewrite contains:**
- Issue statement (copy-paste ready)
- Rule statement (black letter law)
- Application framework (fill-in-the-blank)
- Conclusion template
- Triggers (when to use)
- Examples

**Each POLICY prewrite contains:**
- Overview of policy issue
- Competing arguments (Position A, B, C)
- Exam-ready paragraphs for each position
- Professor's angle (from class signals)
- Past exam appearances

**Status:** Not started  
**Blocking:** Syllabus available, outline structure determined  
**Estimated time:** 30 min (structure only, prewrites built throughout semester)

---

### 2.6 Update MASTER_LOG ⬜
**Task:** Standardize CrimLaw MASTER_LOG format

**Add columns:**
- [ ] `Doctrinal Prewrite?` - ✅ if IRAC analysis exists for this topic
- [ ] `Policy Prewrite?` - ✅ if policy argument exists for this topic

**Format:**
```markdown
| Class# | Date | Topic | Prep | Audio? | Class? | Review? | Outline? | Doctrinal? | Policy? | Signals | Next |
```

**Status:** Not started  
**Blocking:** 2.2 complete  
**Estimated time:** 15 min

---

## Phase 3: Property Restructuring

### 3.1 Apply Standard Structure ⬜
**Task:** Property already has numbered structure, apply Option B format

**Actions:**
- [ ] Rename/restructure to match Option B:
  - `00_ADMIN/` - Keep, add course_style_guide.md + README.md
  - `01_SYLLABUS/` → `01_SOURCES/syllabus/`
  - `02_SOURCES/` → merge into `01_SOURCES/` (past_exams, past_outlines)
  - `03_MAPPING/` → integrate into `00_ADMIN/exam_spec.md`
  - `04_PREP/` → split into `02_PREP/audio/` and `02_PREP/text/`
  - `05_CLASS_NOTES/` → `03_TRANSCRIPTS/` (rename for consistency)
  - `06_REVIEW/` → `04_REVIEWS/`
  - `07_OUTLINE/` → `05_OUTLINE/` (restructure into topic sections)
  - `08_METRICS/` → DELETE (tracking in MASTER_LOG instead)
  - Create `06_PREWRITES/` with DOCTRINAL/ and POLICY/ subfolders
  - Create `99_EXAM_DAY/`
- [ ] Delete `TEMPLATES/` folder (templates now in law-school-common)
- [ ] Create `00_ADMIN/course_style_guide.md`
- [ ] Create `00_ADMIN/README.md` with folder usage guide

**Status:** Not started  
**Blocking:** Phase 1 complete  
**Estimated time:** 30 min

---

### 3.2 Populate from Syllabus ⬜
**Task:** Once syllabus arrives, parse and populate

**Actions:**
- [ ] Parse syllabus into assignment files
- [ ] Populate MASTER_LOG with class schedule
- [ ] Determine outline topic structure
- [ ] Create outline section folders

**Status:** Blocked (waiting for syllabus)  
**Blocking:** Need syllabus  
**Estimated time:** 45 min

---

## Phase 4: Torts Restructuring

### 4.1 Apply Standard Structure ⬜
**Task:** Torts has numbered structure but needs Option B format

**Actions:**
- [ ] Apply Option B structure (00-06 + 99_EXAM_DAY)
- [ ] Populate `00_ADMIN/`:
  - Create MASTER_LOG.md
  - Create exam_spec.md (based on past outlines)
  - Create course_style_guide.md
  - Create README.md
- [ ] Split prep folders into audio/text
- [ ] Create transcript folders (raw/processed)
- [ ] Restructure outline with topic sections
- [ ] Create prewrites structure (DOCTRINAL + POLICY)
- [ ] Create 99_EXAM_DAY/ folder

**Status:** Not started  
**Blocking:** Phase 1 complete  
**Estimated time:** 30 min

---

### 4.2 Index Past Outlines ⬜
**Task:** Torts has 5 past outlines - extract useful content

**Actions:**
- [ ] Review past outlines for professor patterns
- [ ] Create exam_spec.md based on past outline topics
- [ ] Note what topics get heavy coverage

**Status:** Not started  
**Blocking:** 4.1 complete  
**Estimated time:** 45 min

---

### 4.3 Populate from Syllabus ⬜
**Task:** Once syllabus arrives, populate

**Status:** Blocked (waiting for syllabus)  
**Estimated time:** 45 min

---

## Phase 5: Deals Restructuring

### 5.1 Convert to Standard Structure ⬜
**Task:** Deals uses custom structure - complete overhaul to Option B

**Current:**
```
Deals/
├── Assignments/
├── Sources/
├── Outlines/
└── Exams (past years)/
```

**Convert to Option B:**
```
Deals/
├── 00_ADMIN/
│   ├── README.md
│   ├── MASTER_LOG.md
│   ├── exam_spec.md
│   └── course_style_guide.md
├── 01_SOURCES/
│   ├── syllabus/
│   ├── past_exams/
│   └── past_outlines/
├── 02_PREP/
│   ├── audio/
│   └── text/
├── 03_TRANSCRIPTS/
├── 04_REVIEWS/
├── 05_OUTLINE/
├── 06_PREWRITES/
│   ├── DOCTRINAL/
│   └── POLICY/
└── 99_EXAM_DAY/
```

**Actions:**
- [ ] Create new structure
- [ ] Move `Assignments/` → review for useful content, integrate into prep docs or delete
- [ ] Move `Sources/` → `01_SOURCES/`
- [ ] Move `Exams (past years)/` → `01_SOURCES/past_exams/`
- [ ] Move `Outlines/` → `01_SOURCES/past_outlines/`
- [ ] Archive/delete `PREP-SHEET-STYLE-GUIDE.md` (migrated to course_style_guide.md)
- [ ] Archive/delete `PREP-SHEETS-QUALITY-CONTROL.md` (integrated into templates)

**Status:** Not started  
**Blocking:** Phase 1 complete  
**Estimated time:** 45 min

---

### 5.2 Populate from Syllabus ⬜
**Task:** Once syllabus arrives, populate

**Status:** Blocked (waiting for syllabus)  
**Estimated time:** 45 min

---

## Phase 6: LPW-II Setup

### 6.1 Create Structure from Scratch ⬜
**Task:** LPW-II folder is empty - build Option B structure

**Actions:**
- [ ] Create full Option B structure:
  - 00_ADMIN/ (with README, MASTER_LOG, course_style_guide)
  - 01_SOURCES/
  - 02_PREP/ (audio + text)
  - 03_TRANSCRIPTS/ (raw + processed)
  - 04_REVIEWS/
  - 05_OUTLINE/
  - 06_PREWRITES/ (DOCTRINAL + POLICY)
  - 99_EXAM_DAY/
- [ ] Wait for syllabus to populate

**Status:** Not started  
**Blocking:** Phase 1 complete  
**Estimated time:** 20 min

---

## Phase 7: Testing & Validation

### 7.1 Test Workflows ⬜
**Task:** Test prep generation workflow end-to-end

**Actions:**
- [ ] Generate prep for CrimLaw Class 1 using new system
- [ ] Process transcript using new workflow
- [ ] Generate review and outline insert
- [ ] Build first prewrite

**Status:** Not started  
**Blocking:** All phases 1-6 complete  
**Estimated time:** 2 hours

---

### 7.2 Documentation Review ⬜
**Task:** Ensure all documentation is clear

**Files to review:**
- [ ] law-school-common/README.md (update with new structure)
- [ ] FOLDER_STRUCTURE_SPEC.md (ensure accurate)
- [ ] Command interface (test all commands)

**Status:** Not started  
**Blocking:** 7.1 complete  
**Estimated time:** 30 min

---

## Progress Summary

**Total Tasks:** 39  
**Completed:** 0  
**In Progress:** 0  
**Blocked:** 4 (waiting for syllabi)  
**Not Started:** 35

**Estimated Total Time:** ~15 hours  
**Target:** 3 hours/day over 5 days

---

## Notes & Issues

### Decisions Made
- [x] **Structure: Option B (Hybrid)** - Numbered folders + 99_EXAM_DAY/ + activity markers in README
- [x] **Style guides: Two layers** - Universal (WRITING_FOUNDATIONS.md) + Course-specific (course_style_guide.md)
- [x] **Prewrites: DOCTRINAL + POLICY split** - Different structures for different purposes
- [x] **Keep elements-of-style.md and SKILL.md** - Integrate into WRITING_FOUNDATIONS.md, keep originals as reference
- [ ] Confirmed: No METRICS folder (tracking in MASTER_LOG instead)
- [ ] Confirmed: Modular outline (10-20 page sections, not 150-page file)

### Risks
- **Context window limits** - May need to pause and resume
- **Syllabus delays** - Can't fully populate courses until syllabi arrive
- **Breaking existing workflows** - CrimLaw has working system, must preserve what works

### Recovery Plan
- This tracker doc serves as checkpoint
- Can resume at any phase
- Each phase is independent (can do out of order if needed)

---

## Daily Schedule

**Day 1 (Jan 19 - Today):**
- [x] Audit complete
- [x] Create specifications
- [x] Create this tracker
- [ ] Phase 1.1-1.3 (consolidate style guides + templates)

**Day 2 (Jan 20):**
- [ ] Phase 1.4-1.6 (workflows + command interface + archive)
- [ ] Phase 2.1-2.3 (CrimLaw basic restructure)

**Day 3 (Jan 21):**
- [ ] Phase 2.4-2.6 (CrimLaw outline + prewrites)
- [ ] Phase 3.1 (Property restructure)

**Day 4 (Jan 22):**
- [ ] Phase 4.1-4.2 (Torts restructure)
- [ ] Phase 5.1 (Deals restructure)

**Day 5 (Jan 23):**
- [ ] Phase 6.1 (LPW-II setup)
- [ ] Phase 7.1-7.2 (Testing + validation)

**Day 6 (Jan 24):**
- [ ] Buffer for syllabus-dependent work
- [ ] Final cleanup
