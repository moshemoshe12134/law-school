# Law School - Common Resources

Shared templates, scripts, and prompts for all law school subjects.

## Contents

- **Prep Templates**: Standard format for class preparation notes
- **OCR Scripts**: PDF to text conversion tools
- **Echo360 Guide**: How to download and process lecture transcripts
- **Style Guide**: Writing and formatting standards
- **Setup Scripts**: Course system initialization

## Usage

### As Git Submodule (Recommended)
```bash
# In your subject repo
git submodule add https://github.com/YOUR_USERNAME/law-school-common.git common
git submodule update --init --recursive
```

### As Direct Copy
```bash
# Copy needed files to your subject repo
cp -r /path/to/law-school-common/templates ./common/
```

## What Each Subject Imports

### All Subjects
- Prep file format template (`_PREP_FORMAT_EXAMPLE.md`)
- Style guide (`elements-of-style.md`)
- Echo360 transcript guide

### Subjects with Custom Needs
- Civpro: Uses OCR scripts for case materials
- Contracts: Uses outline processor
- LPW: Uses assignment templates

## Maintenance

Keep this repo minimal and well-documented. Each file should have a clear purpose
that benefits multiple subjects.
