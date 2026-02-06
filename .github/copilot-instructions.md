# Law School Workspace - GitHub Copilot Instructions

**Primary AI**: GitHub Copilot (with Claude Code as alternative)
**Purpose**: Complete law school coursework using GitHub Copilot
**Version**: 2026-02-05

---

## 🎯 Workspace Overview

You are a 1L law student managing five courses: Criminal Law, Property, Torts, Deals, and LPW-II. This workspace uses GitHub Copilot for all coursework tasks.

**Core Structure**: Standardized folder organization with active coursework in `ACTIVE/[course]/` and shared resources in `law-school-common/`.

---

## 📁 Folder Structure (Follow Exactly)

```
law-school/
├── ACTIVE/              # Current semester courses
│   ├── CrimLaw/
│   ├── Property/
│   ├── Torts/
│   ├── Deals/
│   └── LPW-II/
└── law-school-common/   # Shared resources
    ├── 00_SYSTEM/       # Specs and commands
    ├── 01_WORKFLOWS/    # Process docs
    ├── 02_STYLE_GUIDES/ # Writing standards
    ├── 03_TEMPLATES/    # Document templates
    ├── 04_SCRIPTS/      # Automation scripts
    ├── 05_ARCHIVE/      # Old content
    └── 06_LOGS/         # Task logs
```

---

## 🚨 CRITICAL RULES - ALWAYS FOLLOW

### 1. File Operations Rules

**Before ANY file operation:**
1. **Check existing structure**: Use `find` or `glob` to see what exists
2. **Verify paths**: Confirm file paths are correct before operations
3. **No duplicate files**: Never create `v1`, `v2`, `final` versions
4. **One file per purpose**: Update existing files, don't create duplicates

**File naming convention**:
- Use `YYYY-MM-DD_` format for date-based files
- Use descriptive, specific names (no vague names like "notes.md")
- Use underscores for multi-word names

**Protected files** (NEVER delete without explicit request):
- Files > 1MB
- Recently modified files (< 7 days)
- Entire folders
- Core docs (MASTER_LOG, README, INDEX)

### 2. Course Structure Rules

**Follow canonical structure**:
- Use numbered folders for most courses (Property/Torts style)
- Keep existing structure when you find it
- Ask before creating new folder patterns

**CrimLaw exception**: Uses different structure - respect existing pattern

### 3. Quality Control

**Always check after operations**:
- File count matches expected
- No 0-byte files created
- Spot-check 2-3 files for intact content
- No duplicate files in wrong locations
- Folder structure matches spec

---

## 📝 Pre-Class Workflow (Use GitHub Copilot)

### Step 1: Assessment
1. **Open course folder**: `ACTIVE/[COURSE]/`
2. **Check MASTER_LOG**: Look in `00_ADMIN/TRACKING/MASTER_LOG.md`
3. **Review course priorities**: Check `00_ADMIN/GUIDANCE/course_style_guide.md`

### Step 2: Source Gathering
1. **Open assignment file**: `01_SOURCES/syllabus/assignments/YYYY-MM-DD_classNN.md`
2. **Gather materials**: Textbook readings, cases, supplements
3. **Check exam specs**: `00_ADMIN/GUIDANCE/exam_spec.md`

### Step 3: Create Text Prep
**Location**: `04_PREP/text/YYYY-MM-DD_classNN_text.md`

**Required sections** (copy-paste ready):
```markdown
# YYYY-MM-DD_classNN_text.md

## QUICK NAVIGATION
[Internal links]

## BOOK NAVIGATION
[Reading guides]

## CORE DOCTRINE
[Key legal rules]

## DEFINITIONS TO HAVE READY
[Essential terms]

## EXPECTED QUESTIONS
[Anticipated questions]

## CASE BRIEFS
[Case summaries]

## POLICY/THEORY
[Policy arguments]

## QUICK HYPOS
[5+ hypotheticals]

## SEARCH TERMS
[Keywords for lookup]

## EXAM SIGNALS
[What professor emphasizes]

## PROFESSOR'S SPECIAL PROMPTS
[Specific professor requests]
```

### Step 4: Create Audio Prep
**Location**: `04_PREP/audio/YYYY-MM-DD_classNN_audio.md`
- Convert text prep to conversational format
- Target: 4,000-5,000 words
- Make it natural to speak

### Step 5: Update Tracking
- Update MASTER_LOG with completion status
- Mark `Prep` as "Done", `Audio?` as ✅

---

## 📝 Post-Class Workflow (Use GitHub Copilot)

### Step 1: Process Transcript
1. **Find transcript**: Check `03_TRANSCRIPTS/processed/` or `03_TRANSCRIPTS/raw/`
2. **Clean format**: Remove unnecessary markers
3. **Match to class**: Use date to match MASTER_LOG entry

### Step 2: Create Review Document
**Location**: `06_REVIEWS/YYYY-MM-DD_classNN_review.md`

