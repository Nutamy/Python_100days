from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("slow")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # self.refresh()
        self.x_move = 10
        self.y_move = 10
        self.setheading(120)

    def refresh(self):
        self.goto(0, 0)
        to_angle = randint(0, 80)
        self.setheading(to_angle)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # self.forward(20)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1