# OUTLINE ARCHITECTURE

## Executive Summary

This document proposes a unified outline system that consolidates multiple student outlines into a single authoritative "Master Outline" with full cross-referencing to source materials. The architecture separates concerns into **Comprehensive** (study depth) and **Attack** (exam speed) versions, with a structured **case reference library** linking each doctrine to its source cases in the textbook.

---

## Problem Statement

**Current State:**
- 6+ different student outlines (F19, S19, S21, multiple instructors)
- Different organizational schemes, varying completeness
- No systematic cross-reference to source materials
- Cases mentioned without full citation or location in textbook/casebook
- No unified case library
- Difficult to validate doctrine accuracy against original sources

**Goals:**
1. Create one authoritative comprehensive outline
2. Link every doctrine and case to its source material with page references
3. Maintain consistency across topics
4. Support both deep study (comprehensive) and exam prep (attack)
5. Enable easy validation and fact-checking against sources
6. Create reusable case library for quick reference

---

## Proposed Architecture

### Layer 1: Master Source Registry
**File**: `07_OUTLINE/_REGISTRY_Cases.md`

A curated, complete index of all Property cases with metadata:

```markdown
# Master Case Registry

## Format per case entry:
- **Case Name** | Jurisdiction | Year
- Citation: [Full citation]
- Textbook Pages: [Singer/Berger/Davidson 8th ed. pages]
- Topics: [Doctrine tags]
- Holding (one sentence): [Rule established]
- Exam Frequency: [High/Medium/Low based on past exam analysis]

## Indexed by:
1. Alphabetical (A-Z)
2. Topic/Doctrine (see Part 2 below)
3. Frequency/Criticality (high-yield cases first)
```

**Why this first?**
- Single source of truth for all case metadata
- Enables linking from outlines without repetition
- Tracks which cases are critical vs. ancillary
- Supports quick validation ("Is this case in the textbook?")

---

### Layer 2: Unified Comprehensive Outline
**File**: `07_OUTLINE/MASTER_Comprehensive_Outline.md`

Hierarchical structure organized by doctrine area:

```markdown
# MASTER COMPREHENSIVE OUTLINE

## Table of Contents
[Auto-generated from headers]

---

## UNIT I: ACQUIRING & JUSTIFYING PROPERTY

### I.A Acquisition by First Possession

#### Rule
[One-sentence black letter rule]

#### Elements/Test
[Numbered, with definitions]

#### Source Authority
- **Primary case(s)**: [Case Name] ([Registry link])
- **Statutory basis**: [If applicable with statute number]
- **Restatement**: [If applicable with section]

#### Key Cases
[Limited to 2-3 most important cases with:]
- Facts (1-2 sentences)
- Holding
- Significance
- Page reference

#### Policy Rationales
[Why the law is this way]

#### Common Applications
[Hypo patterns that trigger this doctrine]

#### Variations/Exceptions
[Nuances and edge cases]

#### Cross-References
- See also: [Related doctrines]
- Contrasts: [Competing doctrines]
- Building block for: [Later doctrines that depend on this]

---

[Repeat for each doctrine]
```

**Key Features:**
- Single authoritative source (not conflicting student versions)- Digestible units (each doctrine 500-1500 words max)
- Every case links back to Registry
- Statutory citations with exact numbers
- Policy context (why courts decided this way)
- Explicit connections to applications and hypos
- Built iteratively from past outlines + textbook

---

### Layer 3: Attack Outline
**File**: `07_OUTLINE/MASTER_Attack_Outline.md`

Condensed checklist version (5-15 pages):

```markdown
# ATTACK OUTLINE

## I.A First Possession

**Rule**: [One sentence]

**Elements**: 
- [ ] Element 1: Definition
- [ ] Element 2: Definition
- [ ] Element 3: Definition

**Key Cases**: Pierson; Popov

**Hypo Triggers**: 
- Competing claimants to unowned thing → first capture
- Labor invested in possession → fairness angle
- [etc.]

**Statutory/Restatement**: [Section number only]
```

**Purpose:**
- Printed format (can memorize key phrases)
- 1-2 page per doctrine area
- Rapid issue-spotting on exam
- Links to comprehensive outline for deep dives (if time permits)

---

### Layer 4: Case Library (Topic-Indexed)
**Files**: `07_OUTLINE/_CASES_[TopicName].md`

