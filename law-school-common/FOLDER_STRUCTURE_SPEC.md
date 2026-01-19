# Standard Course Folder Structure - Definitive Specification

**Date:** Jan 19, 2026  
**Based on analysis of:** CrimLaw (current), Contracts/ConLaw/CivPro (Archive)

---

## Overview

Each course uses **identical structure**. All courses share common resources from `law-school-common/`.

---

## Per-Course Structure

```
CourseNameHere/
├── 00_ADMIN/
│   ├── MASTER_LOG.md                    # Status tracking (see below)
│   └── exam_spec.md                     # Past exam analysis
│
├── 01_SOURCES/
│   ├── syllabus/                        # Syllabus + parsed assignments  
│   │   ├── syllabus.pdf                 # Original PDF
│   │   ├── syllabus_parsed.md           # Markdown version
│   │   └── assignments/                 # Per-class assignment files
│   │       └── YYYY-MM-DD_classNN.md    # What's assigned for each class
│   ├── past_exams/                      # Past exams (PDFs + OCR'd text)
│   └── past_outlines/                   # Past student outlines for reference
│
├── 02_PREP/
│   ├── audio/                           # Audio preps (TTS-ready, 25min)
│   │   └── YYYY-MM-DD_classNN_audio.md
│   └── text/                            # Text preps (cold-call Q&A)
│       └── YYYY-MM-DD_classNN_text.md
│
├── 03_TRANSCRIPTS/
│   ├── raw/                             # Echo360 downloads (unedited)
│   │   └── YYYY-MM-DD_classNN_raw.txt
│   └── processed/                       # Cleaned transcripts
│       └── YYYY-MM-DD_classNN_clean.md
│
├── 04_REVIEWS/                          # Post-class review docs
│   └── YYYY-MM-DD_classNN_review.md     # Exam signals, corrections, outline inserts
│
├── 05_OUTLINE/
│   ├── INDEX.md                         # Master index linking all outline sections
│   ├── 01_formation/                    # Topic-based sections (see below)
│   │   └── consideration.md
│   ├── 02_remedies/
│   │   ├── expectation.md
│   │   └── specific_performance.md
│   ├── 03_defenses/
│   │   └── duress.md
│   ├── exam_signals.md                  # Extracted #EXAM_SIGNAL tags from reviews
│   └── weak_topics.md                   # Topics you got wrong on practice
│
└── 06_PREWRITES/
    ├── INDEX.md                         # Master list of all prewrites
    ├── 01_formation/                    # Copy-paste ready exam answers
    │   ├── consideration_analysis.md
    │   └── offer_acceptance_analysis.md
    ├── 02_remedies/
    │   ├── expectation_damages.md
    │   └── specific_performance.md
    └── 03_defenses/
        └── duress_analysis.md
```

---

## Subfolder Specifications

### 00_ADMIN/

**Purpose:** Course-level tracking and exam strategy

**Contents:**
- `MASTER_LOG.md` - Status tracking for all classes (see format below)
- `exam_spec.md` - Past exam analysis (question types, topic distribution, professor patterns)

**NOT in here:** Templates, style guides, workflows (those live in law-school-common)

---

### 01_SOURCES/

**Purpose:** Read-only reference materials

**Subfolders:**

#### `syllabus/`
- `syllabus.pdf` - Original PDF from professor
- `syllabus_parsed.md` - Markdown version with dates/topics extracted
- `assignments/` - Per-class assignment files
  - `YYYY-MM-DD_classNN.md` - What to read for each class

**Example assignment file:**
```markdown
# Class 12: Heat of Passion Killings
**Date:** 2026-01-29
**Topic:** Voluntary Manslaughter

## Assigned Reading
- Casebook pp. 450-475
- MPC § 210.3
- People v. Berry

## MPC Sections
- § 210.3(1)(b) - Extreme emotional disturbance

## Key Cases
- People v. Berry (adequate provocation test)
- State v. Shane (cooling time)
```

#### `past_exams/`
- PDF files of past exams
- OCR'd text versions
- Organized by year: `2023_Spring_Exam.pdf`

