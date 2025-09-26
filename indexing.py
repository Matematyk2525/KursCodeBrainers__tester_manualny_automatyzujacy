word = "Python"

print(word[0])
print(word[1])
print(word[3])

word = "Python"
print(word[0])
print(word[1])
print(word[5])
print(word[-1])
print(word)
word = "Python"
#   012345
#  -654321
# Pyt start - jest start, end - indeks ktory interesuje + 1
print(word[0:3])  # Pyt
print(word[-2:-1])  # o
print(word[-3:])  # hon   - nie musimy wiedziec jak dlugi jest ciag znakow


kurs = "Codebrainers"
nowy_kurs = kurs  # kopia
nowy_kurs = kurs[:]
# co ile
print(kurs[0:-1:2])
# kurs[start:koniec:krok]
print(f"ilosc znakow {len(kurs)}")
print(kurs[0 : len(kurs)])

t = [1, 2, 3]
print(t[2])
c = (1, 2, 3)
print(c[1])
