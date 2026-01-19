# Structure Design Questions - Exploration Document

**Date:** Jan 19, 2026  
**Purpose:** Think through style guide strategy and folder structure redesign

---

## Question 1: Style Guide Architecture

### Current Problem
We have scattered style guidance:
- CrimLaw: Audio prep style + Class reference style (course-specific: MPC focus, policy-heavy)
- Deals: Prep sheet style (course-specific: transaction design, economic analysis)
- law-school-common: elements-of-style.md (universal writing principles)
- law-school-common: SKILL.md (AI guardrails for applying writing rules)

### User Insight
**Courses are different → prep docs should fit course styles**

Need bifurcation:
1. **Universal/Procedural Writing Guide** - How to write clearly (applies to all courses)
2. **Course-Specific Style Guides** - What matters for THIS course's substance

---

### Proposed Solution: Two-Layer Style System

#### Layer 1: Universal Writing Guide (law-school-common/)
**Location:** `law-school-common/02_STYLE_GUIDES/WRITING_FOUNDATIONS.md`

**Purpose:** Core writing principles that apply to ALL courses

**Contents:**
- Elements of Style principles (active voice, concrete language, omit needless words)
- SKILL.md guardrails (how AI should apply writing rules)
- Legal writing conventions (IRAC, paragraph structure, citation format)
- Tone and voice standards
- Formatting conventions (headings, lists, emphasis)

**This guide addresses:**
- ✅ "How do I write a clear sentence?"
- ✅ "How do I structure an argument?"
- ✅ "What tone should I use?"

**This guide does NOT address:**
- ❌ "What should I emphasize in this specific course?"
- ❌ "What does this professor care about?"

---

#### Layer 2: Course-Specific Style Guides (per course)
**Location:** `[Course]/00_ADMIN/course_style_guide.md`

**Purpose:** What matters for THIS course's substance and professor

**Contents:**
- Course priorities (e.g., CrimLaw = MPC syntax + policy; Deals = economic efficiency + deal structure)
- Professor emphasis (what they reward in answers)
- Doctrinal focus (cases vs. statutes vs. policy)
- Exam format implications (essay vs. short answer → affects prep style)
- Topic-specific conventions (e.g., how to handle MPC sections, how to cite Restatement)

**Example: CrimLaw Course Style Guide**
```markdown
# CrimLaw Course Style Guide (Harcourt)

## Course Priorities (Harcourt-Specific)

1. **MPC Close Reading** (50% of exam)
   - Always cite MPC section numbers (§ 2.02, § 3.04)
   - Parse statutory language carefully
   - Distinguish defined terms vs. common usage
   - Show how elements interact

2. **Policy/Theory** (50% of exam)
   - Expect policy questions on every exam
   - Connect doctrine to justification (why this rule?)
   - Critical theory matters (Foucault, racial justice, etc.)
   - Exam-ready policy paragraphs needed

3. **Cases as Vehicles** (Not Central)
   - Cases illustrate doctrine but aren't exam-central
   - Focus on holdings and reasoning, not facts
   - Use cases for hypo generation

## Prep Doc Priorities

### Audio Prep
- Lead with "the move" (what doctrinal/policy question is this class really about?)
- Frame MPC sections conversationally ("Section 2.02 breaks mens rea into four levels...")
- Include 5-10 likely Socratic questions with short answer starters

### Text Prep
- MPC sections: Full text + element breakdown + defined terms
- Policy: Thesis + arguments + counterarguments + Harcourt's likely angle
- Hypo bank: Prosecution/defense angles for each hypo

## Exam Answer Style

### Doctrinal Analysis
- Always start with MPC section cite
- Parse elements methodically
- Show statutory interpretation moves

### Policy Analysis
- Engage with critical theory (don't just regurgitate retribution/deterrence)
- Reference course themes (power, discretion, racial justice)
- Use Harcourt's vocabulary
```

