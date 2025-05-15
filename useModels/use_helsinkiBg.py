from loadModels.load_helsinkiBg import load_helsinkiBg

def translate(text: str, source_lang: str, target_lang: str) -> str:
    model, tokenizer, device = load_helsinkiBg()

    tokenizer.src_lang = source_lang
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)
    forced_bos_token_id = tokenizer.convert_tokens_to_ids(target_lang)

    outputs = model.generate(
        **inputs,
        num_beams=5,
        length_penalty=1.2,
        early_stopping=False,
        forced_bos_token_id=forced_bos_token_id
    )
    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
