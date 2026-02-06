#!/usr/bin/env python3
"""
Batch OCR for law school readings.
Extracts text from PDFs using direct extraction (fast) or OCR (slow but accurate for scans).
"""

import os
import sys
from pathlib import Path

# Try importing required libraries
try:
    import pdfplumber
except ImportError:
    print("Installing pdfplumber...")
    os.system("pip3 install pdfplumber")
    import pdfplumber

# Optional OCR libraries (only for scanned PDFs)
USE_OCR = False
try:
    from pdf2image import convert_from_path
    import pytesseract
    USE_OCR = True
    print("OCR available (pdf2image + pytesseract)")
except ImportError:
    print("OCR not available. Install with: pip3 install pdf2image pytesseract")
    print("Direct text extraction will still work for digital PDFs.")


def extract_text_direct(pdf_path):
    """Extract text directly from PDF (fast, works for digital PDFs)."""
    text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return "\n\n".join(text), len(text) > 0
    except Exception as e:
        print(f"  Direct extraction error: {e}")
        return "", False


def extract_text_ocr(pdf_path):
    """Extract text from scanned PDF using OCR (slow)."""
    if not USE_OCR:
        return "", False

    try:
        print(f"  Converting to images...")
        images = convert_from_path(pdf_path, dpi=200)

        full_text = []
        for i, image in enumerate(images):
            if (i + 1) % 5 == 0:
                print(f"  OCR page {i+1}/{len(images)}...")
            text = pytesseract.image_to_string(image)
            full_text.append(text)

        return "\n\n".join(full_text), True
    except Exception as e:
        print(f"  OCR error: {e}")
        return "", False


def count_words(text):
    """Count words in text."""
    return len(text.split())


def process_pdf(pdf_path, output_path, force_ocr=False):
    """Process a single PDF file."""
    print(f"\nProcessing: {os.path.basename(pdf_path)}")

    # Check if output already exists
    if os.path.exists(output_path) and not force_ocr:
        print(f"  Skipping (already exists): {output_path}")
        return True

    # Try direct extraction first
    if not force_ocr:
        text, success = extract_text_direct(pdf_path)
        if success and count_words(text) > 50:
            print(f"  Direct extraction: {count_words(text)} words")
        else:
            print(f"  Direct extraction: minimal text, trying OCR...")
            text, success = extract_text_ocr(pdf_path)
            if success:
                print(f"  OCR: {count_words(text)} words")
    else:
        text, success = extract_text_ocr(pdf_path)
        if success:
            print(f"  OCR: {count_words(text)} words")

    # Save text
    if success and text.strip():
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"  Saved: {output_path}")
        return True
    else:
        print(f"  Failed to extract text")
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python3 ocr_batch.py <readings_folder_path> [--force-ocr]")
        print("\nExample:")
        print('  python3 ocr_batch.py "/Users/.../ACTIVE/CrimLaw/01_SOURCES/readings"')
        print("\nOptions:")
        print("  --force-ocr    Use OCR for all PDFs (skip direct extraction)")
        sys.exit(1)

    readings_path = sys.argv[1]
    force_ocr = "--force-ocr" in sys.argv

    if not os.path.isdir(readings_path):
        print(f"Error: Not a directory: {readings_path}")
        sys.exit(1)

    # Find all PDFs
    print(f"Scanning {readings_path} for PDFs...")
    pdf_files = []
    for root, dirs, files in os.walk(readings_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                pdf_files.append(pdf_path)

    if not pdf_files:
        print("No PDF files found.")
        sys.exit(0)

    print(f"Found {len(pdf_files)} PDF files\n")

    # Process each PDF
    success_count = 0
    skip_count = 0
    fail_count = 0

    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"[{i}/{len(pdf_files)}]", end="")

        # Generate output path (same name with .txt extension)
        output_path = os.path.splitext(pdf_path)[0] + ".txt"

        # Skip if already exists (unless force_ocr)
        if os.path.exists(output_path) and not force_ocr:
            print(f" Skipping (exists): {os.path.basename(output_path)}")
            skip_count += 1
            continue

        # Process the PDF
        success = process_pdf(pdf_path, output_path, force_ocr)

        if success:
            success_count += 1
        else:
            fail_count += 1

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total PDFs: {len(pdf_files)}")
    print(f"Successfully processed: {success_count}")
    print(f"Skipped (already exists): {skip_count}")
    print(f"Failed: {fail_count}")
    print("="*60)


if __name__ == "__main__":
    main()
