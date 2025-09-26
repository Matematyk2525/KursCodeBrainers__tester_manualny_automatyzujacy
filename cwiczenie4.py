# * Odwróć podany ciąg
# * Dane:\
# `str1 = "Python"`
# * Oczekiwany wynik:\
# `nohtyP`

str1 = "Python"
str1 = list(str1)
str1.reverse()
convert_to_string = str(str1)
print(convert_to_string)

str2 = "Python"
print(str2[::-1])
