import pytesseract
from pdf2image import convert_from_path
import os

# Path to the PDF file
pdf_path = '/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/ACTIVE/Torts/01_SOURCES/core/Case Briefs for the casebook Tort Law- Principles in -- James M Underwood -- ( WeLib.org ).pdf'

# Output text file path
output_text_path = '/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/ACTIVE/Torts/01_SOURCES/core/case_briefs.txt'

# Convert PDF to images
images = convert_from_path(pdf_path)

# Extract text from each image and combine
full_text = ''
for i, image in enumerate(images):
    print(f"Processing page {i+1}...")
    text = pytesseract.image_to_string(image)
    full_text += text + '\n\n'

# Save the extracted text to a file
with open(output_text_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Text extracted and saved to {output_text_path}")