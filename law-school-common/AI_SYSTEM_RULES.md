# AI System Rules & Conventions

**Purpose:** Strict conventions for AI when working in this repository  
**Applies to:** All AI agents working in law-school monorepo  
**Updated:** 2026-01-19

---

## 🚨 CRITICAL RULES - READ FIRST

### 1. Always Check Existing Structure Before Creating Files
**BEFORE creating any file, search for existing similar files.**

```bash
# Check what already exists
find . -name "*similar_topic*"
grep -r "similar content" .
```

**Rule:** If similar file exists, update it. Don't create duplicates.

---

### 2. No File Proliferation
**Default: ONE file per purpose.**

❌ **WRONG:**
```
notes_draft.md
notes_v2.md
notes_final.md
notes_backup.md
```

✅ **RIGHT:**
```
notes.md  (just update this one file)
```

**Exception:** Only create multiple files when explicitly requested or when there's a clear structural reason (e.g., one file per lecture in a lectures/ folder).

---

### 3. Scripts Must Live in Script Folders

**NEVER put scripts in content folders.**

❌ **WRONG:**
```
Property/
├── notes.md
├── process_notes.py  ← NO!
└── outline.md
```

✅ **RIGHT:**
```
Property/
├── notes.md
├── outline.md
└── scripts/
    └── process_notes.py  ← YES
```

**OR use the common scripts folder:**
```
law-school-common/
└── scripts/
    └── process_notes.py
```

---

### 4. Consult Folder Structure Before Building

**ALWAYS check `_MASTER_STRUCTURE.md` and course README before creating folders.**

```bash
# Check the standard
cat law-school-common/_MASTER_STRUCTURE.md

# Check course-specific structure
cat ACTIVE/CrimLaw/Admin/README.md
```

**Rule:** Follow existing structure. Don't invent new folders.

---

### 5. One Concept = One Location

**Don't scatter the same type of information across multiple places.**

❌ **WRONG:**
```
prep_notes_class1.md      (has prep content)
outline.md                (also has prep content)
study_guide.md            (also has prep content)
```

✅ **RIGHT:**
```
prep/class_01_prep.md     (all prep here)
outline.md                (just outline)
```

**Rule:** Each type of content has ONE designated location.

---

## 📁 Folder Structure Rules

### Standard Course Structure

**Use numbered folders (Property/Torts style) as canonical:**

```
CourseName/
├── 00_ADMIN/           ← Admin, workflows, README
├── 01_SYLLABUS/        ← Syllabus and schedule
├── 02_SOURCES/         ← Textbooks, readings, past exams
├── 03_MAPPING/         ← Crosswalks, exam specs
├── 04_PREP/            ← Per-lecture prep docs
├── 05_CLASS_NOTES/     ← In-class notes, transcripts
├── 06_REVIEW/          ← Post-class review docs
├── 07_OUTLINE/         ← Cumulative outlines
├── 08_METRICS/         ← Time tracking, analytics
├── TEMPLATES/          ← Templates for this course
└── scripts/            ← Course-specific scripts (if any)
```

**CrimLaw uses different structure - that's OK, but don't create new structures without asking.**

---

### Common Folder (law-school-common/)

```
law-school-common/
├── TEMPLATES/          ← Reusable templates
├── scripts/            ← Reusable scripts
├── ocr_scripts/        ← OCR utilities
├── OPTIMIZATION_QUEUE.md
├── _MASTER_STRUCTURE.md
├── POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md
└── AI_SYSTEM_RULES.md  ← This file
```

**Rule:** Only put things here if used by 2+ courses.

---

### Script Organization

**All scripts go in `scripts/` or `ocr_scripts/`:**

```
scripts/
├── setup_course.py
├── parse_syllabus.py
├── extract_exam_signals.sh
└── README.md

ocr_scripts/
├── pdf_to_text.py
├── pptx_to_text.py
└── README.md
```

