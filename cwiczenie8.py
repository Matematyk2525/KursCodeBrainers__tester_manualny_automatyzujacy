#### Ćwiczenie nr 8:
# Zmodyfikuj program ponizej tak aby kwota, ilosc rat oraz oprocentowanie bylo 
# wprowadzane przez uzytkownika i uwzględnij, że w przypadku gdy użytkownik wprowadzi
# literę zamiast cyfry, przerwij program 


# lokata roczna (uproszczonym oprocentowaniem)
# lokata z kapitalizacja miesieczna 
# kredyt (obliczenie raty)

class UserInput:

    @staticmethod
    def get_float_value(parametr):
        pass
    
    @staticmethod
    def get_int_value(parametr):
        pass

class Investment:
    
    def __init__(self, kwota, oprocentowanie, ilosc):
        self.kwota = kwota
        self.oprocentowanie = oprocentowanie
        self.ilosc = ilosc 

    def return_investment_parameters():

        pass 

class SimpleInvestment:

    def calculate_simple_profit(self):
        # Zwrot zysk z prostej lokaty (jak w zadaniu 7)
        pass 

class AdvancedInvestment:

    def calculate_advanced_profit(self):
        # Zwrot zysk z inwestycji z kapitalizacja miesieczna
        pass

class Loan:

    def calculate_monthly_cost(self):
        pass 

    def calculate_profit(self):
        pass 


def main():

    print("TODO")

    if __name__ == "__main__":
        main()
