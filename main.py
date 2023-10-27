import yaml

with open("db_config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print(config)

# pakiet do łączenia się z postgresql
# pip install psycopg2

# pakiet do łączenia się z Oraclem
# pip install cx_oracle

# pakiet do łączenia się z MS SQL
# pip install pymssql

# SQLAlchemy - pakiet do łączenia się do dowolnej bazy
# pip install sqlalchemy