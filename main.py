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


#### ZADANIE 4
# Pobierz od użytkownika liczbę całkowitą i wypisz czy jest dodatnia


#### ZADANIE 5
# Pobierz od użytkownika liczbę całkowitą i wypisz czy jest dodatnia, ujemna czy jest zerem

# liczba = int(input("Podaj liczbę:"))
#
# if liczba > 0:
#     print("Liczba jest dodatnia")
# elif liczba < 0:
#     print("Liczba jest ujemna")
# else:
#     print("Liczba jest zerem")


#### ZADANIE 6

# Napisz program, który pobierze od użytkownika masę i wzrost, a następnie policzy BMI i wypisze na konsolę.
# Dodatkowo - na podstawie wartości obliczonego BMI niech poda komentarz.
#
# < 16 => wygłodzenie
# 16 - 16.999 => wychudzenie
# 17 - 18,49 => niedowaga
# 18,5 - 24,999 => pożądana masa ciała
# 25 - 29,999 => nadwaga
# 30 - 34,999 => otyłość I stopnia
# 35 - 39,999 => otyłość II stopnia (duża)
# > 40 otyłość III stopnia (chorobliwa)

# rozwiązanie zadania 6

# weight = input("Podaj masę [kg]: ")
# weight = float(weight)
#
# height = input("Podaj wzrost [cm]: ")
# height = float(height) / 100
#
# bmi = weight / height**2
#
# if bmi <= 16:
# 	bmi_comment = "wygłodzenie"
# elif bmi <= 17:
# 	bmi_comment = "wychudzenie"
# elif bmi <= 18.5:
# 	bmi_comment = "niedowagę"
# elif bmi <= 25:
# 	bmi_comment = "pożądaną masa ciała"
# elif bmi <= 30:
# 	bmi_comment = "nadwagę"
# elif bmi <= 35:
# 	bmi_comment = "otyłość I stopnia"
# elif bmi <= 40:
# 	bmi_comment = "otyłość II stopnia (duża)"
# else:
# 	bmi_comment = "otyłość III stopnia (chorobliwa)"
#
# print(f"\nTwój wynik BMI:\n- przy wzroście {height} m\n- wadze {weight} kg\nto {bmi:.2f}, co oznacza {bmi_comment}")

# instrukcja pass
# zmienna = 1
# if zmienna != 0:
#     pass
# else:
#     print("cos")

# wyświetl 10 pierwszych liczb całkowitych (razem z zerem)
# for i in range(10):
#     print(i)

# range od - do
# for i in range(5, 15):
#     print(i)

# for i in range(0, 100, 10):
#     print(i)

# krok musi być liczbą całkowitą - to będzie błąd
# for i in range(0, 100, 0.5):
#     print(i)


# modulo = reszta z dzielenia
# print(11 % 3)

#### ZADANIE 7
# Wydrukuj liczby od 1 do 100 razem z informacją czy liczba jest parzysta czy nieparzysta.


# Rozwiązanie zadania 7
# for i in range(1,101):
#     if i%2 == 0:
#         print(f"{i}:parzysta")
#     else:
#         print(f"{i}:nieparzysta")


#### ZADANIE 8
# Napisz symulator lokaty Symulator ma przyjmować zmienne:
# - kwotę lokaty
# - oprocentowanie w skali roku
# - ilość miesięcy na jaką zakładamy lokatę
# Symulator ma dla każdego miesiąca lokaty wypisać który to miesiąc oraz ile mamy aktualnie zgromadzone po doliczeniu odsetek.
# Zakładamy kapitalizację odsetek co miesiąc

