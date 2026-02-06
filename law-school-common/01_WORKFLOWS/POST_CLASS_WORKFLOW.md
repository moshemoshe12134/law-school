# POST-CLASS WORKFLOW [EXAM-FIRST EDITION]

**Updated:** 2026-01-24 (Exam-first strategy implemented)  
**Purpose:** Extract exam-ready material from transcripts, not summarize class events.

**See also:** `ACTIVE/CrimLaw/00_ADMIN/EXAM_FIRST_CLASS_PREP_STRATEGY.md` for full philosophy

---

## Overview

**Philosophy change:**
- **Old:** Comprehensive transcript summary comparing to prep
- **New:** Extract ONLY what Harcourt would reward on exam

**The review is exam prep extraction, not a class diary.**

**Three phases:**

| Phase | Name | Time | Output |
|-------|------|------|--------|
| **Phase 1** | Ingest | 2-3 min | Registered transcript in REVIEW_INDEX |
| **Phase 2** | **Review** | **25-40 min** | **Exam-ready extractions** |
| **Phase 3** | Integrate | 10-15 min | Updated outline + prewrite bank |

**Total time per class:** 35-55 min (up from old 30-45 min)  
**Why increase:** This IS your exam prep. 90% of effort now goes here, not pre-class.

---

## 🎯 COURSE-SPECIFIC REVIEW FORMATS

### Standard Format (CrimLaw, Property, Torts, etc.)
- **Purpose:** Extract exam-ready material
- **Method:** Focus on professor's emphasis, create prewrite fragments
- **Structure:** 7-section format (see Phase 2 below)

### 📋 DEALS-SPECIFIC FORMAT (Exception)

**Why different:** Deals prep documents are rigorous Q&A formats that track literal class steps. The prep is already exam-focused.

**Deals Review Method:**

1. **Primary task:** Compare prep to transcript, note differences
2. **Structure:** Review should RESEMBLE the prep doc (follow its Q&A structure)
3. **Focus:** Highlight what was/wasn't covered and any additions/changes
4. **Output format:**

```markdown
## PREP vs. TRANSCRIPT COMPARISON

### Coverage Overview
- ✅ Covered in Class (matches prep)
- ⏸️ Partially Covered
- ❌ Not Covered in Class

### Additional Content in Class (Not in Prep)
[Material professor added beyond prep questions]

### [Question 1 from Prep]
#### Class Discussion Alignment
- ✅ CLOSELY FOLLOWED PREP / ⚠️ DIFFERENCES NOTED
- [Key points from class matching prep]
- [Differences/additions/emphasis changes]

[Continue for each prep question...]

### Key Concepts (From Prep - Reinforced in Class)
### Exam Signals
### Professor's Magic Phrases
### Doctrinal Insights
```

**Deals Review is primarily a fidelity check:** Did class follow prep? What changed? What was emphasized?

**Why this works for Deals:** The prep already contains the exam-ready analysis. The review validates/adjusts it based on what professor actually emphasized.

---

## Phase 1: Ingest (2-3 min)

**Command:** `ingest transcripts [COURSE]`

**Purpose:** Scan for new transcripts, match to classes, register in tracking.

### Steps

1. **Scan transcript folder:** `ACTIVE/{Course}/03_TRANSCRIPTS/raw/`
2. **Extract date from filename:** Support various patterns (MM-DD, YYYY-MM-DD, etc.)
3. **Match to MASTER_LOG:** Find class number + title
4. **Update REVIEW_INDEX:** Add to "Pending Queue" with status `pending`
5. **Keep original filenames:** Don't rename Echo360 downloads

---

## Phase 2: Review — THE CRITICAL PHASE (25-40 min)

**Command:** `review [COURSE]` or `review [COURSE] class [NN]`

**Purpose:** Extract exam-ready material. This replaces "study time."

### 🚨 ABSOLUTE ACCURACY REQUIREMENTS

**The review is the foundation of your exam prep. Zero tolerance for hallucination.**


#### Rule 1: STICK TO WHAT PROFESSOR ACTUALLY SAID
- Read transcript line by line
- Summarize what professor + class discussion covered
- NOTHING MORE, NOTHING LESS

#### Rule 2: NEVER attribute to professor unless transcript shows it
- NO "professor flagged", "professor emphasized", "Harcourt noted" unless explicitly in transcript
- No invented quotes or paraphrasing as direct statement

