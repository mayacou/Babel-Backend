from typing import List
from io import BytesIO
import base64
from fastapi import HTTPException
from models.translation import TranslatedFile, TranslatedText
from services.pdf_service import PDFService
from services.docx_service import DOCXService

class FileService:
    def __init__(self, file_type: str):
        self.source_type = file_type.lower()
        match self.source_type:
            case "pdf":
                self._service = PDFService()
            case "docx":
                self._service = DOCXService()
            case _:
                raise HTTPException(status_code=400, detail=f"Unsupported file type: {file_type}")

    async def extract_text(self, encoded_file: str):
        if self._service is None:
            raise Exception("No extraction method for raw text.")
        return await self._service.extract_text(encoded_file)

    def generate_translated_files(
        self,
        translated_texts: List[TranslatedText],
        original_file: str = None,
        text_map: list[dict] = None
    ) -> List[TranslatedFile]:
        files = []
        ext = self.source_type

        for t in translated_texts:
            lang = t.target_lang

            if self.source_type == "docx":
                byte_content = self._service.write_text_to_memory(
                    translated_text=t.translated_text,
                    docx_file=original_file,
                    text_map=text_map
                )
            else:
                # PDF route
                buffer = self._service.write_text_to_memory(t.translated_text)
                byte_content = buffer.getvalue()

            encoded = base64.b64encode(byte_content).decode("utf-8")

            files.append(TranslatedFile(
                target_lang=lang,
                file_type=ext,
                filename=f"{lang}_translation.{ext}",
                base64_content=encoded
            ))

        return files