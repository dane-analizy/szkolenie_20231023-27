
# zapisywanie tekstu do pliku

# context manager - konstrukcja with ...:
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