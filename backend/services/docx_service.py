import base64
import tempfile
from typing import Optional, List
from io import BytesIO
from docx import Document
from typing import Optional
from documentParsing.parsers.docx_parser import parse_docx  # from documentParsing
from documentParsing.overlay.docx_overlay import overlay_docx #from documentParsing

class DOCXService:
    async def extract_text(self, encoded_file: str):
        text, text_map = await self.extract_text_from_docx(encoded_file)
        return text, text_map

    def write_text(self, translated_text: str, docx_file: str, text_map: list[dict]) -> str:
        return self.write_text_to_memory(translated_text, docx_file, text_map)


    async def extract_text_from_docx(self, docx_file: Optional[str]) -> str:
        """
        Extracts text from a base64-encoded DOCX file.
        Stores a `text_map` to use later in overlay.
        """
        if not docx_file:
            raise Exception("No DOCX file provided.") 
        try:            
            # Decode base64 file and write to temp file
            decoded_bytes = base64.b64decode(docx_file)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx:
                temp_docx.write(decoded_bytes)
                temp_docx.flush()
                input_path = temp_docx.name

            doc = Document(input_path)

            text_map = parse_docx(doc, text_map=[])
            extracted_texts = [entry.get("text") or entry.get("ocr_text") for entry in text_map]

            return "\n".join(extracted_texts), text_map

        except Exception as e:
            raise Exception(f"DOCX extraction failed: {str(e)}")
    def write_text_to_memory(self, translated_text: str, docx_file: str, text_map: List[dict]) -> bytes:
        """
        Applies translated text to the saved text_map and returns the modified DOCX as bytes.
        
        Args:
            translated_text: The translated text to insert
            docx_file: Base64 encoded original DOCX file
            text_map: Mapping data for text positions
        
        Returns:
            bytes: The modified DOCX file content
        """
        translated_texts = translated_text.splitlines()

        # Decode base64 file
        decoded_bytes = base64.b64decode(docx_file)
        
        # Use BytesIO for in-memory operations
        with BytesIO(decoded_bytes) as input_stream:
            doc = Document(input_stream)
            updated_doc = overlay_docx(doc, text_map, translated_texts, image_map=[])
            
            # Save to memory instead of disk
            output_stream = BytesIO()
            updated_doc.save(output_stream)
            return output_stream.getvalue()