# OUTLINE ARCHITECTURE - VISUAL SUMMARY

## Data Flow & Layer Structure

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    STUDENT EXAM DAY                                     │
│                  (What you use on test)                                 │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
            ┌────────────────────────────────┐
            │   MASTER_Attack_Outline.md     │
            │   (5-15 pages - Checklist)     │
            │   - Issue spotters             │
            │   - Element checklists         │
            │   - Case name + statute #'s    │
            │   - Hypo triggers              │
            └────────┬──────────────┬────────┘
                     │              │
                     ▼              ▼
        ┌────────────────────┐  ┌──────────────────┐
        │   DEEP STUDY       │  │  QUICK LOOKUP    │
        │   (Study period)   │  │  (During exam)   │
        └──────────┬─────────┘  └────────┬─────────┘
                   │                     │
                   ▼                     │
    ┌──────────────────────────────┐    │
    │ MASTER_Comprehensive_Outline │    │
    │ (Complete study resource)    │    │
    │ - Black letter rules         │    │
    │ - Element definitions        │    │
    │ - Full case info (via links) │    │
    │ - Policy context             │    │
    │ - Cross-references           │    │
    └──────────────┬───────────────┘    │
                   │                    │
        ┌──────────┴─────────┬──────────┴──────┐
        │                    │                 │
        ▼                    ▼                 ▼
    ┌─────────────┐  ┌──────────────┐  ┌────────────────┐
    │  Case       │  │   SOURCE     │  │  _REGISTRY_    │
    │  LIBRARY    │  │  CROSSWALK   │  │   Cases.md     │
    │  Files      │  │              │  │                │
    │ (_CASES_*) │  │ Topic→Page→   │  │ Master index   │
    │            │  │ Case Links    │  │ of all cases   │
    │ Depth ref  │  │              │  │                │
    │ by topic   │  │ Validation    │  │ Metadata:      │
    └──────┬──────┘  │ checklist     │  │ - Citation     │
           │         └──────┬───────┘  │ - Textbook pg. │
           │                │         │ - Topics       │
           │                │         │ - Holding      │
           │                ▼         │ - Exam freq.   │
           │         ┌──────────────┐ └────────┬───────┘
           │         │   SINGER     │          │
           │         │ TEXTBOOK     │          │
           │         │ (Pages XXX)  │          │
           │         └──────────────┘          │
           │                ▲                  │
           └────────────────┼──────────────────┘
                            │
                    (Physical validation)
