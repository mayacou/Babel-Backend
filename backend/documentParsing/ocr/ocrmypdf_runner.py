# import ocrmypdf
# import os

# def run_ocr(input_pdf_path, output_pdf_path=None, language="eng"):
#     """
#     Applies OCR to a scanned PDF and saves the output as a searchable PDF.
    
#     Args:
#         input_pdf_path (str): Path to input (scanned) PDF.
#         output_pdf_path (str): Optional path to save OCR result.
#         language (str): OCR language code (default = English).
        
#     Returns:
#         str: Path to OCR’d output PDF.
#     """
#     if output_pdf_path is None:
#         output_pdf_path = os.path.splitext(input_pdf_path)[0] + "_ocr.pdf"

#     ocrmypdf.ocr(
#         input_pdf_path,
#         output_pdf_path,
#         language=language,
#         skip_text=True,   # Only OCR pages that don't have embedded text
#         force_ocr=False,  # Avoid re-OCRing if text exists
#         output_type="pdf"
#     )

#     return output_pdf_path
