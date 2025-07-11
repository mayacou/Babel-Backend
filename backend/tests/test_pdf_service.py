import unittest
from unittest.mock import patch, AsyncMock, MagicMock
from services.pdf_service import PDFService  # adjust import as needed
import base64
from io import BytesIO
import asyncio
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# In order to run this, put documentParsing folder into the backend folder and run from backend:
# python3 -m unittest tests.test_docx_service

class TestPDFService(unittest.TestCase):

    def setUp(self):
        self.service = PDFService()
        
        # Create a simple in-memory PDF file with "Hello, world!"
        pdf_buffer = BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=A4)
        c.drawString(50, 800, "Hello, world!")
        c.save()
        
        pdf_bytes = pdf_buffer.getvalue()
        # Convert the PDF bytes to base64
        self.base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
    
    # Tests extract text from pdf (Note: text is stripped because it returned two extra newlines "\n\n")
    @patch("documentParsing.parsers.pdf_parser.parse_controller")
    def test_extract_text_from_pdf(self, mock_parse_controller):
        """
        Test that extract_text decodes and parses a PDF correctly.
        """
        # Mock parse_controller to return recognized text
        mock_parse_controller.return_value = "Hello, world!"
        
        async def run_test():
            text, err = await self.service.extract_text(self.base64_pdf)
            self.assertEqual(text.strip(), "Hello, world!")
            self.assertIsNone(err)
        
        asyncio.run(run_test())

    @patch("documentParsing.parsers.pdf_parser.parse_controller")
    def test_extract_text_invalid_input(self, mock_parse_controller):
        """
        Test that passing None (or empty) raises an exception.
        """
        async def run_test():
            with self.assertRaises(Exception) as context:
                await self.service.extract_text(None)
            self.assertIn("No PDF file provided", str(context.exception))
        
        asyncio.run(run_test())

    def test_write_text_to_memory(self):
        """
        Test writing text into a PDF in-memory.
        """
        sample_text = "This is PDF text\nAnother line"
        try:
            pdf_io = self.service.write_text_to_memory(sample_text)
            self.assertIsInstance(pdf_io, BytesIO)

            # Just ensure it has PDF data. We can check the signature
            pdf_bytes = pdf_io.getvalue()
            self.assertGreater(len(pdf_bytes), 0)
            # Common PDF signature check
            self.assertTrue(pdf_bytes.startswith(b"%PDF"))
        except Exception as e:
            self.fail(f"write_text_to_memory raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
