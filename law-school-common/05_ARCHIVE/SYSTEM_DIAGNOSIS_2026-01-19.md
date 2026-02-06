# Law School System Diagnosis - Jan 19, 2026

## Current State Summary

**Classes start tomorrow (Jan 20).** You have 5 active courses with wildly inconsistent setups.

---

## Course-by-Course Status

### CrimLaw ✅ (Most Ready)
**Structure:** Custom (Admin/Lectures/Exams)  
**Syllabus:** ✅ Full syllabus parsed into 29 classes with assignments  
**Past Exams:** ✅ Analyzed (2006 Spring exam documented)  
**Past Outlines:** ✅ Indexed (7 past outlines mapped)  
**Prep System:** ✅ Two-doc system (Audio + Class Reference)  
**Preps Done:** Classes 1-2 have audio preps ready; Classes 1-8 have draft packet preps  
**Transcripts:** Folders exist (raw/clean)  
**Reviews:** Empty folder waiting for transcripts  

**What's Missing:**
- QC not done on any prep docs (all marked "pending QC")
- Need to finalize Class 3+ audio preps
- Post-class workflow needs testing (never done a review yet)

---

### Property ⚠️ (Structure Only)
**Structure:** ✅ Numbered system (00-08 folders + MASTER_LOG)  
**Syllabus:** ❌ Placeholder file only  
**Past Exams:** ❌ None  
**Past Outlines:** ❌ None  
**Prep System:** ⚠️ One prep doc exists (Class_01_Prep.md) but no audio, no quality check  
**Preps Done:** 1 draft prep (untested format)  
**Transcripts:** No folder yet  
**Reviews:** Empty folder  

**What's Missing:**
- Syllabus (critical)
- Past exams/outlines
- Audio prep workflow
- Transcript processing setup
- Post-class review system

---

### Torts ⚠️ (Structure Only)
**Structure:** ✅ Numbered system (00-08 folders + past outlines folder)  
**Syllabus:** ❌ None (folder exists but empty)  
**Past Exams:** ❌ None  
**Past Outlines:** ✅ 5 past outlines available (Huang 2022-2024, others)  
**Prep System:** ❌ No preps exist  
**Preps Done:** 0  
**Transcripts:** No folder yet  
**Reviews:** Empty folder  

**What's Missing:**
- Syllabus (critical)
- First prep doc
- Audio prep workflow
- Transcript processing setup
- Post-class review system

---

### Deals ⚠️ (Minimal Setup)
**Structure:** Custom (Assignments/Sources/Outlines/Exams folders)  
**Syllabus:** ❌ None visible  
**Past Exams:** ⚠️ Folder exists ("DEALS/") but contents unknown  
**Past Outlines:** ❌ None visible  
**Prep System:** ⚠️ Has PREP-SHEET-STYLE-GUIDE.md but no actual preps  
**Preps Done:** 0  
**Transcripts:** No folder  
**Reviews:** No folder  

**What's Missing:**
- Syllabus
- Numbered folder structure
- First prep doc
- Full workflow setup

---

### LPW-II ❌ (Empty)
**Structure:** Empty folder  
**Everything:** Missing  

---

## Critical Problems Identified

### Problem 1: No Standardization
- CrimLaw uses Admin/Lectures/Exams structure
- Property/Torts use numbered 00-08 structure
- Deals uses custom structure
- No consistency in file naming or workflows

### Problem 2: Missing Syllabi
- 4 out of 5 courses have no syllabus
- Cannot pre-generate preps without assignment info
- Cannot build master tracking logs

### Problem 3: Prep System Not Replicated
- CrimLaw has tested two-doc system (audio + reference)
- Other courses: nothing
- Audio workflow exists only for CrimLaw
- No TTS automation set up

### Problem 4: Post-Class Workflow Undefined
- Transcript processing exists for CrimLaw but never actually used
- No review template
- No system for extracting exam signals from transcripts
- No quality-check for transcription errors

### Problem 5: Exam Prep Not Operationalized
- Past outlines exist but not indexed/searchable
- No daily drill system
- No spaced repetition
- No "exam signals" extraction from class notes
- Outline building not integrated into post-class workflow

### Problem 6: Too Much Manual Work Required
- Every step requires AI prompting and babysitting
- No click-button automation
- No standardized prompts
- You'll be spending hours daily on system management instead of studying

---

## What You Actually Need

### Immediate (Before Jan 20)
1. **CrimLaw Class 1 prep finalized** - you have audio + packet, just need to listen/read
2. **Property/Torts/Deals Class 1 emergency prep** - minimal cold-call insurance

### This Week (Jan 20-24)
1. **Get all syllabi** - cannot plan without these
2. **Port CrimLaw system to Property/Torts** - standardize everything
3. **Test transcript→review workflow** - after first CrimLaw class
4. **Build automation scripts** - no more manual prompting

### This Month (Jan 2026)
1. **Daily rhythm** - transcripts in, reviews out, outlines growing
2. **Past exam integration** - mine outlines for what actually gets tested
3. **Exam drill system** - 15min/day answering practice hypos

---

## Recommended System Architecture

