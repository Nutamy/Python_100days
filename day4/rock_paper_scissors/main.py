import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors game!")
print("What do you chose? Type \"rock\",\"paper\" or \"scissors\"")
choose = input()
print("Your choice:")
if choose == "rock":
    print(rock)
elif choose == "paper":
    print(paper)
elif choose == "scissors":
    print(scissors)

computer_choose = random.choice(["rock", "paper", "scissors"])
print(f"Computer choice is {computer_choose}, so")
if computer_choose == "rock":
    print(rock)
elif computer_choose == "paper":
    print(paper)
elif computer_choose == "scissors":
    print(scissors)

if choose != computer_choose:
    if choose == "rock" and computer_choose == "scissors" or\
        choose == "paper" and computer_choose == "rock" or\
        choose == "scissors" and computer_choose == "paper":
        print("You win!")
    else:
        print("You lose")
else:
    print("Oooops!")

