#### Ćwiczenie nr 1: napisz program liczący zysk z konta oszczędnościowego.
#### Dla przypisanego do zmiennych wartości: kwota początkowa, lata, oprocentowanie
#### oblicz kwotę zysku po upływie określonej liczby lat i wyświetl wynik.
# * program powinien mieć 3 zmienne: `kwota, miesiace, oprocentowanie`
# * zakładamy roczną kapitalizację odsetek oraz brak podatku belki.
# * dla danych: `kwota = 10000, lat = 3, oprocentowanie = 8` poprawny wynik
#  to `2597.12`
# * dla danych: 100 zł, 2 lat, oprocentowania 7% matematyczny wzór to: 100 * 1,07**2
# Zdefiniowanie zmiennych


# zdefiniowanie zmiennych
kwota = 10000
ilosc_lat = 3
oprocentowanie = 8
# Obliczenia
kwota_koncowa = kwota * (1 + oprocentowanie / 100) ** ilosc_lat
zysk = kwota_koncowa - kwota
# Wynik
kwota_koncowa = round(kwota_koncowa, 2)
print(kwota_koncowa)


print(f"Kwota końcowa {kwota_koncowa:.2f} zł")
print(f"Zysk po 2 latach {zysk:.2f} zł")


# Typy zmienne/niezmienne
alph = "asgdfghdghsafjagdadkhdhkas"
print(alph.upper())
print(alph)
