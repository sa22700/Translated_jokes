"""
Copyright [2025] [Pirkka Toivakka]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from translate import Translator

_translator = None

def get_translator():
    global _translator
    if _translator is None:
        _translator = Translator(from_lang="en", to_lang="fi")
    return _translator

def translate(text: str) -> str:
    if not text or not text.strip():
        return ""
    try:
        return get_translator().translate(text)

    except Exception as e:
        return f"Translation error: {e}"