#### Rule 3: Separate your inferences from lecture content
- Your reasoning → "Doctrinal Insight" section (clearly marked)
- Professor's words → "What Happened" sections
- Label inferences: "Based on reading" or "Doctrinal implication"

#### Rule 4: Source every claim
- Transcript quote → cite line/paragraph
- Casebook → cite pages ("KSSB10 p. 231")
- MPC → cite statute ("MPC §2.01(2)(d)")
- Your inference → label as such

#### Rule 5: Flag gaps honestly
- Unclear → `[TRANSCRIPT_UNCLEAR]`
- From reading → `[FROM READING, not lecture]`
- Synthesis → `[SYNTHESIS based on X + Y]`

#### Rule 6: Quote-heavy, but not quote-confusing
**Goal:** Study the professor (language + framing) without letting quotes drown the concept.
- For each major point: write a **1–2 line “core concept”** first, then add **1–2 short quotes** that are actually useful on an exam.
- Keep quotes short and “wieldable” (aim for ≤ 1–2 sentences).
- Every quote should have:
  - a transcript pointer (line/paragraph), and
  - a one-line “**Use on exam when…**” note (so it’s not just a quote dump).

---

### New Review Document Structure (Exam-Focused)

**Output:** `04_REVIEWS/YYYY-MM-DD_classNN_review.md`

**Focus:** Extract exam-usable material, not summarize events

#### Required Sections

**1. STATUTE/RULE AS HARCOURT FRAMED IT**

```markdown
## 1. STATUTE/RULE AS HARCOURT FRAMED IT

[Copy EXACT language if he read statute aloud]

**How Harcourt parsed elements:**
- Conduct: [what he identified]
- Attendant circumstances: [what he identified]
- Result: [what he identified]

**Key phrases from lecture:**
- [Direct quotes from transcript showing his framing]
- (Prefer 1–2 “wieldable” quotes; add a “Use on exam when…” note)
```

**2. ARGUMENTS HARCOURT PUSHED**

```markdown
## 2. ARGUMENTS HARCOURT ENDORSED (BOTH SIDES)

**Core principle:** For ANY fact pattern, develop PROSECUTOR and DEFENSE arguments. The exam requires arguing both sides credibly.

### Prosecution Arguments
1. [Specific argument]
   - **Status:** ✅ Explicitly endorsed / ⚡ Tacitly approved / ❌ Dismissed
   - **Transcript evidence:** [Quote/line reference]
   - **When he validated it:** [e.g., "That's a good argument," spent 10+ min developing, used in multiple hypos]
   - **Doctrine/cite:** [MPC section, case name]
   - **Use on exam when:** [Brief trigger note]

2. [Another argument]
   - **Status:** ✅ / ⚡ / ❌
   - [Same structure]

### Defense Arguments  
1. [Specific argument]
   - **Status:** ✅ Explicitly endorsed / ⚡ Tacitly approved / ❌ Dismissed
   - **Transcript evidence:** [Quote/line reference]
   - **When he validated it:** [e.g., "That's exactly right," engaged seriously, returned to multiple times]
   - **Doctrine/cite:** [MPC section, case name]
   - **Use on exam when:** [Brief trigger note]

2. [Another argument]
   - **Status:** ✅ / ⚡ / ❌
   - [Same structure]

### Harcourt's Resolution (if any)
[Did he signal which side prevails? Say "this is a close case"?]
[Quote transcript directly - line reference]

### Argument Pairs for Exam Bank
**Issue:** [e.g., "Agency vs. Proximate Cause in Felony Murder"]
- **Prosecution:** [1-sentence version of strongest argument]
- **Defense:** [1-sentence version of strongest counter-argument]
- **Note:** [Both arguments are "valid" per Harcourt - exam requires deploying both]
```

**3. EXAM SIGNALS**

```markdown
## 3. EXAM SIGNALS

### Explicit signals
- [Direct quote]: "This is important because..."
- [Direct quote]: Reference to past exam

### Implicit signals
- [Topic] got [X] minutes of class time
- [Issue] had 3+ hypos constructed
- Energy/voice shift when discussing [topic]

**Tag:** #EXAM_SIGNAL for each
```

**4. MAGIC WORDS / QUOTE BANK (for exam answers)**

