# Torts/01_SOURCES Organization Plan

**Date:** 2026-01-20
**Course:** Torts (Huang)
**Task:** Organize 01_SOURCES folder according to standard structure

---

## Current State

**Files:** 96 total
**Folders:**
- ✅ `syllabus/` - 16K (correct)
- ✅ `past_exams/` - 1.2M (correct, but missing some exams)
- ✅ `past_outlines/` - 23M (correct)
- ❌ `Huang Originals (1)/` - 29M (duplicate)
- ❌ `Huang Outlines (1)/` - 45M (duplicate)
- ❌ `Textbooks/` - 166M (wrong location)
- ❌ `cases/` - 16K (wrong location)

## Problems Identified

1. **Exam duplication:** Same exams in 3 locations
   - `past_exams/` (main)
   - `Huang Originals (1)/Old Exams (1)/Huang Exams (1)/`
   - `Huang Outlines (1)/Huang Exams (1)/`

2. **Outline duplication:** 16 PDF versions in "Huang Outlines (1)/Outline PDFs (To be watermarked) (1)/" duplicate DOCX files in `past_outlines/Huang/`

3. **Textbook location:** Abraham's Tort Theory book (166M) in root instead of `core/`

4. **Cases folder:** Adams v Bullock.docx not in proper location

## Target Structure

```
01_SOURCES/
├── core/                    # NEW - Case supplements and theory
│   ├── abraham_tort_theory.pdf
│   └── cases/
│       └── adams_v_bullock.docx
├── syllabus/                # ✅ KEEP
│   └── Torts 2026 Prof Huang Syllabus as of January 14.pdf
├── past_exams/              # ✅ KEEP + CONSOLIDATE
│   ├── [2013-2018 exams]
│   └── [merged unique exams from duplicate folders]
├── past_outlines/           # ✅ KEEP + DEDUPLICATE
│   ├── Huang/
│   │   └── [Huang-specific outlines]
│   ├── Torts_Spring 2024_Ahmed_Full Outline.docx
│   ├── Torts_Spring 2022_Huang_Full Outline.docx
│   └── Torts Attack Outline.docx
└── README.md                # NEW - Document contents
```

## Execution Steps

### Phase 1: Create core/ and move materials
1. Create `core/` folder
2. Create `core/cases/` subfolder
3. Move `Textbooks/Abrahams The Forms and Functions of Tort Law, 4th....pdf` → `core/abraham_tort_theory.pdf`
4. Move `cases/Adams v Bullock.docx` → `core/cases/adams_v_bullock.docx`

### Phase 2: Consolidate past_exams/
5. Compare exams in `past_exams/` vs duplicate folders
6. Copy unique exams from `Huang Outlines (1)/Huang Exams (1)/` to `past_exams/`
7. Rename exams to consistent naming: `YYYY_Season_Huang_Torts_Exam.pdf`

### Phase 3: Remove duplicate folders
8. Verify all unique content preserved
9. Delete `Huang Originals (1)/`
10. Delete `Huang Outlines (1)/`

### Phase 4: Clean up past_outlines/
11. Remove duplicate DOCX files in `past_outlines/Huang/` (verify no unique content)
12. Organize by professor/year if needed

### Phase 5: Create README and validate
13. Create `README.md` documenting folder contents
14. Validate file count and integrity
15. Verify no broken references

## Expected Outcome

**Before:** 96 files, 7 folders (3 duplicates)
**After:** ~70 files, 4 folders (0 duplicates)

**Space savings:** ~74M (duplicate folders removed)

---

## Risk Assessment

**Low risk:**
- Moving files within same parent directory
- Creating new folders

**Medium risk:**
- Deleting duplicate folders (must verify unique content preserved)

**Mitigation:**
- Spot-check 2-3 files after each move
- Verify no duplicate filenames before deletion
- Keep user informed at each checkpoint
