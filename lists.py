lista = [1, 2, 3]
print(lista)

convert_to_list = list((1, 2, 3))
print(convert_to_list)

convert_str_to_list = list("tojestlista")
print(convert_str_to_list)

lista = [1, 2, 3]
print(lista)
convert_to_list = list((1, 2, 3))
print(convert_to_list)
convert_str_to_list = list("ToJestLista")
print(convert_str_to_list)
print(convert_str_to_list[0:5])
unsorted_list = ["a", "g", "c", "p", "x", "b"]
print(f"Przed sortowaniem {unsorted_list}")
unsorted_list.sort()
print(f"Po sortowaniu {unsorted_list}")
print(f"Litera a występuje tylko {unsorted_list.count('a')}")


new_element = "dodane"
codebrainers_lista = ["a", 123, [1, 3], True, False, None, (1, 3), "testt", "1231312"]
codebrainers_lista.append(new_element)
print(codebrainers_lista[-1] == new_element)
codebrainers_lista.insert(2, new_element)
print(codebrainers_lista)
# ['a', 123, 'dodane', [1, 3], True, False, None, (1, 3), 'testt', '1231312', 'dodane']
print(codebrainers_lista.index("a"))  # sprawdzam gdzie jest a
print(f"Zrzucone {codebrainers_lista.pop()}")
print(f"Po zrzuceniu {codebrainers_lista}")
print("Po zrzuceniu", codebrainers_lista)  # inny sposób formatowania
print("Po zrzuceniu", codebrainers_lista, sep="")  # bez spacji
print("Po zrzuceniu", codebrainers_lista, sep=" — ")  # własny separator
print("Po zrzuceniu", codebrainers_lista, end="")  # bez nowej linii
print("Po zrzuceniu", ", ".join(map(str, codebrainers_lista)))  # Po zrzuceniu 3, 5, 7
print(f"Po zrzuceniu {len(codebrainers_lista)} elementów")
