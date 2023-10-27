# https://official-joke-api.appspot.com/random_joke
# {"type":"general","setup":"What do you call a girl between two posts?","punchline":"Annette.","id":210}

### ZADANIE 54
# Pobierz i wyświetl na ekranie dowcip z API https://official-joke-api.appspot.com/random_joke

from tools.internet import get_json_from_url

JOKES_URL = "https://official-joke-api.appspot.com/random_joke"


def main():
    joke = get_json_from_url(JOKES_URL)
    if joke:
        print(f"- {joke.get('setup')}\n- {joke.get('punchline')}")


if __name__ == "__main__":
    main()