**Example: Deals Course Style Guide**
```markdown
# Deals Course Style Guide

## Course Priorities

1. **Transaction Design** (Primary Focus)
   - How parties structure deals to solve problems
   - Allocation of risk and return
   - Incentive alignment

2. **Economic Analysis** (Lens for Everything)
   - Information asymmetry
   - Agency costs
   - Efficient breach
   - Transaction costs

3. **Minimal Case Law** (Not Doctrine-Heavy)
   - Focus on deal clauses, not judicial opinions
   - Understand common contractual solutions

## Prep Doc Priorities

### Style
- 12th grade reading level (clear, not overly academic)
- Conversational tone ("we" perspective)
- Define terms even if obvious
- Concrete examples for every concept

### Structure
- Start with key concepts overview
- Question-by-question analysis (match class structure)
- Bold answers to yes/no questions
- Bullet points for elaboration

### Content
- Connect every concept to real-world deal problems
- Show WHY parties care about this clause
- Economic rationale before legal doctrine
```

---

### How AI Uses Both Layers

**When generating prep doc:**
```markdown
AI prompt:
"Generate audio prep for CrimLaw Class 5 (Heat of Passion).

WRITING FOUNDATIONS: Follow law-school-common/02_STYLE_GUIDES/WRITING_FOUNDATIONS.md
- Use active voice, concrete language, omit needless words
- Clear paragraph structure, topic sentences
- SKILL.md guardrails apply

COURSE STYLE: Follow CrimLaw/00_ADMIN/course_style_guide.md
- Prioritize MPC § 210.3 close reading + policy (retribution vs. sympathy)
- Lead with 'the move' (what's really being tested here?)
- Include 5-10 Socratic Q&A starters
- Frame for TTS listening (conversational, narrative flow)
"
```

**Result:** Prep doc that is:
- ✅ Well-written (Layer 1)
- ✅ Substantively appropriate for this course (Layer 2)

---

### Files to Keep/Reorganize

**Keep and integrate:**
- ✅ `elements-of-style.md` → Include in WRITING_FOUNDATIONS.md (or keep as reference in 02_STYLE_GUIDES/REFERENCES/)
- ✅ `SKILL.md` → Integrate into WRITING_FOUNDATIONS.md as "AI Application Guidelines"

**New files to create:**
- `law-school-common/02_STYLE_GUIDES/WRITING_FOUNDATIONS.md` (universal)
- `[Course]/00_ADMIN/course_style_guide.md` (course-specific, one per course)

**Consolidate but don't delete:**
- CrimLaw audio/reference style guides → merge into CrimLaw course_style_guide.md
- Deals prep sheet style guide → migrate into Deals course_style_guide.md

---

## Question 2: Activity-Based Folder Structure

### Current Structure (Content-Type Based)
```
CrimLaw/
├── 00_ADMIN/
├── 01_SOURCES/
├── 02_PREP/
├── 03_TRANSCRIPTS/
├── 04_REVIEWS/
├── 05_OUTLINE/
└── 06_PREWRITES/
```

**Problem:** Organized by content type, not by user activity

---

### User Insight
**"Structure based on what I'm trying to do"**

Activities:
1. **Preparing for class** (pre-class activities)
2. **Reviewing class** (post-class activities)
3. **Building knowledge** (ongoing throughout semester)
4. **Taking exam** (exam day materials)

---

### Option A: Activity-Based Top-Level Folders

```
CrimLaw/
├── PREP_FOR_CLASS/          # "I have class tomorrow"
│   ├── audio/               # Audio preps (listen while commuting)
│   ├── text/                # Text preps (cold-call reference during class)
│   └── assignments/         # What's assigned for each class
│
├── AFTER_CLASS/             # "Class just ended"
│   ├── transcripts/         # Download transcript here
│   └── reviews/             # Generated post-class reviews
│
├── BUILDING_KNOWLEDGE/      # "Ongoing learning throughout semester"
│   ├── outline/             # Growing outline (cumulative)
│   ├── prewrites/           # Exam answers (built incrementally)
│   └── sources/             # Reference materials
│       ├── past_exams/
│       └── past_outlines/
│
└── EXAM_TIME/               # "Taking exam now"
    ├── prewrites/           # Copy-paste ready answers (symlink or copy from BUILDING_KNOWLEDGE)
    ├── outline/             # Attack outline (distilled from full outline)
    ├── quick_reference/     # One-pagers, checklists
    └── past_exams/          # Past exams for last-minute review
```