#### `past_outlines/`
- Outlines from past students (for professor patterns)
- Attack outlines
- Full master outlines
- **Keep read-only** - don't edit these, they're reference material

---

### 02_PREP/

**Purpose:** Pre-class materials

**Subfolders:**

#### `audio/` - Audio preps for TTS
- **Format:** Conversational, narrative, TTS-friendly
- **Length:** ~4,000-5,000 words (~25 min spoken at 1.5x)
- **Content:** Central question, minimal doctrine, 5-10 cold-call prompts, 2-3 hypos
- **Naming:** `YYYY-MM-DD_classNN_audio.md`
- **Style guide:** `law-school-common/02_STYLE_GUIDES/WRITING_STYLE.md` (Audio Prep section)

#### `text/` - Text preps for cold-call reference
- **Format:** Searchable Q&A, structured for fast lookup
- **Content:** Expected questions, doctrine (rule statements + elements), case briefs, policy arguments, hypo bank
- **Naming:** `YYYY-MM-DD_classNN_text.md`
- **Style guide:** `law-school-common/02_STYLE_GUIDES/WRITING_STYLE.md` (Text Prep section)

---

### 03_TRANSCRIPTS/

**Purpose:** Class lecture recordings

**Subfolders:**

#### `raw/`
- Direct downloads from Echo360
- **Format:** `.txt` files (raw transcription)
- **Naming:** `YYYY-MM-DD_classNN_raw.txt`
- **Do not edit** - keep original for error detection

#### `processed/`
- Cleaned versions with transcription errors fixed
- **Format:** `.md` files (markdown)
- **Naming:** `YYYY-MM-DD_classNN_clean.md`
- **Fixes:** Legal terms, case names, common mishearings
- **Adds:** Timestamps, speaker labels, section headers

---

### 04_REVIEWS/

**Purpose:** Post-class analysis and exam signal extraction

**Contents:** One review doc per class

**Format:** `YYYY-MM-DD_classNN_review.md`

**Sections:**
1. **What Professor Emphasized** - 3-5 main points from class
2. **Exam Signals** - Explicit or implicit signals tagged with `#EXAM_SIGNAL`
3. **Corrections to Prep** - What was wrong in your prep doc
4. **Doctrinal Insights** - New understanding of rules, elements, MPC syntax
5. **Policy Arguments** - Policy moves professor rewarded
6. **Outline Inserts** - Snippets to add to outline (ready to paste)

**Template:** `law-school-common/03_TEMPLATES/review_template.md`

---

### 05_OUTLINE/

**Purpose:** Cumulative exam-ready outline

**Structure: Topic-Based Sections (NOT one giant file)**

#### The Problem with Single-File Outlines
- 150+ page docs break AI coherence
- Repetition and drift accumulate
- Hard to navigate during exam

#### Solution: Modular Outline Structure

**Based on Contracts (Archive) and CivPro (Archive) approach:**

```
05_OUTLINE/
├── INDEX.md                              # Master table of contents
├── 01_formation/                         # Major topic area
│   ├── _INDEX.md                         # Section TOC
│   ├── consideration.md                  # Specific doctrine
│   ├── offer_acceptance.md
│   └── promissory_estoppel.md
├── 02_remedies/
│   ├── _INDEX.md
│   ├── expectation_damages.md
│   ├── reliance_damages.md
│   └── specific_performance.md
├── 03_defenses/
│   ├── _INDEX.md
│   ├── duress.md
│   ├── unconscionability.md
│   └── mistake.md
├── 04_interpretation/
│   ├── _INDEX.md
│   ├── parol_evidence.md
│   └── good_faith.md
├── exam_signals.md                       # All #EXAM_SIGNAL tags extracted
└── weak_topics.md                        # Topics needing review
```

#### How to Divide Outline Sections

**Step 1: Wait for Syllabus**
- Cannot divide logically until you see course structure
- Professor's syllabus shows natural topic divisions

