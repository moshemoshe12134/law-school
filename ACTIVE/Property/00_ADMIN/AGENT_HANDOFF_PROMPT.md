# Agent Handoff Prompt - Course System Setup

Use this prompt to set up the same system for other law school courses (Torts, Contracts, Civil Procedure, etc.).

---

## PROMPT FOR NEW AGENT:

```
I need you to set up a course management system for my [COURSE NAME] class using the same structure I use for my Property class. Here's what I need:

## Background Context

I have a proven course system that works. You can see the complete structure in my Property folder at:
`/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-Property/`

Review these files to understand the system:
1. `00_ADMIN/SYSTEM_OVERVIEW.md` - Complete system architecture
2. `00_ADMIN/README.md` - Daily workflow
3. `MASTER_LOG.md` - Tracking structure
4. `TEMPLATES/` directory - All templates

## Your Task

Set up an IDENTICAL system for my [COURSE NAME] class at:
`/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-[COURSE NAME]/`

### Steps:

1. **Explore the existing folder** to see what materials I already have (if any)

2. **Create the canonical folder structure**:
   - 00_ADMIN/
   - 01_SYLLABUS/
   - 02_SOURCES/ (with subfolders: core, supplement, exams_raw, statutes)
   - 03_MAPPING/
   - 04_PREP/
   - 05_CLASS_NOTES/ (with subfolders: raw, structured)
   - 06_REVIEW/
   - 07_OUTLINE/ (with subfolders: attack, hypos)
   - 08_METRICS/
   - TEMPLATES/

3. **Organize existing files** (if any) into the proper locations:
   - Move textbooks/supplements to 02_SOURCES/
   - Move past exams to 02_SOURCES/exams_raw/
   - Move past outlines to 07_OUTLINE/
   - Extract any zip files first

4. **Create all templates** (copy from Property, but adapt):
   - Use the Property templates as a base
   - Adjust course profile parameters for [COURSE NAME]:

     **For Torts**:
     - Statute/Code-centric: LOW-MEDIUM (Restatement matters more than statutes)
     - Policy weight: MEDIUM-HIGH (Policy analysis is important)
     - Case depth: HIGH (Cases are foundational - need facts + holdings)
     - Hypos vs. theory: HIGH (Very hypo-heavy for exam)

     **For Contracts/Deals**:
     - Statute/Code-centric: MEDIUM-HIGH (UCC + contract terms matter)
     - Policy weight: LOW-MEDIUM (Less theory, more practical)
     - Case depth: MEDIUM (Cases for doctrine, but contracts/terms heavier)
     - Hypos vs. transaction design: HIGH (Structure/risks/drafting)

     **For Civil Procedure**:
     - Statute/Code-centric: VERY HIGH (Rules-driven)
     - Policy weight: LOW-MEDIUM (Some policy, but rules dominate)
     - Case depth: MEDIUM (Cases interpret rules)
     - Hypos vs. theory: MEDIUM-HIGH (Procedural hypos)

     **For Constitutional Law**:
     - Statute/Code-centric: LOW (Constitutional text, but case-heavy)
     - Policy weight: VERY HIGH (Theory and framework matter most)
     - Case depth: VERY HIGH (Landmark cases define doctrine)
     - Hypos vs. theory: MEDIUM (Framework application)

5. **Create MASTER_LOG.md** with course-specific parameters

6. **Create placeholder files**:
   - 01_SYLLABUS/PLACEHOLDER_syllabus_pending.md
   - 03_MAPPING/PLACEHOLDER_exam_spec.md

7. **Create documentation**:
   - 00_ADMIN/README.md (workflow guide)
   - 00_ADMIN/SYSTEM_OVERVIEW.md (complete overview)
   - 00_ADMIN/conversion_recommendations.md (AI format guide)
   - 02_SOURCES/README.md
   - 07_OUTLINE/README.md
   - TEMPLATES/README.md

8. **Verify everything is AI-digestible**:
   - Document current file formats
   - Note any conversion recommendations
   - Confirm PDFs have text layers

9. **Provide me with a summary** showing:
   - Directory structure created
   - Files organized (count by type/location)
   - Templates created
   - Course profile parameters set
   - Next steps (what I need to do when syllabus arrives)
   - Status: Ready to use

## Important Notes

- **Copy the structure EXACTLY** from Property
- **Adapt the course parameters** for [COURSE NAME]'s specific needs
- **Organize any existing files** I already have
- **Keep strict time limits**: 60-90 min prep target, 2-4 page packet cap
- **Maintain prediction-driven approach**: Accuracy scoring is critical
- **Stay exam-focused**: Everything maps to exam spec

## Current Course: [FILL IN COURSE NAME HERE]

Course folder location: `/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-[COURSE NAME]/`

Let me know if you need to see any files from my Property system for reference.
```

---

## QUICK COPY-PASTE VERSION FOR TORTS:

```
Set up my course management system for Torts using the same structure as my Property class.

Reference system: `/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-Property/`

Review these files first:
- `00_ADMIN/SYSTEM_OVERVIEW.md`
- `00_ADMIN/README.md`
- `MASTER_LOG.md`
- `TEMPLATES/` directory

Target location: `/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-Torts/`

Tasks:
1. Explore existing Torts folder
2. Create identical folder structure (00_ADMIN through 08_METRICS + TEMPLATES)
3. Organize any existing files into proper locations
4. Create all templates (adapt from Property)
5. Create MASTER_LOG.md with Torts parameters:
   - Statute/Code-centric: LOW-MEDIUM (Restatement-focused)
   - Policy weight: MEDIUM-HIGH
   - Case depth: HIGH (Cases are foundational)
   - Hypos: HIGH (Very hypo-heavy)
6. Create placeholder files (syllabus, exam spec)
7. Create all documentation (README files, conversion guide)
8. Verify AI-digestible formats
9. Provide summary with next steps

Make it ready to use when syllabus arrives.
```

---

## CUSTOMIZATION BY COURSE

Just change the course name and parameters in the prompt:

| Course | Statute Weight | Policy Weight | Case Depth | Hypo Focus |
|--------|---------------|---------------|------------|------------|
| **Property** | MEDIUM-HIGH | MEDIUM | MEDIUM-HIGH | HIGH |
| **Torts** | LOW-MEDIUM | MEDIUM-HIGH | HIGH | HIGH |
| **Contracts** | MEDIUM-HIGH | LOW-MEDIUM | MEDIUM | HIGH |
| **Civ Pro** | VERY HIGH | LOW-MEDIUM | MEDIUM | MEDIUM-HIGH |
| **Crim Law** | VERY HIGH (MPC) | HIGH | MEDIUM | HIGH |
| **Con Law** | LOW | VERY HIGH | VERY HIGH | MEDIUM |

---

**Saved**: [Date]
