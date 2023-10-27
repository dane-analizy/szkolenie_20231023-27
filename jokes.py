from flask import Flask, render_template
from tools.db_op import get_sql_results
from tools.config import load_config

app = Flask(__name__)
config = load_config()


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/test/<napis>')
def test_page(napis):
    return f"Podano napis: {napis}"


@app.route('/dodaj/<a>/<b>')
def dodawanie(a, b):
    return f"Suma {a} + {b} = {float(a)+float(b)}"


@app.route('/jokes_list')
def jokes_list():
    types = [ {"name": t[0].upper(), "url": t[0]}
              for t in get_sql_results(config, "select distinct type from jokes;")
    ]
    return render_template("jokes_types.html", types=types)



if __name__ == "__main__":
    app.run(debug=True)


### ZADANIE 58
# Na bazie powyższego kodu przygtuj routing pokazujący dowcipz danej kategorii.