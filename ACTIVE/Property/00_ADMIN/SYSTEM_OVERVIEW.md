# Property Law - Course System Overview

**System Version**: 1.0
**Created**: [Date]
**Status**: ✅ Ready to use (awaiting syllabus)

---

## 📁 Directory Structure

```
law-school-Property/
├── 00_ADMIN/               → Exam rules, policies, workflow documentation
│   ├── README.md          → Quick start guide & daily workflow
│   ├── conversion_recommendations.md → AI format guide
│   └── SYSTEM_OVERVIEW.md → This file
│
├── 01_SYLLABUS/           → Syllabus & assignment table
│   └── PLACEHOLDER_syllabus_pending.md → Action items for when syllabus arrives
│
├── 02_SOURCES/            → Read-only source materials
│   ├── core/             → Main textbook (Singer et al., 8th ed.)
│   ├── supplement/       → Examples & Explanations (Burke et al., 5th ed.)
│   ├── exams_raw/        → 14 past exams (Glass, Heller, Merrill)
│   ├── statutes/         → Statutory materials (to be populated)
│   └── README.md
│
├── 03_MAPPING/            → Crosswalks & exam specification
│   └── PLACEHOLDER_exam_spec.md → Past exams to parse
│
├── 04_PREP/               → Per-class prep packets (2-4 pages each)
│
├── 05_CLASS_NOTES/        → Class notes
│   ├── raw/              → Raw notes from class (can be messy)
│   └── structured/       → Cleaned/organized notes
│
├── 06_REVIEW/             → Post-class review documents
│
├── 07_OUTLINE/            → Cumulative outline & attack materials
│   ├── attack/           → Attack outlines (3 past versions available)
│   ├── hypos/            → Hypo bank (to be built)
│   ├── README.md
│   └── [9 past outlines for reference]
│
├── 08_METRICS/            → Time tracking, accuracy scores, weak topics
│
├── TEMPLATES/             → Reusable templates
│   ├── README.md
│   ├── mapping_crosswalk_template.md
│   ├── prep_packet_template.md
│   ├── review_template.md
│   ├── exam_spec_template.md
│   ├── outline_insert_template.md
│   └── metrics_template.md
│
└── MASTER_LOG.md          → Central tracking spine (class-by-class)
```

---

## 🎯 System Goals

1. **Prevent over-prep**: 60-90 min per class maximum
2. **Stay exam-focused**: Everything maps to exam spec
3. **Build incrementally**: Outline grows class-by-class
4. **Track accuracy**: Learn what professor emphasizes
5. **Identify weaknesses**: Flag and remediate gaps early

---

## 📊 Current Status

### ✅ Completed Setup
- [x] Folder structure created
- [x] All existing files organized and moved
- [x] Templates created (6 templates ready)
- [x] MASTER_LOG.md initialized
- [x] Placeholder files for pending items
- [x] README guides in key directories
- [x] Conversion recommendations documented

### ⏳ Awaiting Input
- [ ] Syllabus (from professor)
- [ ] Assignment table (derived from syllabus)
- [ ] Professor identification (Glass? Heller? Merrill? Other?)
- [ ] Exam spec (parse past exams)

### 📚 Resources Available
- **1 core textbook** (PDF, 8th ed.)
- **1 supplement** (E&E, 5th ed.)
- **14 past exams** (multiple professors)
- **9 past outlines** (Glass - various semesters)
- **3 attack outlines** (condensed versions)

---

## 🚀 Quick Start (When Syllabus Arrives)

### One-Time Setup (30-60 min):
1. **Upload syllabus** to [01_SYLLABUS/](01_SYLLABUS/)
2. **Parse 2-3 past exams** (your professor if possible)
   - Use [TEMPLATES/exam_spec_template.md](TEMPLATES/exam_spec_template.md)
   - Save as [03_MAPPING/exam_spec.md](03_MAPPING/exam_spec.md)
3. **Update MASTER_LOG.md**:
   - Fill in professor, semester, exam date
   - Populate class-by-class table from syllabus
4. **Create crosswalk skeletons** in `03_MAPPING/` for each class

### Per-Class Workflow (60-90 min prep + 20-30 min review):

**BEFORE CLASS**:
1. Check [MASTER_LOG.md](MASTER_LOG.md) for assigned readings
2. Use [TEMPLATES/prep_packet_template.md](TEMPLATES/prep_packet_template.md)
3. Create prep packet: `04_PREP/class_[NUM]_prep.md`
4. Read assigned materials (statutes → cases → supplements)
5. Fill in predictions

**AFTER CLASS**:
1. Use [TEMPLATES/review_template.md](TEMPLATES/review_template.md)
2. Create review: `06_REVIEW/class_[NUM]_review.md`
3. Score predictions (0-2 scale)
4. Extract outline inserts
5. Update [MASTER_LOG.md](MASTER_LOG.md)

**WEEKLY**:
1. Compile metrics using [TEMPLATES/metrics_template.md](TEMPLATES/metrics_template.md)
2. Review weak topics
3. Update spaced repetition queue

---

## 📖 Course Profile: Property Law

Based on typical Property courses, expect:

| Parameter | Setting | Notes |
|-----------|---------|-------|
| **Statute/Code Weight** | MEDIUM-HIGH | Statutes + Restatement matter |
| **Policy Weight** | MEDIUM | Less than CrimLaw, more than Deals |
| **Case Depth** | MEDIUM-HIGH | Cases establish foundational rules |
| **Hypo Focus** | HIGH | Very hypo-heavy for exam prep |
| **Exam Format** | TBD | Parse past exams to determine |

*Adjust after first few classes based on actual professor style*

---

## 🔧 Customization Notes

This system is a **starting point**. Adjust as needed:
- Modify template lengths/sections based on what works
- Tune time caps if necessary (but keep strict limits!)
- Add/remove metrics based on usefulness
- Adapt to professor's specific style after Classes 1-3

---

## 🤖 AI Agent Hand-Off

To delegate tasks to AI agents:

1. **Point to specific template** for the task
2. **Provide inputs**: class number, topic, readings
3. **Specify output location** (which directory)
4. **Reference course parameters** from [MASTER_LOG.md](MASTER_LOG.md)

Example delegation:
> "Create a prep packet for Class 5 using TEMPLATES/prep_packet_template.md. Topic is Adverse Possession. Assigned reading is Singer pp. 123-156 and Restatement § 201. Save as 04_PREP/class_005_prep.md."

---

## 📞 Support & Feedback

**For system questions**:
- See [00_ADMIN/README.md](00_ADMIN/README.md) for workflow guide
- See [TEMPLATES/README.md](TEMPLATES/README.md) for template usage

**For course questions**:
- Check professor's office hours (TBD - from syllabus)
- TA information (TBD - from syllabus)

---

## 🎓 Next Steps

### Immediate (When you have 30 min):
- [ ] Identify your professor
- [ ] Scan 1-2 past exams from that professor
- [ ] Get rough sense of exam format

### Before Class 1:
- [ ] Receive syllabus
- [ ] Create assignment table
- [ ] Parse past exams → create exam spec
- [ ] Update MASTER_LOG.md
- [ ] Prepare Class 1 prep packet

### Ongoing:
- [ ] Maintain daily workflow (prep → class → review)
- [ ] Build outline incrementally
- [ ] Track metrics weekly
- [ ] Adjust system based on what works

---

**System Status**: ✅ Ready to activate when syllabus arrives

**Handoff-Ready**: Yes - all templates, structure, and documentation in place

**Estimated Setup Time Remaining**: 30-60 min once syllabus is available
