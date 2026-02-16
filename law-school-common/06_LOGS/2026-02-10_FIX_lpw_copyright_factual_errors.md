# Fix: LPW-II Copyright Issue Factual Errors

**Date**: 2026-02-10
**Type**: FIX (Corrections)
**Scope**: ACTIVE/LPW-II/99_Assignments/Outline/
**Trigger**: User identified pervasive factual errors in working documents

---

## Summary

Corrected two critical factual misstatements in all LPW-II copyright fair use outlines:
1. Melody vs. lyrics confusion (was: "copied melody," should be: "copied lyrics")
2. Nonprofit structure (was: "EchoCraft is nonprofit," should be: "for-profit parent with nonprofit subsidiary")

---

## Root Cause

Agent made assumptions from outline documents without reading primary source (Record_5_Riven_v_EchoCraft.txt, Exhibits G & H). Carried incorrect assumptions across multiple documents through inference chains.

---

## Files Corrected

1. `ISSUE_TWO_OUTLINE.md` - Factor 3 section, Factor 1 nonprofit description
2. `Brief_Outline_Fair_Use_EchoCraft.md` - Questions Presented, Factor 3 summary, nonprofit structure
3. `FAIR_USE_RULES_FOR_BRIEF.md` - All melody references, nonprofit claims
4. `PARODY_VS_SATIRE_LEGAL_TESTS.md` - Necessity sections, defense arguments
5. `FAIR_USE_LEGAL_FRAMEWORK_ANALYSIS V2.md` - Implication sections

---

## Correct Facts (From Record)

**What was copied**: 7 of 8 lines of LYRICS (not melody)
- Verbatim: 57 of 66 words (86.4%)
- Added: 7 new lines (59 words = 50% new content)
- No mention of melody anywhere in case record

**Who released it**: EchoCraft Ed (nonprofit subsidiary) of EchoCraft Productions (for-profit parent)
- Parent company benefited: PR improvement, revenue -5% → +2%
- CEO Ryan Raine: released for PR strategy
- Nonprofit subsidiary: licensed at $200/school (below cost)

---

## Strategic Implications

1. **Factor 3 MORE vulnerable**: Copying creative expression (lyrics) vs. functional element (melody)
2. **Factor 1 MORE complex**: Must address for-profit parent benefit while arguing nonprofit subsidiary use
3. **Argument shift**: From "mnemonic melody copying" to "quoting inaccurate claims to correct them"

---

## Prevention (Instructions Updated)

Updated `.github/copilot-instructions.md`:
- Added "NEVER CREATE STANDALONE SUMMARY/LOG DOCUMENTS" section
- Added "THINK DEEPLY BEFORE ACTING" requirements
- Integrated with existing 06_LOGS workflow
- Emphasized reading primary sources over inference

---

## Lesson

When making corrections: the corrected files ARE the documentation. Don't create standalone "corrections log" that sits disconnected from workflow.