**Step 2: Create Topic Folders (Week 1 after syllabus)**
Based on syllabus structure, create major topic folders:
- Look for syllabus section headings (e.g., "Part I: Jurisdiction", "Part II: Formation")
- Aim for 4-8 major topic folders
- Each folder = 1-3 weeks of material

**Step 3: Create Doctrine Files (Ongoing)**
As classes progress, create specific doctrine files:
- One file per major rule/concept
- **Target:** 10-20 pages per file (manageable for AI)
- Name files clearly: `self_defense.md`, `negligence_standard.md`

**Example: CrimLaw Outline Structure**
```
05_OUTLINE/
├── INDEX.md
├── 01_elements/
│   ├── actus_reus.md
│   ├── mens_rea.md                       # MPC § 2.02 deep dive
│   └── causation.md                      # MPC § 2.03
├── 02_homicide/
│   ├── murder_first_degree.md
│   ├── heat_of_passion.md
│   ├── felony_murder.md
│   └── unintended_killings.md
├── 03_defenses/
│   ├── self_defense.md                   # MPC §§ 3.04, 3.09
│   ├── necessity.md                      # MPC § 3.02
│   └── duress.md                         # MPC § 2.09
├── 04_inchoate/
│   ├── attempt.md                        # MPC § 5.01
│   ├── complicity.md                     # MPC § 2.06
│   └── conspiracy.md                     # MPC § 5.03
└── 05_theory/
    ├── legality_vagueness.md
    ├── punishment_theory.md
    └── policy_arguments.md               # Exam-ready policy paragraphs
```

#### INDEX.md Format

**Based on ConLaw approach (Archive) - Master index with links:**

```markdown
# Criminal Law - Master Outline Index

**Course:** Criminal Law (Harcourt, Spring 2026)  
**Exam Date:** [Date]  
**Last Updated:** [Auto-generated]

---

## Quick Navigation

**Elements of Crime**
- [Actus Reus](01_elements/actus_reus.md) - Voluntary act requirement
- [Mens Rea](01_elements/mens_rea.md) - MPC § 2.02 (purposely, knowingly, recklessly, negligently)
- [Causation](01_elements/causation.md) - MPC § 2.03 (but-for + proximate cause)

**Homicide**
- [Murder (First Degree)](02_homicide/murder_first_degree.md) - Premeditation, deliberation
- [Heat of Passion](02_homicide/heat_of_passion.md) - Voluntary manslaughter, adequate provocation
- [Felony Murder](02_homicide/felony_murder.md) - Inherently dangerous felony + merger
- [Unintended Killings](02_homicide/unintended_killings.md) - Recklessness, negligence

**Defenses**
- [Self-Defense](03_defenses/self_defense.md) - MPC §§ 3.04, 3.09; duty to retreat
- [Necessity](03_defenses/necessity.md) - MPC § 3.02; lesser evil
- [Duress](03_defenses/duress.md) - MPC § 2.09; threat of death/harm

**Inchoate Crimes**
- [Attempt](04_inchoate/attempt.md) - MPC § 5.01; substantial step test
- [Complicity](04_inchoate/complicity.md) - MPC § 2.06; accomplice liability
- [Conspiracy](04_inchoate/conspiracy.md) - MPC § 5.03; agreement + overt act

**Theory & Policy**
- [Legality & Vagueness](05_theory/legality_vagueness.md) - Fair notice, void for vagueness
- [Punishment Theory](05_theory/punishment_theory.md) - Retribution, deterrence, incapacitation
- [Policy Arguments](05_theory/policy_arguments.md) - Exam-ready policy paragraphs

---

## Exam-Ready Materials

- [Exam Signals](exam_signals.md) - All #EXAM_SIGNAL tags from class
- [Weak Topics](weak_topics.md) - Topics needing review
- [MPC Quick Reference](mpc_quick_reference.md) - All MPC sections cited

---

## Usage During Exam

**Obsidian:** Click any link to jump to that section  
**Print:** Each section prints as separate document  
**Search:** Use Cmd+F to search across all files
```

#### Individual Section Files

