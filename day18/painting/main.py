import turtle
import colorgram
from random import choice
from turtle import Turtle, Screen
turtle.colormode(255)
# Extract 10 colors from an image.
colors = colorgram.extract('hist.png', 10)
extracted_colors = []
for color in colors:
    rgb_color = color.rgb
    extracted_colors.append((rgb_color.r, rgb_color.g, rgb_color.b))
print(extracted_colors)

# colors =[(252, 252, 250), (250, 252, 254), (237, 250, 248), (63, 103, 144), (249, 237, 245), (117, 80, 87), (136, 165, 126), (186, 213, 127), (237, 124, 139), (46, 107, 81)]
colors = extracted_colors
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")
x = -430
y = -350
tim.setpos(x, y)
for y_step in range(10):
    for x_step in range(10):
        tim.dot(20, choice(colors))
        x += 80
        tim.setpos(x, y)
    y += 80
    x = -430
    tim.setpos(x, y)
# tim.dot(20, choice(colors))






screen = Screen()
screen.exitonclick()

