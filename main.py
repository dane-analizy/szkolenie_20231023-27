# lista_liczb = [1, 2, 3]
# lista_liter = ["a", "B", "c", "3"]
# lista_mieszana = [["l", "i", "s", "y"], 12, "asc", "34", 12, 1.56, lista_liczb, 12, "asc", "34", 12, 1.56, lista_liczb,
#                   12, "asc", "34", 12, 1.56, lista_liczb]
#
# print("lista_liczb")
# for liczba in lista_liczb:
#     print(liczba)
#
# print("lista_liter")
# for litera in lista_liter:
#     print(litera)
#
# print("lista_mieszana")
# for element in lista_mieszana:
#     print(element)

#### ZADANIE 16
# Zbuduj listę elementów różnych typów. Przeiteruj po niej i wyświetl kolejne elementy. Wypisz typ każdego z elementów.

# Rozwiązanie zadania 16
# lista_mieszana = [["l", "i", "s", "y"], 12, "asc", "34", 12, 1.56]
# for element in lista_mieszana:
#     print(type(element), element)

# lista = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print( lista[3] ) # 3 element (== o indeksie 3)
# print( lista[-2] ) # przedostatni

# print( lista[4:7]) # od 4 do 7
# print( lista[4:-2]) # do 4 do przedostatniego
# print( lista[::2]) # co drugi
# print( lista[::-1])  # od końca
# print( lista[::-2]) # od końca do drugi


# lista_list = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for element in lista_list:
#     print(element)
#     for el in element:
#         print(el)


# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in liczby:
#     for y in liczby:
#         print(x, y)
#

#### ZADANIE 17
# Wypisz na ekranie tabliczkę mnożenia w zakresie 1-100, pokazując działanie i jego wynik

# Rozwiązanie zadania 17
# for x in range(10):
#     for y in range(10):
#         print(f"{x+1} * {y+1} = {(x+1)*(y+1)}")



# print("iterator")
# lista = range(20)
# print(lista)
# print(lista[::5])
#
# print("lista z iteratora")
# lista_lista = list(lista)
# print(lista_lista)
# print(lista_lista[::5])


# lista = [100, 101, 102, 1]
#
# # dodawanie elementów do listy
# print(lista)
# lista.append(1)
# print(lista)
# lista.append(2)
# lista.append(1)
# print(lista)
#
# # wstawianie w środek listy
# lista.insert(0, 3)
# print(lista)
# lista.insert(2, 10)
# print(lista)
#
# # usunięcie pierwszej napotkanej wartości
# lista.remove(1)
# print(lista)
#
# # usunięcie elementu o konkretnym indeksie
# lista.pop(4)
# print(lista)

# zamiana elementu na liście
# lista = list(range(1, 11))
# print(lista)
# lista[5] = "a"
# print(lista)

# "pseudo" kopia listy - zmiana na oryginale zmienia "kopię"
# lista = list(range(1, 11))
# lista_zapasowa = lista
# print(lista_zapasowa)
# lista[5] = 'abc'
# print(lista_zapasowa)
#

# "pseudo" kopia listy - zmiana na oryginale zmienia "kopię"
# lista = list(range(1, 11))
# lista_zapasowa = lista
# print('pierwsza "kopia"', lista_zapasowa)
# lista_zapasowa[5] = 'abc'
# print("po zmianie na \"lista zapasowa\"", lista_zapasowa)
# print(lista)


# # "prawdziwa" kopia listy - zmiana na oryginale NI Ezmienia kopii
# lista = list(range(1, 11))
# lista_zapasowa = lista.copy()
# print(lista_zapasowa)
# lista[5] = 'abc'
# print(lista_zapasowa)
#
# import sys
# lista = list(range(1, 11))
# print(sys.getsizeof(lista))




### ZADANIE 18
# Napisz program, który pobierze od użytkownika 10 liczb, zapamięta je (zapisze na liście),
# a na koniec wyświetli całą listę pobranych wartości.

# Rozwiązanie zadania 18

# lista = []
#
# for a in range(1,11):
#     liczba = float(input(f"Podaj {a} liczbę do listy: "))
#     lista.append(liczba)
#
# print(lista)

# sortowanie listy
# lista = [1, 25, 78, 65, 12, 74, 3, 5]
# print(sorted(lista))
# print(lista)
#
# lista.sort() # równoznaczne z: lista = sorted(lista)
# print(lista)



##### ZADANIE 19

# Korzystając z programu z poprzedniego zadania pobierz od użytkownika 10 liczb,
# zapamiętaj je na liście, a listę wyświetl w kolejności rosnącej. Podaj też sumę wpisanych liczb.

