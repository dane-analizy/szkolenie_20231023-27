from sqlalchemy import engine, text

def __create_connection_string(config):
    return f"postgresql+psycopg2://{config['db_user']}:{config['db_pass']}@{config['db_host']}:{config['db_port']}/{config['db_name']}"


def create_db_connection(conn_str):
    db_engine = engine.create_engine(conn_str)
    db_connection = db_engine.connect()
    return db_connection


def execute_sql(db_connection, sql_query):
    return list(db_connection.execute(text(sql_query)))


def get_sql_results(config, sql_query):
    conn_str = __create_connection_string(config)
    db_conn = create_db_connection(conn_str)
    results = execute_sql(db_conn, sql_query)
    db_conn.close()
    return results
