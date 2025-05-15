import torch

# List of valid language codes
LANGUAGE_MAP = {
    "ar": "ar_AR", "cs": "cs_CZ", "de": "de_DE", "en": "en_XX", "es": "es_XX", "et": "et_EE", 
    "fi": "fi_FI", "fr": "fr_XX", "gu": "gu_IN", "hi": "hi_IN", "it": "it_IT", "ja": "ja_XX", 
    "kk": "kk_KZ", "ko": "ko_KR", "lt": "lt_LT", "lv": "lv_LV", "my": "my_MM", "ne": "ne_NP", 
    "nl": "nl_XX", "ro": "ro_RO", "ru": "ru_RU", "si": "si_LK", "tr": "tr_TR", "vi": "vi_VN", 
    "zh": "zh_CN", "af": "af_ZA", "az": "az_AZ", "bn": "bn_IN", "fa": "fa_IR", "he": "he_IL", 
    "hr": "hr_HR", "id": "id_ID", "ka": "ka_GE", "km": "km_KH", "mk": "mk_MK", "ml": "ml_IN", 
    "mn": "mn_MN", "mr": "mr_IN", "pl": "pl_PL", "ps": "ps_AF", "pt": "pt_XX", "sv": "sv_SE", 
    "sw": "sw_KE", "ta": "ta_IN", "te": "te_IN", "th": "th_TH", "tl": "tl_XX", "uk": "uk_UA", 
    "ur": "ur_PK", "xh": "xh_ZA", "gl": "gl_ES", "sl": "sl_SI"
}

def fix_lang_code(lang):
    lang_prefix = lang[:2]  # Extract the first two letters
    if lang in LANGUAGE_MAP.values():
        return lang  # Already correct
    if lang_prefix in LANGUAGE_MAP:
        return LANGUAGE_MAP[lang_prefix]  # Fix it
    raise ValueError(f"Unsupported language code: {lang}")

def mbart_translate(text, model, tokenizer, source_language, target_language, config=None, debug=True):
    config = config or {"BEAM_SIZE": 5, "LENGTH_PENALTY": 1.2, "MAX_LENGTH": 999}  

    try:
        # Fix language codes
        source_language = fix_lang_code(source_language)
        target_language = fix_lang_code(target_language)
    except ValueError as e:
        if debug:
            print(f"Language Error: {e}")
        return None

    if debug:
        print(f"Using source_language: {source_language}, target_language: {target_language}")

    # Set tokenizer source language
    try:
        tokenizer.source_language = source_language
    except Exception as e:
        if debug:
            print(f"Error setting source_language -> {source_language}: {e}")
        
    # Convert target language to token ID
    try:
        forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_language)
    except Exception as e:
        if debug:
            print(f"Error converting target_language to token ID: {e}")
        forced_bos_token_id = None

    try:
        prompt = f"{text}"
        inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=False).to(model.device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                num_beams=config["BEAM_SIZE"],
                length_penalty=config["LENGTH_PENALTY"],
                early_stopping=False,
                forced_bos_token_id=forced_bos_token_id,
                max_length=config["MAX_LENGTH"]  # Max length is now infinity
            )

        decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)
        return decoded_output[0] if decoded_output else None

    except Exception as e:
        if debug:
            print(f"Error during inference: {e}")
        return None
    
from loadModels.load_mbart import load_mbart

def translate(text, target_language, source_language="en", config=None, debug=True):
    # Load the model and tokenizer using the load_mbart function
    model, tokenizer, _ = load_mbart()

    # Call mbart_translate to perform the translation
    return mbart_translate(text, model, tokenizer, source_language, target_language, config, debug)

