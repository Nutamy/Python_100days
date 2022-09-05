import turtle
from turtle import Turtle, Screen
from random import choice, randint
colors = ["DeepSkyBlue", "MediumSpringGreen", "Moccasin", "LightCoral", "Violet", "LightSlateGray", "PaleTurquoise"]
tim = Turtle()
tim.pensize(1)
turtle.colormode(255)
tim.speed("fastest")
angels = [0, 90, 180, 270]


def random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red, green, blue)


def circle_move():
    tim.pencolor(random_color())
    tim.right(5)
    tim.circle(100)


for _ in range(1, 360, 5):
    circle_move()


#
#
# def move():
#     tim.pencolor(random_color())
#     angel = choice(angels)
#     tim.setheading(angel)
#     tim.forward(30)
#
#
# for _ in range(200):
#     move()

# def draw(n_side):
#     angle = 360/n_side
#     tim.color(colors[n_side-3])
#     for x in range(n_side):
#         tim.forward(30)
#         tim.right(angle)
#
# for sides in range(3, 11):
#     draw(sides)


















screen = Screen()

screen.exitonclick()