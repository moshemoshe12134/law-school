# IMPLEMENTATION ROADMAP
## From Multiple Outlines to One Master Outline

---

## Quick Start (What to Do First)

**TL;DR**: Follow this order:
1. **Week 1**: Build `_REGISTRY_Cases.md` (extract + validate all cases)
2. **Weeks 2-4**: Build `MASTER_Comprehensive_Outline.md` (topic by topic)
3. **Weeks 3-5**: Build `_CASES_[Topic].md` files (case library by topic)
4. **Week 5**: Build `MASTER_Attack_Outline.md` (condense to essentials)
5. **Week 5-6**: Build `_SOURCE_CROSSWALK.md` (validate everything)

---

## PHASE 1: CASE REGISTRY (Week 1) — 5-8 Hours

### Goal
Create a **single authoritative list of all Property cases** with metadata, so you can:
- Link from outline to case without duplication
- Validate that each case appears in your textbook
- Mark which cases are high-yield (exam frequency)
- Never lose a case citation again

### Step 1.1: Extract All Cases from Existing Outlines

**Input**: 6 existing outlines in `07_OUTLINE/`:
- `F19_Outline.md`
- `Glass_Property_F19_Outline.md`
- `Glass_Property_S19_Outline.md`
- `Glass_Property_S19_Rules.md`
- `Glass_Property_S19_Themes.md`
- `Glass_Property_S21_Outline(Shulman).md`

**Process**:
1. Open each outline
2. Extract case names (in alphabetical order to avoid dups)
3. Create running list with format:
   ```
   Case Name | Full Citation | Jurisdiction | Year | Mentioned in [which outline(s)]
   ```

**Output**: Unsorted list of ~80-100 cases

**Time**: ~2 hours

---

### Step 1.2: Find Each Case in Textbook

**Input**: Your Singer, Berger & Davidson Property textbook (8th ed.)

**Process**:
1. For each case on list:
   - Use textbook index or search
   - Find page numbers where case appears
   - Note: Case may appear on multiple pages (extended discussion, cite, hypo)
   
2. Update format:
   ```
   Case Name | Citation | Textbook Pages | Topics Covered
   ```

**Validation Check**: 
- All cases should appear in Singer (~90% rule; some may be supplement/E&E)
- If case doesn't appear → Flag for review (may be reference-only case from prior outline)

**Output**: Verified case list with page numbers

**Time**: ~3 hours (quick scan of index + 30 sec per case)

---

### Step 1.3: Identify Topic Tags

**Process**:
1. For each case, note which doctrine(s) it primarily establishes
   - Example: *Pierson v. Post* → Tags: "First Possession", "Labor Theory", "Fairness Theory"
   
2. Use topic hierarchy from architecture:
   ```
   Unit I.A - First Possession
   Unit I.B - Labor Theory
   Unit II.A - Trespass
   Unit II.B - Adverse Possession
   Unit III.A - Concurrent Ownership
   ... [etc.]
   ```

**Output**: Case list with topic tags

**Time**: ~1 hour

---

### Step 1.4: Mark Exam Frequency

**Input**: Past exams in `02_SOURCES/exams_raw/`
- 1 Glass exam (with model answer)
- 2 Heller exams (with model answers)
- 11 Merrill exams (various years)

**Process**:
1. Scan past exam questions + model answers
2. Every time a case is cited/discussed, increment case counter
3. Score cases as:
   - **HIGH**: Appears 4+ times across 14 exams (10+ occurrences)
   - **MEDIUM**: Appears 1-3 times (3-9 occurrences)
   - **LOW**: Appears 0-1 times (<3 occurrences)

**Output**: Case list with exam frequency flag

**Time**: ~2 hours (scan model answers for case citations)

---

### Step 1.5: Create _REGISTRY_Cases.md

