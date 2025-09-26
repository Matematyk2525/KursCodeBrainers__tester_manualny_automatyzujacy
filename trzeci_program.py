x = 10
x = 5  # zmienna tekstowa

# python jest językiem case sensitive - rozróżnia wielkość liter w nazwach zmiennych
# nie można zaczynać nazwy zmiennej od cyfry
# nie można używać znaków specjalnych w nazwach zmiennych np. !@#$%^&*()-+=/\|?><,.,~`
# nie można używać spacji w nazwach zmiennych - zamiast spacji używamy podkreślenia _
# nie można używać polskich znaków w nazwach zmiennych - zamiast polskich znaków używamy liter bez ogonków
# nie można używać słów kluczowych Pythona w nazwach zmiennych - np. if, else, for, while, def, return, import, from, as, class, try, except, finally, with, lambda, pass, break, continue, global, nonlocal, assert, yield, raise

test = 20
test1 = 20
test_ = 10
this_is_test_variable = 10

# klasy używają notacji CamelCase
# polega na tym że każda nowa litera w nazwie klasy jest wielka np.
class ThisIsTestClass:
    pass

# funkcje używają notacji snake_case
# polega na tym że każda nowa litera w nazwie funkcji jest mała a słowa są oddzielone podkreśleniem np.
def this_is_test_function():
    pass


# and, or, not, is, in, as, break, continue, def, del, elif, else, except, finally, for, from, global, if, import, lambda, nonlocal, pass, raise, return, try, while, with, yield, True, False, None, class nie uzywać w nazwach zmiennych
# poniższe przykłady są błędne i spowodują błąd

# Zmienne mogą zmieniać typ w trakcie działania programu
# zmienna x najpierw jest liczbą całkowitą, potem zmiennoprzecinkową, potem tekstową
# Python jest językiem dynamicznie typowanym
# oznacza to że nie musimy deklarować typu zmiennej przed jej użyciem
# typ zmiennej jest określany w trakcie działania programu


print(x)
x = 20
print(x)
x = "test"
print(x)
# Inkrementacja dekrementacja
# Inkrementacja to zwiększenie wartości zmiennej o 1
# Dekrementacja to zmniejszenie wartości zmiennej o 1
# Przykład inkrementacji i dekrementacji
# poniższy kod jest poprawny ale nieefektywny
# pokazuje jak działa inkrementacja i dekrementacja
# ale nie jest to sposób w jaki powinniśmy tego używać w praktyce
# poniższy kod jest tylko do celów edukacyjnych
# nie używaj go w praktyce
# zamiast tego używaj operatorów += i -=
# np. a += 1 zamiast a = a + 1
# np. py


a = 10
print(a)
a = a + 1
a = a + 1
a = a + 1
a = a + 1

print(a)
a = a - 1
a = a - 1
a = a - 1
a = a - 1

print(a)
a = a * 2
a = a / 2
a = a**2
print(a)
a = 10

a += 5  # a = a + 5   → wynik: 15
print(a)
a -= 3  # a = a - 3   → wynik: 12
print(a)
a *= 2  # a = a * 2   → wynik: 24
print(a)
a /= 4  # a = a / 4   → wynik: 6.0   (dzielenie daje float)
print(a)
a //= 2  # a = a // 2  → wynik: 3     (dzielenie całkowite)
print(a)

a %= 2  # a = a % 2   → wynik: 1     (reszta z dzielenia)
print(a)
a **= 3  # a = a ** 3  → wynik: 1     (podniesienie do potęgi)
print(a)

# dodawanie do zmiennej tekstowej
text = " Ala ma "
text += "kota"
print(text)
text = text + " i psa"
print(text)
text *= 3
print(f"{text} ")

# podstawowae operacje na zmiennych
