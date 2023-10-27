# pip install Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/test')
def test_page():
    user = {"login": "login_usera",
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "wiek": 40}

    return render_template('test_page.html', param=user)



if __name__ == "__main__":
    app.run(debug=True)


#### ZADANIE 54
# Przygotuj w aplikacji Flask 3 podstrony

#### ZADANIE 55
# Przygotuj dodatkowy template dla aplikacji Flask

#### ZADANIE 56
# Przygotuj template, który wyświetli dane ze słownika opisującego samochód.
