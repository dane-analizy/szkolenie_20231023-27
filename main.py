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
# Korzystając z przygotowany wczesniej funkcji i modułów wczytaj dane z pliku dane_zepsute.csv.
# Dla każdej z osób policz wartość BMI.
# Wyniki zapisz do nowego pliku.
# Jeśli przy liczeniu BMI napotkasz błąd - zapisz to też w pliku wyjściowym (typ błędu)

# try:
#     w = 1/0
# except Exception as e:
#     print(e.__class__.__name__)