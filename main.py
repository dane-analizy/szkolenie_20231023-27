zmienna = "linia 2"
with open("dane_oczyszczone.csv", 'w') as f:
    f.write("linia 1\n")
    f.write(f"{zmienna}\n")


# f = open(...)
# # kolejne instruncje
# f.close()

#### ZADANIE 30

# Napisz program, który przeczyta wiersz po wierszu plik "dane_2.csv" i przepisze go do pliku "dane_oczyszczone.csv"
# tak, aby pominąć puste linie.