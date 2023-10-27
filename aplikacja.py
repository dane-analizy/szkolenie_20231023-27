# pip install Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Moja Strona główna"


@app.route('/test')
def test_page():
    return "strona testowa"


if __name__ == "__main__":
    app.run(debug=True)


#### ZADANIE 54
# Przygotuj w aplikacji Flask 3 podstrony