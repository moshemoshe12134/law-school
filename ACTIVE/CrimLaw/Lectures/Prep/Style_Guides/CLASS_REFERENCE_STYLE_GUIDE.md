# Class Reference Style Guide
**For in-class lookup — comprehensive Q&A format**

---

## PURPOSE
- Comprehensive reference for use during class
- Searchable Q&A format
- Contains detailed doctrine, rules, cases, MPC text
- Quick lookup when Harcourt asks specific questions
- "Cheat sheet" for class participation

## STRUCTURE (Required Sections)

### 1. QUICK NAVIGATION
- Link-based table of contents
- Search by case name, MPC section, or concept
- Time-stamp approximations if possible

### 2. CORE DOCTRINE (The "Rules")
- MPC provisions (verbatim text when available)
- Common law rules
- Elements, tests, standards
- Formatted for quick scanning

### 3. CASES (Detailed Briefs)
For each case:
- **Citation + Court + Year**
- **Facts** (complete but concise)
- **Procedural posture**
- **Issue**
- **Holding** (exact rule)
- **Reasoning** (key points)
- **MPC hook** (what provision this relates to)
- **Policy tension** (what values conflict)
- **Exam hypo** (1-2 sentence application)

### 4. POLICY/THEORY
- Article/reading summaries
- Key quotes (verbatim when important)
- Author's thesis + supporting arguments
- How this changes doctrine application
- Harcourt's likely questions

### 5. HARDCOURT-SPECIFIC
- Typical questions he asks on this topic
- Patterns from past years (if known)
- Foucault/Balkin/Kelman connections
- What he wants you to learn

### 6. QUICK HYPOS
- 5-10 exam-style hypotheticals
- Issue-spotting triggers
- Both sides of arguments

### 7. SEARCH TERMS
- List of keywords for quick finding
- Alternative terms, synonyms

---

## FORMATTING FOR QUICK LOOKUP

**Use collapsible sections when supported:**
```markdown
<details>
<summary>Martin v. State (1944)</summary>
[Facts, holding, etc.]
</details>
```

**Clear headers with keywords:**
```markdown
### Martin v. State (AL 1944) — Voluntary Act — Police Dragged Drunk Man to Highway
```

**Inline formatting for quick scanning:**
- **Bold** key terms and holdings
- *Italic* for case names
- `Code font` for MPC sections
- → Arrow for implications
- ≠ Not equal for distinctions
- ∴ Therefore for conclusions

**Tables for comparisons:**
```markdown
| Case | Voluntary Act? | Time Frame Used | Outcome |
|------|----------------|-----------------|---------|
| Martin | No | Narrow (being on highway) | Acquit |
| Decina | Yes | Broad (driving with epilepsy) | Convict |
```

---

## Q&A FORMAT

**Organize by likely questions:**

### MPC §2.01 Questions
**Q: What does MPC §2.01 require?**
A: [Direct answer with rule]

**Q: What's NOT a voluntary act under §2.01(2)?**
A: [Four categories listed]

**Q: How does Decina fit within §2.01?**
A: [Application with reasoning]

### Case Questions
**Q: What's the rule from Martin?**
A: [Clear holding]

**Q: How does Martin differ from Decina?**
A: [Comparison]

**Q: What if Harcourt asks...?**
A: [Predictive Q&A]

---

## CONTENT PRINCIPLES

**What goes IN class reference:**
- Verbatim MPC text
- Complete case briefs
- Detailed policy summaries with quotes
- Extensive hypo banks
- Balkin dyads
- All citations and sources
- Cross-references to other classes
- Exam strategies specific to this topic

**How it differs from audio prep:**
- NOT conversational
- NOT time-limited
- NOT narrative
- IS comprehensive
- IS formatted for quick lookup
- IS searchable

---

## ORGANIZATION WITHIN FILE

```markdown
# Class Reference — Class #2 — Actus Reus
**For in-class lookup | Thursday, January 22, 2026**

---

## QUICK NAVIGATION
- [Core Doctrine: MPC §2.01](#core-doctrine)
- [Case Briefs](#case-briefs)
- [Kelman Time-Framing](#kelman-time-framing)
- [Policy Tensions](#policy-tensions)
- [Cold Call Prep](#cold-call-prep)
- [Quick Hypos](#quick-hypos)
- [Search Terms](#search-terms)

---

## CORE DOCTRINE: MPC §2.01

### [Full text...]

### [Breakdown by subsection...]

---

## CASE BRIEFS

### Martin v. State (AL 1944)
[Full brief]

### People v. Newton (CA 1970)
[Full brief]

### People v. Decina (NY 1956)
[Full brief]

### Jones v. U.S. (D.C. Cir. 1962)
[Full brief]

---

## KELMAN TIME-FRAMING
[Full summary]

---

## POLICY TENSIONS
[Detailed analysis]

---

## COLD CALL PREP

### If asked about voluntariness:
[Q&A format]

### If asked about specific cases:
[Q&A format]

---

## QUICK HYPOS
[5-10 hypos with issue-spotting]

---

## SEARCH TERMS
actus reus, voluntary act, omission, Kelman, time framing, Martin, Newton, Decina, Jones, MPC 2.01, duty to rescue, Good Samaritan...
```

---

## CONSISTENCY CHECKLIST

Before finalizing class reference:
- [ ] Quick navigation at top
- [ ] All cases fully briefed (facts, holding, reasoning)
- [ ] MPC sections verbatim
- [ ] Q&A format for cold call prep
- [ ] At least 5 quick hypos
- [ ] Search terms listed
- [ ] Cross-references to other classes
- [ ] Tables for comparisons (when applicable)
- [ ] Bold key terms for scanning
- [ ] Collapsible sections for long content

---

## NAMING CONVENTION
File format: `YYYY-MM-DD_classNN_class_reference.md`
Example: `2026-01-22_class02_class_reference.md`

---

## INTEGRATION WITH OUTLINE MAPPING

At bottom of file, include:
```markdown
---

## SOURCE MAPPING
This class covers material from:
- [Outline Name](path) — sections [X] to [Y]
- [Outline Name](path) — heading "[Heading Name]"

Split markers: `%% CLASS 2 START %%` to `%% CLASS 2 END %%`
```

This allows quick lookup in source outlines for deeper dive.
