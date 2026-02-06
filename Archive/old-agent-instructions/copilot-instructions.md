# Law School Monorepo — AI Agent Instructions

> **Read this file first.** It tells you everything you need to know to work in this codebase.
> This file is auto-detected by GitHub Copilot.

---

## 🚨 CRITICAL: Before Any Task

1. **Identify the course** from the user's request (CrimLaw, Property, Torts, Deals, LPW-II)
2. **Read the course MASTER_LOG** at `ACTIVE/{Course}/00_ADMIN/MASTER_LOG.md`
3. **Read the detailed instructions** for the task type (see Quick Reference below)

---

## 📍 Quick Reference: Common Tasks

### Create Prep Docs

**Command patterns**: 
- `"prep for CrimLaw class 2"` — Create prep for specific class number
- `"prep for next Torts class"` — Create prep for next upcoming class
- `"create prep doc for next Property class"` — Same as above

**Creates BOTH:** Text prep (searchable) + Audio prep (TTS-ready) + QC verification

**Exception:** For Deals, only text prep is required (no audio prep).

**READ THESE FILES FIRST:**
1. `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md` — Full procedure (see "prep for [COURSE] class [NN]" and "prep for next [COURSE] class" commands)
2. `law-school-common/01_WORKFLOWS/PRE_CLASS_WORKFLOW.md` — Step-by-step workflow
3. `law-school-common/03_TEMPLATES/text_prep_template.md` — Text prep template
4. `law-school-common/03_TEMPLATES/audio_prep_template.md` — Audio prep template
5. `ACTIVE/{Course}/00_ADMIN/MASTER_LOG.md` — Find class number, date, assignment path

**OUTPUT LOCATIONS:**
- Text prep → `ACTIVE/{Course}/02_PREP/text/YYYY-MM-DD_classNN_text.md`
- Audio prep → `ACTIVE/{Course}/02_PREP/audio/YYYY-MM-DD_classNN_audio.md`

**INPUTS TO READ:**
- Assignment file → path in MASTER_LOG `Assignment` column
- Syllabus sources → `ACTIVE/{Course}/01_SOURCES/syllabus/assignments/`
- **INDEX FILES (READ FIRST for efficiency):**
  - `ACTIVE/{Course}/01_SOURCES/past_outlines/INDEX.md` → Topic → outline location
  - `ACTIVE/{Course}/01_SOURCES/past_exams/INDEX.md` → Topic → past exam questions
- Exam spec → `ACTIVE/{Course}/00_ADMIN/exam_spec.md`

---

### Create Review Docs

**Command patterns**: 
- `"ingest transcripts CrimLaw"` — Scan for new transcripts, register in tracking
- `"review CrimLaw"` — Process next pending transcript
- `"review CrimLaw class 2"` — Process specific class transcript
- `"review CrimLaw all"` — Batch process all pending transcripts
- `"integrate review CrimLaw class 2"` — Push review into sources table, outline, prewrites
- `"review status CrimLaw"` — Show pending/completed reviews

**Three-Phase Workflow:**
1. **Ingest** → Scan transcripts, match to classes, register in REVIEW_INDEX
2. **Review** → Create review doc comparing transcript to prep, extract signals
3. **Integrate** → Update SOURCES_TABLE, outline, prewrite bank

**🚨 CRITICAL REVIEW ACCURACY RULES:**

**The review is the most critical document in the entire semester. Everything hinges on accuracy. It CANNOT tolerate hallucination or misattribution.**

1. **STICK TO WHAT PROFESSOR ACTUALLY SAID**
   - Go line by line, paragraph by paragraph through the transcript
   - Summarize what professor said and what class discussion covered
   - NOTHING MORE, NOTHING LESS

2. **NEVER attribute to professor unless explicitly stated in transcript**
   - DO NOT say "professor flagged", "professor emphasized", "professor mentioned", "Harcourt noted", etc. unless the transcript explicitly shows this
   - If professor didn't say it in lecture, don't attribute it to professor
   - No invented quotes, no paraphrasing as if direct statement

3. **Separate inferences from lecture content**
   - Any reasoning, synthesis, or doctrinal inferences you draw belong in separate sections clearly marked as "Doctrinal Insights" or "Additional Analysis"
   - These sections must be self-contained and clearly distinguished from "What Professor Said"
   - Label clearly: "Based on the reading" or "Doctrinal implication" (not "professor said")

