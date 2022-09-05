import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
states = data.state.to_list()
print(int(data[data.state == "Alaska"].x))
img = r"blank_states_img.gif"
screen = turtle.Screen()
screen.bgpic(img)
screen.title("U.S States Game")
screen.setup(width=740, height=510)

game = turtle.Turtle()
game.penup()
game.color("black")
game.hideturtle()


guessed_states = []

while len(guessed_states) < 50:
    text = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="Enter state")
    answer = text.title()
    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        x = int(data[data.state == answer].x)
        y = int(data[data.state == answer].y)
        game.goto(x, y)
        game.write(f"{answer}", align="center", font=("Arial", 8,  "normal"))
    elif answer == "Exit":
        states_to_learn = [state+", " for state in states if state not in guessed_states]
        file = open("states to learn.csv", "w")
        file.writelines(states_to_learn)
        file.close()
        break

