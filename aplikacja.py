# pip install Flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('templates/home_page.html')

if __name__ == "__main__":
    app.run(debug=True)


#### ZADANIE 54
# Przygotuj w aplikacji Flask 3 podstrony