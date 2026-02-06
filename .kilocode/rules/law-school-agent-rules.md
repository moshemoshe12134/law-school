# Law School Monorepo — AI Agent Instructions

> **Read this file first.** It tells you everything you need to know to work in this codebase.
> This file is auto-detected by Kilo Code.

---

## 🚨 CRITICAL: Before Any Task

1. **Identify the course** from the user's request (CrimLaw, Property, Torts, Deals, LPW-II)
2. **Read the course MASTER_LOG** at `ACTIVE/{Course}/00_ADMIN/MASTER_LOG.md`
3. **Read the detailed instructions** for the task type (see Quick Reference below)

---

## 📍 Quick Reference: Common Tasks

### Create Prep Docs

**Command patterns**: "prep for CrimLaw class 2", "create prep doc for next Property class", "prep this week's classes"

**Creates BOTH:** Text prep (searchable) + Audio prep (TTS-ready) + QC verification

**READ THESE FILES FIRST:**
1. `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md` — Full procedure (see "prep for [COURSE] class [NN]" command)
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

**Command patterns**: "review CrimLaw class 2", "process transcript", "create review from transcript"

**READ THESE FILES FIRST:**
1. `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md` — Full procedure
2. `law-school-common/01_WORKFLOWS/POST_CLASS_WORKFLOW.md` — Step-by-step workflow
3. `law-school-common/03_TEMPLATES/review_template.md` — Review template

**OUTPUT LOCATION:** `ACTIVE/{Course}/04_REVIEWS/YYYY-MM-DD_classNN_review.md`

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

**Prep docs:** `YYYY-MM-DD_classNN_type.md`
- Example: `2026-01-22_class02_text.md`
- Example: `2026-01-22_class02_audio.md`

**Review docs:** `YYYY-MM-DD_classNN_review.md`

**Always get dates and class numbers from MASTER_LOG.md**

---

## 🎯 Agent Behavior Rules

1. **Never create duplicate files** — check if file exists first
2. **Update MASTER_LOG after creating documents** — mark status as "draft" or "done"
3. **Use templates exactly** — copy structure from `law-school-common/03_TEMPLATES/`
4. **Flag missing sources** — don't make up information; mark "[SOURCE NEEDED]"
5. **Check existing examples** — look at existing preps in `02_PREP/text/` for style

---

## 📚 Course-Specific Context

Each course has its own style and professor:

| Course | Professor | Key Characteristics |
|--------|-----------|---------------------|
| CrimLaw | Harcourt | MPC close reading, ~50% policy, critical theory |
| Property | [See 00_ADMIN] | [Check course_style_guide.md] |
| Torts | [See 00_ADMIN] | [Check course_style_guide.md] |
| Deals | [See 00_ADMIN] | [Check course_style_guide.md] |
| LPW-II | [See 00_ADMIN] | [Check course_style_guide.md] |

**For course specifics:** Read `ACTIVE/{Course}/00_ADMIN/course_style_guide.md` and `exam_spec.md`

---

## ✅ Before Completing Any Task

- [ ] Created file in correct location (per folder structure)
- [ ] Used correct naming convention
- [ ] Followed template structure
- [ ] **Case briefs include Issue line** (per standard format: Rule of Law → Facts + Procedural Posture → Issue → Holding & Reasoning → Disposition)
- [ ] Updated MASTER_LOG.md status
- [ ] Flagged any missing sources with "[SOURCE NEEDED]"
