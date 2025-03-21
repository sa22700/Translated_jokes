'''
Copyright [2025] [Pirkka Toivakka]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


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