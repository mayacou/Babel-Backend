from fastapi import HTTPException
from models.requests import FileTranslationRequest
from models.response import TranslationResponse
from services.translation_service import TranslationService
from services.file_service import FileService
from services.chunk_service import get_max_word_length, chunk_text

async def translate_file(request: FileTranslationRequest):
    try:
        source_type = request.source_type.lower()
        file_service = FileService(source_type)

        text_to_translate, text_map = await file_service.extract_text(request.file)

        # CHUNKING - Please use text_chunks where it is needed it returns a list of strings
        max_word_length = get_max_word_length(request.target_languages)
        text_chunks = chunk_text(text_to_translate, max_word_length)

        translator = TranslationService()
        translated_texts = await translator.translate_text(
            text_to_translate, # CHUNKING - replace with text_chunks, make sure list of strings works with it
            request.source_language,
            request.target_languages,
        )

        translated_files = file_service.generate_translated_files(
            translated_texts= translated_texts,
            original_file=request.file,
            text_map=text_map,
        )

        return TranslationResponse(
            source_lang= request.source_language,
            translated_texts= translated_texts,
            translated_files=translated_files
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
