def nazwa():
    return 2


print(type(nazwa()))
lista = [1, 2]
print(type(lista))


class ExampleClass:
    def class_method():
        return 2


print(type(ExampleClass))
print(type(ExampleClass.class_method()))
x = 10
y = "Python"
z = None
print(id(x))
print(id(y))
x = x + 1
print(id(x))
