import base64
import tempfile
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from documentParsing.parsers.pdf_parser import parse_controller

class PDFService:

    async def extract_text(self, encoded_file: str):
        if not encoded_file:
            raise Exception("No PDF file provided.")
            
        try:
            decoded_bytes = base64.b64decode(encoded_file)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(decoded_bytes)
                input_path = temp_pdf.name
            text = parse_controller(input_path)
            if text is None:
                raise Exception("PDF contains unsupported fonts.")
            return text or "", None
        except Exception as e:
            raise Exception(f"PDF extraction failed: {str(e)}")
    
    def write_text_to_memory(self, text: str) -> BytesIO:
        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4
        x = 50
        y = height - 50
        line_height = 12
        for line in text.splitlines():
            if y < 50:
                c.showPage()
                y = height - 50
            c.drawString(x, y, line)
            y -= line_height
        c.save()
        buffer.seek(0)
        return buffer
