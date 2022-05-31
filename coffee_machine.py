from main import MENU
from main import resources


order = input("What would you like? (espresso/latte/cappuccino): ")
water = int(resources["water"])
milk = int(resources["milk"])
coffee = int(resources["coffee"])
money = float(resources["money"])



def determine_user_input(user_input):
    if user_input == "off":
        turn_off()
    elif user_input == "report":
        print_report()
    else:
        make_drink(user_input)


def turn_off():
    return


def print_report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


def resource_check(drink):
    for ingredients in MENU[drink]["ingredients"]:
        for

def make_drink(order):
    if order == "espresso":
    elif order == "latte":
    elif order =="cappuccino":




determine_user_input(order)