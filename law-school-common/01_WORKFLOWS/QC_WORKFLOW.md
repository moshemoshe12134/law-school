# QC WORKFLOW (Quality Control)

**Purpose:** Ensure all deliverables meet quality standards through iterative review.

---

## Overview

**Core principle:** QC happens by editing documents in place, not creating separate QC docs.

**Process:**
1. Generate document using template
2. Self-review against checklist
3. Edit in place to fix issues
4. Track iterations in MASTER_LOG
5. Mark as complete when exam-ready

---

## QC Iteration System

**Iteration counter:** `0` → `1` → `2` → `✓`

- **0** = Not yet reviewed (initial draft)
- **1** = First QC pass complete
- **2+** = Additional QC passes (as needed)
- **✓** = Final/passed (exam-ready)

**Tracking locations:**
- **MASTER_LOG columns:** `Prep_QC`, `Review_QC`, `Outline_QC`
- **Document frontmatter:** `qc_iteration: [0|1|2|✓]`
- **MASTER_LOG Notes:** Brief QC findings

---

## Document QC Workflows

### Audio Prep QC

**Trigger:** After generating audio prep

**Checklist:** Use `03_TEMPLATES/qc_checklist_template.md`

**Steps:**
1. **Review against checklist** (5 min)
   - Structure (INTRO, COLD CALL PREP, CLOSING)
   - Formatting (TTS-friendly, short paragraphs)
   - Content (learning objectives, cold-call prep)
   - Length (4,000-5,000 words)

2. **Edit in place** (5-10 min)
   - Fix any issues found
   - Improve conversational tone
   - Add transitions if missing

3. **Update tracking**
   - Mark `Prep_QC` as `1` in MASTER_LOG
   - Set `status: final` in frontmatter

---

### Text Prep QC

**Trigger:** After generating text prep

**Checklist:** Use `03_TEMPLATES/qc_checklist_template.md`

**Steps:**
1. **Review against checklist** (10 min)
   - Structure (all required sections)
   - Content (rule statements, case briefs, hypos)
   - Formatting (searchable, organized)
   - Completeness (all assignments covered)

2. **Edit in place** (10-15 min)
   - Fix rule statements
   - Complete incomplete sections
   - Add missing case briefs
   - Verify citations

3. **Update tracking**
   - Mark `Prep_QC` as `1` in MASTER_LOG
   - Set `status: final` in frontmatter

---

### Review Document QC

**Trigger:** After creating review document

**Checklist:** Use `03_TEMPLATES/qc_checklist_template.md`

**Steps:**
1. **Review against checklist** (10 min)
   - Structure (all required sections)
   - Content (exam signals, corrections, outline inserts)
   - Completeness (at least one delta, one insert)

2. **Edit in place** (5-10 min)
   - Add missing exam signals
   - Refine outline inserts
   - Complete incomplete sections

3. **Update tracking**
   - Mark `Review_QC` as `1` in MASTER_LOG
   - Set `status: final` in frontmatter

---

### Outline Section QC

**Trigger:** After updating outline section

**Checklist:** Use `03_TEMPLATES/qc_checklist_template.md`

**Steps:**
1. **Review against checklist** (10 min)
   - Structure (black letter law, elements, cases)
   - Content (accurate, integrated professor signals)
   - Length (10-20 pages, not 150)
   - Coherence (no redundancy/drift)

2. **Edit in place** (10-15 min)
   - Fix inaccurate rules
   - Integrate professor's emphasis
   - Remove redundancy
   - Add cross-references

3. **Update tracking**
   - Mark `Outline_QC` as `1` in MASTER_LOG
   - Note in outline frontmatter if needed

---

### Prewrite QC

**Trigger:** After creating or updating prewrite

**Checklist:** Use `03_TEMPLATES/qc_checklist_template.md`

**Steps:**
1. **Review against checklist** (10 min)
   - Structure (IRAC, triggers, framework, examples)
   - Content (accurate rule, complete elements)
   - Usability (copy-paste ready)

2. **Edit in place** (10-15 min)
   - Fix rule statement
   - Refine application framework
   - Add more examples if needed

3. **Update tracking**
   - Note in MASTER_LOG if doctrinal/policy prewrite exists
   - Set `qc_iteration: [1|2|✓]` in frontmatter

---

## Common QC Issues and Fixes

### Audio Prep Issues

**Issue:** Too formal/academic
**Fix:** Rewrite in conversational tone - "Here's the thing..." not "The doctrine requires..."

**Issue:** Too long
**Fix:** Cut dense doctrine - save for text prep - focus on central question + cold calls

**Issue:** Missing cold-call prep
**Fix:** Add 3-4 specific questions professor might ask with answer starters

---

### Text Prep Issues

**Issue:** Incomplete rule statements
**Fix:** Use `03_TEMPLATES/text_prep_template.md` - ensure all elements numbered and defined

**Issue:** Case briefs inconsistent
**Fix:** Apply standard format from `WRITING_FOUNDATIONS.md` - Rule of Law, Facts, Issue, Holding

