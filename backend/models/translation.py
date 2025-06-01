from pydantic import BaseModel
from typing import List

class TranslatedText(BaseModel):
    target_lang: str
    translated_text: str

class TranslatedFile(BaseModel):
    target_lang: str
    file_type: str
    filename: str
    base64_content: str

class TranslationRequest(BaseModel):
    source_text: str
    source_lang: str
    target_langs: List[str]

class TranslationResponse(BaseModel):
    translations: List[TranslatedText]
