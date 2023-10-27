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

# from tools.config import load_config
# from tools.db_op import get_sql_results
# from tools.file_op import save_to_file
#
# config = load_config()
# results = get_sql_results(config, "SELECT * FROM players;")
# print(results)
# save_to_file(results, "players.csv")



## DODAWANIE REKORDÓW DO BAZY DANYCH
# klasa Samochód
# wczytamy do niej dane z csv
# auta zapiszemy do bazy danych
# wyświetlimy dane z bazy

# from tools.file_op import get_file_content
# from tools.db_op import create_db_connection
# from tools.config import load_config
# from sqlalchemy import  text
#
# class Car:
#     model = None
#     marka = None
#     rocznik = None
#     nr_rej = None
#
#     def __init__(self, marka, model, rocznik, nr_rej):
#         self.model = model
#         self.marka = marka
#         self.rocznik = rocznik
#         self.nr_rej = nr_rej
#
#     def __repr__(self):
#         return f"{self.model=} {self.marka=} {self.rocznik=} {self.nr_rej=}"
#
#     @property
#     def gmodel(self):
#         return self.model
#
#     @property
#     def gmarka(self):
#         return self.marka
#
#     @property
#     def grocznik(self):
#         return self.rocznik
#
#     def set_rocznik(self, r):
#         self.rocznik = r
#
#     @property
#     def numer_rejestracyjny(self):
#         return self.nr_rej
#
#
# cars = get_file_content('auta.csv')
#
# #flota = [ Car(model=car[0], marka=car[1], rocznik=(car[2]), nr_rej=car[3])  for car in cars ]
# flota = [ Car(*car)  for car in cars ]
#
# config = load_config()
# conn_str = f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"
# db_conn = create_db_connection(conn_str)
#
# for car in flota:
#     sql_query = f"""
#           INSERT INTO cars (marka,model,rocznik,nr_rej)
#           VALUES('{car.gmarka}', '{car.gmodel}', '{car.grocznik}', '{car.numer_rejestracyjny}');
#           """
#     db_conn.execute(text(sql_query))
#     db_conn.commit()
#
# db_conn.close()



#### ZADANIE 53
# Z bazy postgres i tabeli cars wypisz same Skody.

SELECT * FROM cars WHERE makra='Skoda'