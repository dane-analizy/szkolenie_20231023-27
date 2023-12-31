# https://official-joke-api.appspot.com/random_joke
# {"type":"general","setup":"What do you call a girl between two posts?","punchline":"Annette.","id":210}

### ZADANIE 54
# Pobierz i wyświetl na ekranie dowcip z API https://official-joke-api.appspot.com/random_joke

from tools.internet import get_json_from_url
from tools.config import load_config
from tools.db_op import create_db_connection, create_connection_string
from sqlalchemy import text
import time

JOKES_URL = "https://official-joke-api.appspot.com/random_joke"


def create_table(db_conn):
    sql_query = """
    CREATE TABLE IF NOT EXISTS jokes (
        type varchar,
        setup varchar,
        punchline varchar,
        id int
    );
    """
    db_conn.execute(text(sql_query))
    res = db_conn.commit()
    print(res)


def insert_joke(joke, db_conn):
    # użycie słownika jako sposobu na przekazanie parametrów do zapytania SQL
    sql_query = f"""
    INSERT INTO jokes (type, setup, punchline, id)
    VALUES (:type, :setup, :punchline, :id);
    """
    s = text(sql_query)
    db_conn.execute(s, joke)
    db_conn.commit()

# t = text("SELECT * FROM users WHERE id=:user_id")
# result = connection.execute(t, user_id=12)

def main():
    # ładujemy konfigurację
    config = load_config()

    # tworzymy połączenie do bazy
    conn_str = create_connection_string(config)
    print(conn_str)
    db_conn = create_db_connection(conn_str)

    # jeśli trzeba to tworzymy tabelę
    create_table(db_conn)

    # w pętli co 1 sekundę pobieramy dowcip z API
    for _ in range(100):
        joke = get_json_from_url(JOKES_URL)
        if joke:
            # jeśli się udało - wyświetlamy go
            print(f"- {joke.get('setup')}\n- {joke.get('punchline')}\n\n")
            # i zapisujemy do bazy
            insert_joke(joke, db_conn)

        # czekamy 1 sekundę
        time.sleep(1)

    db_conn.close()


if __name__ == "__main__":
    main()

