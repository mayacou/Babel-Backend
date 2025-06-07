import base64
from services.pdf_service import PDFService 
import asyncio

# Read a test PDF file and encode it in base64
with open("sample_french.pdf", "rb") as f:
   encoded = base64.b64encode(f.read()).decode("utf-8")

service = PDFService()

async def test_extract():
   extracted_text = await service.extract_text(encoded)
   print("Extracted text:", extracted_text)

   pdf_buffer = service.write_text_to_memory(text=extracted_text[0])
   with open("output_test.pdf", "wb") as f:
      f.write(pdf_buffer.read())

asyncio.run(test_extract())
