# import yaml
#
# with open("db_config.yaml", "r", encoding="utf-8") as f:
#     config = yaml.safe_load(f)

# pakiet do łączenia się z postgresql
# pip install psycopg2

# pakiet do łączenia się z Oraclem
# pip install cx_oracle

# pakiet do łączenia się z MS SQL
# pip install pymssql

# SQLAlchemy - pakiet do łączenia się do dowolnej bazy
# pip install sqlalchemy


# podłączenie do bazy POSTGRESQL
# from tools.config import config
# from sqlalchemy import engine, text
#
# # connection string
# conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
#
# # text("SELECT * FROM tabelka;")
# db_engine = engine.create_engine(conn_str)
# db_connection = db_engine.connect()
# print(db_engine, db_connection)


# podłączenie do bazy SQLITE
# from tools.config import config
# from sqlalchemy import engine, text
# #
# # # connection string
# conn_str = "sqlite:///baza_plikowa.sqlite"
# db_engine = engine.create_engine(conn_str)
# db_connection = db_engine.connect()
# print(db_engine, db_connection)
#
# db_connection.close()
# print(db_engine, db_connection)


# wczytanie danych z bazy danych
# from tools.config import config
# from sqlalchemy import engine, text
#
# # connection string
# conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
#
# # podłączenie do bazy
# db_engine = engine.create_engine(conn_str)
# db_connection = db_engine.connect()
#
# # zapytanie sql
# sql_query = "SELECT * FROM players;"
# # wywołanie zapytania
# sql_results = db_connection.execute(text(sql_query))
#
# # przejście przez wyniki
# for result in sql_results:
#     print(result[1], result[3]*100)
#
# db_connection.close()
#
# #### ZADANIE 52
# # Przepisz dane z tabeli 'players' w bazie PostgreSQL do pliku csv o nazwie 'players.csv'
#
# sql_results_list = list(sql_results)


# rozwiązanie
# 1. w tools.config - zmiana na funkcję

from tools.config import load_config
from tools.db_op import get_sql_results
from tools.file_op import save_to_file

config = load_config()
results = get_sql_results(config, "SELECT * FROM players;")
print(results)
save_to_file(results, "players.csv")