# lista = []
#
# for a in range(1,11):
#     liczba = float(input(f"Podaj {a} liczbę do listy: "))
#     lista.append(liczba)
# print(lista)
#
# lista.sort()
# print(lista)
#
# # suma "po jednym elemencie"
# sum_of_numbers: float = 0
# for a in lista:
#     sum_of_numbers = sum_of_numbers + a
# print(sum_of_numbers)
#
# # funkcje wbudowane
# print(sum(lista))
#
# print(min(lista), max(lista))


# l1 = [1, 2, 3]
# l2 = [8, 7, 9]

# dodanie list - rozszerzenie jednej listy o elementy drugiej
# print(l1 + l2)
# l1.extend(l2)
# print(l1)
# print(l2)
#
# print(l1)
# print([*l1, *l2])

# suma elementów listy list
# l = [ [1, 2, 3], [5, 6, 7], [1, 3, 2] ]
# suma = 0
# for el in l:
#     suma = suma + sum(el)
# print(suma)
#
# l1 = [1, 2, 3]
# l2 = [8, 7, 9, 4]

# for licznik in range(len(l1)):
#     print(l1[licznik], l2[licznik])

# for licznik, el1 in enumerate(l1):
#      print(el1, l2[licznik])

# for el1, el2 in zip(l1, l2):
#     print(el1, el2)

# import random
# for _ in range(10):
#     print(random.randint(1, 100))

# lista składana = list comprehention

# l1 = [i for i in range(10)]
# print(l1)
#
#
# l2 = []
# for i in range(10):
#     l2.append(i)
# print(l2)


#### ZADANIE 20
# Korzystając z list składanych wygeneruj listę 10 kolejnych potęg dwójki.
# Wyświetl tę listę. Spróbuj zrobić to w jak najkrótszym zapisie.

# rozwiązanie zadania 20
# print([2**i for i in range(10)])


#### ZADANIE 21
# Korzystając z list składanych wygeneruj listę 10 losowych liczb.
# Wyświetl je w kolejności od najmniejszej do największej.

# rozwiązanie zadania 21
# import random
# print( sorted( [random.randint(1, 100) for _ in range(10)] ) )

# l = []
# for i in range(20):
#     if i > 5:
#         l.append(i)
# print(l)
#
# l = [ i*2 for i in range(20) if i > 5 ]
# print(l)

#### ZADANIE 22
# Korzystając z list składanych wygeneruj listę 20 losowych liczb.
# Na listę powinny trafić tylko liczby parzyste.

# rozwiązanie 22 - NIE UDAŁO SIĘ przygotować w wersji listy składanej
# import random
# l = []
#
# while len(l) <= 20:
#     x = random.randint(1, 100)
#     if not x % 2:
#         l.append(x)
#
# print(l)

# s = "Ala ma kota"
# print(type(s))
# for litera in s:
#     print(litera)

# print(list(s))
# rozdzielenie tekstu na słowa
# print(s.split(' '))

# s = "Zenon;Brzęczyk;95;164"
# l = s.split(';')
# print(l)

#### ZADANIE 23
# Wczytaj do listy zawartość pliku dane.csv. Kolumny rozdzielone są średnikiem. Przygotuj listę list z zawartością pliku.
# Wyświetl zawartość zbudowanej listy.
# Spróbuj to zrobić korzystając z list składanych.

# file_name = 'dane.csv'
# people = [ line.strip().split(';') for line in open(file_name, 'r', encoding='utf-8') ]
# print(people)

##### ZADANIE 24
# Korzystając z poprzedniego zadania napisz program, który z pliku dane.csv wyświetli powiększone imię i nazwisko.

# file_name = 'dane.csv'
# people = [ line.strip().split(';') for line in open(file_name, 'r', encoding='utf-8') ]
#
# for person in people:
#     print(f"Imię: {person[0].upper()}\nNazwisko: {person[1].upper()}\nWzrost i waga: {person[3].upper()} cm, {person[2].upper()} kg",
#           end="\n=======\n")


# import pandas as pd
# df = pd.read_csv("dane.csv", sep=";", header=None)
# print(df)


#### ZADANIE 25
# Dla każdego wpisu w pliku dane.csv wyświetl na konsoli informację o imieniu, nazwisku, wadze i wzroście oraz BMI.

# bmi = weight / height ** 2

# print("afafqaf"
#       "aegeg"
#       "ageag")

# for i in range(3):
#     print(f'''afafqaf
# aegeg
# ageag''')
#     print(i)


