#### Ćwiczenie nr 5:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie były przechowywane
# słowniku, a następnie te wartosci wykorzystywane w obliczeniach

# Zdefiniowanie zmiennych
dane = {"kwota": 10000, "okres": 3, "oprocentowanie": 8}

# Obliczenia
kwota_koncowa = round(
    dane["kwota"] * (1 + dane["oprocentowanie"] / 100) ** dane["okres"] - dane["kwota"],
    2,
)

# Wynik
print(
    f"Dane: kwota={dane['kwota']}, lata={dane['okres']}, oprocentowanie={dane['oprocentowanie']}%"
)


print(f"Zysk wynosi {kwota_koncowa}")