**Pros:**
- ✅ Intuitive - folders match user's current activity
- ✅ Clear what to access when (before class vs. during exam)
- ✅ Exam materials consolidated in one place

**Cons:**
- ❌ Duplication (prewrites appear in two places)
- ❌ Less clear for AI automation (scripts need to know context)
- ❌ "BUILDING_KNOWLEDGE" is vague catch-all

---

### Option B: Hybrid (Content-Type with Activity Markers)

```
CrimLaw/
├── 00_ADMIN/
│   ├── MASTER_LOG.md
│   ├── exam_spec.md
│   └── course_style_guide.md
│
├── 01_SOURCES/              # [THROUGHOUT SEMESTER] Reference materials
│   ├── syllabus/
│   ├── past_exams/
│   └── past_outlines/
│
├── 02_PREP/                 # [BEFORE CLASS] Pre-class materials
│   ├── audio/
│   └── text/
│
├── 03_TRANSCRIPTS/          # [AFTER CLASS] Class recordings
│   ├── raw/
│   └── processed/
│
├── 04_REVIEWS/              # [AFTER CLASS] Post-class analysis
│
├── 05_OUTLINE/              # [THROUGHOUT SEMESTER → EXAM] Growing outline
│   ├── INDEX.md
│   ├── 01_elements/
│   ├── 02_homicide/
│   └── ...
│
├── 06_PREWRITES/            # [THROUGHOUT SEMESTER → EXAM] Exam answers
│   ├── INDEX.md
│   ├── DOCTRINAL/           # Black letter law analyses
│   │   ├── 01_elements/
│   │   ├── 02_homicide/
│   │   └── 03_defenses/
│   └── POLICY/              # Policy arguments
│       ├── punishment_theory.md
│       ├── racial_justice.md
│       └── ...
│
└── 99_EXAM_DAY/             # [EXAM ONLY] Distilled exam materials
    ├── attack_outline.md    # Condensed outline (key rules only)
    ├── prewrites_index.md   # Quick index to all prewrites
    ├── checklist.md         # Don't-forget list
    └── quick_reference/     # One-pagers
```

**Pros:**
- ✅ Content type organization (AI automation easier)
- ✅ Activity markers in comments clarify usage
- ✅ No duplication
- ✅ Exam materials consolidated in 99_EXAM_DAY/
- ✅ Prewrites split by type (doctrinal vs. policy)

**Cons:**
- ❌ Less immediately intuitive than pure activity-based
- ❌ Numbered folders feel bureaucratic

---

### Option C: Activity-Based with Subtype Organization

```
CrimLaw/
├── ADMIN/
│
├── PREP/                    # "I'm preparing for class"
│   ├── FOR_NEXT_CLASS/
│   │   ├── audio/
│   │   └── text/
│   └── SOURCES/
│       ├── syllabus/
│       ├── past_exams/
│       └── past_outlines/
│
├── REVIEW/                  # "I just finished class"
│   ├── transcripts/
│   │   ├── raw/
│   │   └── processed/
│   └── reviews/
│
├── LEARN/                   # "I'm building my understanding"
│   ├── outline/
│   │   ├── INDEX.md
│   │   ├── 01_elements/
│   │   └── ...
│   └── prewrites/
│       ├── INDEX.md
│       ├── DOCTRINAL/
│       └── POLICY/
│
└── EXAM/                    # "I'm taking the exam"
    ├── attack_outline.md
    ├── prewrites_index.md
    ├── checklist.md
    └── quick_reference/
```

**Pros:**
- ✅ Clear activity names (PREP, REVIEW, LEARN, EXAM)
- ✅ No numbering (more readable)
- ✅ Hierarchical organization within activities

**Cons:**
- ❌ "LEARN" is still vague
- ❌ Sources under PREP feels odd (not actively prepping with past exams)

---

### Recommendation: Option B (Hybrid) + Activity Comments

