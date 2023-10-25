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

# input_file = "dane_2.csv"
# output_file = "dane_oczyszczone.csv"
# file_content = [line.strip() for line in open(input_file, 'r', encoding='utf-8') if len(line) > 1]
# f = open(output_file, 'w', encoding='utf-8')
# f.writelines([f"{l}\n" for l in file_content])
# f.close()


input_file = "dane_2.csv"
output_file = "dane_oczyszczone.csv"
file_content = [line.strip() for line in open(input_file, 'r', encoding='utf-8') if len(line) > 1]
with open(output_file, 'w', encoding='utf-8') as f:
    f.writelines([f"{l}\n" for l in file_content])
