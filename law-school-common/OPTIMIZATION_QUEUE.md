# Law School System Optimization Queue

**Created:** 2026-01-19  
**Purpose:** Autonomous optimization backlog for continuous AI work  
**Status:** Active

---

## 🎯 How This Works

This file is your **continuous optimization task list**. When you want me to work autonomously:

**Command:**
```
Work through the OPTIMIZATION_QUEUE. Complete tasks in priority order. 
After finishing each task, mark it complete and immediately start the next. 
Keep working until the queue is empty or I tell you to stop.
Do not ask for permission between tasks—just keep going.
```

---

## 📋 PRIORITY 1: Critical System Improvements

### 1.1 Standardize Folder Structure Across All Courses
**Status:** 🔴 Not Started  
**Effort:** 30 min  
**Impact:** High

**Task:**
- Property and Torts use `00_ADMIN/` to `08_METRICS/` structure
- CrimLaw uses `Admin/`, `Lectures/` structure
- Update `_MASTER_STRUCTURE.md` to reflect numbered system as canonical
- Document migration path for CrimLaw → numbered structure (don't execute migration, just document)

**Done when:**
- [ ] `_MASTER_STRUCTURE.md` shows numbered folders as standard
- [ ] Migration guide created: `MIGRATION_GUIDE.md`
- [ ] All course README files reference the standard

---

### 1.2 Create Unified Transcript Workflow Template
**Status:** 🔴 Not Started  
**Effort:** 20 min  
**Impact:** High

**Task:**
- Based on revised `POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md`
- Create reusable template file: `TEMPLATES/lecture_review_template.md`
- Add to each course's TEMPLATES/ folder (or link to common)
- Update Property MASTER_LOG to include "Transcript?" column

**Done when:**
- [ ] Template file exists in `law-school-common/TEMPLATES/`
- [ ] Template includes all sections from workflow doc
- [ ] MASTER_LOG in Property updated with transcript tracking

---

### 1.3 Build Course-Agnostic Setup Script
**Status:** 🔴 Not Started  
**Effort:** 45 min  
**Impact:** High

**Task:**
- Current `setup_all_course_systems.py` is hardcoded for Contracts
- Refactor to read from `course_config.json` in each course folder
- Config should specify: course name, professor, term, folder structure preference
- Script should create folders, templates, and MASTER_LOG

**Done when:**
- [ ] `setup_all_course_systems.py` is course-agnostic
- [ ] Example `course_config.json` created
- [ ] Documentation in script header explains usage

---

### 1.4 Create Exam Signal Tagger System
**Status:** 🔴 Not Started  
**Effort:** 30 min  
**Impact:** High

**Task:**
- Define standard tags: `#EXAM_SIGNAL`, `#HYPO`, `#POLICY`, `#PROFESSOR_EMPHASIS`
- Create grep script to extract all tagged items: `scripts/extract_exam_signals.sh`
- Generate "Exam Signals Report" that lists all signals by topic
- Add tagging instructions to prep/review templates

**Done when:**
- [ ] Tag definitions documented in `_MASTER_STRUCTURE.md`
- [ ] Script exists and works: `law-school-common/scripts/extract_exam_signals.sh`
- [ ] Example output file created

---

## 📋 PRIORITY 2: Content Organization

### 2.1 Consolidate Professor Quote Database
**Status:** 🔴 Not Started  
**Effort:** 40 min  
**Impact:** Medium

**Task:**
- Create `PROFESSOR_QUOTES.md` in each course's outline folder
- Structure: Topic → Quote → Source (Lecture #, timestamp)
- Extract quotes from any existing review files
- Add to MASTER_LOG as trackable item

**Done when:**
- [ ] Template created: `TEMPLATES/professor_quotes_template.md`
- [ ] Property course has `07_OUTLINE/PROFESSOR_QUOTES.md` started
- [ ] Instructions added to review workflow

---

### 2.2 Build Shared Legal Rules Library
**Status:** 🔴 Not Started  
**Effort:** 60 min  
**Impact:** Medium

**Task:**
- Create `law-school-common/SHARED_RULES/` directory
- Extract cross-cutting doctrines (jurisdiction, standing, burden of proof, etc.)
- Format: Atomic rule files with course cross-references
- Index file that links to all rules

**Done when:**
- [ ] Directory structure created
- [ ] 5-10 example rules documented
- [ ] `INDEX.md` with categorized rule list
- [ ] Instructions on when to add to this library

---

### 2.3 Past Exam Analysis Template
**Status:** 🔴 Not Started  
**Effort:** 30 min  
**Impact:** High

**Task:**
- Create template for analyzing past exams
- Fields: Topic distribution, question types, professor patterns, time allocation
- Python script to generate comparison across multiple years
- Add to `03_MAPPING/` folder in standard structure

**Done when:**
- [ ] Template: `TEMPLATES/past_exam_analysis_template.md`
- [ ] Script: `scripts/exam_pattern_analyzer.py`
- [ ] Example analysis for Property (if exams available)

---

## 📋 PRIORITY 3: Automation & Scripts

### 3.1 Automate MASTER_LOG Metrics
**Status:** 🔴 Not Started  
**Effort:** 45 min  
**Impact:** Medium

**Task:**
- Script to count files in `04_PREP/` and `06_REVIEW/` → calculate "Classes completed"
- Extract prep time from review docs (if timestamped) → calculate "Average prep time"
- Generate updated metrics section for MASTER_LOG
- Make it a weekly task: `scripts/update_master_log_metrics.py`

**Done when:**
- [ ] Script exists and works
- [ ] Can run: `python update_master_log_metrics.py --course Property`
- [ ] Outputs updated metrics in proper format

---

### 3.2 Syllabus Parser (AI-Assisted)
**Status:** 🔴 Not Started  
**Effort:** 60 min  
**Impact:** High

**Task:**
- Create script that feeds syllabus to AI with JSON schema
- AI extracts: lecture number, date, topic, assigned readings, pages
- Outputs `_SOURCE_TRACKER.json`
- Can be run on any course

**Done when:**
- [ ] Script: `scripts/parse_syllabus_ai.py`
- [ ] JSON schema documented
- [ ] Example run on Property or Torts syllabus

---

### 3.3 OCR Batch Processor
**Status:** 🔴 Not Started  
**Effort:** 30 min  
**Impact:** Low

**Task:**
- Enhance existing `ocr_scripts/pdf_to_text.py`
- Add batch mode: process entire folder of PDFs
- Generate extraction log with success/failure status
- Add to documentation

**Done when:**
- [ ] Script enhanced with `--batch` flag
- [ ] Works on folder input
- [ ] Generates `ocr_log.txt` with results

---

## 📋 PRIORITY 4: Documentation & Guides

### 4.1 Write "New Course Setup" Guide
**Status:** 🔴 Not Started  
**Effort:** 40 min  
**Impact:** Medium

**Task:**
- Step-by-step guide for starting a new course
- From folder creation → syllabus parsing → first prep doc
- Include screenshots/examples
- Add to `law-school-common/`

**Done when:**
- [ ] `NEW_COURSE_SETUP_GUIDE.md` created
- [ ] Covers complete workflow
- [ ] Links to all relevant templates and scripts

---

### 4.2 Create "AI Collaboration Guide"
**Status:** 🔴 Not Started  
**Effort:** 30 min  
**Impact:** High

**Task:**
- Document best prompts for each workflow phase
- Prep generation, review extraction, outline building
- Copy-paste ready prompts
- Include examples of good vs. bad prompts

**Done when:**
- [ ] `AI_PROMPTS_LIBRARY.md` created
- [ ] 10+ ready-to-use prompts included
- [ ] Organized by workflow phase

---

### 4.3 Write System Philosophy Doc
**Status:** 🔴 Not Started  
**Effort:** 20 min  
**Impact:** Low

**Task:**
- Document the "why" behind the system design
- Principles: outline-first, exam-signal focused, minimal friction
- Anti-patterns to avoid
- For future reference and onboarding

**Done when:**
- [ ] `SYSTEM_PHILOSOPHY.md` created
- [ ] Covers core principles
- [ ] Explains design decisions

---

## 📋 PRIORITY 5: Course-Specific Improvements

### 5.1 Property Course: Complete MASTER_LOG Setup
**Status:** 🔴 Not Started  
**Effort:** 20 min  
**Impact:** Medium

**Task:**
- Current MASTER_LOG is template with no data
- Parse syllabus (if available) to populate lecture table
- Add past exam analysis row
- Set up metrics tracking

**Done when:**
- [ ] Lecture table populated with available data
- [ ] Metrics section has actual numbers
- [ ] Workflow instructions added

---

### 5.2 CrimLaw: Standardize Transcript Filenames
**Status:** 🔴 Not Started  
**Effort:** 15 min  
**Impact:** Low

**Task:**
- Check if transcripts follow `YYYY-MM-DD_CrimLaw_LectureXX.txt` format
- Rename if needed
- Document naming convention in CrimLaw README

**Done when:**
- [ ] All transcripts follow standard format
- [ ] README updated with naming rules

---

### 5.3 Torts: Initialize MASTER_LOG
**Status:** 🔴 Not Started  
**Effort:** 20 min  
**Impact:** Medium

**Task:**
- Copy MASTER_LOG template to Torts
- Customize for Torts specifics (if known)
- Set up folder structure if incomplete

**Done when:**
- [ ] `MASTER_LOG.md` exists in Torts
- [ ] All folders match standard structure

---

## 🎯 How to Add New Tasks

When you identify optimization opportunities:

```markdown
### X.X Task Title
**Status:** 🔴 Not Started  
**Effort:** [time estimate]  
**Impact:** High/Medium/Low

**Task:**
- Detailed description
- What needs to be done
- Any constraints or requirements

**Done when:**
- [ ] Specific completion criteria
- [ ] Measurable outcomes
- [ ] Verification steps
```

---

## 📊 Status Legend

- 🔴 **Not Started** - Task in queue
- 🟡 **In Progress** - Currently being worked on
- 🟢 **Complete** - Done and verified
- ⏸️ **Blocked** - Waiting on something
- ⏭️ **Skipped** - Deprioritized or irrelevant

---

## 💡 Pro Tips for Continuous Work

1. **Start with:** "Work through OPTIMIZATION_QUEUE in priority order. Keep going until I stop you."
2. **I will:** Mark current task 🟡, complete it, mark 🟢, move to next
3. **You can:** Interrupt anytime with new priority tasks
4. **I'll report:** Progress summary every 5 tasks
5. **When done:** I'll report completion and ask for new tasks

---

## 📈 Progress Tracking

**Tasks Completed:** 0 / 23  
**Last Updated:** 2026-01-19  
**Current Sprint:** Initial setup

**Recently Completed:**
- None yet

**Next Up:**
1. Standardize folder structure
2. Create transcript workflow template
3. Build course-agnostic setup script
