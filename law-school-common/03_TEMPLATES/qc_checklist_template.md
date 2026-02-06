# QC Checklist (Quality Control Standards)

**Purpose:** Defines what "done" means for all document types to ensure consistent quality without bespoke prompting.

---

## QC Process

**How QC works:**
1. QC happens by **editing the document in place** (not separate QC docs)
2. Track QC iterations in MASTER_LOG columns: `Prep_QC`, `Review_QC`, `Outline_QC`
3. QC findings go in MASTER_LOG Notes column OR in doc frontmatter
4. Iteration counter: `0` (unchecked) → `1` (first pass) → `2+` (additional passes) → `✓` (final/passed)

---

## Audio Prep QC (must-pass)

**File location:** `02_PREP/audio/YYYY-MM-DD_classNN_audio.md`

**Filename check:**
- [ ] Matches pattern: `YYYY-MM-DD_classNN_audio.md`

**Frontmatter check:**
- [ ] YAML frontmatter exists with: `doc_type`, `class_number`, `date`, `title`, `status`

**Structure check:**
- [ ] Contains `## INTRO` section
- [ ] Contains `## COLD CALL PREP` section
- [ ] Contains `## CLOSING` section
- [ ] Has at least one `## PART` section with time estimate

**Content check:**
- [ ] Intro includes learning objectives (3-5 bullets)
- [ ] Cold-call prep has 3-4 specific questions with answer starters
- [ ] Closing connects to next class
- [ ] Conversational tone throughout (not overly formal)

**Formatting check (TTS-friendly):**
- [ ] Short paragraphs (3-5 sentences max)
- [ ] No tables (TTS struggles)
- [ ] Minimal inline citations
- [ ] Section headers with time estimates
- [ ] Pronunciation guides for difficult terms

**Length check:**
- [ ] Word count in target range (4,000-5,000 words)
- [ ] Estimated audio length 25-30 minutes

**Quality check:**
- [ ] No dense doctrinal explanations (save for text prep)
- [ ] Stories and examples included
- [ ] Transitions between sections
- [ ] Professor's likely questions addressed

---

## Text Prep QC (must-pass)

**File location:** `02_PREP/text/YYYY-MM-DD_classNN_text.md`

**Filename check:**
- [ ] Matches pattern: `YYYY-MM-DD_classNN_text.md`

**Frontmatter check:**
- [ ] YAML frontmatter exists with: `doc_type`, `class_number`, `date`, `title`, `status`, `inputs.syllabus_assignment`

**Structure check:**
- [ ] Contains `## QUICK NAVIGATION`
- [ ] Contains `## BOOK NAVIGATION`
- [ ] Contains `## CORE DOCTRINE`
- [ ] Contains `## DEFINITIONS TO HAVE READY`
- [ ] Contains `## EXPECTED [PROFESSOR] QUESTIONS (Q→A)`
- [ ] Contains `## CASE BRIEFS`
- [ ] Contains `## POLICY / THEORY`
- [ ] Contains `## QUICK HYPOS` (5+ hypos)
- [ ] Contains `## SEARCH TERMS`
- [ ] Contains `## EXAM SIGNALS` (integrates past exam spec)
- [ ] Contains `## PROFESSOR'S SPECIAL PROMPTS` (if applicable)

**Content check:**
- [ ] Rule statements are complete and copy-ready
- [ ] Elements are numbered and defined
- [ ] Each case brief follows standard format (Rule of Law, Facts, Issue, Holding, Reasoning)
- [ ] Q&A format for expected questions
- [ ] At least 5 quick hypos with both-side arguments
- [ ] Policy section has thesis + arguments + exam-ready paragraphs

**Quality check:**
- [ ] Verbatim statutory text where applicable
- [ ] Case citations included
- [ ] Search terms listed for quick lookup
- [ ] Hypos include "most likely professor move"
- [ ] Cross-references to other classes where relevant

**Comprehensiveness:**
- [ ] All assigned cases briefed
- [ ] All statutes/provisions covered
- [ ] Policy tensions explained
- [ ] **Exam signals included** (past questions + common mistakes for this topic)
- [ ] **Professor's special prompts addressed** (visualization exercises, discussion questions, etc.)
- [ ] **Past outline integration** (how past students organized this — cited where relevant)
- [ ] Missing supplements explicitly flagged (no silent guessing)

---

## Review Doc QC (must-pass)

**File location:** `04_REVIEWS/YYYY-MM-DD_classNN_review.md`

**Filename check:**
- [ ] Matches pattern: `YYYY-MM-DD_classNN_review.md`

**Frontmatter check:**
- [ ] YAML frontmatter exists with: `doc_type`, `class_number`, `date`, `title`, `status`
- [ ] `inputs.text_prep` populated
- [ ] `inputs.transcript_raw` or `inputs.transcript_processed` populated
- [ ] `inputs.assignment` populated
- [ ] `metrics.prediction_accuracy` scored (0/1/2)
- [ ] `transcript_qc.status` set (verified/issues_found/major_problems)

**Structure check:**
- [ ] Contains `## 1. What Professor Emphasized` (3-5 main points)
- [ ] Contains `## 2. Exam Signals` with #EXAM_SIGNAL tags
- [ ] Contains `## 3. Corrections to Prep`
- [ ] Contains `## 4. Doctrinal Insights`
- [ ] Contains `## 5. Policy Arguments`
- [ ] Contains `## 6. Outline Inserts` (copy-ready blocks)
- [ ] Contains `## 7. Source Extraction` (cases, statutes, readings)
- [ ] Contains `## 8. Prewrite Opportunities` (doctrinal + policy)
- [ ] Contains `## 9. Transcript QC` (errors flagged)
- [ ] Contains `## 10. Spaced Reinforcement` section

