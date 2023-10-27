# pip install Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return """
    <html>
    <head>
        <title>Moja strona</title>
    </head>
    <body>
        <h1>Witam na mojej stronie!</h1>
        <table border="1">
        <tr>
            <td>wiersz 1, kolumna 1</td>
            <td>wiersz 1, kolumna 2</td>
        </tr>
        <tr>
            <td>wiersz 2, kolumna 1</td>
            <td>wiersz 2, kolumna 2</td>
        </tr>
        </table>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)


#### ZADANIE 54
# Przygotuj w aplikacji Flask 3 podstrony