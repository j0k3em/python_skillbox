class Propety():
    def __init__(self, worth, percent_tax):
        self.__worth = worth
        self.__percent_tax = percent_tax
        self.__tax = self.__worth/self.__percent_tax

    def get_tax(self):
        return self.__tax

class Appartment(Propety):
    __percent_tax = 1000
    def __init__(self, worth):
        self.worth = worth
        super().__init__(self.worth, self.__percent_tax)

class Car(Propety):
    __percent_tax = 200
    def __init__(self, worth):
        self.worth = worth
        super().__init__(self.worth, self.__percent_tax)

class CountryHouse(Propety):
    __percent_tax = 500
    def __init__(self, worth):
        self.worth = worth
        super().__init__(self.worth, self.__percent_tax)

def tax_pay():
    money = input_value("Введите кол-во денег: ")
    appartment = input_value("Введите стоимость квартиры: ")
    car = input_value("Введите стоимость машины: ")
    country_house = input_value("Введите стоимость дачи: ")
    tax = tax_calculation(appartment, car, country_house)
    check_money(money, tax)

def input_value(text):
    value = 0
    while True:
        try:
            value = int(input(text))
            return value
        except ValueError:
            print("Некорректное значение!")

def tax_calculation(appartment, car, country_house):
    tax = round(Appartment(appartment).get_tax()
    + Car(car).get_tax() \
    + CountryHouse(country_house).get_tax(), 2)
    return tax

def check_money(money, tax):
    if money >= tax:
        print("Олично, денег хватает!")
    else:
        print("Грустно, не хватает ", tax - money, "рублей")

tax_pay()