Separate file for each major topic area:
- `_CASES_FirstPossession.md`
- `_CASES_Adverse_Possession.md`
- `_CASES_Trespass.md`
- `_CASES_Easements.md`
- etc.

**Structure per case**:
```markdown
## [Case Name] ([Citation]) - [Jurisdiction/Year]

**Textbook Location**: [Pp. XXX-XXX in Singer 8th ed.]

**Rule Established**: [One sentence]

**Full Facts**:
[2-3 sentence summary of what happened]

**Procedural Posture**:
[Appellate court? What was lower court ruling?]

**Holding**:
[What did court decide and why (1-2 sentences)]

**Reasoning**:
[Key analytical points - multiple paragraphs if important]

**Dissent** (if notable):
[Key disagreement]

**Policy Implications**:
[Why this rule matters beyond just this case]

**Variations in Other Jurisdictions**:
[If case reflects competing approaches]

**Related Cases**:
[Other cases applying or distinguishing this rule]

**Exam Frequency**: 
[Based on past exam analysis - HIGH/MEDIUM/LOW]

**Hypo Applications**:
[How this rule typically appears on exams]
```

---

### Layer 5: Source Reference Index
**File**: `07_OUTLINE/_SOURCE_CROSSWALK.md`

Maps outline topics → textbook pages → case names

```markdown
# Source Crosswalk

## Singer & Berger & Davidson (8th ed.) - Property

### Chapter 1: Possession and Ownership
- Pages: 1-150
- Topics covered:
  - First Possession (Pierson) → pp. 45-67
  - Rule of Capture → pp. 68-85
  - Finding (Armory, Wilcox) → pp. 86-120
  - [etc.]
  
### Chapter 2: Trespass
- Pages: 151-250
- Topics covered:
  - [etc.]

## Examples & Explanations

### Chapter X: [Topic]
- Pages: [XXX]
- Hypo examples:
  - Hypo [#]: [Name] → pp. [XXX]
  - [etc.]

## Statute Locations
- Common law states: [Citation]
- Restatement (Third): [Sections]
- UCC (if applicable): [Sections]
```

---

## Integration Workflow

### Phase 1: Build Registry (Week 1)
1. Extract all cases from existing 6 outlines
2. Cross-reference to Singer textbook (locate pages)
3. Create standardized metadata
4. Flag gaps/inconsistencies

### Phase 2: Build Master Comprehensive (Weeks 2-4)
1. Read through each existing outline by topic
2. Resolve conflicts (if same doctrine described differently)
3. Add textbook context not in any outline
4. Organize into unified hierarchy
5. Add cross-references and policy context

### Phase 3: Build Case Libraries (Weeks 3-5)
1. Extract full case write-ups from any source outline that has them
2. Supplement with info from textbook
3. Link back to comprehensive outline
4. Mark exam frequency based on past exam analysis (see 02_SOURCES/exams_raw/)

### Phase 4: Create Attack Outline (Week 5)
1. Condense master comprehensive to checklist format
2. 1-2 pages per major topic area
3. Include hypo triggers for quick recall
4. Format for printing/memorization

### Phase 5: Build Source Crosswalk (Ongoing)
1. As you create each section, record page references
2. Build map from outline → textbook → cases
3. Enable validation: "Can I find this in Singer?"

---

## File Organization (Proposed)

```
07_OUTLINE/
├── README.md [Keep as-is]
├── OUTLINE_ARCHITECTURE.md [This file]
│
├── MASTER_Comprehensive_Outline.md [Main study document]
├── MASTER_Attack_Outline.md [Exam day resource]
│
├── _REGISTRY_Cases.md [Master case index]
├── _SOURCE_CROSSWALK.md [Topic → Textbook → Cases]
│
├── _CASES_FirstPossession.md
├── _CASES_AdversePossession.md
├── _CASES_Trespass.md
├── _CASES_Nuisance.md
├── _CASES_Easements.md
├── _CASES_Covenants.md
├── _CASES_Zoning.md
├── _CASES_Estates.md
├── _CASES_Leasehold.md
├── _CASES_Takings.md
│
├── [ARCHIVE] Old Student Outlines
│   ├── F19_Outline.md
│   ├── Glass_Property_F19_Outline.md
│   ├── Glass_Property_S19_Outline.md
│   ├── Glass_Property_S19_Rules.md
│   ├── Glass_Property_S19_Themes.md
│   └── [etc.]
│
├── attack/ [Keep structure as-is for attack hypos]
├── hypos/ [Populate from master outline applications]
```

