---
doc_type: review_doc
class_number: null
date: null # YYYY-MM-DD
title: null
status: draft # draft|review_done|integrated|final
inputs:
  text_prep: null # 02_PREP/text/YYYY-MM-DD_classNN_text.md
  transcript_raw: null # 03_TRANSCRIPTS/raw/{CourseName}-transcript-MM-DD.txt
  assignment: null # 01_SOURCES/syllabus/assignments/YYYY-MM-DD_classNN.md
outputs:
  outline_sections: [] # Outline sections updated
  prewrites_created: [] # List of prewrites created
metrics:
  time_spent_minutes: null
  signal_count: 0 # Number of #EXAM_SIGNAL items
  prewrite_count: 0 # Prewrite fragments created
---

# Review — Class #{class_number} — {date} — {title}

**Purpose:** Extract exam-ready material (NOT summarize class)  
**Target time:** 25-40 minutes  
**Critical output:** PREWRITE FRAGMENTS (Section 5)

---

## 1. STATUTE/RULE AS HARCOURT FRAMED IT

**Harcourt's formulation:**

> [Quote professor's exact language for the rule/statute]
>
> Key language: "[Critical phrases]"

**Elements (as Harcourt numbered them):**
1. [Element 1 as prof described]
2. [Element 2 as prof described]
3. [Element 3 as prof described]

**Harcourt's textual moves:**
- [How prof parsed the language]
- [Where prof pointed to specific words]
- [Definitions prof emphasized]

---

## 2. ARGUMENTS HARCOURT PUSHED

**Prosecution arguments class discussed:**

**Arg 1: [Label]**
- [What the argument is]
- [Why it works according to class]
- Quote: "[Direct quote if Harcourt used specific language]"

**Arg 2: [Label]**
- [What the argument is]
- [Why it works]

**Defense arguments class discussed:**

**Arg 1: [Label]**
- [What the counterargument is]
- [Why it works]
- Quote: "[Direct quote if Harcourt used specific language]"

**Arg 2: [Label]**
- [What the counterargument is]
- [Why it works]

**"Fish/frog" moments (both sides equally compelling):**
- [Moment when Harcourt showed both sides are strong]

---

## 3. EXAM SIGNALS

**Explicit signals:**
- "[Direct quote of professor flagging exam importance]" #EXAM_SIGNAL
- "[Quote about past exams or 'this comes up a lot']" #EXAM_SIGNAL

**Implicit signals:**
- Repeated hypotheticals on: [Topic] #EXAM_SIGNAL
- Pressed class multiple times on: [Distinction] #EXAM_SIGNAL
- Connected to §3.09 / signature issue: [How] #EXAM_SIGNAL

**Connection to past exams:**
- [Which past exam question(s) this connects to]

---

## 4. MAGIC WORDS / PHRASES

**Harcourt's exact language (use on exam):**

- "[Magic phrase 1]" — when discussing [topic]
- "[Magic phrase 2]" — when discussing [topic]
- "The real issue is..." — [Complete the sentence as Harcourt did]

**Time-framing language:**
- [How Harcourt characterized narrow vs. broad framing]

**Policy framing:**
- [Key policy language Harcourt used]

---

## 5. PREWRITE FRAGMENTS ⭐ (CRITICAL OUTPUT)

**Purpose:** Draft exam paragraphs using today's class discussion.

### Fragment 1: [Topic/Doctrine]

**Trigger:** [When to use this on exam — e.g., "Issue-spotter fact pattern with voluntariness question"]

**Prewrite paragraph (issue-spotter format):**

> [Write a 4-6 sentence paragraph using Harcourt's framing and class arguments. Include prosecution + defense arguments. Use magic words. Make this ready to paste into an exam answer.]
>
> Example structure:
> - Issue sentence
> - Rule sentence (using Harcourt's formulation)
> - Prosecution argument from class
> - Defense counterargument from class
> - Conclusion / tension

**Magic words included:**
- [List the specific phrases from Harcourt used in this paragraph]

**Source:** Class [NN] discussion of [Case/Topic]

---

### Fragment 2: [Topic/Doctrine] (if applicable)

**Trigger:** [When to use]

**Prewrite paragraph:**

> [Another exam-ready paragraph]

---

### Policy Fragment (if discussed)

**Trigger:** [When policy question arises]

**Policy paragraph:**

> [1-2 paragraphs discussing policy tension using Harcourt's framing]

---

## 6. OUTLINE INSERTS (copy-paste ready)

**Insert location:** `05_OUTLINE/[section name]/`

```markdown
### [Doctrine Name]

**Rule:** [Harcourt's formulation]
- Element 1: [Description from class]
- Element 2: [Description from class]

**Case:** *[Name]* — [Holding in Harcourt's words]

**Hypo from class:** [Harcourt's example]

**Prosecution argues:** [Argument from class]
**Defense responds:** [Argument from class]

**Policy tension:** [As Harcourt described]

#EXAM_SIGNAL [if applicable]
```

---

## 7. CORRECTIONS TO PREP

**What prep got wrong / what class clarified:**

| My Prep Said | Harcourt Actually Said | Correction |
|--------------|------------------------|------------|
| [My prediction] | [What actually happened] | [How to fix outline] |

**Major deltas (big differences from prep):**
- [Delta 1]
- [Delta 2]

**Lessons for future prep:**
- [Adjustment 1]
- [Adjustment 2]

---

## TRACKING & QC

**Prewrite fragments created:** {metrics.prewrite_count}  
**Exam signals found:** {metrics.signal_count}  
**Time spent:** {metrics.time_spent_minutes} minutes

**QC Checklist:**
- [ ] At least 1 prewrite fragment created (THE CRITICAL OUTPUT)
- [ ] All arguments use Harcourt's exact language/framing
- [ ] Magic words/phrases documented
- [ ] Exam signals tagged with #EXAM_SIGNAL
- [ ] Outline inserts are copy-paste ready
- [ ] Only attributed to professor what transcript explicitly shows
- [ ] No invented quotes or paraphrasing as if direct statement

**Next steps:**
- [ ] Add prewrite fragments to `06_PREWRITES/PREWRITES_BANK.md`
- [ ] Paste outline inserts into `05_OUTLINE/`
- [ ] Update REVIEW_INDEX.md status
- [ ] Update MASTER_LOG.md

---

## ABSOLUTE ACCURACY RULES

🚨 **The review is the most critical document. It CANNOT tolerate hallucination.**

**STICK TO WHAT PROFESSOR ACTUALLY SAID:**
- Go line by line through transcript
- Summarize what professor said and what class discussed
- NOTHING MORE, NOTHING LESS

**NEVER attribute to professor unless explicitly in transcript:**
- NO "professor flagged" unless transcript shows this
- NO "Harcourt emphasized" unless transcript shows this
- NO invented quotes or paraphrasing as if direct statement

**Separate inferences from lecture content:**
- Your inferences go in separate clearly-marked sections
- Label as "Doctrinal insight" or "Based on reading" (NOT "professor said")

**Source every claim:**
- Transcript quote → cite to transcript
- Casebook content → cite to reading
- MPC text → cite to statute
- Your inference → label clearly

**Flag gaps honestly:**
- `[TRANSCRIPT_UNCLEAR]` if unclear
- `[FROM READING, not lecture]` if inferring
- `[SYNTHESIS based on X + Y]` if synthesizing

---

*Last Updated: 2026-01-24 (Exam-first edition)*
