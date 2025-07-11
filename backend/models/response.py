from typing import List
from pydantic import BaseModel
from models.translation import TranslatedText, TranslatedFile

class TranslationResponse(BaseModel):
    source_lang: str
    translated_texts: List[TranslatedText]
    translated_files: List[TranslatedFile]
