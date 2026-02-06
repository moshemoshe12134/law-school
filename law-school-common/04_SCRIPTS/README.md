# 04_SCRIPTS - Automation Scripts

**Purpose:** Contains automation scripts for system maintenance and document processing.

## Current Scripts

### Setup Scripts
- `setup_all_course_systems.py` - Initialize folder structures for all courses

### OCR Scripts
- Located in `../ocr_scripts/` directory:
  - Transcript processing
  - PDF OCR
  - Text extraction

## Usage

1. **When setting up a new semester:** Run `setup_all_course_systems.py`
2. **When processing transcripts:** Use scripts in `../ocr_scripts/`
3. **When automating repetitive tasks:** Add new scripts here

## Script Principles

- All scripts should be idempotent (safe to run multiple times)
- Scripts should validate before making changes (check for existing files)
- Scripts should log actions taken
- Scripts should handle errors gracefully

## Future Scripts

Potential additions:
- Automated MASTER_LOG population from syllabus
- Batch transcript processing
- Prewrite generation from outline sections
- Review document signal extraction
- Cross-course content linking

## Script Maintenance

- Test scripts on non-critical data first
- Keep scripts in version control
- Document usage in README files
- Update this folder's README when adding scripts