**Content check:**
- [ ] At least one concrete "delta" (correction from prep)
- [ ] At least one outline insert (or explicit "no changes needed")
- [ ] Exam signals tagged with #EXAM_SIGNAL
- [ ] Prediction accuracy scored in frontmatter (0/1/2)
- [ ] Professor's emphasis captured in own words

**Source Extraction check:**
- [ ] All cases mentioned in class listed
- [ ] All statutes/rules mentioned listed
- [ ] All readings/scholars mentioned listed
- [ ] Each source has rule/holding summary
- [ ] Exam relevance noted for each source

**Prewrite Identification check:**
- [ ] Doctrinal prewrites identified (if any)
- [ ] Policy prewrites identified (if any)
- [ ] Question type specified (issue-spotter, policy essay, etc.)
- [ ] Professor's framework noted
- [ ] Priority assigned (High/Medium/Low)

**Transcript QC check:**
- [ ] Transcript verified against prep doc expectations
- [ ] Legal term mishearings flagged (e.g., "mens rea" → "men's area")
- [ ] Case name errors flagged
- [ ] `#TRANSCRIPT_VERIFY` tags used for content errors
- [ ] `#UNCLEAR_AUDIO` tags used for garbled sections
- [ ] `#MISSING_CONTENT` tags used for expected but missing topics

**Quality check:**
- [ ] Professor's exact phrasing when memorable included
- [ ] What prof rewards noted
- [ ] Outline inserts are copy-paste ready
- [ ] Spaced reinforcement prompts test key concepts
- [ ] Time spent recorded

**Exam signal check:**
- [ ] Explicit signals ("this is on the exam") captured
- [ ] Implicit signals (repeated patterns) captured
- [ ] Hypo patterns noted
- [ ] Policy emphasis captured

**Integration readiness check:**
- [ ] Source table entries ready to add
- [ ] Outline inserts ready to paste
- [ ] Prewrite fragments ready to extract

---

## Outline Section QC (must-pass)

**File location:** `05_OUTLINE/[topic_folder]/[doctrine].md`

**Filename check:**
- [ ] Descriptive name (e.g., `self_defense.md` not `outline.md`)

**Structure check:**
- [ ] Black letter law section (complete rule statement)
- [ ] Elements breakdown (numbered with definitions)
- [ ] Key cases section (holdings in one sentence each)
- [ ] Professor signals section (from reviews)
- [ ] Length 10-20 pages (not 150 pages)

**Content check:**
- [ ] Rule statement includes all elements
- [ ] Elements numbered consistently
- [ ] Case holdings are accurate
- [ ] Professor's emphasis from class integrated
- [ ] Cross-references to related doctrines

**Quality check:**
- [ ] No redundancy or drift
- [ ] AI coherence maintained (focused scope)
- [ ] Bold key terms for scanning
- [ ] Hierarchical headings
- [ ] Updated after each relevant class

**Integration check:**
- [ ] Review inserts incorporated
- [ ] Exam signals integrated
- [ ] Professor's formulations used
- [ ] Connected to prewrite where applicable

---

## Prewrite QC (must-pass)

**File location:** `06_PREWRITES/DOCTRINAL/[doctrine]_analysis.md` or `06_PREWRITES/POLICY/[topic].md`

**Filename check:**
- [ ] Descriptive name with `_analysis` suffix (doctrinal) or topic name (policy)

**Doctrinal prewrite structure check:**
- [ ] `## PREWRITE` section with copy-paste ready IRAC
- [ ] Issue statement is fill-in-the-blank ready
- [ ] Rule statement is complete with all elements
- [ ] Application has fill-in-the-blank structure
- [ ] Conclusion template provided
- [ ] `## TRIGGERS` section (when to use)
- [ ] `## FRAMEWORK` section (element-by-element breakdown)
- [ ] `## EXAMPLE APPLICATIONS` (2-3 worked examples)

**Policy prewrite structure check:**
- [ ] `## OVERVIEW` paragraph
- [ ] `## POSITIONS` section with at least 2 positions
- [ ] Each position has: Core Thesis, Key Arguments, Exam-Ready Paragraph
- [ ] `## SYNTHESES` if applicable (middle ground)
- [ ] `## COMPARATIVE ANALYSIS` table
- [ ] `## PROFESSOR'S ANGLE` section

**Quality check:**
- [ ] IRAC structure is correct (doctrinal)
- [ ] Rule statement is complete and accurate
- [ ] Application framework guides fact analysis
- [ ] Examples show variations (strong vs. weak facts)
- [ ] Triggers are specific (red flags)
- [ ] Exam-ready paragraphs are copy-paste ready

**Integration check:**
- [ ] References to review content where applicable
- [ ] Professor's emphasis incorporated
- [ ] Past exam appearances noted
- [ ] Policy connections made (doctrinal)

---

## QC Workflow

1. **Generate document** using appropriate template
2. **Self-Review** against checklist above
3. **Mark as `QC: 1`** in MASTER_LOG after first pass
4. **Edit in place** to fix issues found
5. **Mark as `QC: 2`** (or higher) for additional passes
6. **Mark as `QC: ✓`** when exam-ready

**Common issues to fix:**
- Missing sections → Add them
- Incomplete content → Fill gaps
- Poor formatting → Apply standards from WRITING_FOUNDATIONS.md
- Inaccurate rules → Correct based on class notes/reviews
- Missing exam signals → Add #EXAM_SIGNAL tags

**When to mark as `✓` (final/passed):**
- All checklist items pass
- Document has been through at least one QC pass
- Content is accurate and complete
- Formatting is consistent
- Document is exam-ready (could be used on exam today)

---

*Last Updated: 2026-01-19*