**Issue:** No hypos or too few
**Fix:** Add 5+ hypos with both-side arguments - use variations from class

---

### Review Document Issues

**Issue:** No exam signals tagged
**Fix:** Add `#EXAM_SIGNAL` tags throughout - note explicit and implicit signals

**Issue:** Missing outline inserts
**Fix:** Create copy-paste ready blocks for rules/cases/examples from class

**Issue:** No corrections from prep
**Fix:** Compare prep to what professor actually said - note deltas

---

### Outline Issues

**Issue:** Too long (150+ pages)
**Fix:** Split into modular sections (10-20 pages each) - see `FOLDER_STRUCTURE_SPEC.md`

**Issue:** Redundancy/drift
**Fix:** Remove duplicate content - ensure each section has unique purpose

**Issue:** Professor's emphasis not integrated
**Fix:** Add review inserts with professor's language and formulations

---

### Prewrite Issues

**Issue:** Rule statement incomplete
**Fix:** Use review content + text prep - ensure all elements included

**Issue:** Application framework unclear
**Fix:** Create fill-in-the-blank structure - "Here, [FACTS]..."

**Issue:** Not tested on examples
**Fix:** Add 2-3 worked examples showing variations (strong vs. weak facts)

---

## When to Mark as Complete (✓)

**Audio prep:**
- [ ] All checklist items pass
- [ ] Conversational tone throughout
- [ ] TTS-friendly formatting verified
- [ ] Word count in range (4,000-5,000)

**Text prep:**
- [ ] All checklist items pass
- [ ] All cases briefed using standard format
- [ ] 5+ hypos with both-side arguments
- [ ] Searchable and organized

**Review document:**
- [ ] All checklist items pass
- [ ] At least one concrete delta
- [ ] At least one outline insert
- [ ] Exam signals tagged with `#EXAM_SIGNAL`

**Outline section:**
- [ ] All checklist items pass
- [ ] Length 10-20 pages (not 150)
- [ ] Professor's emphasis integrated
- [ ] No redundancy or drift

**Prewrite:**
- [ ] All checklist items pass
- [ ] Rule statement complete and accurate
- [ ] Tested on at least 2 examples
- [ ] Copy-paste ready

---

## QC Workflow Timing

| Document Type | First Pass | Edits | Total |
|---------------|------------|-------|-------|
| Audio prep | 5 min | 5-10 min | 10-15 min |
| Text prep | 10 min | 10-15 min | 20-25 min |
| Review doc | 10 min | 5-10 min | 15-20 min |
| Outline section | 10 min | 10-15 min | 20-25 min |
| Prewrite | 10 min | 10-15 min | 20-25 min |

---

## QC in Daily Workflow

### After Generating Document (Same Day)

1. **Generate** document using template
2. **Self-review** against checklist (5-10 min)
3. **Edit in place** to fix issues (5-15 min)
4. **Update tracking** (mark as QC: 1)

**Result:** Document is "first pass complete"

---

### Weekly Review (Sundays, 30 min)

**Review all documents from the week:**
- [ ] Check for consistent issues
- [ ] Identify patterns to improve
- [ ] Mark any documents needing second pass

**Update MASTER_LOG:**
- [ ] Note which documents got QC: 2
- [ ] Adjust generation process based on learnings

---

### Pre-Exam Review (Week 13-14)

**Final QC pass on key documents:**
- [ ] Outline sections (mark as ✓ when exam-ready)
- [ ] Prewrites (mark as ✓ when tested and working)
- [ ] Attack outline (mark as ✓ when complete)

**Result:** All exam materials are QC'd and ready

---

## QC Documentation

**Where to document QC findings:**

1. **MASTER_LOG Notes column**
   - Brief notes: "Missing cold-call prep, added 3 questions"
   - Patterns: "Consistently missing case names - improve source citation"

2. **Document frontmatter** (optional)
   - `qc_iteration: 1`
   - `qc_notes: "Fixed rule statement, added examples"`

3. **Weekly summary** (in MASTER_LOG)
   - Common issues found
   - Process improvements made
   - Documents needing second pass

---

## Templates and References

**Templates:**
- `03_TEMPLATES/qc_checklist_template.md` (comprehensive checklists)
- All document templates include QC sections

**References:**
- `02_STYLE_GUIDES/WRITING_FOUNDATIONS.md` (writing standards)
- `00_ADMIN/course_style_guide.md` (course-specific standards)

---

## Anti-Patterns to Avoid

❌ **Creating separate QC documents** → QC edits the original in place
❌ **Skipping QC to save time** → Leads to lower quality and rework later
❌ **QC without checklist** → Use `qc_checklist_template.md` for consistency
❌ **Marking as complete too early** → Only mark ✓ when truly exam-ready
❌ **QC immediately after generating** → Let it sit, then QC with fresh eyes if possible

---

*Last Updated: 2026-01-19*
