from loadModels.load_helsinki_lt import load_helsinki_lt_model

def translate(text: str) -> str:
    model, tokenizer, device = load_helsinki_lt_model()

    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)

    outputs = model.generate(**inputs, num_beams=5, length_penalty=1.2, early_stopping=False)

    return tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
