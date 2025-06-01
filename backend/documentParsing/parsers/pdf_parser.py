import pdfplumber
from typing import Optional
import re

APPROVED_FONTS = [
    "Helvetica", "Times-Roman", "Courier",
    "Arial", "Times New Roman", "Calibri",
    "Liberation Serif", "DejaVu Sans", "Noto Sans"
]

def detect_cid_issues(pdf_path: str):
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            if re.search(r'\(cid:\d+\)', text):
                print(f"⚠️ CID encoding artifacts found on page {page_num}.")
                return True
    return False

def extract_embedded_text(pdf_path: str) -> str:
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text += text + "\n\n"
    return full_text

def parse_controller(input_path: str) -> Optional[str]:
    if detect_cid_issues(input_path):
        print("❌ Unsupported font encoding detected.")
        print("📣 Please re-export your PDF using one of the approved fonts:")
        for font in APPROVED_FONTS:
            print(f" - {font}")
        return None  # Abort early
    return extract_embedded_text(input_path)
