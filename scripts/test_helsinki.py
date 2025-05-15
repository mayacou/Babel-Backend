from useModels.use_helsinki_en_fr import translate as translate_fr
from useModels.use_helsinki_en_fi import translate as translate_fi
from useModels.use_helsinki_en_el import translate as translate_el
from useModels.use_helsinki_en_et import translate as translate_et
from useModels.use_helsinki_en_sv import translate as translate_sv

def test_translation(text, target_lang):
   
   if target_lang == "fr":
      translated_text = translate_fr(text)
   elif target_lang == "fi":
      translated_text = translate_fi(text)
   elif target_lang == "el":
      translated_text = translate_el(text)
   elif target_lang == "et":
      translated_text = translate_et(text)
   elif target_lang == "sv":
      translated_text = translate_sv(text)

   if translated_text:
      print(f"Translated text: {translated_text}")
   else:
      print("Translation failed.")

def main():
    text = "Hello, how are you?"  # Change this to the text you want to translate
    test_translation(text, "et")

if __name__ == "__main__":
    main()