---

## Quality Control / Validation Strategy

### Checksum Questions for Master Outline
For each doctrine, before finalizing:
- [ ] Is there a one-sentence black letter rule?
- [ ] Are all elements listed with definitions?
- [ ] Does the primary case appear in Singer textbook?
- [ ] Are page references exact?
- [ ] Are policy rationales explained?
- [ ] Is there a cross-reference to related doctrines?
- [ ] Do case library files exist for all cited cases?
- [ ] Can a student explain this rule to someone else using it?

### Consistency Checks
- All 6 existing outlines agree on this rule? (If not, mark ambiguity)
- Has this case appeared on past exams? (Mark exam frequency)
- Is this doctrine "high-yield" or "nuance only"? (Mark criticality)

---

## Implementation Priorities

**Tier 1 (Must-Have):**
1. Master Comprehensive Outline (unified source of truth)
2. Case Registry (enables linking and validation)
3. Source Crosswalk (proves authority)

**Tier 2 (Should-Have):**
4. Case Library files (depth reference)
5. Attack Outline (exam prep)

**Tier 3 (Nice-to-Have):**
6. Interactive links (if using Obsidian or similar)
7. Flowcharts for complex doctrines
8. Video summaries (if available)

---

## Tools & Workflow

**For Building Outlines:**
- **Format**: Markdown (.md) - AI-friendly, version-controllable
- **Organization**: GitHub-style directory structure
- **Cross-linking**: Wiki-style links to Registry and Case files
- **Version Control**: Git commits after each phase

**For Validation:**
- Compare master outline against each source outline (resolve conflicts)
- Spot-check cases in Singer textbook (confirm page numbers)
- Validate against past exam topics (ensure coverage)

**For Study:**
- Print Attack Outline (1-15 pages)
- Keep Master Comprehensive on computer (for deep dives)
- Reference Case Libraries by topic as needed
- Use Crosswalk to locate textbook sections for missing concepts

---

## Success Metrics

| Metric | Target | How to Measure |
|--------|--------|-----------------|
| Single source of truth established | 1 Master Comprehensive | Outline completed with no conflicts noted |
| Coverage completeness | 100% | Every topic from past exams → outline |
| Source validation | 95%+ cases linkable | Can find 19/20 cases in textbook or past exams |
| Case library depth | 50+ cases documented | Detailed write-ups for high-yield cases |
| Exam preparedness | Testable | Practice exams show issue-spotting improvement |
| Cross-referencing | Functional | Can follow links from outline → cases → textbook |

---

## Next Steps

1. **Create this file** (`OUTLINE_ARCHITECTURE.md`) ← Done
2. **Assign roles**: Who builds which tier?
3. **Set deadlines**: Phased rollout (Registry → Master → Cases → Attack)
4. **Start Phase 1**: Build `_REGISTRY_Cases.md`
5. **Weekly check-ins**: Validate against source materials as you build

---

## Appendix: Topic Hierarchy (Proposed Structure for Master Outline)

```
UNIT I: ACQUIRING & JUSTIFYING PROPERTY
├── I.A Acquisition by First Possession
├── I.B Acquisition by Labor
├── I.C Acquisition by Transfer
└── I.D Intellectual Property

UNIT II: THE RIGHT TO EXCLUDE
├── II.A Trespass
├── II.B Adverse Possession & Prescriptive Easements
├── II.C Nuisance (Boundary of Right to Exclude)
└── II.D Public Access Rights (ADA, Civil Rights, Public Trust)

UNIT III: THE POWER TO SHARE (IN TIME & SPACE)
├── III.A Concurrent Ownership (Tenancies)
├── III.B Marital Property
├── III.C Estates System (Future Interests)
├── III.D Leaseholds
└── III.E Fair Housing

UNIT IV: THE PRIVILEGE TO USE
├── IV.A Easements (Express, Implied, Prescriptive)
├── IV.B Covenants
├── IV.C Zoning & Land Use Regulation
└── IV.D (TBD based on your professor's approach)

UNIT V: IMMUNITY FROM LOSS
├── V.A Eminent Domain (Physical Takings)
├── V.B Regulatory Takings
└── V.C Deprivation of Core Property Rights
```

---

**Document Version**: 1.0  
**Date Created**: January 12, 2026  
**Status**: Ready for Implementation  
**Next Review**: After Phase 1 (Registry) Complete
