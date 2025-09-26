# Wypełnijcie te elementy wartosciami
# można też na slacku przeslac :)
number = 25
number_float = 25.5
characters = "Codebraineers"
flag = True
list_elements = [1, 2, 3, 25]
dict_elements = {"kg": "value"}
set_elements = {1, 2, 3, 25, 1, 2, 3, 25}
tuple_elements = (1, 2, 3, 25)


# Metody i operacje na typach danych
# Czy to jest integer
print(number.is_integer())
print(number_float.is_integer())
# Czy zaczyna/konczy sie na dany znak
print(characters.startswith("X"))
print(characters.endswith("s"))
print(characters.split("o"))
# Uporzadkowana sekwencja
print(list_elements[0])
# Nieuporzadkowane sekwencje
print(dict_elements["kg"])
print(set_elements.pop())
# Krotka
print(tuple_elements)
print(tuple_elements[2])
new_tuple = list(tuple_elements)
new_tuple.append(10)
new_tuple.append("a")
new_tuple.append(True)
tuple_elements = tuple(new_tuple)
print(type(tuple_elements))