```

---

## File Structure

```
07_OUTLINE/
│
├─ OUTLINE_ARCHITECTURE.md ...................... [This document - Full specs]
│
├─ MASTER_Comprehensive_Outline.md ............. [Master Study Resource]
│  │  └─ Unit I: Acquiring Property
│  │     ├─ I.A First Possession
│  │     ├─ I.B Labor Theory
│  │     └─ [etc.]
│  │  └─ Unit II: Right to Exclude
│  │     ├─ II.A Trespass
│  │     ├─ II.B Adverse Possession
│  │     └─ [etc.]
│  │  └─ Unit III: Sharing Property
│  │  └─ Unit IV: Privilege to Use
│  │  └─ Unit V: Immunity from Loss
│
├─ MASTER_Attack_Outline.md ................... [Exam Day Checklist]
│  └─ Same hierarchy as Comprehensive, but 1-2 pages per topic
│
├─ _REGISTRY_Cases.md ......................... [Master Case Index]
│  │  Case Name | Citation | Textbook Pg | Topics | Rule | Exam Freq
│  ├─ Pierson v. Post
│  ├─ Popov v. Hayashi
│  ├─ Brown v. Gobble
│  ├─ State v. Shack
│  └─ [~80+ cases total]
│
├─ _SOURCE_CROSSWALK.md ....................... [Validation Map]
│  │  Outline Topic → Textbook Pages → Case Names
│  ├─ Singer Chapter 1: Possession (pp. 1-150)
│  │  ├─ First Possession (Pierson) → pp. 45-67
│  │  ├─ Rule of Capture → pp. 68-85
│  │  └─ Finding (Armory) → pp. 86-120
│  └─ [Each chapter mapped]
│
├─ Case Libraries (Topic-Organized)
│  ├─ _CASES_FirstPossession.md ............... [Full case write-ups]
│  │  ├─ Pierson v. Post
│  │  ├─ Popov v. Hayashi
│  │  └─ [Others]
│  │
│  ├─ _CASES_AdversePossession.md
│  ├─ _CASES_Trespass.md
│  ├─ _CASES_Easements.md
│  ├─ _CASES_Covenants.md
│  ├─ _CASES_Nuisance.md
│  ├─ _CASES_Zoning.md
│  ├─ _CASES_Estates.md
│  ├─ _CASES_Leasehold.md
│  └─ _CASES_Takings.md
│
├─ [ARCHIVE] Old Outlines ..................... [Historical reference]
│  ├─ F19_Outline.md
│  ├─ Glass_Property_F19_Outline.md
│  ├─ Glass_Property_S19_Rules.md
│  ├─ Glass_Property_S19_Themes.md
│  ├─ Glass_Property_S21_Outline(Shulman).md
│  └─ [etc.]
│
├─ attack/ .................................. [Attack outline variants]
├─ hypos/ ................................... [Exam practice hypos]
│
└─ README.md ................................ [Keep existing]
```

---

## How to Use This Architecture

### For Study Sessions:
1. **Start**: Open `MASTER_Comprehensive_Outline.md`
2. **Deep dive**: Click link to relevant `_CASES_[Topic].md` for full case analysis
3. **Validate**: Cross-reference via `_SOURCE_CROSSWALK.md` to Singer textbook
4. **Hypo practice**: Apply doctrine using examples in Comprehensive Outline

### For Exam Prep:
1. **Print**: `MASTER_Attack_Outline.md` (5-15 pages)
2. **Memorize**: Element checklists and hypo triggers
3. **If stuck**: Use `_REGISTRY_Cases.md` to quickly check case names

### For Clarification:
1. **Question**: "What is the rule for X?"
2. **Find**: Topic in `MASTER_Comprehensive_Outline.md`
3. **Verify**: Cross-reference in `_SOURCE_CROSSWALK.md`
4. **Read case**: Pull up `_CASES_[Topic].md` for full write-up
5. **Original source**: Go to Singer textbook (pages noted)

---

## Key Advantages of This Architecture

| Challenge | How This Solves It |
|-----------|-------------------|
| **Multiple conflicting outlines** | Single Master Outline as source of truth |
| **Cases not verifiable** | Registry + Crosswalk = every case traceable to textbook |
| **Hard to understand "why"** | Comprehensive Outline includes policy context |
| **Too much detail for exam day** | Attack Outline condenses to essentials |
| **Can't find info quickly** | Topic-indexed Case Libraries |
| **Don't know what's high-yield** | Registry marks exam frequency |
| **Disconnected from sources** | Every doctrine links to original textbook |
| **Hard to remember applications** | Comprehensive Outline includes hypo triggers |

---

## Implementation Checklist

### Phase 1: Build Registry (Week 1)
- [ ] Extract all cases from 6 existing outlines
- [ ] Cross-reference to Singer textbook (get page #'s)
- [ ] Create standardized `_REGISTRY_Cases.md`
- [ ] Identify gaps (any case not in textbook?)

### Phase 2: Unified Comprehensive Outline (Weeks 2-4)
- [ ] Read Singer Chapters 1-2 (get structure)
- [ ] Extract topic hierarchy from existing outlines
- [ ] Reconcile conflicts (which version is "right"?)
- [ ] Add policy context from textbook
- [ ] Create `MASTER_Comprehensive_Outline.md`

### Phase 3: Case Library Files (Weeks 3-5)
- [ ] Create `_CASES_[Topic].md` files for each major doctrine
- [ ] Extract case write-ups from existing outlines
- [ ] Supplement with textbook info
- [ ] Add exam frequency data

### Phase 4: Attack Outline (Week 5)
- [ ] Condense comprehensive to 1-2 pages per topic
- [ ] Create `MASTER_Attack_Outline.md`
- [ ] Format for printing/memorization

### Phase 5: Source Crosswalk (Ongoing)
- [ ] Create `_SOURCE_CROSSWALK.md`
- [ ] Record page references as you build each section
- [ ] Enable validation checks

---

## Quick Decision Tree: Which File to Use?

```
START: I need Property law information
│
├─ Q: Is it exam day?
│  ├─ YES → Use MASTER_Attack_Outline.md
│  │        (Quick reference, memorized)
│  │
│  └─ NO → Q: Do I have time for depth?
│     ├─ YES → Use MASTER_Comprehensive_Outline.md
│     │        + click through to _CASES_[Topic].md
│     │        + verify in _SOURCE_CROSSWALK.md
│     │
│     └─ MAYBE → Q: Need quick answer?
│        ├─ YES → Check _REGISTRY_Cases.md
│        │        (Just rule + citation)
│        │
│        └─ NO → Q: Want to understand "why"?
│           └─ YES → Read policy section in
│                    MASTER_Comprehensive_Outline.md
│                    + check related cases in
│                    _CASES_[Topic].md
```

---

## Questions This Architecture Answers

**Study-Phase Questions:**
- "What's the rule for X?" → Check Comprehensive Outline
- "Why did courts decide Y this way?" → Check Policy section + read case
- "What's the hypo trigger?" → Check Applications section
- "Is this in our textbook?" → Check _SOURCE_CROSSWALK.md
- "What did case Z actually hold?" → Check _CASES_[Topic].md
- "Which cases appear on exams?" → Check _REGISTRY_Cases.md (Exam Frequency column)

**Exam-Phase Questions:**
- "How do I spot X issue?" → Check MASTER_Attack_Outline.md
- "What elements do I check?" → Check Element Checklist in Attack Outline
- "Need the case name fast?" → Check _REGISTRY_Cases.md
- "What's the statute number?" → Check MASTER_Attack_Outline.md

---

## Version Control Notes

**Commit when:**
1. Completing each Phase (Registry done → first commit)
2. Adding a new Case Library file
3. Finalizing Comprehensive Outline section (by topic)
4. Creating Attack Outline

**Never commit:**
- Half-finished files
- Conflicted versions (resolve first)
- Without testing links/references

---

## Success Indicators

After implementation, you should be able to:
- [ ] Explain any Property rule in 1 sentence
- [ ] Identify the case that established it + cite page in textbook
- [ ] List all elements in checklist format (30 seconds)
- [ ] Apply rule to a hypo (2-3 minutes)
- [ ] Print Attack Outline to 1-2 sheets (Pierson, Adverse Possession, etc.)
- [ ] Find any case write-up in <1 minute
- [ ] Trace any doctrine back to original Singer textbook

---

**Architecture Status**: Ready to implement  
**Start Date**: Week of January 12, 2026  
**Expected Completion**: Week of January 26, 2026  
**Maintenance**: Weekly updates as you add class notes
