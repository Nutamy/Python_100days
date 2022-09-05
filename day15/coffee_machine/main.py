from art import logo
print(logo)

menu = {
    "Espresso": {"water": 50, "coffee": 18, "price": 1.5},
    "Latte": {"water": 150, "coffee": 24, "milk": 150, "price": 2.5},
    "Cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 3}
}

coffee_machine = {"water": 300,
                  "milk": 200,
                  "coffee": 100,
                  "money": 0}
coffee_machine_work = True
while coffee_machine_work:
    money_taken = 0
    money_enough = False
    resource_enough = True
    choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
    if choice == "report":
        for key in coffee_machine.keys():
            if key == "money":
                print(f"{key.capitalize()}: ${coffee_machine[key]}")
            elif key == "coffee":
                print(f"{key.capitalize()}: {coffee_machine[key]}g")
            else:
                print(f"{key.capitalize()}: {coffee_machine[key]}ml")
    elif choice == "off":
        coffee_machine_work = False
    else:
        if resource_enough:
            for key in menu[choice].keys():
                if key != "price":
                    if coffee_machine[key] >= menu[choice][key]:
                        coffee_machine[key] -= menu[choice][key]
                    else:
                        print(f"Sorry there is not enough {key}")
                        resource_enough = False
                        break
                else:
                    coffee_machine["money"] += menu[choice][key]
        while not money_enough and resource_enough:
            print("Please insert coins.")
            quarter = int(input("How many quarters?: ")) * 0.25
            dime = int(input("How many dimes?: ")) * 0.1
            nickel = int(input("How many nickles?: ")) * 0.05
            penny = int(input("How many pennies?: ")) * 0.01
            money_given = quarter + dime + nickel + penny
            money_taken += money_given
            change = money_taken - menu[choice]["price"]
            print(f"Here is ${change:.2f} in change.")
            print(f"Here is your {choice} Enjoy!")
            if menu[choice]["price"] > money_taken:
                print("There are not enough money")
            else:
                money_enough = True

