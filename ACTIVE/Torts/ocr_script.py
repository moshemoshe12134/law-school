import os
import re

import pdf2image
import pytesseract

pdf_path = "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-Torts/02_SOURCES/core/Abraham's The Forms and Functions of Tort Law, 4th (Concepts -- KENNETH S_ABRAHAM, Kenneth S Abraham, 1946-, by Kenneth S_ -- 2012, 2012 -- Foundation -- 9781609300531 -- 4555cf133eab1cbd86d26f5fa3eaed4b -- Anna’s Archive.pdf"
output_txt = "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school/law-school-Torts/02_SOURCES/core/Abraham_OCR.txt"

dpi = 300
batch_size = 8

page_marker_re = re.compile(r"^--- Page (\d+) ---$")


def get_last_ocr_page(path):
    if not os.path.exists(path):
        return 0
    last_page = 0
    with open(path, "r", errors="ignore") as handle:
        for line in handle:
            match = page_marker_re.match(line.strip())
            if match:
                last_page = int(match.group(1))
    return last_page


info = pdf2image.pdfinfo_from_path(pdf_path)
total_pages = int(info["Pages"])
start_page = get_last_ocr_page(output_txt) + 1

if start_page > total_pages:
    print("OCR already complete:", output_txt)
    raise SystemExit(0)

mode = "a" if start_page > 1 else "w"
with open(output_txt, mode) as f:
    for batch_start in range(start_page, total_pages + 1, batch_size):
        batch_end = min(batch_start + batch_size - 1, total_pages)
        images = pdf2image.convert_from_path(
            pdf_path,
            dpi=dpi,
            first_page=batch_start,
            last_page=batch_end,
        )
        for offset, image in enumerate(images):
            page_num = batch_start + offset
            text = pytesseract.image_to_string(image)
            f.write(f"--- Page {page_num} ---\n")
            f.write(text.rstrip())
            f.write("\n\n")
            f.flush()
        print(f"OCR progress: {batch_end}/{total_pages}")

print("OCR complete. Output saved to", output_txt)
