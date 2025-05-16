from typing import List
import requests
from backend.models.translation import TranslatedText

API_URL = "https://mayacou-babel-router-api.hf.space/translate"

class TranslationService:
    async def translate_text(
        self,
        source_text: str,
        target_langs: List[str]
    ) -> List[TranslatedText]:
        results = []

        for target_lang in target_langs:
            try:
                response = requests.post(
                    API_URL,
                    json={"text": source_text, "target_lang": target_lang},
                    timeout=60
                )
                response.raise_for_status()
                data = response.json()
                translated = data.get("translation", "[No translation returned]")
            except Exception as e:
                translated = f"[ERROR] {str(e)}"

            results.append(TranslatedText(
                target_lang=target_lang,
                translated_text=translated
            ))

        return results
