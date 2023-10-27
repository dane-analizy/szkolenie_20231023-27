from tools.config import load_config
from tools.db_op import get_sql_results


# print("jestem na początku")

def main():
    config = load_config()
    results = get_sql_results(config, "SELECT * FROM cars where lower(marka) = 'skoda';")
    print(results)


if __name__ == "__main__":
    main()