**Why:**
1. **Content-type organization is better for automation** - Scripts can reliably find preps, transcripts, reviews
2. **Activity markers in comments/README clarify usage** - User knows when to access each folder
3. **99_EXAM_DAY consolidates exam materials** - Clear separation between semester work and exam day
4. **Prewrites split by type (DOCTRINAL vs POLICY)** - User's insight about categorization

**Enhanced Option B:**

```
CrimLaw/
├── 00_ADMIN/
│   ├── MASTER_LOG.md
│   ├── exam_spec.md
│   ├── course_style_guide.md
│   └── README.md            # "What's in each folder and when to use it"
│
├── 01_SOURCES/              # [Reference throughout semester]
│   ├── syllabus/
│   ├── past_exams/
│   └── past_outlines/
│
├── 02_PREP/                 # [USE BEFORE CLASS]
│   ├── audio/               # Listen while commuting
│   └── text/                # Read before class, search during cold calls
│
├── 03_TRANSCRIPTS/          # [USE AFTER CLASS]
│   ├── raw/                 # Drop Echo360 download here
│   └── processed/           # Auto-generated cleaned version
│
├── 04_REVIEWS/              # [USE AFTER CLASS]
│   └── YYYY-MM-DD_classNN_review.md  # Auto-generated from transcript
│
├── 05_OUTLINE/              # [Build throughout semester, use on exam]
│   ├── INDEX.md
│   ├── 01_elements/
│   ├── 02_homicide/
│   ├── 03_defenses/
│   ├── 04_inchoate/
│   └── 05_theory/
│
├── 06_PREWRITES/            # [Build throughout semester, use on exam]
│   ├── INDEX.md             # Master list of all prewrites
│   │
│   ├── DOCTRINAL/           # Black letter law IRAC analyses
│   │   ├── INDEX.md
│   │   ├── 01_elements/
│   │   │   ├── actus_reus_analysis.md
│   │   │   ├── mens_rea_analysis.md
│   │   │   └── causation_analysis.md
│   │   ├── 02_homicide/
│   │   │   ├── murder_analysis.md
│   │   │   ├── heat_of_passion_analysis.md
│   │   │   └── felony_murder_analysis.md
│   │   └── 03_defenses/
│   │       ├── self_defense_analysis.md
│   │       ├── necessity_analysis.md
│   │       └── duress_analysis.md
│   │
│   └── POLICY/              # Policy arguments (essay-ready paragraphs)
│       ├── INDEX.md
│       ├── punishment_theory.md              # Retribution vs. deterrence vs. rehab
│       ├── racial_justice_criminal_law.md
│       ├── death_penalty_justifications.md
│       ├── legality_and_vagueness.md
│       ├── foucault_discipline_critique.md
│       └── critical_theory_applications.md
│
└── 99_EXAM_DAY/             # [USE ONLY ON EXAM]
    ├── README.md            # "Open this folder on exam day"
    ├── attack_outline.md    # Condensed rules (3-5 pages)
    ├── prewrites_index.md   # Quick index to all prewrites in 06_PREWRITES/
    ├── checklist.md         # Issue-spotting checklist
    ├── mpc_quick_reference.md  # All MPC sections cited in course
    └── case_quick_reference.md # Major cases in 2-3 lines each
```

---

## Question 3: Prewrite Categorization

### User Insight
**"Prewrites should be defined and categorized (e.g., black letter law or policy)"**

### Two Categories of Prewrites

#### Category 1: DOCTRINAL Prewrites
**Purpose:** Black letter law IRAC analyses (copy-paste ready)

**Structure:**
```markdown
# [Doctrine] Analysis

## PREWRITE (Copy-Paste Ready)

**Issue:** Whether...

**Rule:** [Complete black letter law with elements]

**Application:** [Fill-in-the-blank framework]
Here, [party] DOES/DOES NOT satisfy element 1 because [FACTS].
Element 2 IS/IS NOT met because [FACTS].
...

**Conclusion:** Therefore, [party] CAN/CANNOT...

## TRIGGERS
- When to use this analysis
- Red flags
- Fact patterns

## FRAMEWORK
[Element-by-element breakdown with factors]

## EXAMPLES
[2-3 worked examples]
```

