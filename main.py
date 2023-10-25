# zapisywanie tekstu do pliku

# context manager - konstrukcja with ...: - jeśli uda się otworzyć plik to wykonają się instrukcje
# w bloku with, a na koniec plik zostanie automatycznie zamknięty
# zmienna = "linia 2"
# with open("dane_oczyszczone.csv", 'w') as f:
#     f.write("linia 1\n")
#     f.write(f"{zmienna}\n")

# bez context managera - otwarcie pliku, operacje, zamknięcie
# f = open(...)
# # kolejne instrukcje
# f.close()


#### ZADANIE 30

# Napisz program, który przeczyta wiersz po wierszu plik "dane_2.csv" i przepisze go do pliku "dane_oczyszczone.csv"
# tak, aby pominąć puste linie.

# rozwiązanie A
# input_file = "dane_2.csv"
# output_file = "dane_oczyszczone.csv"
#
# file_content = [ line for line in open(input_file, 'r', encoding='utf-8')]
#
# with open(output_file, 'w', encoding='utf-8') as f:
#     for line in file_content:
#         if len(line) > 1:
#             f.write(line)

# rozwiązanie B
# input_file = "dane_2.csv"
# output_file = "dane_oczyszczone.csv"
#
# file_content = [ line for line in open(input_file, 'r', encoding='utf-8') if len(line) > 1 ]
#
# with open(output_file, 'w', encoding='utf-8') as f:
#     f.writelines(file_content)
#

#### ZADANIE 31

# Napisz program, który przeczyta wiersz po wierszu plik "dane_2.csv" i przepisze go do pliku "dane_oczyszczone.csv"
# tak, aby pominąć puste linie i usunąć zbędne białe znaki z początków i końców linii.

# rozwiązanie zadania 31
# input_file = "dane_2.csv"
# output_file = "dane_oczyszczone.csv"
# file_content = [line.strip() for line in open(input_file, 'r', encoding='utf-8') if len(line) > 1]
# f = open(output_file, 'w', encoding='utf-8')
# f.writelines([f"{l}\n" for l in file_content])
# f.close()

# inna wersja
# input_file = "dane_2.csv"
# output_file = "dane_oczyszczone.csv"
# file_content = [f"{line.strip()}\n" for line in open(input_file, 'r', encoding='utf-8') if len(line) > 1]
# with open(output_file, 'w', encoding='utf-8') as f:
#     f.writelines(file_content)

# lista = [1, 3, 1, 2, 2, 3]
# print("lista:")
# for el in lista:
#     print(el)
# # zbior = [1, 2, 3]
# print("zbior:")
# zbior = set(lista)
# for el in zbior:
#     print(el)

# zbior_a = { 1, 1, 2, 3, 4}
# print("przed dodaniem")
# for el in zbior_a:
#     print(el)
# zbior_b = {3, 4, 5, 6, 7}
#
# zbior_a.add(5)
# print("po dodaniu")
# for el in zbior_a:
#      print(el)


# zbior_a = { 2, 3, 4, 1, 1, 'aefaf', '5'}
# zbior_b = {3, 4, 5, 6, 7}
#
# print("część wspólna a i b")
# print(zbior_a.intersection(zbior_b))
#
# print("suma a i b")
# print(zbior_a.union(zbior_b))
#
# print("róznica a i b")
# print(zbior_a.difference(zbior_b))
#
# print("róznica b i a")
# print(zbior_b.difference(zbior_a))


# s = ", ".join( {"1", "4", "2", "3"} )
# print(s)


#### ZADANIE 32

# Przygotuj dwa zbiory 20 losowych liczb z zakresu 1-20.
# Wypisz wszystkie liczby z obu zbiorów, korzystając z metody .join()
# Przygotuj część wspólną obu zbiorów i też ją wypisz.

# zbior = { i for i in range(10) }


# import random
# # zbior1 = random.sample(range(1, 21), 20)
# # zbior2 = random.sample(range(1, 21), 20)
#
# zbior1 = { random.randint(1,20) for _ in range(20) }
# zbior2 = { random.randint(1,20) for _ in range(20) }
#
# print("zbior 1: " + ', '.join(map(str, zbior1)))
# print("zbior 2: " + ', '.join(map(str, zbior2)))
#
# czesc_wspolna = list(zbior1.intersection(zbior2))
# czesc_wspolna = list(set(zbior1) & set(zbior2))
#
# print("czesc_wspolna: " + ', '.join(map(str, czesc_wspolna)))

# lista = [ 1, 2, 3]
# def f(x):
#     return x*2
#
# # map(f, lista)
# print(list(map(f, lista)))
#
# wynik = [ f(el) for el in lista ]
#

#### ZADANIE 33

# Przygotuj program który, policzy ile jest potrzebnych losowań aby ze zbioru liczb 1-49 wylosować 6 konkretnych,
# podanych przez użytkownika
# moje_liczby = { 1, 2, 3, 4, 5, 6 }

# import random

# losowe 6 liczb z zakresu 1-48 (48, bo range nie domyka przedziału przy końcu!)
# random.sample(range(1, 49), 6)

# czy dwa zbiory są równe:
# zbiór1 == zbiór2
# zbior_a.intersection(zbior_b)

# break = wyjście z pętli
# for el1, el2 in zip(lista1, lista2):
#     if el1 != el2:
#         break

# import random
# import time
#
# moje_liczby = {1, 2, 3, 4, 5}
# liczba_losowan = 0
#
# start_time = time.time()
#
# while True:
#     liczba_losowan += 1
#     lotto = set(random.sample(range(1, 50), 5))
#     print(f"Losowanie: {liczba_losowan:6d} - {' '.join(map(str, lotto))}")
#     if moje_liczby == lotto:
#         break
# end_time = time.time()
# print(f"Losowano {liczba_losowan} razy i zajęło to {end_time-start_time} sekund")


