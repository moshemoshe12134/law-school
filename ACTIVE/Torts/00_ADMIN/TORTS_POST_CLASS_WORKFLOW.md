# TORTS POST-CLASS WORKFLOW [HUANG EDITION]

**Updated:** 2026-01-29  
**Purpose:** Extract exam-ready material from Huang's fact-heavy, Socratic discussions

**Philosophy:** Huang's exams test your ability to argue both sides using facts. Reviews must extract ARGUMENTATION, not summarize doctrine.

---

## Huang's Exam Format (Verified)

### What You're Preparing For

**Exam Structure:**
- 4 hours, 2 questions (1400 + 1200 words)
- Question 1: Complex fact pattern memo (novel scenario, argue both sides)
- Question 2: Policy/theory question (2 topics, pros/cons)

**What Gets Tested:**
1. **Comprehensive issue-spotting** - Find all potential torts
2. **Both-sides analysis** - Plaintiff arguments → Defense counters
3. **Fact manipulation** - "If X changes, then Y outcome"
4. **Untaken precautions** - BPL analysis
5. **Causation** - But-for, proximate cause, scope of liability
6. **Remedies** - Damages, injunctions, class actions
7. **Policy** (~20%) - Deterrence, corrective justice, efficiency

**Sample exam instructions (verbatim):**
> "Sketch the potential arguments and strategies on **both sides**... If there are any crucial facts we should find out, please say so... Feel free to suggest arguments about how the law **should** treat these facts."

---

## The Critical Shift: From Class Summary to Exam Extraction

### ❌ Old Approach (Don't Do This)

"Today Huang discussed Adams v. Bullock. He explained that Cardozo held..."

### ✅ New Approach (Do This)

"**Exam-ready arguments from today:**

