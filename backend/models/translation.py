from pydantic import BaseModel

class TranslatedText(BaseModel):
    target_lang: str
    translated_text: str

class TranslatedFile(BaseModel):
    target_lang: str
    file_type: str
    filename: str
    base64_content: str