**Template**:
```markdown
# MASTER CASE REGISTRY

## [A-Z Alphabetical Index]

### Armory v. Delamarie
- **Citation**: (1722)
- **Jurisdiction**: England
- **Year**: 1722
- **Textbook Pages**: Singer 8th ed., pp. 86-92
- **Topics**: Finding; Relativity of Title; Possessory Interests
- **Holding**: Finder of goods has superior possessory rights to all except true owner; subsequent possessor cannot claim against finder.
- **Exam Frequency**: MEDIUM (appears in 3 past exams)
- **Related Cases**: *Wilcox v. Stroup*, *Charrier v. Bell*

### Brown v. Gobble
- **Citation**: 474 S.E.2d 489 (W. Va. 1996)
- **Jurisdiction**: West Virginia
- **Year**: 1996
- **Textbook Pages**: pp. XXX
- **Topics**: Adverse Possession; Tacking
- **Holding**: [One sentence]
- **Exam Frequency**: HIGH
- **Related Cases**: [Others]

[... continue alphabetically ...]

## [Topic Index]

### Unit I: Acquiring Property
- *Pierson v. Post*
- *Popov v. Hayashi*
- *I.N.S. v. Associated Press*
- [etc.]

### Unit II: Right to Exclude
- [Cases related to trespass, AP, easements]

[... organize by unit ...]

## [Notes]
- Total cases indexed: ~85
- HIGH frequency: ~25 cases
- Gaps identified: [Any cases from E&E not in textbook?]
```

**Deliverable**: File `_REGISTRY_Cases.md` (~3-4 pages)

**Time**: ~1 hour (compile formatted data)

---

### Phase 1 Checklist
- [ ] Extracted all cases from 6 outlines
- [ ] Found page numbers in Singer for ~90% of cases
- [ ] Tagged with doctrine areas
- [ ] Scored exam frequency from past exams
- [ ] Created `_REGISTRY_Cases.md`
- [ ] Validated: no obvious duplicates or errors

**Phase 1 Complete When**: You can open `_REGISTRY_Cases.md` and find any case in 10 seconds

---

## PHASE 2: MASTER COMPREHENSIVE OUTLINE (Weeks 2-4) — 20-30 Hours

### Goal
Create a **single, authoritative outline** that:
- Consolidates all 6 existing outlines into one voice
- Adds depth from textbook that existing outlines miss
- Links every case to Registry (no duplication)
- Includes policy rationales (not just rules)
- Shows hypo applications (exam patterns)

### Step 2.1: Choose Your Unit Order