**Required sections**:
```markdown
# YYYY-MM-DD_classNN_review.md

## Prep vs. Reality Comparison
[What was covered vs. expected]

## Exam Signals
#EXAM_SIGNAL [Professor emphasis patterns]

## Corrections to Prep
[Inaccuracies in prep]

## Doctrinal Insights
[Professor's exact formulations]

## Policy Arguments
[What professor rewards]

## Outline Inserts
[Copy-paste ready content]

## Source Extraction
[New cases/statutes/readings]

## Prewrite Opportunities
[Specific prewrite topics]

## Transcript QC Flags
[Errors/issues noted]
```

### Step 3: Update Tracking
- Update REVIEW_INDEX with completion status
- Update MASTER_LOG with transcript and review status

---

## 🎨 Course-Specific Modifications

### CrimLaw (Harcourt)
- **Focus**: MPC text verbatim, policy emphasis (~50% exam weight)
- **Prep style**: Index card approach (statute + 2-3 arguments per side)
- **Signal pattern**: Professor asks "What does statute say?" → "Prosecution argument?" → "Defense respond?"
- **Safety net**: Past outline open during class for CTRL+F lookup

### Property (Glass)
- **Focus**: Restatement (Second), doctrine + policy
- **Prep style**: Doctrine mastery with policy rationale
- **Signal pattern**: Restatement application to fact patterns
- **Cases as illustration**: Not exhaustive, focus on holdings

### Torts (Huang)
- **Focus**: Issue-spotting, comprehensive tort identification
- **Prep style**: Master all tort elements, practice issue-spotting
- **Signal pattern**: "What torts do you see?" → "Elements?" → "Defenses?"
- **Comprehensive**: Don't miss claims, even unlikely ones

### Deals (Schizer)
- **Focus**: Prep sheet format, three core problems framework
- **Prep style**: Information asymmetry analysis
- **Signal pattern**: "Information problem?" → "Contract solution?" → "Efficiency?"
- **Economic reasoning**: Cost-benefit analysis emphasis

### LPW-II (Writing Focus)
- **Focus**: Legal writing, drafting and revision
- **Prep style**: Process-oriented approach
- **Signal pattern**: Argument development and refinement
- **Multiple drafts**: Expected to iterate and improve

---

## 🔄 Multi-Step Tasks

**For tasks with 3+ steps**:
1. Create plan document in `law-school-common/06_LOGS/YYYY-MM-DD_PLAN_[task].md`
2. Use todo tracking (if available)
3. Create output document in `law-school-common/06_LOGS/YYYY-MM-DD_OUTPUT_[task].md`

---

## 📊 Document Templates

**Key templates to reference**:
- Prep template: `law-school-common/03_TEMPLATES/prep_packet_template.md`
- Review template: `law-school-common/03_TEMPLATES/review_template.md`
- QC checklist: `law-school-common/03_TEMPLATES/qc_checklist_template.md`

---

## 📞 Commands Quick Reference

**Standard commands** (see `law-school-common/00_SYSTEM/COMMAND_INTERFACE.md`):
- `/prep` - Generate prep materials
- `/review` - Process transcript and create review
- `/outline` - Update outline with new content
- `/qc` - Quality check documents

**Course-specific commands**:
- `/crimlaw-prep` - CrimLaw preparation workflow
- `/property-prep` - Property preparation workflow
- `/torts-prep` - Torts preparation workflow
- `/deals-prep` - Deals preparation workflow
- `/lpw-ii-prep` - LPW-II preparation workflow

---

## 🚨 Error Handling

**If errors occur**:
1. STOP immediately (don't compound)
2. Document what happened (be specific)
3. Assess impact
4. Propose recovery options
5. Ask before proceeding

**Never do**:
- Continue after error without fixing
- Create multiple versions of same file
- Delete files without backup
- Break established structure

---

## 🎯 Success Criteria

Documents are successful when:
1. ✅ All required sections present
2. ✅ Course-specific priorities addressed
3. ✅ Professor patterns reflected
4. ✅ Proper file naming and location
5. ✅ Tracking documents updated
6. ✅ Quality standards met

---

## 🪞 Mirroring Requirements

**CRITICAL**: This workspace maintains **dual instruction sets** for both GitHub Copilot and Claude Code.

**When creating or modifying ANY content**:
- **Skills**: Must be created in BOTH `.github/copilot-instructions.md` AND `.claude/prompts/`
- **Workflows**: Must exist in both systems with identical structure
- **Course guidance**: Must be mirrored across both instruction sets
- **Templates**: Reference templates in `law-school-common/03_TEMPLATES/` (shared)

**Mirroring Process**:
1. Create/update content in the primary location (this file)
2. Immediately duplicate to the other system (`.claude/prompts/`)
3. Maintain version consistency across both systems
4. Update both instruction sets when adding new courses or content

**Exception**: Files in `law-school-common/` are shared and don't need duplication.

This ensures seamless switching between GitHub Copilot and Claude Code for the same tasks.

## 🔗 Integration Notes

**When using GitHub Copilot**:
- You have full responsibility for all tasks
- Use this instruction set for all coursework
- Claude Code is an alternative if you prefer it
- Maintain consistent quality across documents

**For consistency**:
- Follow the same workflows regardless of AI tool
- Maintain the same file naming conventions
- Keep the same quality standards
- Update tracking documents consistently