**Keep focused:** Each file covers ONE doctrine
**Target length:** 10-20 pages (not 150 pages)
**Structure:**
1. **Black Letter Law** - Rule statement
2. **Elements Breakdown** - Numbered elements with definitions
3. **Cases** - Key cases with holdings
4. **Hypos** - Practice problems
5. **Policy** - Exam-ready policy paragraphs
6. **Professor Signals** - What prof emphasized (from reviews)

---

### 06_PREWRITES/

**Purpose:** Exam-ready answers built throughout semester

**Critical insight:** Your ConLaw performance shows prewrites are the most effective exam prep. Build these as you learn topics, not last-minute before exam.

**Structure: Mirrors outline structure**

```
06_PREWRITES/
├── INDEX.md                              # Master list of all prewrites
├── 01_formation/                         # Major topic area
│   ├── consideration_analysis.md
│   ├── offer_acceptance_analysis.md
│   └── promissory_estoppel_analysis.md
├── 02_remedies/
│   ├── expectation_damages.md
│   ├── reliance_damages.md
│   └── specific_performance.md
└── 03_defenses/
    ├── duress_analysis.md
    └── unconscionability_analysis.md
```

**Each prewrite file contains:**

1. **Issue Statement** (copy-paste ready)
   ```markdown
   **Issue:** Whether [party] can [claim/defense] under [doctrine].
   ```

2. **Rule Statement** (black letter law, complete)
   - All elements numbered
   - Standards/tests clearly stated
   - Statutory citations included

3. **Application Framework** (fill-in-the-blank structure)
   ```markdown
   **Application:**
   Here, [party] DOES/DOES NOT satisfy element 1 because [FACTS showing...].
   Element 2 IS/IS NOT met because [FACTS showing...].
   [Continue for all elements]
   ```

4. **Conclusion Template**
   ```markdown
   **Conclusion:** Therefore, [party] CAN/CANNOT [claim/defense] under [doctrine].
   ```

5. **Triggers** (when to use this analysis)
   - Red flags that signal this issue
   - Fact patterns that invoke this doctrine
   - Keywords to watch for

6. **Example Applications** (2-3 worked examples)
   - Short fact patterns
   - Complete IRAC analysis
   - Show variations (weak facts vs. strong facts)

**Format:**
- **Naming:** `[doctrine]_analysis.md` (e.g., `self_defense_analysis.md`)
- **Length:** 2-4 pages per prewrite (focused on one doctrine)
- **Style:** Copy-paste ready, fill-in-the-blank friendly
- **Updates:** Refine after each class as understanding deepens

**Building prewrites throughout semester:**

**Week 1-2 (After each class):**
- Identify 1-2 testable doctrines from class
- Build skeleton prewrites (issue, rule, structure)

**Weeks 3-8 (Ongoing):**
- Flesh out prewrites with professor's emphasis
- Add examples from class hypos
- Refine application frameworks based on what prof rewards

**Weeks 9-12 (Refinement):**
- Test prewrites on past exam questions
- Identify gaps
- Add edge cases and variations

**Week 13-14 (Exam prep):**
- Practice applying prewrites under time pressure
- Memorize issue/rule statements
- Drill fill-in-the-blank application

**Example: CrimLaw Self-Defense Prewrite**

