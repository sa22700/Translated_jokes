from translate import Translator

class TranslateJoke:
    def __init__(self, source_lang="en", target_lang="fi"):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = Translator(from_lang=self.source_lang, to_lang=self.target_lang)

    def translate(self, text):
        if not text or not text.strip():
            return ""

        try:
            translated_text = self.translator.translate(text)
            return translated_text if translated_text else ""

        except Exception as e:
            return e