4. **Source every claim**
   - Transcript quote → cite line/paragraph from transcript
   - Casebook content → cite to reading ("from KSSB10 p. 231")
   - MPC text → cite to statute ("MPC §2.01(2)(d)")
   - Your inference → label as "Doctrinal insight" or "Additional analysis"

5. **Flag gaps honestly**
   - If transcript is unclear: mark "[TRANSCRIPT_UNCLEAR]"
   - If you're inferring from readings: "[FROM READING, not lecture]"
   - If you're synthesizing: "[SYNTHESIS based on X + Y]"

**READ THESE FILES FIRST:**
1. `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md` — Full procedure (see review commands)
2. `law-school-common/01_WORKFLOWS/POST_CLASS_WORKFLOW.md` — Complete 3-phase workflow
3. `law-school-common/03_TEMPLATES/review_template.md` — Review template
4. `law-school-common/03_TEMPLATES/review_index_template.md` — Tracking index
5. `law-school-common/03_TEMPLATES/sources_table_template.md` — Running sources table

**OUTPUT LOCATIONS:**
- Reviews → `ACTIVE/{Course}/04_REVIEWS/YYYY-MM-DD_classNN_review.md`
- Review tracking → `ACTIVE/{Course}/00_ADMIN/REVIEW_INDEX.md`
- Sources table → `ACTIVE/{Course}/05_OUTLINE/SOURCES_TABLE.md`

**INPUTS TO READ:**
- Transcripts → `ACTIVE/{Course}/03_TRANSCRIPTS/raw/` (any naming, matched by date)
- Text prep → `ACTIVE/{Course}/02_PREP/text/YYYY-MM-DD_classNN_text.md`
- Assignment → from MASTER_LOG

**TRANSCRIPT MATCHING:** Files matched by date extracted from filename (YYYY-MM-DD), not by class number. Supports various naming patterns.

---

### Update Outline

**Command patterns**: "update outline", "add to outline section"

**READ:** `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md`

**OUTPUT LOCATION:** `ACTIVE/{Course}/05_OUTLINE/`

---

### Create Prewrite

**Command patterns**: "prewrite consideration doctrine", "create IRAC prewrite for self-defense"

**READ THESE FILES FIRST:**
1. `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md`
2. `law-school-common/03_TEMPLATES/prewrite_doctrinal_template.md`
3. `law-school-common/03_TEMPLATES/prewrite_policy_template.md`

**OUTPUT LOCATION:** `ACTIVE/{Course}/06_PREWRITES/`

---

## 📁 Folder Structure

```
law-school/
├── ACTIVE/                          # Current semester courses
│   ├── CrimLaw/
│   ├── Property/
│   ├── Torts/
│   ├── Deals/
│   └── LPW-II/
│       ├── 00_ADMIN/                # MASTER_LOG.md, exam_spec.md
│       ├── 01_SOURCES/              # Syllabus, readings, past exams
│       ├── 02_PREP/                 # Pre-class prep docs
│       │   ├── audio/               # TTS-friendly audio preps
│       │   └── text/                # Searchable text preps
│       ├── 03_TRANSCRIPTS/          # Class transcripts
│       ├── 04_REVIEWS/              # Post-class reviews
│       ├── 05_OUTLINE/              # Course outline
│       └── 06_PREWRITES/            # Exam-ready paragraphs
│
├── law-school-common/               # Shared across all courses
│   ├── 00_SYSTEM/                   # AI rules, commands, folder spec
│   ├── 01_WORKFLOWS/                # Step-by-step workflows
│   ├── 02_STYLE_GUIDES/             # Writing standards
│   └── 03_TEMPLATES/                # All templates
│
└── Archive/                         # Past semester courses
```

---

## 🔑 Key Files to Read

| Purpose | Path |
|---------|------|
| All commands & procedures | `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md` |
| AI rules & conventions | `law-school-common/00_SYSTEM/AI_SYSTEM_RULES.md` |
| Folder structure spec | `law-school-common/00_SYSTEM/FOLDER_STRUCTURE_SPEC.md` |
| Pre-class workflow | `law-school-common/01_WORKFLOWS/PRE_CLASS_WORKFLOW.md` |
| Post-class workflow | `law-school-common/01_WORKFLOWS/POST_CLASS_WORKFLOW.md` |
| QC workflow | `law-school-common/01_WORKFLOWS/QC_WORKFLOW.md` |

---

## ⚙️ Naming Conventions

**🚨 CRITICAL: Use EXACT naming format. No variations allowed.**

