import torch


def small_100_translate(text, model, tokenizer, source_language, target_language, config=None, debug=True):
    config = config or {"BEAM_SIZE": 5, "LENGTH_PENALTY": 1.2, "MAX_LENGTH": 999}  

    if debug:
        print(f"Using source_language: {source_language}, target_language: {target_language}")
    
    try:
        tokenizer.src_lang = source_language 
    except Exception as e:
        if debug:
            print(f"Error setting source_language -> {source_language}: {e}")

    try:
        tokenizer.tgt_lang = target_language  
    except Exception as e:
        if debug:
            print(f"Error setting target_language -> {target_language}: {e}")
        return None


    try:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=False).to(model.device)

        with torch.no_grad():
            output = model.generate(
                **inputs,
                num_beams=config["BEAM_SIZE"],
                length_penalty=config["LENGTH_PENALTY"],
                early_stopping=False,
                max_length=config["MAX_LENGTH"]
            )

        decoded_output = tokenizer.batch_decode(output, skip_special_tokens=True)
        return decoded_output[0] if decoded_output else None

    except Exception as e:
        if debug:
            print(f"Error during inference: {e}")
        return None


from loadModels.load_small_100 import load_small_100

def translate(text, target_language, source_language="en", config=None, debug=True):
    # Load the model and tokenizer using the load_small_100 function
    model, tokenizer, _ = load_small_100()

    # Call small_100_translate to perform the translation
    return small_100_translate(text, model, tokenizer, source_language, target_language, config, debug)


