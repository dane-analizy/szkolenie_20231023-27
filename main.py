# from file_op import get_file_content, save_to_file
# from obliczenia import bmi
#
# print(bmi(80, 185))
#
# import time
#
# from sklearn import metrics
# metrics.pair_confusion_matrix()
#
# from sklearn.metrics import pair_confusion_matrix
# from sklearn.metrics import pairwise
# from sklearn.metrics import precision_recall_curve
#
# pair_confusion_matrix()
#
# from sklearn.metrics.pair_confusion_matrix()
#
# from bs4 import *
#
#
# import pandas as pd
# import numpy as np


# from file_op import *
# get_file_content()
# save_to_file()

# import file_op
# file_op.get_file_content()
# save_to_file()

# import pandas as pd
# pd.read_excel()

# from pandas import *
# import pandas as pd
#
# def read_excel():
#     print("mój czytacz excela")
#
# pd.read_excel()



# from tools.file_op import get_file_content
#
# get_file_content()

# from tools import file_op
# file_op.save_to_file()

# import tools
# print(tools.version)
#
# from tools import file_op
# file_op.save_to_file()


#### ZADANIE 41
# Zbuduj pakiet "matematyka" z dwoma modułami: mnozenie i dodawanie. W mnozeniu niech będzie funkcja pomnoz(a, b),
# a w dodawaniu funkcja dodaj(a, b).
# Napisz też kod, który importuje te funkcje i ich używa.

# powstał folder "matematyka" razem ze wszystkimi plikami w nim zawartymi
# import matematyka.mnozenie as mn
# import matematyka.dodawanie as dod
# print(mn.pomnoz(5,4))
# print(dod.dodaj(5,4))


#### ZADANIE 42
# Wypisz na konsoli wynik dzielenia 1 przez kolejne liczby z zakresu -10 do +10.

# for i in range(-10, 10):
#     print(f"{i}, {1/i}")

#### ZADANIE 43
# Wypisz na konsoli wynik dzielenia 1 przez kolejne liczby z zakresu -10 do +10.
# Zrób tak, żeby program nie zatrzymywał się prz zerze.

# for i in range(-10, 10):
#     if i == 0:
#         continue
#     print(f"{i}, {1/i}")

# liczba = input("Podaj liczbę: ")
# liczba = float(liczba)
# print(liczba**2)

# złapanie błędu
# print("początek programu")
# liczba = 0
# try:
#     wynik = 1 / liczba
#     print(wynik)
# except:
#     print("Wystąpił błąd")
# print("koniec programu")


#### ZADANIE 44
# Wypisz na konsoli wynik dzielenia 1 przez kolejne liczby z zakresu -10 do +10.
# Zrób tak, żeby program nie zatrzymywał się przy zerze wykorzystując konstrukcję try-except

# rozwiązanie
# for i in range(-10, 10):
#     try:
#         print(f"{i}, {1/i}")
#     except:
#         print("Pamiętaj nie dziel przez zero!")
#

# dzielenie w funkcji obsługującej błąd
# def podziel(a, b):
#     """Funkcja dzieli liczbę a przez b i zwraca wynik. Jeśli napotka błąd - wyświetla komunikat i zwraca None"""
#     try:
#         wynik = a/b
#     except:
#         print("Pamiętaj nie dziel przez zero!")
#         wynik = None
#     return wynik
#
#
# for i in range(-10, 10):
#     w = podziel(1, i)
#     if w:
#         print(w)

# lista = [-2, -1, 0, 1, 'ala ma kota', 3, 5, (12, 13)]
# for el in lista:
#     try:
#         print(f"{el}, {1/el}")
#     except ZeroDivisionError:
#         print(f"{el} - Pamiętaj nie dziel przez zero!")
#     except TypeError:
#         print(f"{el} - Nie umiem dzielić przez to coś!")
#     except Exception as e:
#         print(f"{el} - inny błąd", type(e), e)



