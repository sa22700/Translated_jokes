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
