from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

resource = CoffeeMaker()
item = Menu()
money = MoneyMachine()
print("What would you like? ", item.get_items())

order = input()
if order == "report":
    resource.report()
else:
    is_available = item.find_drink(order)
    check = resource.is_resource_sufficient(is_available)
    payment = money.make_payment(check)




