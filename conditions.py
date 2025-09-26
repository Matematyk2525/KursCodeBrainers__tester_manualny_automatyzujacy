if 5 > 0:
    print("Test")
#################
if 5 < 0:
    print("To sie wykona?")
else:
    print("Jestem w else")
#################
a = 8
if a > 9:
    print("a jest wieksze od 9")
elif a > 8:
    print("a jest wieksze od 8")
else:
    print("a jest wieksze od 7")

condition = 1 == 1
print(condition)

if condition:
    print("To jest prawda")

# and, or, not
if 1 > 0 and 2 > 1:  # Sprawdz warunek 1 i warunek 2, oba musza prawda!
    print("AND")

if 1 < 0 or 2 > 1:  # Sprawdz warunek 1, jesli to nieprawda, to sprawdz kolejny
    print("OR")

if 1 > 0 or 2 < 1:  # Sprawdz warunek 1, jesli to nieprawda, to sprawdz kolejny
    print("OR1")

if not False:
    print("NOT")

if not True:
    print("NOT1")


print(1 > 0 and 2 > 1)  # True
print(1 < 0 or 2 < 1)  # False
