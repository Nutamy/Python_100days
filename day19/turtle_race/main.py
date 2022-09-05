from turtle import Turtle, Screen
from random import randint
play = True
screen = Screen()

racing_distance = 700
screen.setup(width=racing_distance, height=400)
while play:
    screen.bgcolor("PaleGreen")
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color?: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    competitors = {}
    x = -1*(racing_distance/2-20)
    y = -100
    for competitor in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        competitors[colors[competitor]] = new_turtle
        new_turtle.penup()
        new_turtle.color(colors[competitor])
        new_turtle.goto(x, y + competitor * 40)

    winner_color = ""
    winner_position = -1000
    while winner_position < racing_distance/2-20:
        step_competitors = {}

        for competitor in competitors.keys():
            turtle = competitors[competitor]
            turtle.forward(randint(0, 10))
            step_competitors[competitor] = turtle.xcor()
        for turtle in step_competitors.keys():
            if step_competitors[turtle] > winner_position:
                winner_position = step_competitors[turtle]
                winner_color = turtle
    text = ""
    if user_bet == winner_color:
        text = f"You win! The {winner_color} is the fastest!"
        print(text)
    else:
        text = f"Oh! NO! The {winner_color} is the faster than yours!"
        print(text)
    next = screen.textinput(title=text, prompt="Type exit or next to start a new race: ")
    if next == "exit":
        play = False
    else:
        screen.clear()
screen.exitonclick()