**Plaintiff (little Leo's family):**
- Untaken precautions: (1) higher fence (cost: low, benefit: prevented injury), (2) insulated wire, (3) shield under bridge (already had partial shield, just extend it)
- Foreseeability: Trolley company knew kids play here, had been sued 10x for electrocutions
- Cheapest cost avoider: Company can take precautions cheaper than every kid avoiding wires

**Defense (trolley company):**
- Unforeseeable: Freak accident, who expects 12-year-old with 8-foot wire?
- Prohibitive cost: Cardozo says only way to prevent is bury wire underground = impossible
- Plaintiff's negligence: Leo deliberately tried to hit wire, contributory negligence"

---

## Three-Phase Process

| Phase | Time | Output | Priority |
|-------|------|--------|----------|
| **Phase 1: Ingest** | 2 min | Registered in REVIEW_INDEX | Low |
| **Phase 2: REVIEW** | **40-50 min** | **Exam-ready arguments** | **CRITICAL** |
| **Phase 3: Integrate** | 10 min | Updated outline + hypo bank | High |

**Total:** 50-60 min per class (this IS your exam prep)

---

## Phase 1: Ingest (2 min)

**Command:** `ingest transcripts Torts`

**Purpose:** Register transcript in tracking system

**Steps:**
1. Scan `03_TRANSCRIPTS/raw/` for new files
2. Match date to class number in MASTER_LOG
3. Add to REVIEW_INDEX with status `pending`
4. Keep original filenames (no renaming)

---

## Phase 2: REVIEW - Extract Exam Material (40-50 min)

**Command:** `review Torts` or `review Torts class [NN]`

**Output:** `04_REVIEWS/YYYY-MM-DD_classNN_review.md`

### 🚨 ABSOLUTE ACCURACY REQUIREMENTS

#### Rule 1: Only attribute to Huang what transcript shows
- ❌ "Huang emphasized..." (unless transcript says "This is important")
- ❌ "Huang flagged..." (unless explicit signal)
- ✅ "Class spent 20 minutes on X" (observable)
- ✅ "Huang asked 'What if...' 3 times" (observable)

#### Rule 2: Separate transcript from inference
- Transcript evidence → Quote with line numbers
- Your reasoning → Label as "Doctrinal insight" or "Exam strategy"
- Never blur the line

#### Rule 3: Focus on WHAT arguments were made
- Not "Huang taught negligence"
- But "Plaintiff arguments that got traction: (1) X, (2) Y..."

---

### Review Document Structure (Exam-Focused)

#### SECTION 1: FACT PATTERNS USED

```markdown
## 1. FACT PATTERNS USED

### [Case Name] - How Huang Used It

**The Story (as told in class):**
[2-3 sentences: key facts Huang emphasized]

**What Huang focused on:**
- [Specific fact 1] - He asked "what if this was different?"
- [Specific fact 2] - He dwelled on this for 10+ minutes
- [Untaken precaution] - Multiple students argued about this

**Variations Huang constructed:**
- "What if the pier was 4 feet tall?" → Changes [outcome/argument]
- "What if there was a warning sign?" → [Impact on liability]
- "What if plaintiff was 5 instead of 12?" → [Different standard of care]

**Why this fact pattern matters for exam:**
[This type of scenario = likely exam pattern]
```

#### SECTION 2: ARGUMENTS DEVELOPED IN CLASS

```markdown
## 2. ARGUMENTS DEVELOPED IN CLASS

### Plaintiff's Side

#### Argument 1: [Specific untaken precaution]
- **Student who made it:** [Name if relevant]
- **How Huang responded:** [Pushed back? Accepted? Developed further?]
- **BPL analysis as discussed:**
  - Burden: [Cost of precaution discussed]
  - Probability: [Likelihood of harm discussed]
  - Loss: [Magnitude of injury discussed]
- **Counter-arguments raised:** [Defense responses]

#### Argument 2: [Foreseeability]
- **Key phrase from class:** "[Direct quote]"
- **Evidence discussed:** [Prior incidents, industry knowledge, etc.]
- **How to use on exam:** When fact pattern involves [trigger]

### Defense Side

#### Counter-argument 1: [Prohibitive cost]
- **How framed in class:** [Specific language]
- **Evidence/reasoning:** [Economic impact, feasibility, etc.]
- **Plaintiff's response:** [How they countered]

#### Counter-argument 2: [Unforeseeable harm]
- **Key phrase:** "[Direct quote from class]"
- **Cardozo rhetoric discussed:** [How defense uses impossibility argument]

### Both-Sides Balance

**Where arguments were roughly equal:**
- [Issue where no clear winner]
- Exam implication: Must present BOTH sides thoroughly

**Where one side dominated:**
- [Argument that clearly won]
- Exam implication: Can conclude more confidently here
```

#### SECTION 3: JURY INSTRUCTION LANGUAGE

```markdown
## 3. JURY INSTRUCTION LANGUAGE

### Instructions Read/Discussed

**Illinois [Section Number]:**
"[Exact text if Huang read it]"

**How Huang parsed it:**
- Element 1: [His explanation]
- Element 2: [His explanation]
- Standard: [How he framed "reasonable person"]

**Key phrases to use on exam:**
- "reasonable person under circumstances similar to those shown by evidence"
- "[Other exact jury instruction language]"

### Objective vs. Subjective Discussion

**What circumstances CAN be considered:**
- [Age, mental capacity, experience - for children]
- [Physical disability - if relevant]

**What CANNOT be considered:**
- [Defendant's actual thoughts/intentions]
- [Defendant's specific capabilities beyond standard]
```

#### SECTION 4: FACT MANIPULATION TECHNIQUES

```markdown
## 4. FACT MANIPULATION TECHNIQUES

### Technique 1: "What more facts would we want?"

**Facts Huang asked about:**
- [Fact 1] - This matters because [impact on liability]
- [Fact 2] - Discovery focus: shows [foreseeability/custom/etc.]

**How to deploy on exam:**
"It would be useful to know whether [X]. If [X is true], then plaintiff wins because [Y]. If [X is false], then defense wins because [Z]."

### Technique 2: Precaution variations

**Precautions discussed:**
- [Precaution 1]: Cost [high/low], Effectiveness [high/low]
- [Precaution 2]: Custom argument - [who does this]
- [Precaution 3]: Regulatory argument - [standard]

**How to deploy on exam:**
"Defendant failed to take reasonable precautions such as [X], which would have cost [low/high] but prevented [injury]. By contrast, [alternative precaution Y] would have been prohibitively costly because [reason]."

### Technique 3: Changing one fact

**Fact changes from class:**
| Original Fact | Changed To | Impact |
|---------------|-----------|--------|
| [Fact 1] | [Variation] | [Outcome shifts plaintiff/defense] |
| [Fact 2] | [Variation] | [Changes foreseeability] |

**Pattern recognition:**
When exam gives you [type of fact], consider arguing [variation]
```

#### SECTION 5: EXAM SIGNALS

```markdown
## 5. EXAM SIGNALS

### Explicit Signals
- [Direct quote with transcript line]: "This will be on the exam"
- [Reference to past exam]: "I've tested this before as..."
- [Time allocation]: Spent 25 minutes on [topic] (= important)

### Implicit Signals
- **Multiple hypos on same issue** - [Topic] had 4 variations = likely exam focus
- **Both-sides couldn't resolve** - [Issue] debated heavily = exam will test this
- **"Issues of first impression" language** - Huang said "no cases on this yet" = exam pattern
- **Policy discussion depth** - [Topic] got 10 min policy = Question 2 material

### Patterns Matching Past Exams
- **Novel technology scenario** - [Discussed AI/robots/new tech] = 2017/2018 exam pattern
- **Class action discussion** - [Certification issues] = always in exams
- **Causation complexity** - [Multiple causes, lost chance] = frequently tested

**Tag for tracking:** #EXAM_SIGNAL
```

#### SECTION 6: PREWRITE FRAGMENTS (CRITICAL OUTPUT)

```markdown
## 6. PREWRITE FRAGMENTS

### Fragment 1: [Topic] Issue-Spotter

**Trigger:** When exam presents [type of scenario]

**Prewrite paragraph (ready to adapt):**

[Plaintiff's name] may argue that [Defendant] was negligent in failing to [untaken precaution]. Under the reasonable person standard, a reasonably careful [defendant type] would have [specific action] because [reason tied to BPL]. The burden of [precaution] was [low/reasonable] as evidenced by [custom/industry practice/cost analysis]. The probability of [injury type] was [high/foreseeable] given [prior incidents/known dangers]. The magnitude of loss was [severe] as shown by [injury description]. Here, [apply to specific facts].

However, [Defendant] can counter that [defense argument]. The precaution was [prohibitively costly/unforeseeable/etc.] because [specific reasoning]. [Additional defense points using fact variations].

**Magic words to include:**
- "reasonable person under circumstances similar to those shown by evidence"
- "untaken precautions"
- "[Specific phrase Huang used repeatedly]"

### Fragment 2: Causation Analysis

**Trigger:** When multiple causes or proximate cause issue

**Prewrite paragraph:**

[Adapt based on today's causation discussion]

### Fragment 3: [Additional topics as covered]

[Continue for each major issue covered in class]
```

#### SECTION 7: OUTLINE INSERTS

```markdown
## 7. OUTLINE INSERTS (Copy-Paste Ready)

### For Negligence Section

**Rule:** [As Huang framed it, with jury instruction cite]

**Reasonable Person Standard - Huang's Emphasis:**
- Objective test, but "under circumstances"
- [Specific circumstances that CAN be considered]
- [Specific circumstances that CANNOT]

**Untaken Precautions Framework:**
1. Identify what defendant didn't do
2. Cost-benefit analysis (BPL)
3. Custom/industry practice comparison
4. Foreseeability of risk
5. Magnitude of potential harm

**Case Example:** *[Case name]* - [1 sentence holding in Huang's words]
- Facts: [Key facts]
- Plaintiff argued: [Arguments from class]
- Defense argued: [Arguments from class]
- Use on exam when: [Trigger scenario]

### For [Other sections as applicable]

[Continue for each doctrinal section covered]
```

#### SECTION 8: HYPO BANK ADDITIONS

```markdown
## 8. HYPO BANK ADDITIONS

### Hypo 1: [From class discussion]

**Facts:** [Scenario Huang constructed or student proposed]

**Issue:** [Legal question]

**Plaintiff argues:**
- [Argument 1 with BPL analysis]
- [Argument 2 with foreseeability]

**Defense argues:**
- [Counter 1]
- [Counter 2]

**Likely outcome:** [Based on class discussion]

**Why this hypo matters:** [Pattern recognition for exam]

### Hypo 2-5: [Continue for each hypo discussed]

[These are GOLD for exam prep - Huang's hypos = exam patterns]
```

#### SECTION 9: CORRECTIONS TO PREP

```markdown
## 9. CORRECTIONS TO PREP

### What prep missed
- [Topic Huang spent 15+ min on that wasn't emphasized in prep]
- [Argument angle prep didn't include]

### What prep over-emphasized
- [Topic prep focused on but Huang barely mentioned]

### Better framing for next time
- Focus more on [X]
- De-emphasize [Y]
- Add [Z] argument type to standard prep template
```

---

## Process Steps (40-50 min)

### Step 1: Read Transcript (10-12 min)

**Mark as you read:**
- [ ] Arguments that got traction (plaintiff side)
- [ ] Counter-arguments (defense side)
- [ ] Fact variations Huang constructed
- [ ] "What if" questions
- [ ] Time allocation (topics with 10+ min)
- [ ] Exam signals (explicit or implicit)

### Step 2: Extract Arguments (10-12 min)

**For each major issue:**
1. Plaintiff's best arguments (from class discussion)
2. Defense counter-arguments (from class discussion)
3. How Huang framed the tension
4. Which side seemed stronger (if any)

**Format:** Ready-to-use on exam

### Step 3: Document Fact Manipulation (5 min)

**Capture:**
- Original facts → Variations discussed
- "What more facts" questions raised
- Impact of each fact change on outcome

**Purpose:** Learn Huang's fact manipulation patterns

### Step 4: Create Prewrite Fragments (12-15 min)

**THE MOST IMPORTANT STEP**

**Minimum:** 1 full paragraph per major issue
**Format:** Both-sides IRAC
**Language:** Use exact phrases from class

**Must be:** Ready to paste into exam answer (with light adaptation)

### Step 5: Build Outline Inserts (3-5 min)

**Copy-paste ready blocks:**
- Rules as Huang framed them
- Case holdings in his language
- Argument frameworks that worked

### Step 6: Update Hypo Bank (3-5 min)

**Add every hypo from class:**
- Huang's constructed variations
- Student-proposed scenarios
- Both-sides analysis

### Step 7: Note Corrections (2-3 min)

**What to adjust:**
- Prep emphasis misalignments
- Arguments to add to future preps
- Doctrinal framings to correct

---

## Quality Control Checklist

### Accuracy
- [ ] No Huang attributions without transcript evidence
- [ ] Quotes marked as quotes with line numbers
- [ ] Inferences labeled as "Doctrinal insight" or "Exam strategy"
- [ ] Sources cited for all claims

### Completeness (Must-Haves)
- [ ] Section 2: Arguments from BOTH sides (not just one)
- [ ] Section 6: At least 2 prewrite fragments (exam-ready paragraphs)
- [ ] Section 7: At least 1 outline insert (or note "no updates")
- [ ] Section 8: All hypos from class documented
- [ ] Section 5: Exam signals tagged

### Exam-Readiness
- [ ] Prewrite fragments use Huang's exact language
- [ ] Arguments structured: Plaintiff → Defense → Counter-counter
- [ ] BPL analysis included where applicable
- [ ] Fact variations documented
- [ ] "What more facts" questions captured
- [ ] Both-sides balance maintained

---

## Phase 3: Integrate (10-15 min)

**Command:** `integrate review Torts class [NN]`

### Step 3.1: Update Outline

**Location:** `05_OUTLINE/[relevant sections]`

1. Paste outline inserts from Section 7
2. Add case examples with Huang's language
3. Tag exam signals
4. Integrate argument frameworks

### Step 3.2: Add to Hypo Bank

**Location:** `06_PREWRITES/HYPO_BANK.md`

1. Paste all hypos from Section 8
2. Mark source: "Class [NN] - [Date]"
3. Tag by doctrine area
4. Note exam relevance

### Step 3.3: Add to Prewrite Bank

**Location:** `06_PREWRITES/PREWRITES_BANK.md`

**Format:**

```markdown
## [Doctrine Name] - Issue-Spotter Prewrite

**Source:** Class [NN] (YYYY-MM-DD)

**Trigger:** When exam presents [scenario type]

**Prewrite paragraph (both-sides):**
[The polished paragraph from Section 6, ready for exam]

**Key arguments to include:**
- Plaintiff: [List from class]
- Defense: [List from class]

**Magic words:**
- [Huang's exact phrases]
- [Jury instruction language]
```

### Step 3.4: Update Tracking

**REVIEW_INDEX.md:**
- Status: `pending` → `integrated`
- Count prewrites added
- Count hypos added

**MASTER_LOG.md:**
- Mark `Review?` as ✅
- Mark `Outline?` as ✅
- Record exam signals count
- Update `Next_Action`

---

## Weekly Synthesis (Sunday, 90 min)

### Purpose: Convert Raw Reviews into Polished Exam Material

**Every Sunday:**

#### Task 1: Review Week's Prewrites (20 min)
- Read all prewrite fragments from that week
- Identify overlaps and gaps
- Note common argument patterns

#### Task 2: Polish into Full Prewrites (45 min)
- Take 4-6 fragments
- Expand into complete both-sides analysis
- Add fact variations
- Incorporate multiple class discussions
- Format as exam-ready paragraphs

#### Task 3: Hypo Practice (25 min)
- Take 2-3 hypos from week's bank
- Write out full analysis (timed: 10 min each)
- Compare to class discussion
- Refine approach

---

## Time Allocation Guide

**For typical 75-minute Huang class:**

| Task | Time | % of Effort | Priority |
|------|------|-------------|----------|
| Read transcript | 10 min | 20% | Medium |
| Extract both-sides arguments | 12 min | 25% | HIGH |
| Draft prewrite fragments | 15 min | 30% | CRITICAL |
| Build outline inserts | 5 min | 10% | Medium |
| Document fact manipulation | 4 min | 8% | High |
| Update hypo bank | 3 min | 6% | High |
| **Total** | **49 min** | **100%** | |

**The prewrite fragments ARE your exam prep.** This is where 30% of time goes.

---

## Anti-Patterns to Avoid

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Summarize what Huang said | Extract arguments students made |
| Focus on doctrine lecture | Focus on argumentation practice |
| Note "Huang emphasized X" without proof | Quote transcript or note observable signals |
| Create one-sided arguments | Always extract BOTH plaintiff and defense |
| Skip prewrite fragments | This is THE critical output |
| Wait to integrate | Do same day while fresh |

---

## Agent Instructions Summary

```
FOR HUANG TORTS REVIEWS:

GOAL: Extract exam-ready argumentation (NOT summarize class)

CRITICAL OUTPUTS (in order of importance):
1. Prewrite fragments (Section 6) - 2+ paragraphs, both-sides, exam-ready
2. Arguments from class (Section 2) - Plaintiff AND defense
3. Hypo bank additions (Section 8) - Every hypo discussed
4. Outline inserts (Section 7) - Huang's language/framing
5. Fact manipulation techniques (Section 4) - Variations discussed

HUANG-SPECIFIC REQUIREMENTS:
- Focus on FACTS over doctrine
- Extract untaken precautions with BPL analysis
- Document "what if" variations
- Capture both-sides arguments (never one-sided)
- Include jury instruction language
- Note "what more facts" questions
- Tag exam signals (#EXAM_SIGNAL)

ACCURACY:
- Only attribute to Huang what transcript shows
- Separate transcript evidence from your inferences
- Quote with line numbers
- Label reasoning as "Doctrinal insight" or "Exam strategy"

PREWRITE FRAGMENT FORMAT:
- Full paragraph (not outline)
- Both plaintiff AND defense arguments
- BPL analysis where applicable
- Fact-specific (tied to class discussion)
- Uses Huang's exact language
- Ready to adapt for exam (paste + modify)

TIME ALLOCATION:
- 30% on prewrite fragments (THE MOST IMPORTANT)
- 25% on extracting arguments
- 20% on reading transcript
- 25% on everything else
```

---

*Last Updated: 2026-01-29 (Huang Edition)*
