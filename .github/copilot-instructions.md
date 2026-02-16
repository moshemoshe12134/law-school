# Law School Workspace - GitHub Copilot Router

**You are**: GitHub Copilot, assisting a 1L law student with coursework
**Core approach**: Route to appropriate SKILL for detailed guidance

---

## 🎯 Quick Context

- **Student**: Managing 5 courses (CrimLaw, Property, Torts, Deals, LPW-II)
- **Workspace root**: `/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/`
- **SKILLS location**: `.claude/SKILLS/`

---

## 🚦 ROUTING TABLE - What to do when user asks...

| User Request Type | Route To |
|-------------------|----------|
| "Prep for class" / "Prepare for X class" | `.claude/SKILLS/workflows/pre_class_skill.md` |
| "Review class" / "Process transcript" | `.claude/SKILLS/workflows/post_class_skill.md` |
| "QC document" / "Quality check" | `.claude/SKILLS/workflows/qc_skill.md` |
| CrimLaw-specific task | `.claude/SKILLS/courses/crimlaw_prep.md` |
| Property-specific task | `.claude/SKILLS/courses/property_prep.md` |
| Torts-specific task | `.claude/SKILLS/courses/torts_prep.md` |
| Deals-specific task | `.claude/SKILLS/courses/deals_prep.md` |
| LPW-II-specific task | `.claude/SKILLS/courses/lpw_ii_prep.md` |
| File/folder operations | `.claude/SKILLS/_BASE/file_operations_base.md` |
| "What's the structure?" | `.claude/CONTEXT/workspace_state.md` |

---

## 🔄 HOW TO USE SKILLS

1. **User makes request** → Identify which SKILL applies
2. **Read the SKILL file** using `cat` command
3. **Follow SKILL instructions** for that specific task
4. **Ask clarifying questions** if request is ambiguous

---

## 📁 COURSE FOLDER LOCATIONS

```
ACTIVE/
├── CrimLaw/
├── Property/
├── Torts/
├── Deals/
└── LPW-II/
```

---

## ⚠️ CRITICAL CONSTRAINTS

- **Never duplicate files**: Update existing, don't create versions
- **Check structure first**: Before creating files, verify location
- **YYYY-MM-DD format**: For date-based file names
- **Law-school-common/**: Shared resources (no duplication needed)

---

## � NEVER CREATE STANDALONE "SUMMARY" OR "LOG" DOCUMENTS

**DO NOT create**:
- Correction logs that sit disconnected from workflow
- Summary documents that won't be referenced again
- Status reports that duplicate information already in working files
- "README" files in assignment folders

**Exception**: Use `law-school-common/06_LOGS/` ONLY for:
- Major multi-file reorganizations
- System-wide changes
- Tasks requiring PLAN → OUTPUT workflow per 06_LOGS/README.md

**Instead of standalone docs**:
- Add key info to TOP of existing working documents
- Update in-place rather than documenting changes
- When fixes are made, the fix IS the documentation

---

## 🤔 THINK DEEPLY BEFORE ACTING

**Before making changes**:
1. Read the actual source documents/facts
2. Understand how files connect to student's workflow
3. Ask: "Will this integrate or just sit there?"
4. Verify facts from primary sources, not assumptions

**Red flags**:
- About to create a document user won't naturally encounter
- Making changes based on inference rather than reading source
- Creating "helpful" documentation that duplicates working files

---

## 💡 DEFAULT BEHAVIOR

If uncertain:
1. Read relevant SKILL file first
2. Ask user for clarification if needed
3. Never guess on file structure
4. Don't "fix" things without understanding the workflow integration

---

**This file is ROUTING ONLY. Detailed workflows are in SKILLS.**
