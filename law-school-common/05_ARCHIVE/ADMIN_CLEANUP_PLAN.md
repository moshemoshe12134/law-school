# Admin Cleanup Audit - Jan 19, 2026

## Current State (Per Course)

### CrimLaw/Admin/
**Tracking:**
- `Master_Log.md` - ✅ Comprehensive class pipeline table
- `Metrics/` - folder exists

**Instructions:**
- `Command_Interface.md` - ✅ Standard prompts for common tasks
- `Two_Doc_Prep_System.md` - ✅ Workflow documentation
- `Per_Class_Prep_Blueprint.md` - ✅ What to cover per class
- `README.md` - general info

**Templates:**
- `Templates/Audio_Prep_TEMPLATE.md`
- `Templates/Class_Reference_TEMPLATE.md`
- `Templates/Prep_Packet_TEMPLATE.md`
- `Templates/Review_Doc_TEMPLATE.md`
- `Templates/QC_Checklists.md`

**Style Guides:**
- `Lectures/Prep/Style_Guides/AUDIO_PREP_STYLE_GUIDE.md`
- `Lectures/Prep/Style_Guides/CLASS_REFERENCE_STYLE_GUIDE.md`

**Sources:**
- `Sources/` - past outlines, exam materials
- `Syllabus/` - parsed syllabus with assignments
- `Mapping/` - past outlines index

**Clutter:**
- `ARCHIVE/` - old system files
- `Archive.md` - what was archived
- `Scripts/` - may have useful automation

---

### Property/00_ADMIN/
**Tracking:**
- `../MASTER_LOG.md` - ⚠️ Template only, not populated

**Instructions:**
- `SYSTEM_OVERVIEW.md` - ⚠️ Generic system overview (211 lines)
- `AGENT_HANDOFF_PROMPT.md` - ⚠️ Prompt for handing work to AI
- `README.md` - quick start

**Templates:**
- `../TEMPLATES/` folder with 7 templates

**Clutter:**
- `conversion_recommendations.md` - ⚠️ AI format guide (delete?)

---

### Torts/00_ADMIN/
**Everything:** Empty folder

---

### Deals/
**Style Guides:**
- `Assignments/PREP-SHEET-STYLE-GUIDE.md` - ✅ Detailed writing style guide (393 lines)
- `Assignments/PREP-SHEETS-QUALITY-CONTROL.md` - QC checklist

**Structure:** Custom folders (Assignments/Sources/Outlines/Exams)

---

### law-school-common/
**Global:**
- `AI_SYSTEM_RULES.md` - ✅ Rules for AI file management
- `README.md` - workspace overview
- `SYSTEM_DIAGNOSIS_2026-01-19.md` - current diagnosis
- `OPTIMIZATION_QUEUE.md` - task queue

**Workflows:**
- `POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md` - transcript processing workflow
- `echo360_transcript_guide.md` - how to download transcripts

**Style:**
- `elements-of-style.md` - general writing style
- `SKILL.md` - unclear purpose

**Templates:**
- `_PREP_FORMAT_EXAMPLE.md` - example prep doc
- `_MASTER_STRUCTURE.md` - outdated structure doc

**Clutter:**
- `_HOUSEKEEPING_REPORT_2025-10-24.md` - old report (delete)
- `setup_all_course_systems.py` - hardcoded for Contracts (needs refactor)
- `ocr_scripts/` - PDF OCR tools
- `misc/` - unknown contents

---

## Problems Identified

### 1. Scattered Style Guides (3 locations)
- CrimLaw: Audio prep + Class reference style guides
- Deals: Prep sheet style guide
- law-school-common: elements-of-style.md
**Problem:** No single source of truth for writing quality

### 2. Scattered Templates (3 locations)
- CrimLaw: 5 templates
- Property: 7 templates
- No shared template library
**Problem:** Duplication, inconsistent formats

### 3. Scattered Instructions (2+ locations)
- CrimLaw: Command_Interface + Two_Doc_Prep_System + Per_Class_Prep_Blueprint
- Property: SYSTEM_OVERVIEW + AGENT_HANDOFF_PROMPT
- law-school-common: POST_CLASS_TRANSCRIPT_WORKFLOW
**Problem:** Can't find the canonical workflow

### 4. Inconsistent Tracking
- CrimLaw: Detailed Master_Log with class pipeline
- Property: Empty MASTER_LOG template
- Others: Nothing
**Problem:** No visibility into what's done/pending

### 5. No Central Command Interface
- CrimLaw has Command_Interface.md but it's course-specific
- Other courses: no standard commands
**Problem:** Every task requires manual prompting

### 6. Unclear What's Obsolete
- ARCHIVE folders
- Old reports
- Outdated structure docs
- conversion_recommendations.md
**Problem:** Clutter makes it hard to find current docs

---

## Recommended Structure

### law-school-common/ (Global)
```
law-school-common/
├── 00_SYSTEM/
│   ├── AI_RULES.md                      # AI file management rules
│   ├── COMMAND_INTERFACE.md              # Standard prompts (course-agnostic)
│   └── FOLDER_STRUCTURE.md               # Canonical folder structure
│
├── 01_WORKFLOWS/
│   ├── PRE_CLASS_WORKFLOW.md             # Generate preps
│   ├── POST_CLASS_WORKFLOW.md            # Process transcripts
│   └── EXAM_PREP_WORKFLOW.md             # Daily drills + outline building
│
├── 02_STYLE_GUIDES/
│   ├── WRITING_STYLE.md                  # Consolidated writing standards
│   └── FORMATTING_STANDARDS.md           # Markdown conventions
│
├── 03_TEMPLATES/
│   ├── audio_prep_template.md
│   ├── text_prep_template.md
│   ├── review_template.md
│   ├── master_log_template.md
│   └── exam_spec_template.md
│
├── 04_SCRIPTS/
│   ├── generate_prep.sh                  # Automated prep generation
│   ├── process_transcript.sh             # Automated transcript processing
│   ├── extract_signals.sh                # Exam signal extraction
│   └── daily_drill.sh                    # Daily practice
│
├── 05_ARCHIVE/
│   └── [old files moved here]
│
└── README.md                             # System overview + quick start
```

