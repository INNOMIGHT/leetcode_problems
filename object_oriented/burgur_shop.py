class BurgurList:

    def __init__(self):
        self.available_burgurs = {
            "1. Mc Aloo Tikki": 50.00,
            "2. Mc Veggie": 60.00,
            "3. Mc Spicy Paneer": 80.00,
            "4. Mc Chicken": 90.00,
            "5. Extra Long Cheese Burger": 100.00,
            "6. Chicken Mcgrill": 120.00,
            "7. Mc Egg Burger": 110.00,
            "8. Nothing from here": 00.00,
        }
    
    def show_burgur_menu(self):
        print(self.available_burgurs)


class AdditionalsList:

    def __init__(self):
        self.additionals = {
            "1. Extra Cheese": 25.00,
            "2. French Fries": 80.00,
            "3. Extra Patti": 40.00,
            "4. Nothing from here": 00.00,
        }

    def show_additionals_menu(self):
        print(self.additionals)


class DrinksList:

    def __init__(self):
        self.drinks = {
            "1. Coke": 55.00,
            "2. Pepsi": 51.00,
            "3. Red Bull": 155.00,
            "4. Nothing from here": 00.00,
        }

    def show_drinks_menu(self):
        print(self.drinks)


class TaxesList:

    def __init__(self):
        self.taxes = {
            "Service Tax": 15/100,
            "VAT": 10/100
        }
    
    def apply_taxes(self):
        return self.taxes["Service Tax"] + self.taxes["VAT"]


class TakeOrder(BurgurList, AdditionalsList, DrinksList):

    def __init__(self):
        self.burgurs_price = 0
        self.additionals_price = 0
        self.drinks_price = 0

    def take_order(self):
        burgur_keys = list(self.available_burgurs)
        additional_keys = list(self.additionals)
        drink_keys = list(self.drinks)
        
        print("Here is the burgur menu: " + str(BurgurList.show_burgur_menu()))
        no_of_burgurs = int(input("Enter the number of burgurs you want to order: "))
        for i in range(1, no_of_burgurs+1):
            burgur = int(input("Chose Burgur " + str(i) + ": "))
            self.burgurs_price += self.available_burgurs[burgur_keys[burgur-1]]

        print("Here is the additionals menu: " + str(AdditionalsList.show_additionals_menu()))
        no_of_additionals = int(input("Enter the number of additionals you want to order: "))
        for i in range(1, no_of_additionals+1):
            additional = int(input("Chose Additional " + str(i) + ": "))
            self.additionals_price += self.additionals[additional_keys[additional-1]]
        
        print("Here is the additionals menu: " + str(AdditionalsList.show_additionals_menu()))
        no_of_drinks = int(input("Enter the number of drinks you want to order: "))
        for i in range(1, no_of_drinks+1):
            drink = int(input("Chose Drink " + str(i) + ": "))
            self.drinks_price += self.drinks[drink_keys[drink-1]]


class CalculateBill(TakeOrder, TaxesList):

    def __init__(self):
        self.bill_without_tax = self.burgurs_price + self.additionals_price + self.drinks_price
    
    def bill_calculator(self):
        return self.bill_without_tax * TaxesList.apply_taxes()


class BurgurShop:

    def initialize(self):
        TakeOrder.take_order
        bill = CalculateBill.bill_calculator
        print("Here is your order, fresh and delicious!")
        print("I hope you enjoyed your meal. Here is the bill for your order. Thank you. " + str(bill))


initialize_shop = BurgurShop()
initialize_shop.initialize()
    