**Recommended**: Follow Singer textbook chapter order (it's organized logically)

**Alternative**: Follow existing outlines' order (check if they align)

**Your Choice**: [Decide based on your syllabus]

---

### Step 2.2: Topic by Topic (Repeat for I.A → V.C)

**For each doctrine (Example: I.A - First Possession):**

#### 2.2a: Read All Versions
- Open each of 6 outlines
- Find how they discuss this topic
- Note:
  - Points of agreement
  - Points of disagreement
  - Variations in rule statement
  - Cases each cites

**Time per topic**: ~30 min

#### 2.2b: Read Textbook Section
- Find corresponding Singer chapter(s)
- Note:
  - What policy rationales does Singer emphasize?
  - What cases does Singer prioritize?
  - Are there nuances outlines missed?
  - What hypo examples does Singer give?

**Time per topic**: ~30 min

#### 2.2c: Reconcile Conflicts
- If outlines disagree, which version is "right"?
  - Check Singer: Does textbook favor one version?
  - Check case law: Is one version better-supported?
  - Mark if genuine ambiguity (acknowledge both interpretations)

**Examples of conflicts to watch for**:
- "Is X element required for Y rule?" (Maybe varies by jurisdiction)
- "Which case is foundational?" (Might be competing doctrines)
- "How do courts apply this?" (Different approaches)

**Time per topic**: ~20 min

#### 2.2d: Write Master Version
- Draft unified doctrine explanation using template from `MASTER_Comprehensive_Outline_EXAMPLE.md`
- Format:
  1. One-sentence rule
  2. Elements/Test (numbered)
  3. Source authority (cases → Registry; statutes; Restatement)
  4. Key cases (2-3 most important, with facts + holding)
  5. Statutory/Restatement text
  6. Policy rationales (why this rule?)
  7. Common applications (hypo patterns)
  8. Variations/exceptions
  9. Cross-references (to other doctrines)

**Time per topic**: ~60 min (first few); ~30 min (gets faster)

#### 2.2e: Validate
- Does rule make sense?
- Can you find all cited cases in Registry?
- Are page numbers correct?
- Did you explain "why" (policy), not just "what" (rule)?

**Time per topic**: ~10 min

---

### Step 2.3: Build the Hierarchy

**Total Topics to Cover** (~30-40 major doctrines):

**Unit I: Acquiring & Justifying Property** (~8 doctrines)
- I.A First Possession
- I.B Labor / Information goods
- I.C Acquisition by Transfer
- I.D Copyright/Patent
- I.E (others specific to your course)

**Unit II: Right to Exclude** (~6 doctrines)
- II.A Trespass
- II.B Adverse Possession
- II.C Prescriptive Easements
- II.D Public Accommodations Law
- II.E First Amendment/Public Trust
- II.F (others)

**Unit III: Sharing Property** (~10 doctrines)
- III.A Concurrent Ownership
- III.B Marital Property
- III.C Estates System
- III.D Leaseholds
- III.E Fair Housing
- (others per your syllabus)

**Unit IV: Privilege to Use** (~8 doctrines)
- IV.A Nuisance
- IV.B Easements (Express)
- IV.C Easements (Implied)
- IV.D Covenants
- IV.E Zoning
- (others)

**Unit V: Immunity from Loss** (~4 doctrines)
- V.A Eminent Domain
- V.B Regulatory Takings
- V.C Per Se Takings
- V.D (others)

**Time Estimate**: 
- 30-40 topics × ~90 min/topic = 45-60 hours
- Compressed to 3 weeks = 15-20 hours/week = 3-4 hours/day

---

### Step 2.4: Insert Template Format

Use this structure for EACH topic in `MASTER_Comprehensive_Outline.md`:

```markdown
### [TOPIC CODE] [TOPIC NAME]

#### Black Letter Rule
[One sentence: "X rule means Y result when Z condition is met"]

#### Elements/Test
[Numbered list: To establish X, show 1) ..., 2) ..., 3) ...]
- Each element has: Definition, Source, Ambiguity

#### Source Authority
[List of key cases with Registry links + statutes + Restatement]

#### Key Cases
[2-3 most important cases: Facts, Holding, Significance]

#### Statutory/Restatement Text
[Full text of relevant statute/restatement section]

#### Policy Rationales
[Why courts chose this rule; competing policies]

#### Common Applications / Hypo Triggers
[Patterns that trigger this rule on exams]

#### Variations & Exceptions
[Edge cases and nuances]

#### Cross-References
[Links to other doctrines: builds on, contrasts with, building block for]

---
```

---

### Phase 2 Checklist (Per Topic)
- [ ] Read how all 6 outlines discuss this topic
- [ ] Read textbook section
- [ ] Resolved conflicts (picked "best" version or acknowledged ambiguity)
- [ ] Wrote master version (~500-1500 words)
- [ ] Linked all cases to Registry
- [ ] Included policy rationale (not just rule)
- [ ] Listed hypo applications
- [ ] Added cross-references

**Phase 2 Complete When**: `MASTER_Comprehensive_Outline.md` is 40-50 pages, covering all major doctrines, with every case linked to Registry

---

## PHASE 3: CASE LIBRARY FILES (Weeks 3-5) — 10-15 Hours

### Goal
Create **topic-specific case files** (`_CASES_[Topic].md`) for deep reference:
- Full write-ups of important cases
- Extracted from existing outlines + supplemented from textbook
- Enable quick lookup by topic
- Support deep study without cluttering main outline

### Step 3.1: Create Files by Topic

**Create one file per major doctrine**:
- `_CASES_FirstPossession.md` (contains: Pierson, Popov, maybe 2-3 others)
- `_CASES_AdversePossession.md` (Brown v. Gobble, etc.)
- `_CASES_Trespass.md`
- `_CASES_Easements.md`
- etc.

---

### Step 3.2: Extract Case Write-Ups

**For each case in a topic file**:

1. **Extract from existing outlines** (if they have detailed case write-ups)
   - Does *Pierson v. Post* appear as a detailed section in any outline?
   - Copy the write-up (with citation to source outline)

2. **Supplement from textbook**
   - Read case in Singer
   - Add any missing facts, reasoning, or policy context
   - Note page numbers

3. **Format consistently**:
   ```markdown
   ## [Case Name] ([Citation]) - [Jurisdiction/Year]
   
   **Textbook Location**: Singer 8th ed., pp. XXX
   
   **Rule Established**: [One sentence]
   
   **Full Facts**: [2-3 sentences]
   
   **Procedural Posture**: [Court level, what lower court decided]
   
   **Holding**: [What court decided]
   
   **Reasoning**: [Key analytical points]
   
   **Policy Implications**: [Why rule matters]
   
   **Related Cases**: [Other cases that apply/distinguish]
   
   **Exam Frequency**: HIGH/MEDIUM/LOW
   
   **Hypo Applications**: [How this typically appears on exams]
   ```

**Time per case**: ~15-30 min (depending on complexity)

---

### Step 3.3: Link from Main Outline

In `MASTER_Comprehensive_Outline.md`, update case citations to link:

```markdown
#### Key Cases

**[*Pierson v. Post*](./_CASES_FirstPossession.md#pierson-v-post)** (NY 1805)
- **Facts**: [Brief summary]
- [Link to full write-up in _CASES_FirstPossession.md]
```

---

### Phase 3 Checklist
- [ ] Created 8-10 `_CASES_[Topic].md` files
- [ ] Extracted case write-ups from existing outlines
- [ ] Supplemented from textbook for missing detail
- [ ] Formatted consistently
- [ ] Linked from main outline
- [ ] High-yield cases (50+) have detailed write-ups

**Phase 3 Complete When**: Can click through from any outline topic to detailed case write-up in <2 seconds

---

## PHASE 4: ATTACK OUTLINE (Week 5) — 5-8 Hours

### Goal
Create a **5-15 page condensed version** suitable for exam day:
- Issue-spotter checklists
- Element lists (minimal prose)
- Case names only (no facts)
- Statute numbers only (no full text)
- Hypo triggers

### Step 4.1: Start from Master Comprehensive

**For each major topic**:
1. Open corresponding Comprehensive section
2. Extract: Rule (1 sentence) + Elements (list form)
3. Condense everything else:
   - Policy → delete
   - Case facts → keep case NAME ONLY
   - Cross-references → keep only critical ones
   - Hypo applications → keep TRIGGER WORDS

### Step 4.2: Format for Exam Use

**Target format** (~0.5-1 page per topic):

```markdown
## I.A First Possession

**Rule**: First to reduce unowned object to actual possession owns it.

**Elements**:
1. Unowned property (not currently owned by anyone)
2. Intent to possess
3. Actual reduction to possession (varies by object: kill animal, find object, etc.)

**Key Cases**: 
- *Pierson v. Post* — Killing > chasing
- *Popov v. Hayashi* — Pre-possessory interest (modern exception)

**Statute/Restatement**: Common law (no statute); Restatement § X.X

**Hypo Triggers**:
- Multiple people competing for same unowned thing
- Question: Who did it first?
- Competing evidence: Labor/effort vs. actual control

**Quick Test for Exams**:
- [ ] Is the object truly UNOWNED? (If on someone's land or owned, different rules apply)
- [ ] Did someone INTEND to possess it?
- [ ] Did they ACTUALLY reduce to possession? (Type of object matters)
- [ ] Who did this first?

**Variation**: *Popov* allows pre-possessory interest (effort + proximity) in some jurisdictions
```

### Step 4.3: Create Table of Contents

Keep complete TOC (so you can find topics fast):
```markdown
# ATTACK OUTLINE

## UNIT I: ACQUIRING PROPERTY
- I.A First Possession (p. 1)
- I.B Labor / Information (p. 2)
- [etc.]

## UNIT II: RIGHT TO EXCLUDE
[etc.]
```

### Step 4.4: Format for Printing

**Optimization**:
- Single-spaced or 1.5-spaced (more content per page)
- Minimal margins (but readable)
- Numbered sections (easy reference: "See I.A line 3")
- If you use colors: make sure printer-friendly
- Aim for 5-15 pages total (most common: 8-12 pages)

---

### Phase 4 Checklist
- [ ] Condensed each major topic to 0.5-1 page
- [ ] Included: Rule, Elements, Case names, Statute #'s, Hypo triggers
- [ ] Removed: Policy details, case facts, verbose explanations
- [ ] Created complete TOC
- [ ] Formatted for printing (readable, compact)
- [ ] Total length: 5-15 pages

**Phase 4 Complete When**: Can print, read one page (5 min), spot issue on hypo question (1-2 min)

---

## PHASE 5: SOURCE CROSSWALK (Weeks 5-6) — 3-5 Hours

### Goal
Create **_SOURCE_CROSSWALK.md** that maps:
- **Outline Topic** → **Textbook Page** → **Case Names**

So you can:
- Validate every claim against source material ("Is this really in Singer?")
- Find topic in textbook without searching
- Trace doctrine back to original source

### Step 5.1: Template Structure

```markdown
# SOURCE CROSSWALK

## Singer, Berger & Davidson (8th ed.) - Property Law

### CHAPTER 1: Acquiring Ownership

**Outline Topic**: Unit I.A First Possession
**Textbook Pages**: pp. 1-150
**Main Cases in Singer**:
- *Pierson v. Post* (pp. 45-67) → Outline Section I.A
- *Popov v. Hayashi* (pp. 68-85) → Outline Section I.A, Variation
- *Armory v. Delamarie* (pp. 92-100) → Outline Section I.B
**Hypo Examples in Singer**: pp. 110-120 (various examples)
**Key Policy Discussion**: pp. 34-44 (fairness vs. efficiency)

### CHAPTER 2: Trespass & Possession

**Outline Topic**: Unit II.A Trespass
**Textbook Pages**: pp. 151-250
**Main Cases in Singer**:
[etc.]

## Examples & Explanations - Property (Burke & Myers, 5th ed.)

### Chapter X: [Topic]
**Outline Topic**: Unit [X].[Y]
**E&E Pages**: pp. XXX
**Hypo Examples**: 
- Hypo X.Y → pp. XXX
- [etc.]

## Statutes & Restatement

### Restatement (Third) of Property
- § X.X (First Possession) → Outline I.A
- § Y.Y (Trespass) → Outline II.A
- [etc.]

## Validation Summary

| Outline Unit | Textbook Sections | Case Count | Validated? |
|--------------|------------------|-----------|-----------|
| Unit I.A | pp. 1-150 | 3 | ✓ |
| Unit I.B | pp. 151-200 | 2 | ✓ |
| [etc.] | | | |

**Total**: All outline topics traceable to Singer
**Completeness**: 95%+ of outline claims verified in textbook
```

### Step 5.2: Build by Reading Through Singer

1. Read Singer Chapter by Chapter
2. For each chapter, note:
   - Which outline topics it covers
   - Page ranges
   - Main cases
   - Hypo examples

3. Update Crosswalk as you go

---

### Step 5.3: Spot-Check Random Topics

**Validation**:
- Pick 5-10 random topics from master outline
- For each:
  - Open Crosswalk
  - Find textbook pages
  - Skim textbook pages
  - Verify: "Is the rule as I stated it?"
  - Fix any discrepancies

---

### Phase 5 Checklist
- [ ] Created `_SOURCE_CROSSWALK.md`
- [ ] Mapped all major outline topics to textbook chapters
- [ ] Listed page ranges and main cases per topic
- [ ] Validated 5+ random topics against textbook
- [ ] Created summary table (✓ = verified)

**Phase 5 Complete When**: Can open Crosswalk, find any outline topic, go to textbook page, and find relevant case/discussion within 1 minute

---

## FINAL VALIDATION & QA

### Checklist Before "Done"

**Master Outline**:
- [ ] Every major doctrine covered
- [ ] Every case links to Registry
- [ ] Every rule has: elements, policy, hypo trigger, cross-reference
- [ ] No conflicting statements
- [ ] 40-50 pages total

**Case Registry**:
- [ ] All cases from 6 outlines included
- [ ] Page numbers verified in Singer
- [ ] Exam frequency marked
- [ ] Organized alphabetically + by topic
- [ ] 3-4 pages

**Case Library Files**:
- [ ] 1 file per major doctrine
- [ ] High-yield cases (~50+) detailed
- [ ] Linked from master outline
- [ ] 15-20 pages total

**Attack Outline**:
- [ ] 1 page per 2-3 topics (5-15 pages total)
- [ ] Printable format
- [ ] Can issue-spot from it in 2 minutes

**Source Crosswalk**:
- [ ] All outline topics mapped to textbook pages
- [ ] 90%+ of cases verified
- [ ] Validation table created

---

## File Checklist (What Should Exist)

After all phases complete, your `07_OUTLINE/` folder should have:

```
├── OUTLINE_ARCHITECTURE.md ..................... ✓ (Already created)
├── ARCHITECTURE_SUMMARY.md ..................... ✓ (Already created)
├── MASTER_Comprehensive_Outline_EXAMPLE.md .... ✓ (Already created)
│
├── MASTER_Comprehensive_Outline.md ............ [To Build - Phase 2]
├── MASTER_Attack_Outline.md ................... [To Build - Phase 4]
│
├── _REGISTRY_Cases.md ......................... [To Build - Phase 1]
├── _SOURCE_CROSSWALK.md ....................... [To Build - Phase 5]
│
├── _CASES_FirstPossession.md .................. [To Build - Phase 3]
├── _CASES_AdversePossession.md ................ [To Build - Phase 3]
├── _CASES_Trespass.md ......................... [To Build - Phase 3]
├── _CASES_Easements.md ........................ [To Build - Phase 3]
├── _CASES_Covenants.md ........................ [To Build - Phase 3]
├── _CASES_Nuisance.md ......................... [To Build - Phase 3]
├── _CASES_Zoning.md ........................... [To Build - Phase 3]
├── _CASES_Estates.md .......................... [To Build - Phase 3]
├── _CASES_Leasehold.md ........................ [To Build - Phase 3]
├── _CASES_Takings.md .......................... [To Build - Phase 3]
│
├── [ARCHIVE] ............................... [Move old files here]
│   ├── F19_Outline.md
│   ├── Glass_Property_F19_Outline.md
│   ├── [etc.]
│
├── attack/ .................................. [Existing - keep as-is]
├── hypos/ ................................... [Existing - populate later]
│
└── README.md ................................ [Keep existing]
```

---

## Weekly Tracking

### Week 1 (Registry)
- **Mon-Tue**: Extract all cases from 6 outlines
- **Wed-Thu**: Find page numbers in Singer
- **Fri**: Tag topics + exam frequency; compile `_REGISTRY_Cases.md`
- **Deliverable**: `_REGISTRY_Cases.md` (complete, validated)

### Weeks 2-4 (Comprehensive Outline)
- **Daily**: 1 doctrine per day (Mon-Fri) = 5 docs/week × 3 weeks = 15 docs
- **Rate**: ~90 min per doctrine (read 6 versions + Singer + reconcile + write)
- **Deliverable**: `MASTER_Comprehensive_Outline.md` (40-50 pages)

### Weeks 3-5 (Case Libraries, Parallel with Comprehensive)
- **Simultaneous with Weeks 2-4**: Build `_CASES_[Topic].md` files
- **Rate**: 2-3 case library files per week
- **Deliverable**: 8-10 `_CASES_[Topic].md` files

### Week 5 (Attack Outline)
- **Mon-Wed**: Condense each comprehensive section
- **Thu-Fri**: Format + print test
- **Deliverable**: `MASTER_Attack_Outline.md` (5-15 pages, printable)

### Weeks 5-6 (Source Crosswalk)
- **Parallel with Week 5**: As you finalize sections, map to textbook
- **Rate**: Build Crosswalk incrementally (don't wait until end)
- **Deliverable**: `_SOURCE_CROSSWALK.md` (complete validation)

---

## Time Budget Summary

| Phase | Task | Hours | Weeks |
|-------|------|-------|-------|
| 1 | Case Registry | 8 | 1 |
| 2 | Comprehensive Outline | 30 | 3 |
| 3 | Case Libraries | 12 | 2.5 (parallel with Phase 2) |
| 4 | Attack Outline | 6 | 1 |
| 5 | Source Crosswalk | 4 | 1 (parallel with Phase 4) |
| **QA & Validation** | **Spot-checks, linking, formatting** | **6** | **All phases** |
| **TOTAL** | | **66 hours** | **6 weeks** |

**Hours per week**: ~11 hours/week = 2-3 hours/day

**Realistic timeline**: 6 weeks starting January 12 = ready by ~February 23

---

## Critical Success Factors

1. **Start with Registry** (Phase 1)
   - Everything else depends on having definitive case list
   - Don't skip; don't rush

2. **Consolidate ruthlessly** (Phase 2)
   - Goal is ONE master outline, not 6 outlined merged
   - Resolve conflicts, don't list both versions
   - Check Singer as tiebreaker

3. **Link religiously** (All phases)
   - Every case in Comprehensive → links to Registry
   - Every topic in Comprehensive → links to Case Library
   - Every Case Library → links to Textbook page
   - Broken links = useless

4. **Validate before finalizing** (Phase 5)
   - Spot-check random topics against Singer
   - Ask: "Can I find this case/page in my textbook?"
   - If not, fix it

5. **Prioritize HIGH-yield content** (All phases)
   - Spend more time on cases that appear on exams
   - Mark these clearly in Registry + Attack Outline
   - Memorize 25 high-yield cases; learn others as backup

---

## Maintenance (After "Done")

**Weekly During Class**:
- Add new cases from lecture to Registry
- Update Comprehensive Outline with new applications
- Add class hypos to Case Library notes

**Before Exam**:
- Re-read Attack Outline 3-4 times
- Practice 5-10 past exam questions
- Validate your issue-spotting against Attack checklist

---

## Success Metrics (How to Know It's "Done")

- [ ] Can name 25 high-yield cases from memory
- [ ] Can sketch any doctrine rule in 1 sentence without notes
- [ ] Can list elements for any doctrine in <30 seconds
- [ ] Can find any case write-up in <1 minute
- [ ] Can trace any rule back to Singer textbook
- [ ] Can apply rule to a hypo in <5 minutes
- [ ] Print Attack Outline is <15 pages, memorable
- [ ] No broken links in Comprehensive Outline
- [ ] Every case in Registry is verified in Singer

---

**Document Status**: Implementation Roadmap Complete  
**Date**: January 12, 2026  
**Next Step**: Start Phase 1 (Case Registry) this week!  
**Questions?** Refer back to `OUTLINE_ARCHITECTURE.md` for detailed specs
