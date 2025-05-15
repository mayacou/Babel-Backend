# TODO potential change way we get root directory by changing PYTHONPATH

import sys
import os

# Get the parent directory of the current file
# If you're in the `scripts` directory, this will correctly point to the project root
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the root directory to sys.path
sys.path.append(root_dir)

print("SYS PATH: " , sys.path)

def translate_for_single_language(text, source_lang, target_lang):
    if target_lang in ["fr", "de"]:
        from useModels.use_example import translate
        return {"target_lang": target_lang, "translated_text": translate(text, "eng_Latn", source_lang, f"{target_lang}_Latn")}
    elif target_lang in ["tr"]:
        from useModels.use_example import translate
        return {"target_lang": target_lang, "translated_text": translate(text = text,  source_lang=source_lang, target_lang=target_lang)}
    elif target_lang in ["hu"]:
        from useModels.use_helsinki_hu import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    elif target_lang in ["lt"]:
        from useModels.use_helsinki_lt import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    elif target_lang in ["sk"]:
        from useModels.use_helsinki_sk import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    elif target_lang in ["es", "is", "it", "mk", "pl", "tr"]:
        from useModels.use_nllb import translate
        return {"target_lang": target_lang, "translated_text": translate(text, target_lang, source_lang)}
    elif target_lang in ["sl", "sq"]:
        from useModels.use_small_100 import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    elif target_lang in ["hr", "lv", "nl", "no", "pt", "ro"]:
        from useModels.use_mbart import translate
        return {"target_lang": target_lang, "translated_text": translate(text)}
    else:
        return {"target_lang": target_lang, "translated_text": "No model available for this language"}

def route_to_model(text, source_lang, target_langs):
    translated_texts = []
    for target_lang in target_langs:
        translated_texts.append(translate_for_single_language(text, source_lang, target_lang))
    
    return translated_texts

