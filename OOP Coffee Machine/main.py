from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee = CoffeeMaker()
item = Menu()
money = MoneyMachine()

while is_on:

    print("What would you like? ", item.get_items())

    order = input()
    if order == "report":
        coffee.report()
        money.report()
    elif order == "off":
        exit()
    else:
        is_available = item.find_drink(order)
        check = coffee.is_resource_sufficient(is_available)
        if check:
            payment = money.make_payment(is_available.cost)
            if payment:
                coffee.make_coffee(is_available)

        else:
            print("not enough resource")