#### ZADANIE 45
# Wypisz na konsoli wynik dzielenia 1 przez podaną przez użytkownika liczbę.
# Zrób tak, żeby program nie zatrzymywał się jeśli użytkownik wpisze coś błędnego.
# Przygotuj funkcję dzielącą, przygotuj funkcję rzutującą ciąg prowadzony przez użytkownika na float.
# W przypadku błędów - wypisz odpowiednie komunikaty.

# def str_to_float(s):
#     wynik = None
#     try:
#         wynik = float(s)
#     except Exception as e:
#         print(f"To nie jest liczba (błąd: {e})")
#     return wynik
#
# def podziel(liczba):
#     wynik = None
#     try:
#         wynik = 1/liczba
#     except Exception as e:
#         print(f"Nie mogę tego podzielić (błąd: {e})")
#     return wynik
#
#
# liczba = input("Podaj liczbę: ")
# liczba = str_to_float(liczba)
# wynik = podziel(liczba)
# if wynik:
#     print(wynik)


# l = 1
# try:
#     w = 1/l
#     print("policzone dzielenie")
#     ww = 1/0
#     print("policzone dzielenie przez zero")
# except Exception as e:
#     # xxx = 10/0
#     print('='*70)
#     print("Typ błędu:")
#     print(type(e))
#     print('='*70)
#     print("Komunikat błędu:")
#     print(str(e))
#     print('=' * 70)
#     print("Traceback błędu:")
#     print(e.with_traceback(None))
#     print('=' * 70)


#### ZADANIE 46
# Korzystając z przygotowany wcześniej funkcji i modułów wczytaj dane z pliku dane_zepsute.csv.
# Dla każdej z osób policz wartość BMI.
# Wyniki zapisz do nowego pliku.
# Jeśli przy liczeniu BMI napotkasz błąd - zapisz to też w pliku wyjściowym (typ błędu)

# try:
#     w = 1/0
# except Exception as e:
#     print(e.__class__.__name__)


# from tools.obliczenia import str_to_float, bmi
# from tools.file_op import get_file_content, save_to_file
#
# file_content_input = get_file_content('dane_zepsute.csv')
# file_content_output = []
#
# for line in file_content_input:
#     first_name, last_name = line[0], line[1]
#     weight, error_w = str_to_float(line[2])
#     height, error_h = str_to_float(line[3])
#     if weight and height:
#         bmi_value = bmi(weight, height)
#         # error_w, error_h = "", ""
#     else:
#         bmi_value = 'blad'
#
#     file_content_output.append(
#         (
#             first_name, last_name,
#             weight, height,
#             bmi_value,
#             error_w, error_h
#         )
#     )
#
# save_to_file(file_content_output, 'dane_zepsute_wyjscie.csv')



# pobieranie danych z internetu

# instalujemy pakiet requests
# pip install requests

# import requests
# import json
#
# url = "https://jsystems.pl/static/blog/python/dane.json"
# # url = 'https://devszczepaniak.pl/wprowadzenie-do-rest-api/'
#
# result = requests.get(url)
# # odpowiedź z serwera
# print(result)
#
# # status odpowiedzi
# # print(f"result.status_code={result.status_code}")
# print(f"{result.status_code=}")
# print('=' * 80)
#
# # zawartość odpowiedzi - zserializowane do tekstu
# # print(f"{result.text=}")
# print('=' * 80)
#
# # zawartość odpowiedzi - oryginał
# # print(f"{result.content=}")
#
# res_json = result.json()
# print(type(res_json))
# for k,v in res_json.items():
#     print(k,v)



# import requests
# url = "https://gfwghowguhwog.wgwgwg"
# try:
#     result = requests.get(url)
# except Exception as e:
#     pass
#
# print(result)
# print(f"{result.status_code=}")


# import requests
# url = "https://jsystems.pl/dupa"
# try:
#     result = requests.get(url)
# except Exception as e:
#     pass
#
# print(result)
# print(f"{result.status_code=}")

# autoryzacja do api
# dokumentacja https://requests.readthedocs.io/en/latest/user/authentication/
# import requests
# url = "https://jsystems.pl/dupa"
# result = requests.get(url, auth=("login", "haslo"))

