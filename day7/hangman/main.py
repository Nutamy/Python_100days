import random

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar\
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk\
lion lizard llama mole monkey moose mouse mule newt otter owl panda\
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep\
skunk sloth snake spider stork swan tiger toad trout turkey turtle\
weasel whale wolf wombat zebra'.split()
while True:
    puzzle = random.choice(words)
    print("_"*len(puzzle), "\n")
    while True:
        try:
            mistakes = int(input("The word is guessed!\nSo, How many mistakes do you think you can afford?\n"))
            break
        except:
            print("Please type a number")
    if mistakes < 5:
        print("Wow! It will be hard! Goog luck!")
    elif mistakes < 10:
        print("I am sure, you'll get it! Good luck!")
    elif mistakes >= 10:
        print("Oh, Are you a little baby? Why do you want to play so easily?")
    #print(puzzle)


    puzzle_list = []
    for letter in puzzle:
        puzzle_list.append(letter)
    guess_list = []
    temp_list = []
    for _ in puzzle_list:
        temp_list.append("_")
    while len(temp_list) != 0 and mistakes > 0:
        guess = input("\nTry to guess a letter\n")
        if guess not in puzzle_list:
            mistakes -= 1
        if guess not in guess_list:
            guess_list.append(guess)
        temp_list = []
        for letter in puzzle_list:
            flag = True
            for guess_letter in guess_list:
                if letter == guess_letter:
                    print(letter, end=" ")
                    flag = False
            if flag:
                temp_list.append("_")
                print("_", end=" ")
        print(f"\nYou can make {mistakes} mistakes")
    if mistakes != 0:
        print("Wow! Congratulation! You win!")
        print("""
    ░░░░░░░░░░░░░░░░░░░░░░█████████
    ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
    ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
    ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
    ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
    ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
    ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
    ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
    ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
    ░░████████████░░░█████████████████
        """)
    else:
        print("""
    ░░░░░░░░░░░█████████████
    ░░░░░░░░░███░███░░░░░░██
    ███░░░░░██░░░░██░██████████
    ████████░░░░░░████░░░░░░░██
    ████░░░░░░░░░░██░░██████████
    ████░░░░░░░░░░░███░░░░░░░░░██
    ████░░░░░░░░░░░██░░██████████
    ████░░░░░░░░░░░░████░░░░░░░░█
    ████░░░░░░░░░░░░░███░░████░░█
    █████████░░░░░░░░░░████░░░░░█
    ███░░░░░██░░░░░░░░░░░░░█████
    ░░░░░░░░░███░░░░░░░██████
    ░░░░░░░░░░░██░░░░░░██
    ░░░░░░░░░░░░███░░░░░██
    ░░░░░░░░░░░░░░██░░░░██
    ░░░░░░░░░░░░░░░███░░░██
    ░░░░░░░░░░░░░░░░░██░░░█
    ░░░░░░░░░░░░░░░░░░█░░░█
    ░░░░░░░░░░░░░░░░░░██░██
    ░░░░░░░░░░░░░░░░░░░███
    """)
        print("You lose")
    again = input("Would you like to try again? Type \"yes\" or \"no\"\n")
    if again == "no":
        break
