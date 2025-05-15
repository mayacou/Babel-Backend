from typing import List, Optional
from pydantic import BaseModel

class TextTranslationRequest(BaseModel):
    source_text: str 
    source_language: str
    target_languages: List[str]

class FileTranslationRequest(BaseModel):
    file: str  # base64-encoded
    source_type: str  # 'pdf' or 'docx'
    source_language: str
    target_languages: List[str]