# pokazać konfigurację w JSONie
# import json
#
# config = {
#     "login": "login_do_bazy",
#     "password": "hasłoDoBazy123!",
#     "db_server": "123.123.123.13",
#     "db_name": "baza_danych",
#     "db_table": "tabela_z_danymi",
#     "db_privileges": ['read', 'create', 'dump']
# }
#
# # zapisanie obiektu do JSONa
# with open("konfiguracja.json", 'w') as f:
#     json.dump(config, f)


# import json
# import yaml # pip install pyyaml
#
# # wczytanie obiektu z pliku JSONa
# with open("konfiguracja.json", 'r') as f:
#     config = json.load(f)
#
# print("wczytany konfig:")
# print(config)
#
# with open("konfiguracja.yaml", 'w') as f:
#     yaml.dump(config, f)


# import yaml # pip install pyyaml
#
# # wczytanie obiektu z pliku YAML
# with open("konfiguracja.yaml", 'r', encoding='utf-8') as f:
#     config = yaml.safe_load(f)
#
# print("wczytany konfig:")
# print(config)


### ZADANIE 47
# Pobierz dane z API z adresu https://jsystems.pl/static/blog/python/dane.json i zapisz je jako plik 'dane.yaml' na dysku.

# import yaml
# import requests
#
# url = "https://jsystems.pl/static/blog/python/dane.json"
# plik = 'dane.yaml'
# result = requests.get(url)
# res_json = result.json()
#
# with open(plik, 'w') as f:
#     yaml.dump(res_json, f)


# from tools.internet import  get_json_from_url
#
# print(get_json_from_url('https://jsystems.pl/static/blog/python/dane.json'))


#### ZADANIE 48
# Korzystają z API NBP (endpoint https://api.nbp.pl/api/exchangerates/tables/a/?format=json) pobierz tablicę
# z aktualnymi notowaniami walut i zapisz je do pliku waluty.csv, w formacie:
# symbol waluty ; nazwa waluty ; kurs


# from tools.internet import get_json_from_url
# from tools.file_op import save_to_file, save_to_file_from_dict
#
# dane = get_json_from_url("https://api.nbp.pl/api/exchangerates/tables/a/?format=json")[0]
#
# # lista krotek
# notowanie = []
# for waluta in dane.get('rates'):
#     notowanie.append( (waluta.get('code'), waluta.get('currency'), waluta.get('mid')) )
#
# # lista krotek - list comprehention style
# # notowanie = [(waluta.get('code'), waluta.get('currency'), waluta.get('mid')) for waluta in dane.get('rates')]
# save_to_file(notowanie, 'notowanie_walut_krotki.csv', sep=';')
#
# # lista słowników
# notowanie_w = [ waluta for waluta in dane.get('rates')]
# save_to_file_from_dict(notowanie_w, 'notowanie_walut_słownik.csv', sep=';')


##### ZADANIE 49
# Korzystają z API NBP (endpoint https://api.nbp.pl/api/exchangerates/rates/a/usd/2023-01-01/2023-10-26/?format=json)
# pobierz tablicę z historycznymi notowaniami USD i wypisz dni, w których dolar kosztował mniej niż 4 zł.


# from tools.internet import get_json_from_url
#
# url = "https://api.nbp.pl/api/exchangerates/rates/a/usd/2023-01-01/2023-10-26/?format=json"
# dane = get_json_from_url(url)
#
# wyniki = [(d.get('effectiveDate'), d.get('mid'))
#           for d in dane['rates']
#           if d.get('mid') < 4]
#

# wyniki = [(d.get('effectiveDate'), d.get('mid')) for d in dane['rates'] if d.get('mid') < 4]

# wyniki = []
# for d in dane['rates']:
#     if d.get('mid') < 4:
#         wyniki.append(
#             ( d.get('effectiveDate'), d.get('mid') )
#         )

# print(wyniki)



