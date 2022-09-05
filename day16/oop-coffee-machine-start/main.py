from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
items = menu.get_items()
while True:
    order = input(f"What would you like? {items}: ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        resource_enough = coffee_maker.is_resource_sufficient(drink)
        if resource_enough:
            paid = False
            while not paid:
                paid = money_machine.make_payment(drink.cost)
            if paid:
                coffee_maker.make_coffee(drink)

