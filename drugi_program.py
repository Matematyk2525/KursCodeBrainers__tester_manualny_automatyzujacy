print(2 + 2)  # dodawanie)
print(2 * 3)  # mnozenie
print(3 - 10)  # odejmowanie
print(3 / 10)  # dzielenie
print(10 // 3)  # obcinamy czesc dziesietna 10 / 3 = 3.33 po obcieciu zostaje 3
print(10 % 3)  # reszta z dzielenia bo 10 / 3 = reszta jest 1
print(2**2)  # potegowanie
print(2**0.5)  # pierwiastek kwadratowy

# print(10 / 0) 	bład dzielenia przez 0
# print(10 / '1') bład dzielenia przez string


print(10 / 2 * 3 + 40 + 12 - 100**2)
print((10 / 2) * (3 + 40) + (12 - 100) ** 2)

a = 1
b = 2
x = 3
h = 4
result = 2 * a + x + b
print(result)

# Podstawowe operacje matematyczne w Pythonie
# 1. Dodawanie np. 2 + 2 = 4
zmienna = a + b
print(zmienna)

# 2. Odejmowanie np. 2 - 2 = 0
zmienna = a - b
print(zmienna)

# 3. Mnożenie np. 2 * 2 = 4
zmienna = a * b
print(zmienna)

# 4. Dzielenie (zawsze wynik typu float) np. 5 / 2 = 2.5
zmienna = a / b
print(zmienna)

# 5. Dzielenie całkowite (zaokrągla w dół) np. 5 // 2 = 2
zmienna = a // b
print(zmienna)

# 6. Reszta z dzielenia (modulo)
zmienna = a % b
print(zmienna)

# 7. Potęgowanie np. 2 ** 3 = 8
zmienna = a**b
print(zmienna)

# 8. Pierwiastkowanie (jako potęga ułamkowa) np.
zmienna = a**0.5  # pierwiastek kwadratowy 4 ** 0.5 = 2
zmienna = a ** (1 / 3)  # pierwiastek sześcienny 8 ** (1/3) = 2
print(zmienna)
# lub używając funkcji
pow(a, 0.5)  # pierwiastek kwadratowy 4 ** 0.5 = 2
pow(a, 1 / 3)  # pierwiastek sześcienny 8 ** (1/3) = 2
print(zmienna)
# lub z modułu math:
import math

math.sqrt(a)  # pierwiastek kwadratowy
math.pow(a, 1 / 3)  # pierwiastek sześcienny
# lub z classy która można stworzyć i zaimportować do innego pliku
print(zmienna)


# Kolejność działań matematycznych
# 1. Nawiasy
# 2. Potęgowanie
# 3. Mnożenie i dzielenie (od lewej do prawej)
# 4. Dodawanie i odejmowanie (od lewej do prawej)
#  Napisz wzór na delte ax^2 + bx + c = 0
#  delta = b^2 - 4ac


# wzór na bmi # bmi = masa (kg) / wzrost^2 (m^2)
dominika_wzrost = 1.66  # wzrost w metrach
dominika_waga_rano = 60  # waga w kilogramach

dominika_bmi = dominika_waga_rano / dominika_wzrost**2
print(dominika_bmi)


# wzór na pole trójkąta


pole_trojkata = 0.5 * a * h
print(pole_trojkata)

# wzór na pole koła
pole_kola = math.pi * (a**2)
print(pole_kola)

# wzór na pole kwadratu
pole_kwadratu = a**2
print(pole_kwadratu)
# wzór na pole prostokąta

pole_prostokata = a * b
print(pole_prostokata)
# wzór na pole trapezu
pole_trapezu = 0.5 * (a + b) * h
print(pole_trapezu)
# wzór na pole równoległoboku
pole_rownolegloboku = a * h
print(pole_rownolegloboku)
# wzór na pole rombu
pole_rombu = 0.5 * a * h
print(pole_rombu)
# wzór na pole sześcianu
pole_szescianu = 6 * (a**2)
print(pole_szescianu)
# wzór na pole prostopadłościanu
pole_prostopadloscianu = 2 * (a * b + a * h + b * h)
print(pole_prostopadloscianu)
# wzór na pole kuli
pole_kuli = 4 * math.pi * (a**2)
print(pole_kuli)
# wzór na pole walca
pole_walca = 2 * math.pi * a * (a + h)
print(pole_walca)
# wzór na pole stożka
pole_stozka = math.pi * a * (a + math.sqrt(h**2 + a**2))
print(pole_stozka)
# wzór na pole graniastosłupa
pole_podstawy = pole_kwadratu
obwod_podstawy = pole_kwadratu * 4
h = a = 10  # wysokość
pole_graniastoslupa = 2 * f"{pole_podstawy}" + f"{obwod_podstawy}" * h

print(pole_graniastoslupa)
