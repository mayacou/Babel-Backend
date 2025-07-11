import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def get_max_word_length(target_languages: list[str]) -> int:
    helsinki_word_limits = {
        "el": 50,
        "et": 50,
        "fi": 50,
        "fr": 40,
        "sv": 140,
        "hu": 50,
        "lt": 50,
        "sk": 140,
        "bg": 50,
        "cs": 140,
        "da": 140,
        "de": 150,
    }

    max_word_length = 700  # Default for non-Helsinki languages

    for lang in target_languages:
        if lang in helsinki_word_limits:
            if helsinki_word_limits[lang] < max_word_length:
                max_word_length = helsinki_word_limits[lang]

    return max_word_length

def chunk_text(text: str, safe_word_limit: int) -> list[str]:
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    
    chunks = []
    current_chunk = []
    current_word_count = 0

    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue

        word_count = len(sentence.split())

        # If sentence is longer than the safe word limit by itself, split it
        if word_count > safe_word_limit:
            if current_chunk:
                chunks.append(' '.join(current_chunk))
                current_chunk = []
                current_word_count = 0
            words = sentence.split()
            for i in range(0, len(words), safe_word_limit):
                chunks.append(' '.join(words[i:i+safe_word_limit]))
            continue

        # Otherwise, see if it fits in the current chunk
        if current_word_count + word_count <= safe_word_limit:
            current_chunk.append(sentence)
            current_word_count += word_count
        else:
            # Start a new chunk
            chunks.append(' '.join(current_chunk))
            current_chunk = [sentence]
            current_word_count = word_count

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

