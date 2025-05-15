from typing import List 
from scripts.model_router import route_to_model
from models.translation import TranslatedText

class TranslationService:
    async def translate_text(
        self, 
        source_text: str, 
        source_lang: str, 
        target_langs: List[str] 
    ) -> List[TranslatedText]:  #
        try:
            results = route_to_model(source_text, source_lang, target_langs)
            return [TranslatedText(**t) for t in results]
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}")
