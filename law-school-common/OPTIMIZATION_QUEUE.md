# Law School System - Optimization Queue

**Updated:** 2026-01-19  
**Purpose:** Track actually useful improvements

---

## 🎯 Active Tasks

### 1. Update _MASTER_STRUCTURE.md
**Impact:** Medium  
**Why:** Current doc still shows old structure; should reflect monorepo setup

**Task:** Update to match current ACTIVE/ folder organization

---

### 2. Exam Signal Extraction
**Impact:** High  
**Why:** Actually helps with exam prep

**Task:**
- Simple grep for tags like `#EXAM_SIGNAL` across all course notes
- Output: one markdown file per course listing all signals
- Script: `law-school-common/scripts/extract_exam_signals.sh`

---

### 3. Past Exam Pattern Analysis
**Impact:** High  
**Why:** Helps predict what's on your exams

**Task:**
- Template for analyzing past exams (topic frequency, question types)
- Place in each course's `03_MAPPING/` folder when doing exam prep

---

## 📋 Backlog (Maybe Useful Later)

### Course Setup When Needed
- If starting a new course with the numbered structure, copy Property's folder setup
- No need for a script; just manual copy + rename

### Syllabus Parsing (if you get one)
- If a professor provides a structured syllabus, extract dates/topics manually or with simple AI prompt
- Don't need a dedicated script for this

---

## ❌ Rejected Tasks (Not Worth It)

- ~~Course-agnostic setup script~~ - Overkill, just copy folders manually
- ~~MASTER_LOG metrics automation~~ - Takes longer to build than to update manually
- ~~Professor quote database~~ - Already captured in review notes, no need for separate system
- ~~Shared legal rules library~~ - Courses don't overlap enough to justify this
- ~~OCR batch processor~~ - Process PDFs as needed, not in bulk
- ~~AI collaboration guide~~ - Just ask me what you need, no need for prompt library
- ~~System philosophy doc~~ - Philosophy should be obvious from usage
- ~~New course setup guide~~ - You'll remember from doing it once
- ~~Transcript filename standardization~~ - Current names work fine
- ~~Course-specific MASTER_LOG initialization~~ - Do when needed, not preemptively

---

## 💡 Usage

Just ask me to work on specific tasks from the Active list when you want them done.
