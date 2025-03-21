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


import requests
import translate_joke

class JokeFetcher:
    def __init__(self):
        self._translator = None

    @property
    def translator(self):
        if self._translator is None:
            self._translator = translate_joke.TranslateJoke()
        return self._translator

    def fetch_joke(self):
        url = 'https://v2.jokeapi.dev/joke/Any'
        try:
            response = requests.get(
                url = url,
                headers = {'Accept': 'application/json'},
                params = {'type': 'single'}
            )

            if response.status_code == 200:
                data = response.json()
                data['joke'] = self.translator.translate(data['joke'])
                print(data['joke'])

            else:
                print(f"Error: {response.status_code}, {response.text}")

        except requests.exceptions.RequestException as e:
            print(e)

JokeFetcher().fetch_joke()
