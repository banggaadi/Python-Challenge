MENUS = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 9000,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15000,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 25000,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for resource, value in resources.items():
        print(resource, ":", value)
    pesan()

def check_resource(order):
    print("Checking resources for", order, ": ")
    for menu in MENUS:
        if menu == order:
            for key, value in MENUS[menu]["ingredients"].items():
                if resources[key] < MENUS[menu]["ingredients"][key]:
                    print("Sorry we're out!")
                    pesan()
                else:
                    print(key, ":", value)
                    resources[key] = resources[key] - MENUS[menu]["ingredients"][key]


def check_money(order):
    print("Checking payment")
    for menu in MENUS:
        if menu == order:
            cost = MENUS[menu]["cost"]
            print("Cost:", cost)

    goceng = int(input("How many 5000-an you have?"))
    ceban = int(input("How many 10000-an you have?"))

    total_money = (goceng * 5000) + (ceban * 10000)

    if cost == total_money:
        print("Thank you! there will be no change")
    elif cost > total_money:
        print("Oops you don't have enough money")
    elif total_money > cost:
        total_money = total_money - cost
        print("Thank you! here is your change: ",total_money)
    pesan()



def pesan():
    global available
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "report":
        report()
    elif order == "espresso":
        check_resource(order)
        check_money(order)
    elif order == "latte":
        check_resource(order)
        check_money(order)
        pesan()
    elif order == "cappuccino":
        check_resource(order)
        check_money(order)
    elif order == "off":
        available = False

available = True
while available:
    pesan()


# def report():
#     for resource, value in resources.items():
#         print(resource, ":", value)
#
# def check_resource(menu):
#     print("Checking resources for", menu, ":")
#     for key, value in MENUS[menu]["ingredients"].items():
#         if resources[key] < value:
#             print("Sorry, we're out of", key)
#             return False
#         else:
#             print(key, ":", value)
#             resources[key] -= value
#     return True
#
# def check_money(menu):
#     print("Checking payment for", menu, ":")
#     cost = MENUS[menu]["cost"]
#     print("Cost:", cost)
#
#     goceng = int(input("How many 5000-an do you have? "))
#     ceban = int(input("How many 10000-an do you have? "))
#
#     total_money = (goceng * 5000) + (ceban * 10000)
#
#     if cost == total_money:
#         print("Thank you! There will be no change.")
#     elif cost > total_money:
#         print("Oops, you don't have enough money.")
#     elif total_money > cost:
#         change = total_money - cost
#         print("Thank you! Here is your change:", change)
#
# def pesan():
#     order = input("What would you like? (espresso/latte/cappuccino): ")
#     if order == "report":
#         report()
#     elif order == "off":
#         return False
#     elif order in MENUS:
#         if check_resource(order):
#             check_money(order)
#     else:
#         print("Invalid choice. Please choose from the menu.")
#     return True
#
# available = True
# while available:
#     available = pesan()
#
#
