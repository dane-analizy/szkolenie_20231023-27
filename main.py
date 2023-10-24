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
# # "prawdziwa" kopia listy - zmiana na oryginale NI Ezmienia kopii
# lista = list(range(1, 11))
# lista_zapasowa = lista.copy()
# print(lista_zapasowa)
# lista[5] = 'abc'
# print(lista_zapasowa)