```markdown
## 4. MAGIC WORDS / QUOTE BANK

[Copy Harcourt's exact formulations that would sound good on exam]
[Each bullet should include a transcript pointer + “Use on exam when…”]

- "The real issue is..."
- "Consciously disregarding a substantial and unjustifiable risk"
- "There's no need to spend time on [X]"
- [Other precise language]
```

**5. PREWRITE FRAGMENTS (CRITICAL OUTPUT)**

```markdown
## 5. PREWRITE FRAGMENTS

**Purpose:** Draft exam-ready paragraphs using BOTH prosecution and defense arguments from class

### Issue-Spotter Paragraph (Prosecution → Defense)

**Issue:** [e.g., "Agency vs. Proximate Cause"]

**Prosecution argument:**
[1-2 sentences using Harcourt's language and arguments he endorsed]
[Include relevant cite/doctrine]

**Defense argument:**  
[1-2 sentences using Harcourt's language and arguments he endorsed]
[Include relevant cite/doctrine]

**Example structure:**
"The prosecution will argue [X] under the proximate cause theory, citing [case/MPC]. However, the defense will counter that under the agency theory adopted in *Canola*, [Y]. As the court noted, 'most modern progressive thought favors restriction rather than expansion of the felony-murder rule.'"

### Policy Connection (if applicable)

[1 paragraph connecting doctrine to Harcourt's themes]
[Power, race, incarceration, Foucault, Kelman]
[Only include if Harcourt explicitly made this connection in class]
```

**6. OUTLINE INSERTS (ready to paste)**

```markdown
## 6. OUTLINE INSERTS

**Rule:** [Professor's formulation, with citation]

**Elements:** [As professor broke them down]

**Case:** *[Name]* — [Holding in professor's words from transcript]

**Distinctions:** [How professor distinguished from other cases]
```

**7. CORRECTIONS TO PREP**

```markdown
## 7. CORRECTIONS TO PREP

**What prep missed:**
- [Topic professor spent 15+ min on that wasn't in prep]

**What prep over-emphasized:**
- [Topic prep focused on but professor skipped]

**Better framing for next time:**
- [How to adjust future preps based on this class]
```

---

### Inputs Required

| Input | Location | Purpose |
|-------|----------|---------|
| Transcript | `03_TRANSCRIPTS/raw/*.txt` | Primary source |
| Text Prep | `02_PREP/text/YYYY-MM-DD_classNN_text.md` | Comparison baseline |
| Past Outlines INDEX | `01_SOURCES/past_outlines/INDEX.md` | Standard doctrine check |

---

### Process (Step-by-Step)

**Step 1:** Read transcript start to finish (10 min)
- Mark sections where Harcourt emphasized something
- Mark where he constructed hypos
- Mark where students made arguments he rewarded

**Step 2:** Extract statute/rule framing (3 min)
- Copy exact language if he read statute
- Note how he parsed elements

**Step 3:** Extract arguments (5 min)
- List prosecution arguments that got traction
- List defense arguments that got traction
- Note Harcourt's resolution/assessment

**Step 4:** Identify exam signals (3 min)
- Flag explicit references to exams/importance
- Note time allocation (topics with 15+ min)
- Note multiple hypos on same issue

**Step 5:** Collect magic words (2 min)
- Copy Harcourt's precise formulations
- Flag phrases that match model answer language
- Add “Use on exam when…” to each so you remember how to deploy it

**Step 6:** Draft prewrite fragment (8-12 min)
- Write 1 paragraph issue-spotter using today's doctrine
- Include both prosecution and defense arguments from class
- Use Harcourt's exact framing/language

**Step 7:** Create outline inserts (3 min)
- Format as copy-paste ready blocks
- Include rule, elements, cases, distinctions

**Step 8:** Note prep corrections (2 min)
- What to adjust for future preps

---

### QC Checks

**Accuracy:**
- [ ] No professor attributions without transcript evidence
- [ ] Direct quotes marked as quotes
- [ ] Inferences clearly labeled as such
- [ ] Sources cited for all claims

**Completeness:**
- [ ] All 7 sections present
- [ ] At least 1 prewrite fragment (THE critical output)
- [ ] At least 1 outline insert (or note "no changes")
- [ ] Exam signals tagged

**Usability:**
- [ ] Prewrite fragment is exam-ready (could paste into answer)
- [ ] Outline inserts are formatted for direct paste
- [ ] Quote bank is exact quotes from professor
- [ ] Quotes don’t overwhelm: each major point has a short “core concept” first

