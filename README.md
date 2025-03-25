# Translated_jokes

**Program:** Translated_jokes
**Author:** Pirkka Toivakka
**License:** Apache License 2.0

## What does the program do?

This program fetches a random joke from [JokeAPI](https://jokeapi.dev/) in English and translates it into Finnish.

Translation is done using `translate` library.

The program consists of two parts:

- `make_jokes.py`: Application logic, which fetches and displays a joke.
- `translate_joke.py`: Class responsible for text translation.

## How to run the program?

### 1. **How to install dependencies**
You need `requests` and `translate` libraries. You can install them like this:

**create venv**

python -m venv venv

**activate venv**

venv\Scripts\activate

pip install requests translate

**Or use requirements.txt content**

pip install -r requirements.txt

### 2. **How to run the program**

python make_jokes.py


**Ohjelma:** Translated_jokes
**Tekijä:** Pirkka Toivakka  
**Lisenssi:** Apache License 2.0

## Mitä ohjelma tekee?

Tämä ohjelma hakee satunnaisen vitsin [JokeAPI](https://jokeapi.dev/):sta englanniksi ja kääntää sen suomeksi.  

Käännös tapahtuu `translate`-kirjaston avulla.

Ohjelma koostuu kahdesta osasta:

- `make_jokes.py`: Sovelluksen päälogiikka, joka hakee ja näyttää vitsin.
- `translate_joke.py`: Luokka, joka vastaa tekstin kääntämisestä.

## Miten ohjelmaa ajetaan?

### 1. **Näin asennat riippuvuudet**
Tarvitset `requests`- ja `translate`-kirjastot. Voit asentaa ne näin:

**luot venvin**

python -m venv venv

**aktivoi venv**

venv\Scripts\activate

pip install requests translate

**Tai vaihtoehtoisesti asenna reuquirements.txt sisältö**

pip install -r requirements.txt

**Näin ajat ohjelmaa**

python make_jokes.py