```markdown
# Self-Defense Analysis

## PREWRITE (Copy-Paste Ready)

**Issue:** Whether [defendant] can assert self-defense under MPC § 3.04.

**Rule:** Under MPC § 3.04, the use of force is justifiable when the actor believes such force is immediately necessary for protection against the use of unlawful force by another on the present occasion. The defense requires: (1) the actor held a subjective belief that force was necessary, (2) the belief was objectively reasonable, (3) the threat was imminent, and (4) the force used was proportional to the threat. Under MPC § 3.09, if the actor is recklessly or negligently mistaken about the need for self-defense, the defense is unavailable in a prosecution for an offense requiring recklessness or negligence.

**Application:**

Here, [defendant] HELD/DID NOT HOLD a subjective belief that force was necessary because [FACTS showing what defendant thought/perceived]. This belief WAS/WAS NOT objectively reasonable because [FACTS showing what reasonable person would believe given circumstances]. The threat WAS/WAS NOT imminent because [FACTS showing temporal proximity—immediate vs. future]. The force used WAS/WAS NOT proportional because [FACTS comparing degree of force used vs. threat faced—deadly force requires deadly threat]. Under § 3.09, defendant's belief WAS/WAS NOT reckless or negligent because [FACTS showing what defendant knew or should have known].

**Conclusion:** Therefore, [defendant] CAN/CANNOT assert self-defense under MPC § 3.04.

---

## TRIGGERS

**Invoke self-defense when:**
- Defendant used force against another person
- Defendant claims they were defending themselves
- Question about whether force was justified
- Victim was aggressor or defendant perceived threat

**RED FLAGS:**
- Defendant was initial aggressor (may lose self-defense)
- Defendant had duty to retreat (MPC doesn't require retreat except in own dwelling vs. co-occupant)
- Force was excessive (used deadly force against minor threat)
- Threat was not imminent (preemptive strike, revenge)
- Defendant provoked the confrontation

---

## FRAMEWORK

### Element 1: Subjective Belief in Necessity of Force

**What to show:** What did defendant actually believe at the time?

**Fact patterns:**
- Statements defendant made ("I thought he was going to kill me")
- Defendant's actions (fled vs. escalated)
- Defendant's knowledge of victim (history of violence, prior threats)

**Analysis:**
If defendant articulated fear OR acted consistently with fear → subjective belief likely satisfied

### Element 2: Objective Reasonableness

**Standard:** Would a reasonable person in defendant's circumstances believe force was necessary?

**Factors:**
- Size/strength disparity
- Weapons present
- Defendant's vulnerability (cornered, outnumbered)
- Victim's actions (aggressive vs. defensive)
- Context (high-crime area, history between parties)

**Not reasonable if:**
- Defendant knew victim was joking
- Threat was minor (insult, push) and defendant used deadly force
- Defendant had safe alternatives (could have left)

### Element 3: Imminence

**Temporal requirement:** Threat must be immediate, not future

**Imminent:**
- Victim reaching for weapon
- Victim charging at defendant
- Victim cornering defendant with violent intent

**NOT imminent:**
- Victim threatened future harm ("I'll get you tomorrow")
- Preemptive strike against anticipated attack
- Revenge for past harm

### Element 4: Proportionality

**Rule:** Force used must be proportional to threat faced

**Non-deadly force justified against:**
- Non-deadly threats (punch, shove, restraint)

**Deadly force justified only against:**
- Deadly threats (gun, knife, serious bodily harm)
- Threat of serious bodily injury

**Disproportionate:**
- Shooting someone who pushed you
- Using weapon against unarmed attacker (unless size/strength disparity makes it reasonable)

### MPC § 3.09: Mistaken Belief

**Rule:** If defendant's belief in need for self-defense was reckless or negligent, self-defense is unavailable in prosecution for offense requiring that culpability

**Application:**
- If charged with murder (purposely/knowingly), even reckless mistake allows self-defense
- If charged with manslaughter (recklessly), reckless mistake defeats self-defense
- If charged with negligent homicide, even negligent mistake defeats self-defense

---

## EXAMPLE APPLICATIONS

### Example 1: Clear Self-Defense

**Facts:** Victim pulled knife and lunged at defendant in alley. Defendant drew gun and shot victim once.

**Analysis:**
Defendant held subjective belief force was necessary (drew weapon in response to knife). Belief was objectively reasonable (knife = deadly weapon, lunging = imminent attack). Threat was imminent (lunging, not future threat). Force was proportional (deadly force vs. deadly force). Self-defense succeeds.

### Example 2: Failed Self-Defense (Disproportionate)

**Facts:** Victim shoved defendant in bar argument. Defendant pulled gun and shot victim.

**Analysis:**
Defendant may have subjectively believed force was necessary (felt threatened). But belief was NOT objectively reasonable (shove is not deadly threat). Force was NOT proportional (deadly force vs. non-deadly force). Self-defense fails.

### Example 3: § 3.09 Issue (Reckless Mistake)

**Facts:** Defendant saw victim reach into pocket. Defendant thought victim was reaching for gun and shot victim. Victim was reaching for phone. Defendant had been told by unreliable source that victim carries gun, but defendant never verified.

**Analysis:**
Defendant held subjective belief (thought gun). But belief may have been RECKLESS (consciously disregarded substantial risk that victim was unarmed by relying on unverified info). If charged with reckless manslaughter, § 3.09 defeats self-defense. If charged with murder, § 3.09 doesn't apply and self-defense may succeed despite recklessness.
```

