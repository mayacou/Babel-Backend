import base64
import tempfile
from io import BytesIO
from reportlab.lib.pagesizes import A4
from documentParsing.parsers.pdf_parser import parse_controller
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(TTFont('NotoSans', './documentParsing/fonts/NotoSans-Regular.ttf'))

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
        doc = SimpleDocTemplate(buffer, pagesize=A4)
        
        styles = getSampleStyleSheet()
        style = styles['Normal']
        style.fontName = 'NotoSans'
        style.fontSize = 12
        style.leading = 14

        story = []
        for line in text.splitlines():
            story.append(Paragraph(line, style))
            story.append(Spacer(1, 6))

        doc.build(story)
        buffer.seek(0)
        return buffer
