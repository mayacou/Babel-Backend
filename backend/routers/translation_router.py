from fastapi import APIRouter, HTTPException
from typing import List
from models.translation import TranslationRequest, TranslationResponse
from services.translation_service import TranslationService

translation_router = APIRouter()
translation_service = TranslationService()

@translation_router.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    try:
        translations = await translation_service.translate_text(
            source_text=request.source_text,
            source_lang=request.source_lang,
            target_langs=request.target_langs
        )
        return TranslationResponse(translations=translations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 