**Never:**
- Scripts in root folders
- Scripts mixed with content files
- Scripts in ADMIN/ folders (unless it's `Admin/Scripts/` subfolder)

---

## 📝 File Naming Conventions

### Dates: YYYY-MM-DD Format
```
✅ 2026-01-22_class02_prep.md
✅ 2026-01-22_CrimLaw_Lecture02.txt
❌ jan-22-2026.md
❌ class_02_jan_22.md
```

### Be Specific, Not Vague
```
✅ lecture_05_review.md
✅ actus_reus_outline.md
❌ notes.md
❌ doc.md
❌ temp.md
```

### Use Underscores for Multi-Word Names
```
✅ exam_prep_checklist.md
✅ past_exam_analysis.md
❌ exam-prep-checklist.md
❌ ExamPrepChecklist.md
```

---

## 🔄 Update Don't Duplicate

### When Adding Content

**Check if there's already a file for this:**

1. **Prep for a class?** → Update `04_PREP/lecture_XX_prep.md`
2. **Review after class?** → Update `06_REVIEW/lecture_XX_review.md`
3. **Rule/concept?** → Add to `07_OUTLINE/outline.md`
4. **Professor quote?** → Add to `07_OUTLINE/PROFESSOR_QUOTES.md` (if it exists)

**Don't create:** `new_prep_notes.md`, `additional_review.md`, `more_outline.md`

---

### When Improving Content

**Update the existing file, don't create a new version:**

```bash
# ❌ WRONG
mv outline.md outline_old.md
create outline_v2.md

# ✅ RIGHT
# Just edit outline.md directly
```

**Git tracks history - you don't need version files.**

---

## 🧹 Housekeeping Rules

### 1. Check for Redundancy Before Creating

**Ask yourself:**
- Does this file already exist under a different name?
- Can I add this to an existing file instead?
- Is this creating unnecessary fragmentation?

### 2. Delete/Consolidate When You See Duplication

**If you find:**
```
prep_notes_v1.md
prep_notes_v2.md
prep_notes_final.md
```

**Do this:**
```bash
# Merge into one file
cat prep_notes_final.md > prep_notes.md
rm prep_notes_v1.md prep_notes_v2.md prep_notes_final.md
```

### 3. Use README Files to Explain Structure

**Every major folder should have README.md:**

```
Property/
├── 00_ADMIN/
│   └── README.md  ← Explains admin files
├── 04_PREP/
│   └── README.md  ← Explains prep workflow
└── 07_OUTLINE/
    └── README.md  ← Explains outline organization
```

### 4. Scripts Need Documentation

**Every script should have:**
- Header comment explaining purpose
- Usage example
- Required inputs/outputs

```python
#!/usr/bin/env python3
"""
Parse syllabus into structured JSON.

Usage:
    python parse_syllabus.py syllabus.txt output.json

Outputs:
    JSON file with lectures, readings, dates
"""
```

---

## ⚠️ Common Anti-Patterns to Avoid

### 1. "Notes Explosion"
❌ Creating 10 different note files for the same lecture

**Fix:** One prep file, one review file per lecture.

### 2. "Script Scatter"
❌ Python files everywhere in content folders

**Fix:** All scripts in `scripts/` folder.

### 3. "Duplicate Documentation"
❌ Multiple README files saying the same thing

**Fix:** One README per folder max. Use links to common docs.

### 4. "Version File Hell"
❌ `outline_v1.md`, `outline_v2.md`, `outline_final.md`

**Fix:** Just `outline.md` - Git tracks versions.

### 5. "Orphan Files"
❌ Files with no clear purpose or location

**Fix:** If you can't explain where it goes in the structure, don't create it.

---

## 🎯 When to Break These Rules

**You may break these rules when:**
1. User explicitly requests it
2. There's a clear structural reason (explain in commit message)
3. You're following an established pattern in that course

**But first:** Ask the user if they want to break convention.

---

## 📊 Self-Check Before Creating Files

**Ask yourself:**

1. ✅ Did I check if this file already exists?
2. ✅ Is this in the right folder per `_MASTER_STRUCTURE.md`?
3. ✅ Can I update an existing file instead?
4. ✅ If it's a script, is it in `scripts/`?
5. ✅ Does the filename follow conventions?
6. ✅ Am I creating necessary structure or unnecessary clutter?

**If you answered "no" to any → reconsider the approach.**

---

## 🔧 Enforcement

**When working in this repo:**

1. **Before creating any file:** Reference this document
2. **Before creating any folder:** Check `_MASTER_STRUCTURE.md`
3. **Before writing a script:** Make sure it goes in `scripts/`
4. **Before duplicating content:** Search for existing versions

**This document is law. Follow it.**

---

## 📚 Related Documents

- [_MASTER_STRUCTURE.md](law-school-common/_MASTER_STRUCTURE.md) - Standard folder structure
- [OPTIMIZATION_QUEUE.md](law-school-common/OPTIMIZATION_QUEUE.md) - Task backlog
- [POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md](law-school-common/POST_CLASS_TRANSCRIPT_WORKFLOW_📋.md) - Transcript workflow

---

## 💡 Philosophy

**Simplicity over complexity.**
**One canonical location over scattered duplicates.**
**Update over recreate.**
**Structure before content.**

Keep the system clean. Keep the system maintainable.
