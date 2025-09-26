def nazwa():
    pass

instancja_funkcji = nazwa()

suma = lambda arg1, arg2: arg1 + arg2
print(suma(1, 2))

pitagoras = lambda a, b, c, d: ((a * a) + (b * b)) ** 0.5 + c * d
print(pitagoras(1, 2, 3, 4))

# Podejscie klasyczne
empty_list = []
for element in range(1, 21):
    empty_list.append(element)
print(empty_list)

# Podejscie funkcyjne, inline
empty_list1 = [e for e in 'Python']
print(empty_list1)

empty_list2 = [digit for digit in range(1, 21)]
print(empty_list2)


empty_list3 = [digit for digit in range(1, 21) if digit % 2 == 0]
print(empty_list3)
# 2, 4, 6, 8, 10, 12, 14, 16, 18, 20

log_file = 'logs.txt'
with open(log_file) as f:
    opened_file = f.read()
    wystapienia = opened_file.count("ERROR")
    print(f'W pliku znaleziono {wystapienia} wystapien słowa "Error"')


tekst = "googl e.com"
wystapienia = {znak: tekst.count(znak) for znak in tekst}
print(wystapienia)


