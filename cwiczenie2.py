#### Ćwiczenie nr 2:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie bylo
# wprowadzane przez uzytkownika

# Zdefiniowanie zmiennych


# zdefiniowanie zmiennych
kwota = float(input("Wprowadz kwote: "))
ilosc_lat = int(input("Wprowadz ilość lat: "))
oprocentowanie = float(input("Wprowadź wysokość oprocentowania: "))
# Obliczenia
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat
zysk = kwota_koncowa - kwota
# Wynik
kwota_koncowa = round(kwota_koncowa, 2)
print(f" Zysk z inwestycji wynosi {kwota_koncowa}")


kwota = float(input("Podaj kwotę: "))
ilosc_lat = int(input("Podaj ilość lat: "))
oprocentowanie = float(input("Podaj oprocentowanie: "))

# Obliczenia
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota

# Wynik
print(f"Zysk wynosi {kwota_koncowa:.2f}")


lem = kwota
kwota = round(kwota, 2)
print(kwota)
