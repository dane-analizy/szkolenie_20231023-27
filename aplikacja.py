# pip install Flask

from flask import Flask, render_template
from tools.file_op import get_file_content

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


@app.route('/auto')
def car_page():
    user = {"login": "login_usera",
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "wiek": 40}
    auto = {"model": "Kodiaq",
            "marka": "Skoda",
            "nr_rej": "WA 12345"}
    return render_template('car_page.html', user=user, auto=auto)



@app.route('/list')
def list_page():
    dane = get_file_content("dane.csv")
    dane = [ {"first_name":el[0],
            "last_name":el[1],
            "weight":el[2],
            "height":el[3]}
             for el in dane ]

    return render_template('list_page.html', users=dane)


if __name__ == "__main__":
    app.run(debug=True)


#### ZADANIE 54
# Przygotuj w aplikacji Flask 3 podstrony

#### ZADANIE 55
# Przygotuj dodatkowy template dla aplikacji Flask

#### ZADANIE 56
# Przygotuj template, który wyświetli dane ze słownika opisującego samochód.
