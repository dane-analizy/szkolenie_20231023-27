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
from tools.config import config
from sqlalchemy import engine, text
#
# # connection string
conn_str = "sqlite:///baza_plikowa.sqlite"
db_engine = engine.create_engine(conn_str)
db_connection = db_engine.connect()
print(db_engine, db_connection)

db_connection.close()
print(db_engine, db_connection)