---
## Phase 3: Integrate (10-15 min)

**Command:** `integrate review [COURSE] class [NN]`

**Purpose:** Push review extractions into permanent exam prep.

### Step 3.1: Update Outline

**Location:** `05_OUTLINE/[relevant sections]`

1. Paste outline inserts from review
2. Add exam signal tags
3. Integrate Harcourt's language

### Step 3.2: Add to Prewrite Bank

**Location:** `06_PREWRITES/PREWRITES_BANK.md`

1. Take prewrite fragment from review
2. Polish if needed (but keep Harcourt's framing)
3. Add to prewrite bank with trigger conditions

**Format:**

```markdown
## [Doctrine Name] — Issue-Spotter Prewrite

**Source:** Class [NN] (YYYY-MM-DD)

**Trigger:** [When to use this on exam]

**Prewrite paragraph:**
[The polished paragraph from review, ready to paste into exam answer]

**Magic words to include:**
- [Key phrases from Harcourt]
```

### Step 3.3: Update Tracking

**REVIEW_INDEX.md:**
- Move from "Pending" to "Completed"
- Status: `review_done` → `integrated`
- Record sources/prewrites counts

**MASTER_LOG.md:**
- Mark `Review?` as ✅
- Mark `Outline?` as ✅
- Update `Signals` count
- Update `Next Action`

---

## Weekly Synthesis (NEW — 60 min on Sundays)

**Purpose:** Polish prewrite fragments into exam-ready paragraphs

### Tasks

1. **Review week's prewrite fragments** (15 min)
   - Read all fragments from that week's reviews
   - Identify which can be combined
   - Note gaps in coverage

2. **Polish into full prewrites** (30 min)
   - Take 3-5 fragments
   - Expand into complete IRAC paragraphs
   - Add prosecution + defense arguments
   - Use Harcourt's magic words throughout

3. **Outline consolidation** (15 min)
   - Check outline coherence
   - Merge related sections
   - Update SOURCES_TABLE

---

## Agent Instructions Summary

**For agents generating reviews:**

```
GOAL: Extract exam-ready material (NOT summarize class)

REQUIRED OUTPUTS:
1. Statute/Rule as Harcourt Framed It
2. Arguments Harcourt Pushed (prosecution + defense)
3. Exam Signals (explicit + implicit, tagged)
4. Magic Words / Phrases (exact quotes)
5. Prewrite Fragments (THE CRITICAL OUTPUT - 1+ paragraphs)
6. Outline Inserts (copy-paste ready)
7. Corrections to Prep

ABSOLUTE ACCURACY:
- Only attribute to professor what transcript explicitly shows
- Quote directly, don't paraphrase as if quote
- Separate your inferences into "Doctrinal Insight" sections
- Source every claim
- Flag gaps honestly ([TRANSCRIPT_UNCLEAR], etc.)

PREWRITE FRAGMENT REQUIREMENTS:
- 1 paragraph minimum (issue-spotter format)
- Includes prosecution + defense arguments from class
- Uses Harcourt's exact language/framing
- Ready to paste into exam answer
- If Harcourt did policy discussion, add policy paragraph too

TIME ALLOCATION:
- This is exam prep, not class summary
- 80% of effort on prewrite fragments + outline inserts
- 20% on documenting what happened
```

---

## Anti-Patterns to Avoid

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Summarize what happened in class | Extract exam-usable material |
| Write diary of class events | Write prewrite paragraphs |
| Compare extensively to prep | Note major deltas only |
| Process without extracting prewrites | ALWAYS create at least 1 prewrite fragment |
| Focus on "coverage" | Focus on what Harcourt emphasized |
| Delay review | Do same day while fresh |

---

## Time Allocation Guide

**For a typical 75-minute class:**

| Activity | Time | % of Review Effort |
|----------|------|-------------------|
| Read transcript | 10 min | 15% |
| Extract statute/arguments | 8 min | 12% |
| Draft prewrite fragment | 12 min | 35% (MOST IMPORTANT) |
| Create outline inserts | 5 min | 15% |
| Collect exam signals/magic words | 5 min | 12% |
| Note corrections | 3 min | 7% |
| **Total Phase 2** | **40-45 min** | **100%** |

---

*Last Updated: 2026-01-24 (Exam-first edition)*