# rozwiązanie wersja A
#
# # wczytanie danych
# file_name = 'dane.csv'
# people = [ line.strip().split(';') for line in open(file_name, 'r', encoding='utf-8') ]
#
# # przetworzenie i oczyszczenie
# people_clean = []
# for person in people:
#     people_clean.append(
#         [person[0], person[1], float(person[2]), float(person[3])/100]
#     )
#
# # wyświetlenie wyniku
# for person in people_clean:
#     bmi = person[2] / (person[3] ** 2)
#     print(f"{person[0]} {person[1]} ({100*person[3]} cm, {person[2]} kg) - BMI = {bmi:.1f}")
#

# rozwiązanie wersja B

# # wczytanie danych
# file_name = 'dane.csv'
# people = [line.strip().split(';') for line in open(file_name, 'r', encoding='utf-8')]
#
# # przetworzenie i oczyszczenie
# people_clean = []
# for person in people:
#     weight = float(person[2])
#     height = float(person[3]) / 100
#     bmi = weight / height ** 2
#     people_clean.append(
#         [person[0], person[1], weight, height, bmi]
#     )

# # wyświetlenie wyniku
# for person in people_clean:
#     print(f"{person[0]} {person[1]} ({100 * person[3]} cm, {person[2]} kg) - BMI = {person[4]:.1f}")


# print(sorted(people_clean))

# sortowanie od największej
# l = [1, 5, 6, 8, 7]
# print(sorted(l, reverse=True))

import random

# l = [ [4, 'd'], [1, 'c'], [2, 'b'], [3, 'a']]
# print(sorted(l, key=lambda x: x[1]))

# def funkcja(x):
#     return x[1]
#
# print(sorted(l, key=lambda x: funkcja(x)))

#### ZADANIE 26
# Wczytaj dane z pliku dane.csv.
# Dla każdego policz wskaźnik BMI, a następnie posortuj listę wartości BMI rosnąco. Wyświetl wynik na konsoli

# # wczytanie danych
# file_name = 'dane.csv'
# people = [line.strip().split(';') for line in open(file_name, 'r', encoding='utf-8')]
#
# # przetworzenie i oczyszczenie
# people_clean = []
# for person in people:
#     weight = float(person[2])
#     height = float(person[3]) / 100
#     bmi = weight / height ** 2
#     people_clean.append(
#         [person[0], person[1], weight, height, bmi]
#     )
#
# # sortowanie po BMI, malejąco
# # people_clean.sort(key=lambda x: x[4], reverse=True)
#
# # wyświetlenie wyniku
# for person in sorted(people_clean, key=lambda x: x[4], reverse=True):
#     print(f"{person[0]} {person[1]} ({100 * person[3]} cm, {person[2]} kg) - BMI = {person[4]:.1f}")


# lista = [1, 2, 3, 4, 'a', 'b', 'c']
# print(lista)
# krotka = (1, 2, 3, 4, 'a', 'b', 'c')
# print(krotka)

# krotka = (1, 2, 3, 4, 'a', 'b', 'c')
# print(krotka[4])
# for i, element in enumerate(krotka):
#     print(i, element)

# lista = [1, 2, 3, 4, 'a', 'b', 'c']
# lista[4] ='xxxxx'
# print(lista)
#
# krotka = (1, 2, 3, 4, 'a', 'b', 'c')
# krotka[4] ='xxxxx'
# print(krotka)

# krotka = (1, 5, 32, 43)
# print(sorted(krotka, reverse=True))
# print(krotka[::2])

# krotka = tuple([ i for i in range(10) ])
# print(krotka)
# lista = list(krotka)
# print(lista)

# file_name = 'dane.csv'
# people = tuple([line.strip().split(';') for line in open(file_name, 'r', encoding='utf-8')])
#
# # # przetworzenie i oczyszczenie
# people_clean = []
# for person in people:
#     weight = float(person[2])
#     height = float(person[3]) / 100
#     bmi = weight / height ** 2
#     people_clean.append(
#         [person[0], person[1], weight, height, bmi]
#     )


# cos = "afageeg"
# print(len(cos))
# cos = [1 ,2 ,3 ,3]
# print(len(cos))
# cos = ('a', 'b' ,'c')
# print(len(cos))

# łączenie krotek
# krotkaa = (1, 2, 3)
# krotkab = (4, 5, 6)
# krotkawynik = krotkaa + krotkab
# print(krotkawynik, type(krotkawynik))

#### ZADANIE 27
# Stwórz dwie krotki: jedną z 10 liczbami losowymi od 0 do 10, druga z 10 liczbami losowymi od 100 do 150.
# Połącz je w jedną krotkę i wyświetl posortowane od największych

# import random
# l1 = tuple([random.randint(0,10) for _ in range(10)])
# l2 = tuple([random.randint(100,150) for _ in range(10)])
# print(tuple(sorted(l1+l2,reverse=True)))


