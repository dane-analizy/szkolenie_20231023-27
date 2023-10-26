def str_to_float(s):
    wynik = None
    error = ""
    try:
        wynik = float(s)
    except Exception as e:
        error = e.__class__.__name__
    return wynik, error


def bmi(waga: float, wzrost: float) -> float:
    """Funkcja wylicza wskaźnik BMI.
    Ma zastosowanie w różnych sytuacjach.


    Bardzo fajna funkcja.

    :param waga: masa ciała w kiliogramach
    :param wzrost: wzrost w centymetrach
    :return: wskaźnik BMI
    """
    return waga/((wzrost/100)**2)