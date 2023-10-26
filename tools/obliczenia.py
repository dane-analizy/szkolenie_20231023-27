def bmi(waga: float, wzrost: float) -> float:
    """Funkcja wylicza wskaźnik BMI.
    Ma zastosowanie w różnych sytuacjach.


    Bardzo fajna funkcja.

    :param waga: masa ciała w kiliogramach
    :param wzrost: wzrost w centymetrach
    :return: wskaźnik BMI
    """
    return waga/((wzrost/100)**2)