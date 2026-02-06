#!/usr/bin/env python3
"""
Generic PDF to text converter using Tesseract OCR.
Usage: python3 pdf_to_text.py <pdf_file> [output_file] [dpi]
"""

import sys
import os
from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

def pdf_to_text(pdf_path, output_path=None, dpi=300):
    """Convert PDF to text using OCR."""
    
    # Default output path
    if output_path is None:
        output_path = Path(pdf_path).stem + "_text.txt"
    
    print(f"Converting PDF: {pdf_path}")
    print(f"DPI: {dpi}")
    print(f"Output: {output_path}")
    print("\nConverting pages (this may take a while)...\n")
    
    # Convert PDF to images
    try:
        images = convert_from_path(pdf_path, dpi=dpi)
    except Exception as e:
        print(f"Error converting PDF to images: {e}")
        return False
    
    total_pages = len(images)
    print(f"Total pages: {total_pages}\n")
    
    # OCR each page
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, image in enumerate(images, 1):
            print(f"Processing page {i}/{total_pages}...", end='\r')
            
            # Perform OCR
            try:
                text = pytesseract.image_to_string(image)
                
                # Write page marker and text
                f.write(f"\n{'='*80}\n")
                f.write(f"PAGE {i}\n")
                f.write(f"{'='*80}\n\n")
                f.write(text)
                f.write("\n")
            except Exception as e:
                print(f"\nError processing page {i}: {e}")
                continue
    
    print(f"\n\nConversion complete!")
    print(f"Output saved to: {output_path}")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 pdf_to_text.py <pdf_file> [output_file] [dpi]")
        print("\nExamples:")
        print("  python3 pdf_to_text.py document.pdf")
        print("  python3 pdf_to_text.py document.pdf output.txt")
        print("  python3 pdf_to_text.py document.pdf output.txt 400")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    dpi = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file not found: {pdf_path}")
        sys.exit(1)
    
    success = pdf_to_text(pdf_path, output_path, dpi)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
