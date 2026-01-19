# File Conversion Recommendations for AI Digestion

**Last Updated**: [Date]
**Purpose**: Ensure all materials are in formats that AI agents can easily read, analyze, and work with.

---

## Current File Inventory & Status

### ✅ Already AI-Digestible (No conversion needed)

| Location | File Type | Status | Notes |
|----------|-----------|--------|-------|
| `02_SOURCES/core/` | PDF | ✅ Good | Modern PDFs with text layer; AI can extract content |
| `02_SOURCES/supplement/` | PDF | ✅ Good | Modern PDFs with text layer; AI can extract content |
| `02_SOURCES/exams_raw/` | PDF (14 files) | ✅ Good | AI can parse exam questions and model answers |
| `MASTER_LOG.md` | Markdown | ✅ Excellent | Native markdown is ideal for AI |
| `TEMPLATES/*.md` | Markdown | ✅ Excellent | Native markdown is ideal for AI |

### ✅ Good Format (DOCX - AI-readable, but consider conversion)

| Location | File Type | Recommendation | Priority |
|----------|-----------|----------------|----------|
| `07_OUTLINE/*.docx` (9 files) | DOCX | Convert to Markdown for active editing | MEDIUM |

**Details**:
- `Glass_Property_F19_Outline.docx`
- `Glass_Property_S19_Outline.docx`
- `Glass_Property_S19_Rules.docx`
- `Glass_Property_S19_Themes.docx`
- `Property_Glass_F19.docx`
- `Property_Glass_S21_Outline(Shulman).docx`
- `Property_Glass_F19 (Attack).docx` (in `attack/`)
- `Property_Glass_S21_Attack(Shulman).docx` (in `attack/`)

**Why Convert?**
- Markdown is plain text → easier for AI to read/write/edit
- Version control friendly (can track changes with git)
- Faster for AI agents to parse and generate
- Universal compatibility (no Microsoft dependencies)

**When to Convert?**
- **If using these as templates**: Convert now
- **If just referencing**: Keep as DOCX (AI can still read)
- **For your own outline**: Start fresh in Markdown (`.md`)

---

## Recommended AI-Friendly Formats

### Tier 1 (Best for AI Collaboration):
1. **Markdown (`.md`)** ← PREFERRED for all new documents
   - Use for: Prep packets, reviews, outlines, notes, crosswalks
   - Why: Plain text, easy to edit, AI-native, version control friendly

### Tier 2 (Good for AI Reading):
2. **Plain Text (`.txt`)**
   - Use for: Quick notes, simple lists
   - Why: Universal, lightweight

3. **DOCX**
   - Use for: If you must use Word (AI can read, but slower to edit)
   - Why: Structured, but requires parsing

4. **PDF (with text layer)**
   - Use for: Final documents, source materials (read-only)
   - Why: AI can extract text, but not ideal for editing

### Tier 3 (Avoid for Working Documents):
5. **PDF (scanned images)** - AI struggles without OCR
6. **Handwritten notes (images)** - AI can read but text is better
7. **Proprietary formats** (`.pages`, `.odt`, etc.) - unnecessary friction

---

## Conversion Process (If Needed)

### To Convert DOCX → Markdown:

**Option 1: Use Pandoc** (command-line tool)
```bash
pandoc input.docx -o output.md
```

**Option 2: Manual copy-paste**
- Open DOCX in Word
- Copy content
- Paste into `.md` file
- Clean up formatting using markdown syntax

**Option 3: Use AI Agent**
- Ask AI to read DOCX and create clean markdown version
- AI can reformat, restructure, and improve organization

### To Convert PDF → Markdown (for editable content):

**For source materials (textbooks, supplements)**:
- ❌ DO NOT convert entire books (too large, copyright issues)
- ✅ DO extract relevant sections as needed into prep packets/outlines

**For past outlines (if needed)**:
- Use AI to read PDF and extract key content into markdown
- Restructure using your outline template

---

## Workflow Recommendations

### For New Documents (going forward):

| Document Type | Format | Location |
|---------------|--------|----------|
| Prep packets | `.md` | `04_PREP/` |
| Class notes (structured) | `.md` | `05_CLASS_NOTES/structured/` |
| Reviews | `.md` | `06_REVIEW/` |
| Outline inserts | `.md` | `07_OUTLINE/` |
| Crosswalks | `.md` | `03_MAPPING/` |
| Metrics | `.md` | `08_METRICS/` |

### For Source Materials (read-only):

| Material | Keep As | Location |
|----------|---------|----------|
| Textbooks | PDF | `02_SOURCES/core/` |
| Supplements | PDF | `02_SOURCES/supplement/` |
| Statutes | PDF or `.txt` | `02_SOURCES/statutes/` |
| Past exams | PDF | `02_SOURCES/exams_raw/` |

### For Past Outlines (reference):

**Option A (Recommended)**: Keep as-is (DOCX/PDF)
- Reference when needed
- Extract relevant sections into your own markdown outline

**Option B**: Convert to Markdown
- Only if you plan to heavily edit/reuse
- Use as starting template

---

## AI Agent Instructions

When creating new documents:
1. **Always use Markdown** (`.md`) format
2. **Use templates** from `TEMPLATES/` directory
3. **Keep formatting simple**:
   - Headers: `#`, `##`, `###`
   - Lists: `-` or `1.`
   - Bold: `**text**`
   - Code blocks: triple backticks
   - Tables: Markdown table syntax

When reading existing documents:
- PDFs → Extract text directly
- DOCX → Parse structure and content
- Markdown → Read natively (fastest)

---

## Conversion Priority List

### HIGH Priority (Do before starting semester):
- [ ] None currently - structure is good!

### MEDIUM Priority (Optional, based on usage):
- [ ] Convert frequently-referenced DOCX outlines to Markdown if using as templates

### LOW Priority (Leave as-is):
- [ ] Past outlines in DOCX/PDF (keep for reference)
- [ ] Source materials in PDF (read-only is fine)

---

## Summary: You're Already 95% AI-Ready!

✅ **Good news**: Most of your files are already in AI-friendly formats:
- PDFs (textbooks, exams) → AI can extract text
- Markdown templates → Perfect for AI collaboration
- DOCX outlines → AI can read (conversion optional)

🎯 **Going forward**: Use Markdown (`.md`) for all new working documents

🤖 **AI agents will handle**:
- Reading PDFs to extract doctrine/cases
- Parsing DOCX outlines for reference
- Creating new markdown documents from templates
- Editing and updating your study materials

---

**No immediate conversion work required. System is ready to use!**
