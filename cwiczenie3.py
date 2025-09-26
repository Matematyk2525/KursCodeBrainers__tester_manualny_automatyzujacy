# Biorąc pod uwagę 2 ciągi, `s1` i `s2` zwróć
# nowy ciąg złożony z pierwszego, środkowego i
# ostatniego znaku każdego ciągu wejściowego
# Dane:
#   * `s1 = "America"`
#   * `s2 = "Japan"`
# Oczekiwany wynik:
# `AJrpan`
str1 = "America"
str2 = "Japan"
# Pierwszy znak
print(str1[0])
print(str1[-1])
print(str2[0])
print(str2[-1])
print(str1[len(str1) // 2])  # znak srodkowy z str1
print(str2[len(str2) // 2])  # znak srodkowy z str2
# Zastapic str[0], 1, itd.... jako zmienne
# new_str = zmienna1 + ...
new_str = (
    str1[0]
    + str2[0]
    + str1[len(str1) // 2]
    + str2[len(str2) // 2]
    + str1[-1]
    + str2[-1]
)
print(f"Nowy ciag znakow {new_str}")
# Przyklad z ciagiem o dlugosci 4
str3 = "test"
print(len(str3) // 2)
