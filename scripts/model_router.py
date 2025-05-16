# TODO potential change way we get root directory by changing PYTHONPATH
# AS OF RIGHT NOW THIS IS NO LONGER USED!!!!!!!!!! -MAYA 5/16/2025

import sys
import os
from backend.huggingface_api import translate_with_huggingface

# Get the parent directory of the current file
# If you're in the `scripts` directory, this will correctly point to the project root
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the root directory to sys.path
sys.path.append(root_dir)

print("SYS PATH: " , sys.path)

MODEL_MAP = {
    "bg": "Helsinki-NLP/opus-mt-tc-big-en-bg",
    "cs": "Helsinki-NLP/opus-mt-en-cs",
    "da": "Helsinki-NLP/opus-mt-en-da",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "el": "Helsinki-NLP/opus-mt-tc-big-en-el",
    "es": "facebook/nllb-200-distilled-600M",
    "et": "Helsinki-NLP/opus-mt-tc-big-en-et",
    "fi": "Helsinki-NLP/opus-mt-tc-big-en-fi",
    "fr": "Helsinki-NLP/opus-mt-tc-big-en-fr",
    "hr": "facebook/mbart-large-50-many-to-many-mmt",
    "hu": "Helsinki-NLP/opus-mt-tc-big-en-hu",
    "is": "facebook/nllb-200-distilled-600M",
    "it": "facebook/nllb-200-distilled-600M",
    "lt": "Helsinki-NLP/opus-mt-tc-big-en-lt",
    "lv": "facebook/mbart-large-50-many-to-many-mmt",
    "mk": "facebook/nllb-200-distilled-600M",
    "nb": "facebook/mbart-large-50-many-to-many-mmt", #place holder!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    "nl": "facebook/mbart-large-50-many-to-many-mmt",
    "no": "facebook/mbart-large-50-many-to-many-mmt", #place holder!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    "pl": "facebook/nllb-200-distilled-600M",
    "pt": "facebook/mbart-large-50-many-to-many-mmt",
    "ro": "facebook/mbart-large-50-many-to-many-mmt",
    "sk": "Helsinki-NLP/opus-mt-en-sk",
    "sl": "alirezamsh/small100",
    "sq": "alirezamsh/small100",
    "sv": "Helsinki-NLP/opus-mt-en-sv",
    "tr": "facebook/nllb-200-distilled-600M"
    
}

def translate_for_single_language(text, source_lang, target_lang):
    model_id = MODEL_MAP.get(target_lang)
    if model_id:
        translated_text = translate_with_huggingface(text, model_id)
        return {"target_lang": target_lang, "translated_text": translated_text}
    else:
        return {"target_lang": target_lang, "translated_text": "No Hugging Face model available for this language"}