**When to build each prewrite:**
- After class covers that doctrine
- When reviewing for midterm/exam
- When working through past exam questions

**Template:** `law-school-common/03_TEMPLATES/prewrite_template.md`

---

## MASTER_LOG.md Format

**Purpose:** Single source of truth for course status

**Columns:**
- `Class#` - Sequential number
- `Date` - YYYY-MM-DD
- `Topic` - Brief topic
- `Assignment` - Link to assignment file
- `Prep Status` - Not Started / Draft / Done
- `Prep_QC` - QC iterations: `0` (unchecked) / `1` / `2+` / `✓` (passed)
- `Audio?` - ✅ if audio prep exists
- `Class Done?` - ✅ if class attended
- `Transcript?` - ✅ if transcript downloaded
- `Review?` - ✅ if review doc completed
- `Review_QC` - QC iterations: `0` / `1` / `2+` / `✓`
- `Outline?` - ✅ if outline sections updated
- `Outline_QC` - QC iterations: `0` / `1` / `2+` / `✓`
- `Prewrite?` - ✅ if prewrite exists for this topic
- `Exam Signals` - Count of signals from this class
- `Next Action` - What needs to happen next
- `Notes` - Brief QC issues, blockers, context

**QC Process:**
- QC happens by **editing the document in place** (no separate QC docs)
- Each QC pass increments counter: `0` → `1` → `2` → `✓`
- QC findings go in Notes column or in doc frontmatter
- Workflow: Generate draft → QC pass 1 → Edit → QC pass 2 (if needed) → Mark `✓`

**Example:**
```markdown
# MASTER LOG - Criminal Law

## Class Pipeline

| Class# | Date | Topic | Assignment | Prep | Audio? | Class? | Transcript? | Review? | Outline? | Prewrite? | Signals | Next Action |
|--------|------|-------|------------|------|--------|--------|-------------|---------|----------|-----------|---------|-------------|
| 1 | 2026-01-20 | Criminal Law & Justice | [link](01_SOURCES/syllabus/assignments/2026-01-20_class01.md) | Done | ✅ | ✅ | ✅ | ✅ | ✅ | | 3 | Build prewrite |
| 2 | 2026-01-22 | Actus Reus | [link](01_SOURCES/syllabus/assignments/2026-01-22_class02.md) | Done | ✅ | ✅ | ✅ | Pending | | | 0 | Review transcript |
| 3 | 2026-01-23 | Mens Rea | [link](01_SOURCES/syllabus/assignments/2026-01-23_class03.md) | Done | ✅ | | | | | | 0 | Attend class |
| 4 | 2026-01-27 | Intended Killings | [link](01_SOURCES/syllabus/assignments/2026-01-27_class04.md) | Draft | | | | | | | 0 | Generate audio |
| 5 | 2026-01-29 | Heat of Passion | [link](01_SOURCES/syllabus/assignments/2026-01-29_class05.md) | | | | | | | | 0 | Generate prep |
```

---

## Summary: Key Principles

1. **No giant outline files** - Break into 10-20 page sections
2. **Wait for syllabus** - Topic structure follows professor's organization
3. **Master INDEX.md** - Single file linking all sections (like ConLaw Archive)
4. **Modular updates** - Reviews feed specific outline sections, not one massive file
5. **Exam-ready format** - Each section can be printed/searched independently
6. **MASTER_LOG** - Clear visibility into what's done/pending
7. **Consistent naming** - `YYYY-MM-DD_classNN_type.md` for everything
