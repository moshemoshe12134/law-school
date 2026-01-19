# Law School Projects - Master Organizational Structure

**Standard folder structure for ALL courses**

## Required Folders (Every Course Must Have)

```
[COURSE_NAME]/
├── textbook/                    # Textbook PDFs and extracted text
│   ├── [original_pdf]
│   └── [extracted_text]
│
├── syllabus/                    # Course syllabus (PDF and text)
│   ├── [syllabus_pdf]
│   └── [syllabus_text]
│
├── transcripts/                 # Lecture audio transcripts
│   └── YYYY-MM-DD_[Course].txt  # Named by date
│
├── course_reference/            # Core reference documents
│   ├── class_schedule.txt       # Date ↔ Lecture mapping
│   ├── reading_assignments.txt  # Lecture → Pages/Topics
│   └── [organized_readings].txt # Textbook organized by topic/lecture
│
├── additional/                  # Supplementary materials
│   ├── source_materials/        # Cases, complaints, readings
│   │   ├── cases/
│   │   ├── complaints/
│   │   └── readings/
│   ├── practice_exercises/      # Problems, exercises, practice
│   │   ├── ta_sections/
│   │   ├── problems_hypos/
│   │   └── glannon/
│   ├── lecture_support/         # Professor materials
│   │   ├── class_notes/
│   │   ├── powerpoints/
│   │   └── slides/
│   └── exam_prep/               # Exam preparation materials
│       ├── past_exams/
│       ├── practice_answers/
│       └── writing_examples/
│
├── prep/                        # Pre-lecture preparation (to be created)
│   └── lecture_[XX]_prep.txt
│
├── review/                      # Post-lecture review (to be created)
│   └── lecture_[XX]_review.txt
│
└── _ai_reference/               # AI-only documentation
    ├── AI_GUIDE.md              # Quick reference for AI
    └── [other_readme_files]     # Verbose docs for AI use
```

## Naming Conventions

### Files
- **Transcripts**: `YYYY-MM-DD_[CourseName].txt` (e.g., `2025-09-02_Contracts.txt`)
- **Prep docs**: `lecture_[XX]_prep.txt` (e.g., `lecture_05_prep.txt`)
- **Review docs**: `lecture_[XX]_review.txt` (e.g., `lecture_05_review.txt`)
- **Extracted textbook**: `[COURSE]_textbook_extracted.txt`
- **Organized readings**: `[COURSE]_readings_by_topic.txt` (if applicable)

### Folders
- All lowercase with underscores: `course_reference`, `lecture_support`
- Exception: `Lecture Transcripts` can stay as-is for user visibility

## Purpose of Each Folder

### `textbook/`
- Original textbook PDF
- OCR-extracted full text
- Any supplementary textbook materials

### `syllabus/`
- Course syllabus (PDF and OCR'd text)
- Any syllabus updates or amendments

### `transcripts/` (or `Lecture Transcripts/`)
- Audio transcripts from each lecture
- Named by date for easy lookup

### `course_reference/`
- **Core navigation files** - most frequently accessed
- Class schedule (date/lecture mapping)
- Reading assignments
- Organized/extracted readings

### `additional/`
- **Everything else** - supplementary materials
- Organized into subcategories:
  - `source_materials/` - primary sources (cases, complaints, articles)
  - `practice_exercises/` - problems to work through
  - `lecture_support/` - professor's materials (notes, slides)
  - `exam_prep/` - exam-related materials

### `prep/` and `review/`
- Working folders for your study materials
- Created as needed throughout semester

### `_ai_reference/`
- Documentation for AI assistant
- User doesn't need to read these
- Includes verbose READMEs, guides, etc.

## File Index System

Each course has an index file: `_FILE_INDEX.txt`
- Lists every file in the course folder
- Shows file location and purpose
- Updated whenever files are added/moved
- Used by AI to check for duplicates and determine placement

Master index: `/law school projects/_MASTER_FILE_INDEX.txt`
- Cross-course index
- Tracks all files across all courses
- Helps identify duplicates across courses
