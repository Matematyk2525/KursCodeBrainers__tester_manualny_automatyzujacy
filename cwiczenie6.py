#### Ćwiczenie nr 6:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie były przechowywane
# słowniku, a następnie te wartosci wykorzystywane w obliczeniach

# Zdefiniowanie zmiennych
dane = [
    {"kwota": 1000, "ilosc_lat": 3, "oprocentowanie": 5},
    {"kwota": 2500, "ilosc_lat": 5, "oprocentowanie": 4.5},
    {"kwota": 5000, "ilosc_lat": 2, "oprocentowanie": 3},
]

for zestaw in dane:
    kwota = zestaw["kwota"]
    ilosc_lat = zestaw["ilosc_lat"]
    oprocentowanie = zestaw["oprocentowanie"]

    # Obliczenia
    zysk = kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota

    print(f"Dane: kwota={kwota}, lata={ilosc_lat}, oprocentowanie={oprocentowanie}%")

    # Wynik
    print(f"  Zysk wynosi {zysk:.2f}\n")
