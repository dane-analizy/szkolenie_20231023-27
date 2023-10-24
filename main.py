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