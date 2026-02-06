# Plan: CrimLaw course_files_export Organization

**Date:** 2026-01-21
**Task:** Meticulously organize course_files_export folder
**Location:** ACTIVE/CrimLaw/01_SOURCES/course_files_export/

---

## Executive Summary

The `course_files_export` folder contains **249 files** across multiple categories that need to be organized according to the standardized folder structure. Current organization is inconsistent (mixed naming conventions, redundant folders, unclear hierarchy).

---

## Current State Analysis

### Existing Structure

```
course_files_export/
├── Past Exams/                    # 19 years of exams (2002-2025)
├── Powerpoint Slides/             # Organized by year (2020-2025)
├── Readings and Class Materials/  # Topic-based PDFs
├── Syllabus/                      # Single PDF file
├── TA Slides 2025/                # Current + historical TA sessions
├── unfiled/                       # Contains syllabus PDF
└── course_image/                  # (Empty - doesn't exist)
```

### Issues Identified

1. **Inconsistent naming**: Mixed capitalization ("Past Exams" vs spec's "past_exams")
2. **Redundant syllabus**: Both `Syllabus/` and `unfiled/` contain same file
3. **Missing folders**: `lecture_slides/`, `readings/`, `ta_slides/` not in spec
4. **No documentation**: No README files explaining contents
5. **Poor naming**: "Readings and Class Materials" too verbose
6. **No integration**: Existing 01_SOURCES structure has duplicate/outdated content

---

## Target Structure

According to [FOLDER_STRUCTURE_SPEC.md](../../law-school-common/00_SYSTEM/FOLDER_STRUCTURE_SPEC.md):

```
01_SOURCES/
├── syllabus/                      # ✓ Already exists with assignments
│   ├── syllabus.pdf              # Need to add
│   ├── syllabus_parsed.md        # ✓ Already exists
│   └── assignments/              # ✓ Already exists
├── past_exams/                    # ⚠️ Exists but incomplete (only 1 file)
├── past_outlines/                 # ✓ Already exists
├── lecture_slides/                # ❌ Need to create
├── readings/                      # ❌ Need to create
└── ta_slides/                     # ❌ Need to create
```

---

## Reorganization Plan

### Phase 1: Integrate Past Exams

**Action:** Merge course_files_export exams into existing `past_exams/`

**Steps:**
1. Backup existing `01_SOURCES/past_exams/2006 Spring Exam.pdf` (just in case)
2. Move all `Past Exams/*` folders to `past_exams/`
3. Standardize naming: "Spring 2025 Exam" → "2025_Spring"
4. Create `INDEX.md` listing all exams with metadata

**Files affected:** ~80 PDFs across 19 exam years

---

### Phase 2: Organize Lecture Slides

**Action:** Create `lecture_slides/` and reorganize by year

**Steps:**
1. Create `01_SOURCES/lecture_slides/`
2. Move `Powerpoint Slides/*` to `lecture_slides/`
3. Rename year folders: "2025 Slides" → "2025_Spring"
4. Standardize slide naming within folders
5. Create `INDEX.md` with slide descriptions

**Files affected:** ~45 PPT/PDF files

---

### Phase 3: Organize Readings

**Action:** Create `readings/` and organize by topic

**Steps:**
1. Create `01_SOURCES/readings/`
2. Move `Readings and Class Materials/*` to `readings/`
3. Standardize folder names:
   - "01. Introduction" → "01_introduction"
   - "02. The Elements of Criminal Law" → "02_elements"
   - "03. The Law of Homicide" → "03_homicide"
   - etc.
4. Create `INDEX.md` mapping topics to class sessions

**Files affected:** ~80 PDFs across 10 topics

---

### Phase 4: Organize TA Slides

**Action:** Create `ta_slides/` and organize by year/TA

**Steps:**
1. Create `01_SOURCES/ta_slides/`
2. Move `TA Slides 2025/*` to `ta_slides/`
3. Structure: `ta_slides/2025_spring/`, `ta_slides/historical/`
4. Organize historical slides by TA name:
   - `historical/corine_2021/`
   - `historical/chris_2023/`
   - `historical/abby_2023/`
   - `historical/vineet_2021/`
   - `historical/isaiah_2021/`
5. Create `INDEX.md` with TA names and topics covered

**Files affected:** ~50 PPT files

---

### Phase 5: Syllabus Integration

**Action:** Consolidate syllabus files

**Steps:**
1. Compare `Syllabus/Harcourt Criminal Law Syllabus 2026.pdf` (1.6MB) with existing `syllabus/Harcourt_CrimLaw_Syllabus_2026.txt` (50KB)
2. If PDF is better quality/original:
   - Copy to `syllabus/syllabus.pdf`
3. Delete `course_files_export/Syllabus/` folder
4. Delete `course_files_export/unfiled/` folder (redundant)

---

### Phase 6: Clean Up course_files_export

**Action:** Remove empty folder after migration

**Steps:**
1. Verify all files moved successfully
2. Delete `course_files_export/` folder (now empty)

---

### Phase 7: Documentation

**Action:** Create README files

**Steps:**
1. Create `01_SOURCES/README.md` explaining folder structure
2. Create `INDEX.md` files in each subfolder:
   - `past_exams/INDEX.md`
   - `lecture_slides/INDEX.md`
   - `readings/INDEX.md`
   - `ta_slides/INDEX.md`

---

## Validation Checklist

After reorganization:

- [ ] All files accounted for (count should be ~249)
- [ ] No broken symlinks or references
- [ ] Folder names match spec (lowercase, underscores)
- [ ] README files exist
- [ ] Spot-check 5 random files open correctly
- [ ] `course_files_export/` folder deleted
- [ ] Git status shows expected changes

---

## Risk Mitigation

**Potential Issues:**
1. File conflicts with existing `past_exams/`
   - **Solution:** Check dates/quality, keep better version

2. Broken links in assignments
   - **Solution:** Update assignment files if they reference old paths

3. Missing files during migration
   - **Solution:** Count files before/after each move

---

## Estimated Time

- Phase 1 (Past Exams): 10 min
- Phase 2 (Lecture Slides): 8 min
- Phase 3 (Readings): 10 min
- Phase 4 (TA Slides): 8 min
- Phase 5 (Syllabus): 3 min
- Phase 6 (Cleanup): 2 min
- Phase 7 (Documentation): 10 min

**Total:** ~50 minutes

---

## Next Actions

1. User approval to proceed
2. Execute Phase 1-7 in order
3. Validate each phase before proceeding
4. Create output document with results
