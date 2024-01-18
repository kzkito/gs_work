import deepl

def translator_deepl(text, lang, key):
    translator = deepl.Translator(key)
    result = translator.translate_text(text, target_lang=lang)
    capitalized_result = result.text[0].upper() + result.text[1:]
    return capitalized_result

# 使用例
# auth_key = "your_deepl_auth_key"  # DeepL APIキー
# translated_text = translate_text_with_deepl("こんにちは世界！", "EN", auth_key)
# print(translated_text)  # 英語へ翻訳されたテキストを出力


            
# import deepl

# auth_key = "f63c02c5-f056-..."  # Replace with your key
# translator = deepl.Translator(auth_key)

# result = translator.translate_text("Hello, world!", target_lang="FR")
# print(result.text)  # "Bonjour, le monde !"