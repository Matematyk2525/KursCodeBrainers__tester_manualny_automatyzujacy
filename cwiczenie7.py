#### Ćwiczenie nr 7:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie bylo
# wprowadzane przez uzytkownika i uwzględnij, że w przypadku gdy użytkownik wprowadzi
# literę zamiast cyfry, przerwij program


# Zdefiniowanie zmiennych
def get_user_input(parametr):
    data = ""
    while True:
        data = input(f"Podaj {parametr}: ")
        if not data.isnumeric():
            print("Prawdopodobnie podales literę")
        elif data.isnumeric():
            print("Dokonujemy konwersji")
            data = float(data)
            return data


# Policzenie zysku
def count_earnings(kwota, oprocentowanie, ilosc_lat):
    return kwota * (1 + oprocentowanie / 100) ** ilosc_lat - kwota


def main():
    kwota = get_user_input("Kwotę")
    print(f"Podana kwota to {kwota}")

    ilosc_lat = int(get_user_input("Ilosc Lat"))
    print(f"Ilosc lat {ilosc_lat}")

    oprocentowanie = get_user_input("Oprocentowanie")
    print(f"Podane oprocentowanie {oprocentowanie}")

    print(f"Zysk wynosi {count_earnings(kwota, oprocentowanie, ilosc_lat):.2f}")


if __name__ == "__main__":
    main()
