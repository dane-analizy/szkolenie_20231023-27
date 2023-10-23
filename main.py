# print("Hello world!")

# zmienna = 123
# zmienna2 = "abc"

# print(zmienna)
# print("zmienna")
# print(zmienna2)

# zmienna = zmienna + 5
# print(zmienna)
# print(zmienna + 10)
# print(zmienna)

# definicja zmiennych
# tekst_a = "aaaa"
# tekst_b = "bbbb"
# liczba = 123

# # dodanie zmiennych tekstowych - "sklejenie ciągów"
# tekst_wynikowy = tekst_a + tekst_b
# print(tekst_wynikowy)
#
# # dodanie liczby do tekstu
# zmienna_wynikowa = tekst_a + str(liczba)
# print(zmienna_wynikowa)
#
# # formatowanie printa
# print("Tekst: {}\nLiczba: {}".format(tekst_a, liczba))
#
# # za dużo zmiennych, za mało miejsca na nie
# print("Tekst: {}\nLiczba: {}".format(tekst_a, liczba, tekst_b))

# za mało zmiennych
# print("Tekst: {}\nLiczba: {}".format(tekst_a))

# f-string
# print(f"Tekst : {tekst_a}\nLiczba: {liczba}")

# f-string z wyrażeniem
# print(f"Tekst : {tekst_a}\nLiczba: {liczba+10}")

# formatowanie f-string
# 2023-10-23 10:14:56
# {dt:%Y-%m-%d %H:%M:%S}

# imie = input("Podaj imię: ")
# print(imie)


#### ZADANIE 1
# Pobierz od użytkownika jego imię i nazwisko (w dwóch krokach) i wyświetl powitanie w postaci "Witaj Imię Nazwisko"

### Rozwiązanie zadania 1

# imie = input("Podaj imie: ")
# nazwisko = input("Podaj nazwisko: ")
# print("Witaj " + imie + " " + nazwisko)
#
# print(f"Witaj {imie} {nazwisko}")


#### ZADANIE 2
# Pobierz od użytkownika dwie liczby i wyświetl wynik ich dodawania oraz mnożenia

### Rozwiązanie zadania 2
#
# liczba1 = int(input("Podaj liczbę1 "))
# liczba2 = int(input("Podaj liczbę2 "))
#
# print(f"Suma: {liczba1+liczba2}")
# print(f"Iloczyn: {liczba1*liczba2}")


#### ZADANIE 3
# Napisz program, który pobierze od użytkownika masę i wzrost, a następnie policzy BMI i wypisze wynik na konsolę.
# BMI = masa / wzrost^2
# wzrost w metrach
# masa w kg

# liczba zmiennoprzecinkowa z tekstu: float()
# print(float("1.23")*2)

# liczba X do potęgi N
# x**n
# pow(x, n)

# Rozwiązanie zadania 3

# zaokrąglenie w obliczeniach
# masa = float(input("Podaj masę w kg: "))
# wzrost = float(input("Podaj wzrost w m: "))
# bmi = round(masa / wzrost**2, 2)
# print(bmi)
# print(f"Przy wzroście {wzrost}m i masie {masa}kg Twój wskaźnik BMI to {bmi}")

# zaokrąglenie przy wyświetlaniu
# masa = float(input("Podaj masę w kg: "))
# wzrost = float(input("Podaj wzrost w m: "))
# bmi = masa / wzrost**2
# print(f"Przy wzroście {wzrost}m i masie {masa}kg Twój wskaźnik BMI to {bmi:.2f}")