### Standard Folder Structure (All Courses)
```
CourseNameHere/
├── 00_ADMIN/
│   ├── syllabus.md               # parsed from PDF
│   ├── MASTER_LOG.md             # class tracking + metrics
│   └── exam_spec.md              # past exam analysis
├── 01_SOURCES/
│   ├── past_exams/
│   └── past_outlines/
├── 02_PREP/
│   ├── audio/                    # 25-min audio preps (TTS)
│   └── text/                     # text preps for cold calls
├── 03_TRANSCRIPTS/
│   ├── raw/                      # Echo360 downloads
│   └── processed/                # cleaned + formatted
├── 04_REVIEWS/
│   └── YYYY-MM-DD_ClassNN_review.md  # extract exam signals
├── 05_OUTLINE/
│   └── outline.md                # cumulative, exam-focused
└── scripts/
    ├── generate_prep.sh          # one-click prep generation
    ├── process_transcript.sh     # clean + review generation
    └── extract_signals.sh        # grep for #EXAM_SIGNAL tags
```

### Pre-Class Workflow (50min total)
**Input:** Syllabus assignment for that class  
**Process:**
1. Run `./scripts/generate_prep.sh ClassNN` → generates audio + text prep
2. TTS converts audio prep to MP3
3. You listen (25min) while commuting/walking
4. You skim text prep (25min) - focus on cold-call Q&A section

**Output:** Ready for class with zero reading

### Post-Class Workflow (30min + automated)
**Input:** Echo360 transcript download (raw text)  
**Process:**
1. Drop transcript into `03_TRANSCRIPTS/raw/`
2. Run `./scripts/process_transcript.sh ClassNN`
   - Cleans transcription errors using context
   - Generates review doc with:
     - What professor emphasized (exam signals)
     - Corrections to prep doc
     - Outline updates needed
3. You review the output (5min), add manual notes (5min)
4. Script auto-updates outline

**Output:** Outline grows, exam signals captured, no manual work

### Daily Exam Drill (15min)
**Input:** Past exam questions + current outline  
**Process:**
1. Run `./scripts/daily_drill.sh` → picks 1 hypo from past exams
2. You outline answer (5min)
3. Compare to past outline answer (5min)
4. Flag gaps → review queue

**Output:** Daily practice, gaps identified early

---

## Automation Scripts Needed

### 1. `generate_prep.sh CourseNameHere ClassNN`
- Reads syllabus assignment for ClassNN
- Pulls relevant past outlines
- Generates audio prep (conversational, 25min)
- Generates text prep (Q&A format, cold-call focused)
- Uses standardized prompt (no manual input needed)

### 2. `process_transcript.sh CourseNameHere ClassNN`
- Takes raw Echo360 transcript
- Fixes common transcription errors (legal terms, case names)
- Extracts exam signals (professor emphasis, hypos, "this will be on exam")
- Generates review doc
- Updates outline automatically

### 3. `extract_signals.sh CourseNameHere`
- Greps all review docs for `#EXAM_SIGNAL` tags
- Generates report: topic → all signals
- Outputs to `05_OUTLINE/exam_signals_index.md`

### 4. `daily_drill.sh CourseNameHere`
- Picks random hypo from past exams
- Presents question
- Waits for your answer
- Shows model answer from past outlines
- Logs your performance

---

## Writing Quality Issue

You mentioned AI writing is poor. Solutions:

### Option 1: Style Guide Integration
- Create `law-school-common/WRITING_STYLE.md` with examples of good writing
- Include in every prompt: "Follow writing style from WRITING_STYLE.md"
- Problem: Style drift with iteration

### Option 2: Example-Based Learning
- Save your best prep/review docs as templates
- Prompts: "Generate prep in the style of [example file]"
- More consistent than guidelines

### Option 3: Two-Pass System
- First pass: AI generates content (facts, doctrine, analysis)
- Second pass: Rewrite for clarity using fixed templates
- You edit templates once, reuse forever

**Recommended:** Option 2 + 3 hybrid
- Templates for structure
- Example files for tone/style
- Minimal manual editing needed

---

## Action Plan for Tomorrow (Jan 19 Evening)

### Task 1: Finalize CrimLaw Class 1 Prep (30min)
1. Listen to existing audio prep
2. Skim text prep
3. You're ready for class

### Task 2: Emergency Prep for Other Classes (if needed)
Only if you have cold call in Property/Torts/Deals tomorrow:
1. Check syllabus/assignment (if available)
2. Generate minimal cold-call prep using CrimLaw template
3. Focus on case names + holdings only

### Task 3: Collect All Syllabi (10min)
- Download from Canvas/email
- Save to each course's 00_ADMIN/ folder
- Critical for planning this week

---

## Action Plan for This Week

### Monday Jan 20 (After Classes)
1. Test transcript workflow with CrimLaw Class 1
2. Identify what works/doesn't work

### Tuesday Jan 21
1. Get syllabi for Property/Torts/Deals
2. Parse into assignment files (like CrimLaw has)
3. Build master logs for each course

### Wednesday Jan 22
1. Generate preps for rest of week (Property/Torts/Deals)
2. Test audio TTS workflow

### Thursday Jan 23
1. Build automation scripts (generate_prep.sh, process_transcript.sh)
2. Test with one course

### Friday Jan 24
1. Deploy scripts to all courses
2. Generate next week's preps in batch
3. System should be autonomous by end of week

---

## Success Metrics

By end of January, you should have:
- ✅ All 5 courses using identical structure
- ✅ Pre-class prep taking <50min total
- ✅ Post-class review taking <30min total
- ✅ Outlines growing automatically
- ✅ Daily exam drills running (15min/day)
- ✅ Zero time spent "babysitting AI"
- ✅ All work happening via script execution

---

## Bottom Line

**Current state:** 1 course partially ready, 4 courses not ready, no automation  
**What you need:** Standardized structure + automated workflows + zero manual prompting  
**Timeline:** 1 week to build, then fully autonomous  
**Your time investment after setup:** 50min pre-class + 30min post-class + 15min drills = 95min/day total
