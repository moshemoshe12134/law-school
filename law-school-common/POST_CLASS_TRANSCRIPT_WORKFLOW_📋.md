# Post-Class Transcript Workflow

**Created:** 2026-01-19  
**Revised:** 2026-01-19 (simplified and aligned with existing systems)  
**Purpose:** Extract doctrine, exam signals, and outline material from lecture transcripts

---

## 🎯 Core Principle

**Transcripts are not diaries—they're mining operations.**

Your goal: Extract structured legal content (rules, holdings, policy, professor signals) and inject it directly into your outline. The transcript workflow is part of your **Review phase**, not a separate system.

---

## 📁 File Structure (Fits Your Existing Systems)

### For Numbered Systems (Property, Torts):
```
05_CLASS_NOTES/
└─ Lecture_XX/
    ├─ transcript_raw.txt                    ← Raw download
    └─ in_class_notes.md                     ← Your handwritten notes

06_REVIEW/
└─ Lecture_XX_review.md                      ← COMBINED review + transcript extraction
```

### For CrimLaw (Existing Structure):
```
Lectures/
├─ Transcripts/
│   └─ YYYY-MM-DD_CrimLaw_LectureXX.txt      ← Raw download
├─ Prep/
│   └─ lecture_XX_prep.md
└─ Reviews/
    └─ lecture_XX_review.md                  ← COMBINED review + transcript extraction
```

---

## � The Workflow (30 minutes total)

