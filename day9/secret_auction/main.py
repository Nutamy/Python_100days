import random

while True:
    treasure_list = ["vase", "plate", "bowl", "crown", "chain", "earrings", "bracelet", "diadem", "service"]
    adjective_list = ["gold", "silver", "bronze", "pewter", "iron", "antique", "rare", "magnificent"]
    print("\nWelcome to the Secret Auction!")
    lot = random.choice(adjective_list).capitalize() + " " + random.choice(treasure_list)
    print(f"Today at our auction a very valuable lot is played: \n{lot}")

    auction = {}
    while True:
        print(f"The lot is the {lot}")
        name = input("Enter your name to place a bet: ")
        bet = int(input(f"What is your bet?: "))
        last = input("Type \"last\" if you are the last in the line\nOtherwise press Enter\n")
        auction[name] = bet
        if last == "last":
            break
    win_name = ''
    win_bet = 0
    for person in auction:
        if auction[person] > win_bet:
            win_bet = auction[person]
            win_name = person

    print(f"Congratulations! {win_name} win! The bet was {win_bet}\nHere is your {lot}\n")

    again = input("Type \"exit\" to stop\nPress Enter to look the next lot\n")
    if again == "exit":
        break