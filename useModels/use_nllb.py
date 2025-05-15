import torch
from loadModels.load_nllb import load_nllb
LANGUAGE_MAP = {
    "en": "eng_Latn",  # English
    "es": "spa_Latn",  # Spanish
    "fr": "fra_Latn",  # French
    "de": "deu_Latn",  # German
    "it": "ita_Latn",  # Italian
    "pt": "por_Latn",  # Portuguese
    "ru": "rus_Cyrl",  # Russian
    "zh": "zho_Hans",  # Chinese (Simplified)
    "ja": "jpn_Jpan",  # Japanese
    "ko": "kor_Hang",  # Korean
    "ar": "arb_Arab",  # Arabic
    "hi": "hin_Deva",  # Hindi
    "bn": "ben_Beng",  # Bengali
    "tr": "tur_Latn",  # Turkish
    "pl": "pol_Latn",  # Polish
    "sv": "swe_Latn",  # Swedish
    "nl": "nld_Latn",  # Dutch
    "no": "nno_Latn",  # Norwegian
    "fi": "fin_Latn",  # Finnish
    "da": "dan_Latn",  # Danish
    "cs": "ces_Latn",  # Czech
    "sk": "slk_Latn",  # Slovak
    "ro": "ron_Latn",  # Romanian
    "hu": "hun_Latn",  # Hungarian
    "he": "heb_Hebr",  # Hebrew
    "ur": "urd_Arab",  # Urdu
    "vi": "vie_Latn",  # Vietnamese
    "th": "tha_Thai",  # Thai
    "id": "ind_Latn",  # Indonesian
    "ms": "msa_Latn",  # Malay
    "tl": "tgl_Latn",  # Tagalog
    "sw": "swh_Latn",  # Swahili
    "fa": "pes_Arab",  # Persian
    "km": "khm_Khmr",  # Khmer
    "my": "mya_Mymr",  # Burmese
    "sr": "srp_Cyrl",  # Serbian
}


def nllb_translate(text, model, tokenizer, source_language, target_language, config=None, debug=True):
    config = config or {"BEAM_SIZE": 5, "LENGTH_PENALTY": 1.2, "MAX_LENGTH": 1000000000}
    
    source_language = LANGUAGE_MAP.get(source_language, None)
    target_language = LANGUAGE_MAP.get(target_language, None)

    try:
        if debug:
            print(f"Using source_language: {source_language}, target_language: {target_language}")

        # Set tokenizer source language
        tokenizer.src_lang = source_language

        # Convert target language to token ID
        try:
            forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_language)
        except Exception as e:
            if debug:
                print(f"Error converting target_language to token ID: {e}")
            forced_bos_token_id = None

        # Prepare input for translation
        prompt = f"{text}"
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=False).to(model.device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                num_beams=config["BEAM_SIZE"],
                length_penalty=config["LENGTH_PENALTY"],
                early_stopping=False,
                forced_bos_token_id=forced_bos_token_id,
                max_length=config["MAX_LENGTH"]
            )

        decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)
        return decoded_output[0] if decoded_output else None

    except Exception as e:
        if debug:
            print(f"Error during inference: {e}")
        return None

def translate(text, target_language, source_language="en", config=None, debug=True):
    # Load model and tokenizer using the load_nllb function
    model, tokenizer, _ = load_nllb()
    
    return nllb_translate(text, model, tokenizer, source_language, target_language, config, debug)
 