**Prep docs:** `YYYY-MM-DD_classNN_type.md`
- Text prep: `YYYY-MM-DD_classNN_text.md` (NEVER `_prep.md`)
- Audio prep: `YYYY-MM-DD_classNN_audio.md` (NEVER `_audio_prep.md`)
- Example: `2026-01-22_class02_text.md`
- Example: `2026-01-22_class02_audio.md`
- **Deals exception:** For classes where Panel 2 is on call, include 'Panel2' in the name: `YYYY-MM-DD_classNN_Panel2_text.md`

**Review docs:** `YYYY-MM-DD_classNN_review.md`

**FORBIDDEN naming patterns:**
- ❌ `_prep.md` (use `_text.md` instead)
- ❌ `_audio_prep.md` (use `_audio.md` instead)
- ❌ `_class_reference.md` (use `_reference.md` if needed, but not in 02_PREP)

**Always get dates and class numbers from MASTER_LOG.md**

---

## 🎯 Agent Behavior Rules

1. **Never create duplicate files** — check if file exists first
2. **Use EXACT naming conventions** — `_text.md` and `_audio.md` only (see Naming Conventions section)
3. **Update MASTER_LOG after creating documents** — mark status as "draft" or "done"
4. **Use templates exactly** — copy structure from `law-school-common/03_TEMPLATES/`
5. **Flag missing sources** — don't make up information; mark "[SOURCE NEEDED]"
6. **Check existing examples** — look at existing preps in `02_PREP/text/` for style

---

## 📝 CRITICAL: Tone, Voice, and Intellectual Honesty

### Writing Style Rules

**Direct, confident voice. No hedging. No hand-holding.**

**FORBIDDEN PHRASES** (never use these):
- "This sounds like X, but it's actually Y"
- "You might think X, but really Y"
- "It may seem like X"
- "This appears to be X"
- "Here's why this matters..."
- "Let me explain..."
- "This is important because..."
- "What this means is..."

**Core principles:**

1. **Don't editorialize about how things sound or seem.** Just explain them directly.

2. **No meta-commentary.** Don't tell the reader what they might think before correcting them.

3. **No defensive over-explaining.** State things clearly and move on.

4. **Write like you're talking to an intelligent peer,** not lecturing down to someone you assume is confused.

5. **Be direct and economical.** Cut any sentence that's about the sentence itself rather than the content.

6. **No nervous hand-holding.** Don't anticipate objections or soften claims unless there's a genuine ambiguity.

**Example of BAD (hedging) writing:**
> "This might seem simple, but actus reus is actually quite complex. You might think it just means 'a bad act,' but it really means something more specific. Here's why this matters: without understanding this distinction, you'll struggle in class."

**Example of GOOD (direct) writing:**
> "Actus reus requires a voluntary act or legally significant omission. Criminal liability needs conduct under the defendant's control, not reflexes or status."

### Intellectual Honesty and Common Sense

**Think critically. Dig deeper. Steelman arguments.**

1. **Probe claims that don't pass the smell test—then dig deeper to find where the theory DOES have bite.**

   If a theoretical framework (like CLS time-framing) is supposed to show "manipulable doctrine," but the examples given are just common sense distinctions, **don't stop there**. Call out the weak examples, then find BETTER examples that actually demonstrate the theory's power.

   - **Bad example (doesn't prove theory):** Decina vs. Martin. It's obvious: driving when you know you have seizures creates danger (voluntary risky choice). Being physically dragged onto a highway by police isn't your choice at all. It would shock the conscience to hold Martin liable or to let Decina walk. These aren't "time-framing games"—they're straightforward moral intuitions.

   - **But then ask:** Where DOES time-framing genuinely matter? Find a fact pattern where reasonable minds could sincerely frame the act two different ways and reach opposite conclusions based solely on framing choice.

2. **Provide concrete, specific fact patterns—not hand-waving gestures.**

   When you claim doctrine is manipulable or a distinction is outcome-determinative, **show it with a real hypothetical**. Example format:

   > **Hypo:** Defendant has a history of seizures but hasn't had one in 5 years. Doctor said "probably safe to drive, but small risk remains." Defendant drives, has unexpected seizure, kills pedestrian.
   >
   > **Narrow frame:** The seizure itself—involuntary, no actus reus.
   > **Broad frame:** The decision to drive with any seizure risk—voluntary, actus reus satisfied.
   >
   > **Key:** Reasonable people could SINCERELY disagree here. The doctor said "probably safe." Is that enough to make driving voluntary risk-creation? Or is a 5-year gap enough to make the seizure truly unforeseeable? **This** is where time-framing has real bite—not in Decina/Martin.

3. **Ask obvious questions when facts are weird.**

   If police are removing someone from their home and placing them on a highway, that's bizarre. Note the oddity and provide context (use web search if needed to understand historical context—was this common practice in 1940s Alabama for removing "undesirables"?). Don't just accept weird facts; explain them.

4. **Distinguish between:**
   - **Weak examples that don't prove the theory** (Decina/Martin don't show manipulability)
   - **Strong examples that DO prove the theory** (find genuine edge cases)
   - **The theory's actual power** (may be valid even if current examples are poor)