# importowanie funkcji z zewnętrznych pakietów
# pakiet.modul.funkcja()
#
# from pakiet import modul
# modul.funkcja()
#
# from pakiet import funkcja
# funkcja()
#
# from pakiet.modul import funkcja
# funkcja()
#
# import time
# time.time()
# time.sleep()
# time.mktime()


# from faker import Faker
# fake = Faker('pl-PL')
# print(fake.first_name())
# print(fake.last_name())
# print(fake.phone_number())
# print(fake.street_name())
# print(fake.city())

###### ZADANIE 34

# Wygeneruj 10 tysięcy fałszywych "osób" za pomocą pakietu Faker i zapisz je do pliku osoby.csv
# Na osobę składa się: imię, nazwisko, ulica, numer domu, miasto, numer telefonu, wiek z przedziału 18-80 lat

# import random
# from faker import Faker
# fake = Faker('pl-PL')
# file_name = "osoby.csv"
# l_osob = 10000
# sep= ','
#
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(f"imię,nazwisko,ulica,numer_domu,miasto,numer_telefonu,wiek\n")
#     for _ in range(l_osob):
#         f.write(f"{fake.first_name()}{sep}{fake.last_name()}{sep}{fake.street_name()}"
#                 f"{sep}{random.randint(1, 159)}{sep}{fake.city()}{sep}{fake.phone_number()}{sep}{random.randint(18, 80)}\n")
#


# słowniki

# d = {
#     'klucz1': 1,
#     'klucz2': 'ala ma kota',
#     'klucz3': [1, 2, 'a', 'b'],
#     'klucz4': (90,80,70),
#     'klucz5': { 1,2,3},
# }

# for k in d:
#     print(k)
#
# same klucze
# print(d.keys())
#
# same wartosci
# print(d.values())
#
# klucze i wartości
# print(d.items())

# for k,v in d.items():
#     print(f"Klucz = {k}, wartość dla klucza = {v}")

# print(d['klucz3'])
# # print(d['klucz6'])
# print(d.get('klucz6', 'nie ma takiego klucza'))
# print("jeszcze działam")

# d = {}
#
# d['klucz_aaaa'] = 123
#
# d['klucz_aaaa'] = 'abc'
#
# print(d['klucz_aaaa'])

# d = {
#     1: 123,
#     2: 567,
#     'a': 'abdf',
#     (1, 'a'): [ 1, 2, 2]
# }
#
#
# for k,v in d.items():
#     print(f"Klucz = {k}, wartość dla klucza = {v}")
#     print(f"d['{k}'] = '{v}'")



##### ZADANIE 35
# Utwórz pusty słownik d. Dodaj do niego 10 elementów - kluczem jest kolejna liczba w postaci stringu,
# a wartością dla klucza jest liczba losowa.
# Wpisz cały słownik


# rozwiązanie A
# import random
# d = {}
# ile_razy = 10
# for i in range(ile_razy):
#     d[str(i)] = random.randint(1, 20)
# print(d)
#
# for k,v in d.items():
#     print(f"Klucz = {k}, wartość dla klucza = {v}")

# rozwiązanie B
# import random
# ile_razy = 10
# d = { str(i):random.randint(1, 20) for i in range(ile_razy) }
# print(d)


# import random
# ile_razy = 10
# d = { str(i):random.randint(1, 20) for i in range(ile_razy) if i % 2 }
# print(d)

# zagnieżdzone słowniki w słownikach, listy słowników itd
# d = {
#     'a': 1,
#     'b': 'abc',
#     'c': {
#         'd_a': 69,
#         'c': 'klucz b drugi raz'
#     },
#     'items': [
#         {'al': 1, 'bl': 2, 'b': 'cos'},
#         {'al': 2, 'bl': 3, 'b': 125}
#     ],
#     'krotka': (1, 2, 3)
# }
#
# # print(d)
#
# for k,v in d.items():
#     print(f"Klucz = {k}, wartość jest typu {type(v)} i jest równa: {v}")
#     if isinstance(v, dict):
#         print("podsłownik")
#         for kk, vv in v.items():
#             print(f"\tKlucz = {kk}, wartość jest typu {type(vv)} i jest równa: {vv}")
#     if isinstance(v, list):
#         print("lista")
#         for i_el, el in enumerate(v):
#             print(f"\t{i_el} = {el}")




### ZADANIE 36

# Użyj danych z zadania tworzącego 10 tysięcy fałszywych "osób" (plik osoby.csv).
# Wczytaj te dane do listy słowników. Niech każda z osób ma swój kolejny numer (nadany w ramach generowania listy)
# i niech będzie to klucz w słowniku.
# Dla przypomnienia: na osobę składa się: imię, nazwisko, ulica, numer domu, miasto, numer telefonu, wiek z przedziału 18-80 lat.

# imię,nazwisko,ulica,numer_domu,miasto,numer_telefonu,wiek
# Rafał,Klucznik,Konarskiego,94,Będzin,+48 504 307 537,59

input_file = 'osoby.csv'
sep = ','
people = {}
for id, line in enumerate(open(input_file, 'r', encoding='utf-8')):
    if id == 0:
        continue
    person_data = line.strip().split(sep)
    person_dict = {
        'first_name': person_data[0],
        'last_name': person_data[1],
        'street': person_data[2],
        'house_number': person_data[3],
        'city': person_data[4],
        'phone': person_data[5],
        'age': int(person_data[6])
    }
    people[id] = person_dict

print(people[1410])


### ZADANIE 37
# Jako ciąg dalszy zadania 36 - policz w którym mieście mieszka najwięcej osób.
# Listę zaprezentuj w kolejności od największej liczby mieszkańców
