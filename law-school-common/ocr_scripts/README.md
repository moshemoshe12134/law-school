# OCR Scripts

Shared OCR utilities for converting PDFs to text across all law school projects.

## Important: Book Pages vs PDF Pages

**Book page numbers** (printed on the pages) are different from **PDF page numbers** (position in the PDF file).

For example:
- Book page 1 might be at PDF page 20 (after title page, copyright, table of contents, etc.)
- The **page offset** is the difference: `PDF page - book page = offset`
- In this example: `20 - 1 = 19` (offset = 19)

You **must** determine the correct page offset before extracting pages from a casebook.

## Scripts

### `find_page_offset.py`
Helper tool to determine the page offset for a casebook PDF.

**Usage:**
```bash
python3 find_page_offset.py <casebook_pdf>
```

This interactive tool helps you:
1. Check specific PDF pages to see their content
2. Calculate the offset from known book/PDF page pairs
3. Get the exact offset value to use in extraction scripts

### `extract_casebook_pages.py`
Extract specific page ranges from a casebook based on syllabus assignments.

**Features:**
- Automatically converts book page numbers to PDF page numbers
- Verifies page numbers every 10 pages to catch offset errors
- Extracts all readings into a single master document
- Shows progress and verification status

**Before using:**
1. Run `find_page_offset.py` to determine the page offset
2. Edit `extract_casebook_pages.py` and set `PAGE_OFFSET` to the correct value
3. Then run the extraction

**Usage:**
```bash
python3 extract_casebook_pages.py <casebook_pdf> [output_file] [dpi]
```

**Verification:**
The script verifies page numbers every 10 pages by checking if the extracted text contains the expected page number. This helps catch offset errors early without slowing down the extraction too much.

### `pdf_to_text.py`
Generic PDF to text converter using Tesseract OCR.

**Usage:**
```bash
python3 pdf_to_text.py <pdf_file> [output_file] [dpi]
```

**Examples:**
```bash
# Convert with default settings (300 DPI)
python3 pdf_to_text.py document.pdf

# Specify output file
python3 pdf_to_text.py document.pdf output.txt

# Use higher DPI for better quality (slower)
python3 pdf_to_text.py document.pdf output.txt 400
```

## Requirements

Install dependencies:
```bash
pip install pdf2image pytesseract
```

Also requires Tesseract OCR to be installed on your system:
- macOS: `brew install tesseract`
- Linux: `apt-get install tesseract-ocr`

## Notes

- Higher DPI values (e.g., 400) provide better OCR quality but take longer to process
- Default DPI of 300 is a good balance between quality and speed
- Output files include page markers for easy navigation
