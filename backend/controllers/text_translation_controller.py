from fastapi import HTTPException
from models.requests import TextTranslationRequest
from models.response import TranslationResponse
from services.translation_service import TranslationService
from services.file_service import FileService
from services.chunk_service import get_max_word_length, chunk_text

async def translate_text(request: TextTranslationRequest):
    if not request.source_text:
        raise HTTPException(status_code=400, detail="Missing source_text")
    
    # CHUNKING - Please use text_chunks where it is needed it returns a list of strings
    max_word_length = get_max_word_length(request.target_languages)
    text_chunks = chunk_text(request.source_text, max_word_length)

    translator = TranslationService()
    translated_texts = await translator.translate_text(
        request.source_text, # CHUNKING - replace with text_chunks, make sure list of strings works with it
        request.source_language,
        request.target_languages,
    )

    file_service = FileService("pdf")
    
    # Create translated files (1 per language)
    translated_files = file_service.generate_translated_files(
       translated_texts=translated_texts
    )

    return TranslationResponse(
        source_lang= request.source_language,
        translated_texts= translated_texts,
        translated_files= translated_files
        )
    
    
