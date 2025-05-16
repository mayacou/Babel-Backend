import asyncio
from backend.services.translation_service import TranslationService

async def main():
    service = TranslationService()
    source_text = "Hello, how are you?"
    source_lang = "en"
    target_langs = ["fr"]  # Add more if you want

    results = await service.translate_text(source_text, source_lang, target_langs)

    for result in results:
        print(f"{result.target_lang}: {result.translated_text}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(main())


