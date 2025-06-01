from typing import List
import aiohttp
import asyncio
import traceback
from models.translation import TranslatedText

API_URL = "https://mayacou-babel-router-api.hf.space/translate"
MAX_RETRIES = 3
TIMEOUT = 60 * 10

class TranslationService:
    async def translate_text(
        self,
        source_text: str,
        source_lang: str,
        target_langs: List[str]
    ) -> List[TranslatedText]:
        async with aiohttp.ClientSession() as session:
            tasks = [
                self._translate_single(session, source_text, source_lang, target_lang)
                for target_lang in target_langs
            ]
            return await asyncio.gather(*tasks)

    async def _translate_single(
        self,
        session: aiohttp.ClientSession,
        source_text: str,
        source_lang: str,
        target_lang: str
    ) -> TranslatedText:
        for attempt in range(MAX_RETRIES):
            try:
                async with session.post(
                    API_URL,
                    json={"text": source_text, "source_lang": source_lang, "target_lang": target_lang},
                    timeout=TIMEOUT
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        if attempt < MAX_RETRIES - 1:
                            await asyncio.sleep(1 * (attempt + 1))  # Exponential backoff
                            continue
                        return TranslatedText(
                            target_lang=target_lang,
                            translated_text=f"[ERROR] HTTP {response.status}: {error_text}"
                        )
                    
                    data = await response.json()
                    if "translation" not in data:
                        return TranslatedText(
                            target_lang=target_lang,
                            translated_text=f"[ERROR] Unexpected response format: {data}"
                        )
                    
                    return TranslatedText(
                        target_lang=target_lang,
                        translated_text=data["translation"]
                    )
            except asyncio.TimeoutError:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(1 * (attempt + 1))  # Exponential backoff
                    continue
                return TranslatedText(
                    target_lang=target_lang,
                    translated_text=f"[ERROR] Request timed out after {TIMEOUT} seconds (attempt {attempt + 1}/{MAX_RETRIES})"
                )
            except aiohttp.ClientError as e:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(1 * (attempt + 1))  # Exponential backoff
                    continue
                error_details = f"Network error: {str(e)}\n{traceback.format_exc()}"
                return TranslatedText(
                    target_lang=target_lang,
                    translated_text=f"[ERROR] {error_details}"
                )
            except Exception as e:
                error_details = f"Unexpected error: {str(e)}\n{traceback.format_exc()}"
                return TranslatedText(
                    target_lang=target_lang,
                    translated_text=f"[ERROR] {error_details}"
                )
