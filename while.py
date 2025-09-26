i = 0
while True:
    print(f"Go {i}")
    i += 1  # i = i + 1
    if i >= 10:
        break
i = 0
while i <= 10:
    print(f"Go 2: {i}")
    i += 1  # i = i + 1
ui = input("Podaj wartosc ")
while ui.isdigit():
    print("Jest cyfrą!")
    break