### Step 1: Download Raw Transcript (2 min)
- Download immediately after class (while it's fresh)
- Save to appropriate location:
  - **CrimLaw:** `Lectures/Transcripts/YYYY-MM-DD_CrimLaw_LectureXX.txt`
  - **Property:** `05_CLASS_NOTES/Lecture_XX/transcript_raw.txt`

### Step 2: Create UNIFIED Review Document (25 min)

**File:** `06_REVIEW/Lecture_XX_review.md` (or `Lectures/Reviews/lecture_XX_review.md`)

This ONE document contains everything. No fragmentation.

#### Template Structure:

```markdown
# Lecture XX Review: [Topic Name]

**Date:** YYYY-MM-DD  
**Status:** ✅ Review complete | Outline updated  
**Transcript Downloaded:** Yes

---

## 📊 META: Prep vs. Reality Check

### What I Got Right ✅
- Martin v. State was central
- Voluntary act requirement emphasized

### What I Missed/Underweighted ⚠️
- **Kelman time-framing** - Professor spent 15 min (expected 5)
- Introduced as "recurring theme for semester" → flag for every topic going forward

### Schedule Adjustments
- Jones v. US (omissions) moved to next class
- Will likely connect time-framing to Mens Rea next week

**Learning:** When syllabus mentions "Kelman" or similar theorist → 3x prep time

---

## 🎯 EXAM SIGNALS (from transcript)

### Direct Signals
1. **"This is the single most important..."** → Time-framing for actus reus
2. **"You need to understand this cold"** → Voluntary act vs. omission distinction
3. **Asked 3 hypos on this** → Status vs. act (Robinson sleepwalking)

### Pattern Observations
- Spent 20 min on one case (Martin) → likely exam-worthy
- Referenced Kelman 5 times → theoretical framework matters
- Cold called on policy, not just facts → need policy arguments ready

---

## 📝 DOCTRINAL EXTRACTION (Goes to Outline)

### Rules Stated/Clarified

#### Actus Reus - Voluntary Act Requirement
> **"A crime requires a voluntary act. The question is: when do we start the clock?"**  
> — Professor Harcourt, 10:23 AM

**Black Letter:** Actus reus requires:
1. A voluntary physical act, OR
2. An omission where there's a duty to act

**Kelman's Time-Framing Concept:**
- **Broad framing:** Include events leading up to the act (Decina driving knowing he has epilepsy)
- **Narrow framing:** Focus only on the involuntary moment (epileptic seizure itself)
- **Exam application:** Lawyers manipulate the time frame to argue voluntary vs. involuntary

#### Cases Discussed

**Martin v. State (20 min discussion)**
- Rule: Police cannot create the actus reus by forcing the defendant to commit the prohibited act
- Holding: Conviction overturned—being forced onto highway ≠ voluntary appearance
- Professor's emphasis: "This is about government overreach, not just criminal law"

**Newton (Unconsciousness Defense) (10 min)**
- Sleepwalking = no voluntary act
- But: Time-framing matters—did D create the dangerous situation voluntarily?

**Decina (Epilepsy) (10 min)**
- Prior voluntary act (driving) + knowledge of seizures = criminal liability
- Broader time frame captures the voluntary choice

### Policy Arguments (Professor's Language)

> **"Criminal law is fundamentally flexible. That's not a bug, it's a feature."**

- Flexibility allows adaptation to new situations
- But creates indeterminacy → manipulation by skilled lawyers
- Kelman's critique: Same facts = criminal OR not, depending on framing

---

## 📖 PROFESSOR QUOTES (For Exam Essays)

> **"Time-framing is how lawyers manipulate the actus reus element. You can make something criminal or not criminal just by where you draw the line."**  
> — Class 2, 10:23 AM

> **"Don't get stuck on the word 'voluntary.' Ask: when did the defendant's choice begin?"**  
> — Class 2, 10:45 AM

> **"This course is about seeing how indeterminate the law really is."**  
> — Class 2, opening remarks

**Use these for:**
- Essay introductions (show you're sophisticated)
- Policy sections (frame using his language)
- Cold call responses ("As you mentioned, Professor...")

---

## ✏️ OUTLINE UPDATES NEEDED

**To add:**
- [ ] Expand Kelman time-framing section in "I. Actus Reus"
- [ ] Add policy critique subsection: "Indeterminacy of Actus Reus"
- [ ] Create "Recurring Themes" master section (add time-framing as first entry)
- [ ] Flag Martin case as "exam-heavy" (20 min discussion)
- [ ] Add professor quotes to each doctrinal section

**Cross-references:**
- Time-framing will likely connect to Mens Rea (next class)
- Omissions topic continues next class (Jones v. US)

---

## 🔮 PREDICTIONS FOR NEXT CLASS

**Likely Topics:**
- Jones v. US (omissions liability)
- Transition to Mens Rea (MPC §2.02)

**What to prep extra:**
- Omissions doctrine—duty to act
- How time-framing applies to mens rea
- Policy: Why does law require positive duties?

**Prep adjustment:** Allocate extra time to theoretical readings (not just cases)
```

---

## 🎯 Key Differences from Old Workflow

| Old Approach | New Approach |
|--------------|--------------|
| 4 separate files per class | 1 unified review doc |
| "Post-Class" as separate phase | Integrated into Review phase |
| Focus on "what happened" | Focus on **extractable doctrine** |
| Prediction scoring (gamification) | Prediction **adjustment** (learning) |
| Transcript as diary | Transcript as **mining source** |
| Bash scripts for templates | Simple markdown template (AI fills it) |

---

## ⚡ Execution: How to Use This

### Right After Class (5 min):
1. Download transcript to correct folder
2. Tell AI: "I just downloaded Lecture XX transcript. Create the review doc using the template."

### Same Evening (20 min):
1. AI reads your prep doc + transcript + in-class notes
2. AI fills out the template:
   - Compares prep vs. reality
   - Extracts exam signals
   - Pulls doctrinal rules and cases
   - Finds professor quotes
   - Lists outline updates
3. You review and edit

### Next Morning (5 min):
1. Copy doctrinal extraction → paste into outline
2. Update MASTER_LOG: mark "Transcript ✅" and "Review ✅"
3. Adjust next prep based on "Predictions" section

---

## 📊 Tracking (Minimal Overhead)

**In MASTER_LOG:**

Add two columns:
- `Transcript?` → ✅ or ⏳
- `Review?` → ✅ or ⏳

```markdown
| Lecture | Date | Topic | Prep | Transcript | Review | Outline Updated |
|---------|------|-------|------|------------|--------|-----------------|
| 1 | 01-20 | Intro | ✅ | ✅ | ✅ | ✅ |
| 2 | 01-22 | Actus Reus | ✅ | ✅ | ⏳ | ⏳ |
```

**No separate tracking files. No prediction scores. Just: did you do it?**

---

## 🛠️ AI Prompt for This Workflow

**After downloading transcript, use this prompt:**

```
I just finished Lecture XX on [Topic]. I have:
1. My prep doc: [link to prep]
2. In-class notes: [link to notes]
3. Raw transcript: [link to transcript]

Please create my Lecture XX Review document using this template:
[paste template from above]

Focus on:
- Extracting black-letter rules and holdings
- Identifying exam signals (his emphasis, hypos, "this is important")
- Comparing my prep predictions vs. what actually happened
- Pulling verbatim professor quotes for essay use
- Flagging what needs to go into my outline

Be specific with case names, policy arguments, and cross-references.
```

---

## 💡 Why This Approach Works

### 1. **No File Fragmentation**
- One review doc, not four
- Everything in one place for quick reference
- Easy to search and navigate

### 2. **Outline-First Mindset**
- Transcript extraction feeds directly into outline sections
- No separate "quote bank"—quotes live in doctrinal context
- Focus on **usable legal content**, not "what happened" storytelling

### 3. **Integrated with Existing System**
- Uses your current folder structure (no "Post_Class" folder)
- Part of Review phase (already in your workflow)
- Works with both numbered (Property) and named (CrimLaw) systems

### 4. **Feedback Loop Without Gamification**
- Still tracks "prep vs. reality"
- But focuses on **learning adjustment**, not scoring
- Question: "What do I prep differently?" not "Did I get 8/10?"

### 5. **AI-Native**
- One prompt generates the whole document
- AI compares prep vs. transcript automatically
- You edit and refine, not write from scratch

### 6. **Time-Efficient**
- 2 min: Download
- 3 min: Run AI prompt
- 20 min: Review and edit AI output
- 5 min: Update outline and log
- **Total: 30 min**

---

## 📋 Implementation Checklist

### One-Time Setup (5 min)
- [ ] Save this template in your common/ folder
- [ ] Add "Transcript?" and "Review?" columns to MASTER_LOG
- [ ] Create AI prompt bookmark for quick access

### Per-Class Workflow (30 min)
- [ ] Download transcript to appropriate folder
- [ ] Run AI prompt with prep + notes + transcript
- [ ] Review and edit AI-generated review doc
- [ ] Copy doctrinal sections → paste into outline
- [ ] Update MASTER_LOG checkboxes
- [ ] Adjust next class prep based on learnings

### Weekly Audit (15 min, Sundays)
- [ ] Review all transcripts for the week
- [ ] Look for patterns in "what I missed"
- [ ] Consolidate professor quotes into outline
- [ ] Check if predictions are getting more accurate

---

## 🎯 Success Metrics

**After 5 classes:**
- ✅ All 5 transcripts downloaded and reviewed
- ✅ Outline has 15-20 verbatim professor quotes
- ✅ Can identify 3 "professor patterns" (what he emphasizes)
- ✅ Prep adjustments are more targeted

**After 15 classes (midterm):**
- ✅ Full professor quote library in outline
- ✅ "Prep vs. reality" gaps closing
- ✅ Can predict exam-heavy topics with 80% accuracy
- ✅ Outline language mirrors professor's language

**Before exam:**
- ✅ Outline = your prep + professor's emphasis + past exam patterns
- ✅ No surprises on what professor values
- ✅ Ready to write in his conceptual framework

---

## 🚫 Anti-Patterns to Avoid

❌ **Creating separate "quotes" file** → Quotes should live in doctrinal context  
❌ **Scoring prediction accuracy** → Focus on adjusting, not gamifying  
❌ **Reading transcript cover-to-cover** → Mine for specific content  
❌ **Delaying transcript review** → Do it same day while class is fresh  
❌ **Skipping outline integration** → The whole point is to feed your outline  
❌ **Over-engineering with scripts** → Keep it simple, template-based  

---

## 📁 Final File Structure Example

### CrimLaw:
```
Lectures/
├─ Transcripts/
│   ├─ 2026-01-20_CrimLaw_Lecture01.txt
│   └─ 2026-01-22_CrimLaw_Lecture02.txt
├─ Prep/
│   ├─ lecture_01_prep.md
│   └─ lecture_02_prep.md
└─ Reviews/
    ├─ lecture_01_review.md  ← Includes transcript extraction
    └─ lecture_02_review.md  ← Includes transcript extraction
```

### Property (Numbered):
```
05_CLASS_NOTES/
├─ Lecture_01/
│   ├─ transcript_raw.txt
│   └─ in_class_notes.md
└─ Lecture_02/
    ├─ transcript_raw.txt
    └─ in_class_notes.md

06_REVIEW/
├─ Lecture_01_review.md  ← Includes transcript extraction
└─ Lecture_02_review.md  ← Includes transcript extraction
```

---

## 🎓 Bottom Line

**Old thinking:** "I need to know what happened in class."  
**New thinking:** "I need to extract doctrine and signals from class to build my outline."

**Transcripts aren't for memory—they're for mining.**

Use this workflow to turn every lecture into structured, outline-ready, exam-focused content. No fragmentation, no busywork, just extraction and integration.