**Examples:**
- Self-defense analysis
- Actus reus analysis
- Mens rea analysis
- Heat of passion analysis
- Attempt analysis

**When to use:** Doctrinal essay questions, issue spotting, rule application

---

#### Category 2: POLICY Prewrites
**Purpose:** Policy arguments (essay-ready paragraphs on recurring themes)

**Structure:**
```markdown
# [Policy Topic]

## Overview
What is this policy issue about?

## Competing Arguments

### Position A: [e.g., Retributive Justice]
**Thesis:** [One sentence]

**Arguments:**
- Argument 1 with support
- Argument 2 with support
- Argument 3 with support

**Exam-ready paragraph:**
[2-3 sentences stating position and main argument, ready to drop into essay]

### Position B: [e.g., Deterrence]
**Thesis:** [One sentence]

**Arguments:**
- Argument 1 with support
- Argument 2 with support

**Exam-ready paragraph:**
[2-3 sentences]

### Position C: [e.g., Critical Theory Critique]
**Thesis:** [One sentence]

**Arguments:**
- Argument 1 with support
- Argument 2 with support

**Exam-ready paragraph:**
[2-3 sentences]

## Professor's Angle
What does this prof care about? (from class signals)

## Past Exam Appearances
How has this appeared on exams?
```

**Examples:**
- Punishment theory (retribution vs. deterrence vs. rehabilitation)
- Racial justice in criminal law
- Death penalty justifications
- Legality and fair notice
- Foucault's discipline critique
- Critical theory applications

**When to use:** Policy essay questions, normative arguments, justification sections

---

### Why This Categorization Works

**Different purposes:**
- DOCTRINAL = answering "what is the law and how does it apply?"
- POLICY = answering "why is this the law and should it be?"

**Different structures:**
- DOCTRINAL = IRAC with fill-in-the-blank
- POLICY = competing arguments with exam-ready paragraphs

**Different update cycles:**
- DOCTRINAL = refined as you learn elements and factors
- POLICY = refined as you understand professor's theoretical preferences

**Different exam usage:**
- DOCTRINAL = Use for every rule application (backbone of exam)
- POLICY = Use for normative questions, justifications, critiques

---

## Implementation Recommendations

### For Style Guides
1. Create `law-school-common/02_STYLE_GUIDES/WRITING_FOUNDATIONS.md`
   - Integrate elements-of-style.md principles
   - Integrate SKILL.md guardrails
   - Add legal writing conventions

2. Create `[Course]/00_ADMIN/course_style_guide.md` for each course
   - Course priorities (what matters for THIS course)
   - Professor emphasis
   - Exam format implications

3. Keep originals as reference:
   - Move `elements-of-style.md` → `law-school-common/02_STYLE_GUIDES/REFERENCES/`
   - Move `SKILL.md` → integrated into WRITING_FOUNDATIONS.md (delete standalone)

### For Folder Structure
1. Use **Option B (Hybrid)** structure
   - Numbered folders for content type
   - Activity markers in comments/README
   - 99_EXAM_DAY/ for exam materials

2. Split prewrites into DOCTRINAL and POLICY subfolders

3. Create `00_ADMIN/README.md` in each course explaining folder usage

### For Prewrite System
1. Build DOCTRINAL prewrites as doctrines are learned (ongoing)
2. Build POLICY prewrites as themes emerge from class (mid-semester)
3. Track in MASTER_LOG with separate columns:
   - `Doctrinal Prewrite?` - ✅ if IRAC analysis exists
   - `Policy Prewrite?` - ✅ if policy argument exists

---

## Next Steps

1. Get user feedback on:
   - Style guide two-layer approach
   - Folder structure (Option B vs. other options)
   - Prewrite categorization

2. Once approved, implement:
   - Create WRITING_FOUNDATIONS.md
   - Create course_style_guide.md templates
   - Restructure folders
   - Update REORG_TRACKER.md with new plan