5. **Steelman theoretical frameworks.**

   If a professor's theoretical framework (Foucault, CLS, etc.) uses weak examples, don't dismiss the entire framework. Find where it DOES have bite:

   - **CLS time-framing:** Maybe the critique works better for provocation doctrine (when did the "cooling off" period start?) or felony murder (when did the felony end?)
   - **Foucault on carceral power:** Maybe the critique is stronger for probation/parole conditions than for core criminal prohibitions

   Present the **strongest version** of the theoretical position, even if the casebook examples are weak.

6. **For class purposes, arrive at a tenable position that shows sophisticated engagement.**

   Don't just debunk; synthesize. Example:

   > "Kelman's time-framing critique is powerful for genuine edge cases where reasonable minds could sincerely frame the act differently. But Decina/Martin aren't those cases—they're straightforward moral intuitions. Better examples would be: [specific hypo]. The critique shows doctrine provides vocabulary for arguing outcomes, but that's different from proving outcomes are purely arbitrary. Time-framing channels argument; it doesn't eliminate constraints."

**Example of SHALLOW (bad) writing:**
> "Kelman shows that time-framing is outcome-determinative. Courts manipulate whether to use narrow or broad time frames to reach preferred results, proving that doctrine is indeterminate."

**Example of SUPERFICIALLY CRITICAL (better but insufficient) writing:**
> "Kelman argues courts manipulate time frames. But Decina and Martin are just common sense, so the theory is wrong."

**Example of INTELLECTUALLY ENGAGED (good) writing:**
> "Kelman argues courts manipulate time frames to reach preferred outcomes. The canonical examples—Decina and Martin—are poor illustrations. Decina knew he had seizures and drove anyway; holding him liable is straightforward culpability. Martin was physically dragged onto the highway by police; letting him walk is straightforward lack of volition. These aren't 'interpretive games'—they're common-sense moral distinctions.
>
> But Kelman's critique has genuine bite in harder cases. Consider: Defendant had seizures as a teenager, none for 15 years, doctor cleared him to drive. Then an unexpected seizure while driving kills someone. Narrow frame: the seizure was involuntary and unforeseeable. Broad frame: any history of seizures makes driving a knowing risk. Reasonable people could sincerely disagree about which frame is appropriate here. THAT's where time-framing becomes outcome-determinative—not in the easy cases the casebook uses.
>
> The critique shows doctrine is contestable, providing vocabulary for argument rather than mechanical answers. That's different from pure indeterminacy."

### When Writing Audio Preps

**Audio preps must be conversational but not condescending.**

- Write for spoken delivery (natural sentence rhythm, occasional contractions)
- But maintain direct, confident tone
- No phrases like "Let's talk about..." or "Now, here's the thing..."
- Just explain the substance

**Length targets:**
- 25-35 minutes for doctrinal classes
- Detailed case analysis (not bullet-point summaries)
- Anticipate pushback, but don't over-soften

---

## 📚 Course-Specific Context

Each course has its own style and professor:

| Course | Professor | Key Characteristics |
|--------|-----------|---------------------|
| CrimLaw | Harcourt | MPC close reading, ~50% policy, critical theory |
| Property | [See 00_ADMIN] | [Check course_style_guide.md] |
| Torts | [See 00_ADMIN] | [Check course_style_guide.md] |
| Deals | Schizer | Panel discussion format; prep docs should include 'Panel 2' in filename when Panel 2 is on call (e.g., YYYY-MM-DD_classNN_Panel2_text.md); audio preps not required |
| LPW-II | [See 00_ADMIN] | [Check course_style_guide.md] |

**For course specifics:** Read `ACTIVE/{Course}/00_ADMIN/course_style_guide.md` and `exam_spec.md`

---

## ✅ Before Completing Any Task

- [ ] Created file in correct location (per folder structure)
- [ ] Used correct naming convention
- [ ] Followed template structure
- [ ] Updated MASTER_LOG.md status
- [ ] Flagged any missing sources with "[SOURCE NEEDED]"
