lista_liczb = [1, 2, 3]
lista_liter = ["a", "B", "c", "3"]
lista_mieszana = [["l", "i", "s", "y"], 12, "asc", "34", 12, 1.56, lista_liczb, 12, "asc", "34", 12, 1.56, lista_liczb,
                  12, "asc", "34", 12, 1.56, lista_liczb]

print("lista_liczb")
for liczba in lista_liczb:
    print(liczba)

print("lista_liter")
for litera in lista_liter:
    print(litera)

print("lista_mieszana")
for element in lista_mieszana:
    print(element)

#### ZADANIE 16
# Zbududuj listę elementów różnych typów. Przeiteruj po niej i wyświetl kolejne elementy. Wypisz typ każdego z elementów.