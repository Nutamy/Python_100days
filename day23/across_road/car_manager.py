from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.goto(randint(300, 301), randint(-200, 200))

    def drive(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())

    def new_level(self):
        if self.xcor() < 300:
            self.reset()
            self.penup()
            self.goto(-400, 0)



