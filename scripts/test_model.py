import sys
import os

# Get the parent directory of the current file
# If you're in the `scripts` directory, this will correctly point to the project root
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the root directory to sys.path
sys.path.append(root_dir)

# Import loaders here
from loadModels.load_mbart import load_mbart
from loadModels.load_small_100 import load_small_100
from loadModels.load_nllb import load_nllb



def load_model_by_name(model_name):
    match model_name:
        case "mbart":
            return load_mbart()
        case "small":
            return load_small_100()
        case "nllb":
            return load_nllb()
        # Add more cases here as needed
        case _:
            raise ValueError(f"Model {model_name} is not supported.")


# Import translates here
from useModels.use_mbart import mbart_translate
from useModels.use_small_100 import small_100_translate
from useModels.use_nllb import nllb_translate

def translate_with_model(model_name, text, model, tokenizer, source_lang, target_lang, config=None, debug=False):
    match model_name:
        case "mbart":
            return mbart_translate(text, model, tokenizer, source_lang, target_lang, config, debug)
        case "small":
            return small_100_translate(text, model, tokenizer, source_lang, target_lang, config, debug)
        case "nllb":
            return nllb_translate(text, model, tokenizer, source_lang, target_lang, config, debug)
        # Add more cases here as needed

        case _:
            raise ValueError(f"Model {model_name} is not supported.")


def test_translation(model_name, text, source_lang, target_lang):
    model, tokenizer, device = load_model_by_name(model_name)

    translated_text = translate_with_model(model_name, text, model, tokenizer, source_lang, target_lang, debug=True)

    if translated_text:
        print(f"Translated text: {translated_text}")
    else:
        print("Translation failed.")

def main():
    # Set the model name and other variables here
    model_name = "nllb"  # Change this to your desired model
    text = "hello how are you"
 

    source_lang = "en"  # Change this to the source language code
    target_lang = "es"  # Change this to the target language code

    # Call the translation test with provided arguments
    test_translation(model_name, text, source_lang, target_lang)

if __name__ == "__main__":
    main()