# nowalista = []
#
# for x in ...:
#     if x > 10:
#         nowalista.append( funk(x) )
#
# []
# [1]
# [1, 2]
# [1, 2, 3]
#
# nowalista = [ funk(x) for x in ... if x > 10 ]
#
# { funk(x):funkb(x) for x in ... if x < 10 }



# wczytanie danych z pliku excela
# potrzebny dodatkowy pakiet
# pip install openpyxl
# import pandas as pd
#
# # wczytanie danych z excela - plik waluty.xlsx, arkusz waluty
# dane = pd.read_excel('waluty.xlsx', sheet_name='waluty')
# # print(dane)
# # print(dane['mid'].sum())
#
# # lista słowników z tabeli:
# dane_dict = dane.to_dict('records')
# # print(dane_dict)
#
# # budujemy listę słowników
# drogie_waluty = []
# for waluta in dane_dict:
#     if waluta['mid'] > 1:
#         drogie_waluty.append(waluta)
#
# # print(drogie_waluty)
#
# # dataframe z listy słowników
# dane_xls = pd.DataFrame(drogie_waluty)
# print(dane_xls)
#
# # zapis do pliku xls
# dane_xls.to_excel("waluty_drogie.xlsx", index=False)

# import pandas as pd
#
# # wczytanie danych z excela - plik waluty.xlsx, arkusz waluty
# dane = pd.read_excel('waluty.xlsx', sheet_name='waluty')
# print(dane)


# programowanie obiektowe - klasy i metody
# person_dict = {
#     'first_name': person_data[0],
#     'last_name': person_data[1],
#     'street': person_data[2],
#     'house_number': person_data[3],
#     'city': person_data[4],
#     'phone': person_data[5],
#     'age': int(person_data[6])
# }
#

# class Person:
#     first_name = "Jan"
#     last_name = "Kowalski"
#     city = "Warszawa"
#     age = 35
#
#     def print_me(self):
#         print(f"Jestem {self.first_name} {self.last_name}. Mieszkam w {self.city} i mam {self.age} lat.")
#
# p1 = Person()
# p1.print_me()
#
# p2 = Person()
# p2.print_me()
#
# print(p1)
# print(p2)



# class Person:
#     first_name = None
#     last_name = None
#     city = None
#     age = None
#
#     def print_me(self):
#         print(f"Jestem {self.first_name} {self.last_name}. Mieszkam w {self.city} i mam {self.age} lat.")
#
# p1 = Person()
# p1.first_name = "Józek"
# p1.last_name = "Nowak"
# p1.print_me()


### ZADANIE 50
# Zdefiniuj klasę Car, która zawiera: model, markę i nr rejestracyjny.
# W ramach klasy Car zdefiniuj metodę print_me().
# Utwórz 2 różne obiekty klasy Car i wykonaj na nich metodę prtint_me()

# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#
#     def print_me(self):
#         print(f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}.")
#
#
# s1 = Samochod()
# s1.model = "Omega"
# s1.marka = "Opel"
# s1.nr_rejestracyjny = "DW8373737"
#
# s2 = Samochod()
# s2.model = "Focus"
# s2.marka = "Ford"
# s2.nr_rejestracyjny = "DW1828333"
#
# s1.print_me()
# s2.print_me()


# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#
#     def __init__(self):
#         print("jestem w konstruktorze")
#
#     def print_me(self):
#         print(f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}.")
#
#
# s1 = Samochod()
# print("obiekt klasy utowrzony")
# s1.print_me()
# s1.model = "Omega"
# s1.marka = "Opel"
# s1.nr_rejestracyjny = "DW8373737"
#
# s1.print_me()



# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#
#     def __init__(self, model, marka, nr_rej):
#         print("jestem w konstruktorze")
#         self.model = model
#         self.marka = marka
#         self.nr_rejestracyjny = nr_rej
#
#     def print_me(self):
#         print(f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}.")
#
#
# s1 = Samochod("Opel", "Omega", "DW8373737")
# print("obiekt klasy utowrzony")
# s1.print_me()




# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#
#     def __init__(self, model, marka, nr_rej):
#         print("jestem w konstruktorze")
#         self.model = model
#         self.marka = marka
#         self.nr_rejestracyjny = nr_rej
#
#     def print_me(self):
#         print(f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}.")
#
#
# s1 = Samochod("Opel", "Omega", "DW8373737")
# s1.print_me()
#
# s1.nr_rejestracyjny = "WA 123456"
# s1.print_me()


# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#     przebieg = 0
#
#     def __init__(self, model, marka, nr_rej):
#         self.model = model
#         self.marka = marka
#         self.nr_rejestracyjny = nr_rej
#
#     def print_me(self):
#         print(f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}. Na liczniku mam {self.przebieg} km.")
#
#     def przejedz(self, odleglosc):
#         self.przebieg += odleglosc
#
#     def get_przebieg(self):
#         return self.przebieg
#
#
# s1 = Samochod("Opel", "Omega", "DW8373737")
# s1.print_me()
#
# s1.przejedz(1000)
# s1.print_me()
#
# print(s1.get_przebieg())


### ZADANIE 51
# Do klasy Samochod dodaj metodę "zmien_wlasciciela" która zmieni numer rejestracyjny.


# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#     przebieg = 0
#
#     def __init__(self, model, marka, nr_rej):
#         self.model = model
#         self.marka = marka
#         self.nr_rejestracyjny = nr_rej
#
#     def print_me(self):
#         print(f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}. Na liczniku mam {self.przebieg} km.")
#
#     def przejedz(self, odleglosc):
#         self.przebieg += odleglosc
#
#     def zmien_wlasciciela(self, nowe_blachy):
#         self.nr_rejestracyjny = nowe_blachy
#
#     def get_przebieg(self):
#         return self.przebieg
#
#
# s1 = Samochod("Opel", "Omega", "DW8373737")
# s1.print_me()
#
# s1.zmien_wlasciciela("WJ 98765")
# s1.print_me()
#


# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#     przebieg = 0
#
#     def __init__(self, model, marka, nr_rej):
#         self.model = model
#         self.marka = marka
#         self.nr_rejestracyjny = nr_rej
#
#     def __repr__(self):
#         return f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}. Na liczniku mam {self.przebieg} km."
#
#     def przejedz(self, odleglosc):
#         self.przebieg += odleglosc
#
#     def zmien_wlasciciela(self, nowe_blachy):
#         self.nr_rejestracyjny = nowe_blachy
#
#     def get_przebieg(self):
#         return self.przebieg
#
#
# s1 = Samochod("Opel", "Omega", "DW8373737")
# print(s1)



# class Samochod:
#     model = None
#     marka = None
#     nr_rejestracyjny = None
#
#     def __init__(self, model, marka, nr_rej):
#         self.model = model
#         self.marka = marka
#         self.nr_rejestracyjny = nr_rej
#
#     def __repr__(self):
#         return f"Samochód marki {self.marka} {self.model} o numerze rej. {self.nr_rejestracyjny}"
#
#
# flota = [
#     Samochod("Opel", "Omega", "DW 83737"),
#     Samochod("Audi", "A6", "WA 12345"),
#     Samochod("Ford", "Focus", "XD 12345")
#     ]
#
# for auto in flota:
#     print(auto)


class Samochod:
    model = None
    marka = None
    __nr_rejestracyjny = None
    __uszkodzony = False

    def __init__(self, model, marka, nr_rej):
        self.model = model
        self.marka = marka
        self.__nr_rejestracyjny = nr_rej

    def __repr__(self):
        return f"Samochód marki {self.marka} {self.model} o numerze rej. {self.__nr_rejestracyjny} ({'uszkodzony' if self.__uszkodzony else 'sprawny'})"

    def __szkoda(self, uszkodzony):
        self.__uszkodzony = uszkodzony

    def zrob_dzwona(self):
        self.__szkoda(True)

    @property
    def czy_uszkodzony(self):
        return self.__uszkodzony


s = Samochod("Opel", "Omega", "DW 83737")
print(s)
s.zrob_dzwona()
print(s)

print(s.czy_uszkodzony)
