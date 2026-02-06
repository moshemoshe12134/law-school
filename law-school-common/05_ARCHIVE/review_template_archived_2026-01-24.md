# ARCHIVED: Old Review Template

**Archived:** 2026-01-24  
**Reason:** Replaced with exam-first extraction format (7-section structure emphasizing prewrite fragments)

**See:** New version at `law-school-common/03_TEMPLATES/review_template.md`

---

---
doc_type: review_doc
class_number: null
date: null # YYYY-MM-DD
title: null
status: draft # draft|review_done|integrated|final
inputs:
  text_prep: null # 02_PREP/text/YYYY-MM-DD_classNN_text.md
  transcript_raw: null # 03_TRANSCRIPTS/raw/{CourseName}-transcript-MM-DD.txt
  transcript_processed: null # 03_TRANSCRIPTS/processed/YYYY-MM-DD_classNN_clean.md
  assignment: null # 01_SOURCES/syllabus/assignments/YYYY-MM-DD_classNN.md
outputs:
  outline_sections: [] # Outline sections updated
  sources_added: 0 # Count of sources added to SOURCES_TABLE
  prewrites_created: [] # List of prewrites created
metrics:
  prediction_accuracy: null # 0|1|2 (missed/partial/accurate)
  time_spent_minutes: null
  signal_count: 0 # Number of #EXAM_SIGNAL items
  sources_count: 0 # Cases + statutes + readings extracted
  prewrite_count: 0 # Prewrite opportunities identified
transcript_qc:
  status: verified # verified|issues_found|major_problems
  errors_flagged: 0
---

# Review — Class #{class_number} — {date} — {title}

---

## 1. What Professor Emphasized (3-5 main points)

1. [Main point 1] #EXAM_SIGNAL
2. [Main point 2]
3. [Main point 3]
4. [Main point 4]
5. [Main point 5]

---

## 2. Exam Signals #EXAM_SIGNAL

**Explicit signals:**
- [ ] "[Quote from professor]" - [Topic]
- [ ] Repeated hypo pattern: [Description]
- [ ] Connected to past exam: [Which exam/question]

**Implicit signals:**
- [ ] [Topic] emphasized with multiple hypos #EXAM_SIGNAL
- [ ] [Distinction] tested repeatedly #EXAM_SIGNAL
- [ ] Policy focus on [theme] #EXAM_SIGNAL

---

## 3. Corrections to Prep

**My prep said:** [Rule/interpretation from prep]
**Prof clarified:** [Actual rule/interpretation]
**Fix:** [Corrected language for outline]

**My prediction:** [What I thought prof would emphasize]
**Actually emphasized:** [What prof actually focused on]
**Lesson:** [How to adjust future prep]

---

## 4. Doctrinal Insights

**New understanding:**
- [Insight 1 about rule application]
- [Insight 2 about element interpretation]

**Statutory/professor moves:**
- Textual moves: [How prof parsed language]
- Element attachment: [How prof connected elements]
- Definition emphasis: [Terms prof defined]

---

## 5. Policy Arguments

**Strong arguments prof rewarded:**
- [Argument 1]: [Why prof liked it]
- [Argument 2]: [Why prof liked it]

**Strong critiques prof anticipated:**
- [Critique 1]: [How prof framed it]
- [Critique 2]: [How prof framed it]

**Exam-ready policy paragraphs:**
- [Theme 1]: [Paragraph starter with thesis]
- [Theme 2]: [Paragraph starter with thesis]

---

## 6. Outline Inserts (copy-ready)

> Paste-ready blocks to add into `05_OUTLINE/` without rewriting.

### Insert: [Topic/Section]

```markdown
[Clean, concise rule/example/hypo]
- Element: [Description]
- Case: [Name] - [Holding]
- Hypo: [Prof's example]
- Policy: [Key tension]
```

### Insert: [Another Section]

```markdown
[Content block]
```

---

## 7. Source Extraction (for SOURCES_TABLE)

> All sources mentioned in this class. Check box when added to `05_OUTLINE/SOURCES_TABLE.md`.

### Cases

| ☐ | Case Name | Rule/Holding | Exam Point | New/Update |
|---|-----------|--------------|------------|------------|
| ☐ | *[Case 1]* | [Holding] | [Why it matters] | New |
| ☐ | *[Case 2]* | [Holding] | [Why it matters] | Update |

### Statutes/Rules

| ☐ | Citation | Key Provision | Prof's Interpretation |
|---|----------|---------------|----------------------|
| ☐ | [Statute] | [Provision] | [How prof parsed it] |

### Readings/Scholars

| ☐ | Source | Main Point | Prof's Use |
|---|--------|------------|-----------|
| ☐ | [Reading/Scholar] | [Point] | [How prof used it] |

---

## 8. Prewrite Opportunities

> Potential exam questions arising from this lecture. Flag for `06_PREWRITES/`.

### Doctrinal Prewrites Identified

| ☐ | Doctrine | Question Type | Prof's Framework | Priority |
|---|----------|---------------|-----------------|----------|
| ☐ | [Doctrine 1] | Issue-spotter | [Framework] | High |
| ☐ | [Doctrine 2] | Application | [Framework] | Medium |

### Policy Prewrites Identified

| ☐ | Topic | Question Type | Prof's Angle | Priority |
|---|-------|---------------|-------------|----------|
| ☐ | [Topic 1] | Policy essay | [Prof's view] | High |

### Prewrite Fragment (if ready to extract now)

**Doctrine:** [Name]
**Trigger:** [When to invoke this analysis]
**IRAC Starter:**
> [Issue] Whether [party] can [claim/defense] under [doctrine].
> [Rule] Under [source], [doctrine] requires: (1) [element]...
> [Application template]

---

## 9. Transcript QC

> Flag any transcript accuracy issues for correction.

**Verification status:** ✅ Verified / ⚠️ Issues Found / ❌ Major Problems

### Errors Detected

| Flag | Section | Issue | Suggested Correction |
|------|---------|-------|---------------------|
| #TRANSCRIPT_VERIFY | [Location] | [What's wrong] | [Correction] |
| #UNCLEAR_AUDIO | [Location] | [Garbled text] | [Best guess] |
| #MISSING_CONTENT | [Topic] | Expected but not found | [Check recording] |

**Common legal term corrections applied:**
- [Mishearing] → [Correction]

---

## 10. Spaced Reinforcement (10–15 minutes later)

**Self-quiz prompts (closed-book):**

1. [Prompt testing key concept]
2. [Prompt about case holding]
3. [Prompt about policy tension]
4. [Prompt about element application]
5. [Prompt about distinction]

---

## METRICS

**Prediction accuracy:** {metrics.prediction_accuracy} (0=missed, 1=partial, 2=accurate)
**Time spent:** {metrics.time_spent_minutes} minutes
**Exam signals found:** {metrics.signal_count}
**Sources extracted:** {metrics.sources_count}
**Prewrite opportunities:** {metrics.prewrite_count}

**What to prep differently next time:**
- [Adjustment 1]
- [Adjustment 2]
