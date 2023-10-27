from tools.config import load_config
from tools.db_op import get_sql_results
from tools.file_op import save_to_file

LISTA_MAREK = ['skoda', 'ford']


def main():
    config = load_config()
    for marka in LISTA_MAREK:
        results = get_sql_results(config,
                                  f"SELECT * FROM cars WHERE lower(marka) = '{marka}';")
        save_to_file(results, f"auta_{marka}.csv")


if __name__ == "__main__":
    main()


# select imie, nazwisko, numer_konta from klienci

"""
for klient in results:
    f"select * from rachunki where numer_konta = '{klient['numer_konta']}"

    select * from rachunki where numer_konta in (select numer_konta from klienci)
"""