### Per-Course Structure (All Courses)
```
CourseNameHere/
├── 00_ADMIN/
│   ├── MASTER_LOG.md                     # Status tracking (standard format)
│   └── exam_spec.md                      # Past exam analysis
│
├── 01_SOURCES/
│   ├── syllabus/                         # Syllabus + parsed assignments
│   ├── past_exams/
│   └── past_outlines/
│
├── 02_PREP/
│   ├── audio/                            # Audio preps (TTS-ready)
│   └── text/                             # Text preps (cold-call reference)
│
├── 03_TRANSCRIPTS/
│   ├── raw/                              # Echo360 downloads
│   └── processed/                        # Cleaned transcripts
│
├── 04_REVIEWS/                           # Post-class review docs
│
├── 05_OUTLINE/                           # Cumulative outline
│
└── 06_METRICS/                           # Time tracking, weak topics
```

---

## Consolidation Plan

### Step 1: Merge Style Guides → law-school-common/02_STYLE_GUIDES/WRITING_STYLE.md
**Sources to merge:**
- CrimLaw/Lectures/Prep/Style_Guides/AUDIO_PREP_STYLE_GUIDE.md
- CrimLaw/Lectures/Prep/Style_Guides/CLASS_REFERENCE_STYLE_GUIDE.md
- Deals/Assignments/PREP-SHEET-STYLE-GUIDE.md
- law-school-common/elements-of-style.md

**Result:** One comprehensive style guide covering:
- Audio prep style (conversational, TTS-friendly)
- Text prep style (Q&A format, cold-call focused)
- Writing quality standards (tone, vocabulary, structure)

### Step 2: Merge Templates → law-school-common/03_TEMPLATES/
**Sources:**
- CrimLaw/Admin/Templates/* (5 files)
- Property/TEMPLATES/* (7 files)

**Result:** Unified template library with:
- audio_prep_template.md
- text_prep_template.md
- review_template.md
- master_log_template.md
- exam_spec_template.md

### Step 3: Merge Workflows → law-school-common/01_WORKFLOWS/
**Sources:**
- CrimLaw/Admin/Two_Doc_Prep_System.md
- CrimLaw/Admin/Per_Class_Prep_Blueprint.md
- law-school-common/POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md

**Result:** Three clear workflows:
- PRE_CLASS_WORKFLOW.md
- POST_CLASS_WORKFLOW.md
- EXAM_PREP_WORKFLOW.md

### Step 4: Create Command Interface → law-school-common/00_SYSTEM/COMMAND_INTERFACE.md
**Source:**
- CrimLaw/Admin/Command_Interface.md (adapt to be course-agnostic)

**Result:** Standard commands that work for all courses:
- `prep for [course] [class_num]` → generates audio + text prep
- `review [course] [class_num]` → processes transcript + generates review
- `status [course]` → shows MASTER_LOG summary
- `drill [course]` → daily exam practice

### Step 5: Standardize MASTER_LOG Format
**Source:**
- CrimLaw/Admin/Master_Log.md (best example)

**Result:** Every course gets identical MASTER_LOG with columns:
- Class# | Date | Topic | Status | Prep Done? | Review Done? | Outline Updated? | Exam Signals | Next Action

### Step 6: Clean Up Course Folders
**Actions:**
- Move CrimLaw to numbered structure (00-06)
- Populate Torts 00_ADMIN/
- Restructure Deals to match standard
- Archive old READMEs, conversion guides, etc.

---

## Files to Archive/Delete

**Archive (move to law-school-common/05_ARCHIVE/):**
- law-school-common/_HOUSEKEEPING_REPORT_2025-10-24.md
- law-school-common/_MASTER_STRUCTURE.md (outdated)
- law-school-common/_PREP_FORMAT_EXAMPLE.md (will be replaced by template)
- CrimLaw/Admin/ARCHIVE/* (already archived)
- CrimLaw/Admin/Archive.md
- Property/00_ADMIN/conversion_recommendations.md
- Property/00_ADMIN/AGENT_HANDOFF_PROMPT.md (redundant)

**Delete (no value):**
- All duplicate README.md files (except workspace root)
- .DS_Store files
- Empty placeholder files

---

## Success Criteria

After cleanup, you should have:

✅ **One style guide** - law-school-common/02_STYLE_GUIDES/WRITING_STYLE.md  
✅ **One template library** - law-school-common/03_TEMPLATES/  
✅ **Three clear workflows** - law-school-common/01_WORKFLOWS/  
✅ **Standard commands** - law-school-common/00_SYSTEM/COMMAND_INTERFACE.md  
✅ **Identical MASTER_LOGs** - Every course has same format  
✅ **Identical folder structure** - All courses use 00-06 numbering  
✅ **No clutter** - Old files archived, duplicates removed  
✅ **Clear visibility** - Both you and AI can see what's done/pending at a glance
