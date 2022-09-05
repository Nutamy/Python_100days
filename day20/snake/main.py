from random import randint, choice
import time
from turtle import Turtle, Screen
screen = Screen()
width = 500
height = 400
screen.setup(width=width, height=height)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake game")

snake = []
body_length = 3
position_snake = []


def create_snake(length, x, y):
    x = x
    y = y
    for _ in range(length):
        new_piece = Turtle(shape="square")
        new_piece.penup()
        new_piece.color("white")
        new_piece.setpos(x, y)
        new_pos = new_piece.pos()
        position_snake.append(new_pos)
        snake.append(new_piece)
        x -= 20
    print(position_snake)


def move_body(head, list_pos):
    print(head)
    print(list_pos)
    print(snake[0].heading())
    new_pos_list = list_pos[:-1]
    new_pos_list.insert(0, head)
    for piece in range(1, len(snake)):
        snake[piece].goto(new_pos_list[piece])
    return new_pos_list


def move_head(list_pos):
    snake[0].forward(10)
    new_pos = snake[0].pos()
    return move_body(new_pos, list_pos)



def right(list_pos):
    snake[0].right(90)
    snake[0].forward(10)
    new_pos = snake[0].pos()
    return move_body(new_pos, list_pos)


def left(list_pos):
    snake[0].setheading(90)
    snake[0].forward(10)
    new_pos = snake[0].pos()
    return move_body(new_pos, list_pos)


def clear():
    snake.reset()


create_snake(body_length, 0, 0)


play = True
while play:
    screen.update()
    position_snake = move_head(position_snake)
    time.sleep(0.1)
    screen.onkey(fun=right, key="d")
    screen.onkey(fun=left, key="a")
    screen.onkey(fun=clear, key="c")
    print("000")
#     enemy_exist = True
#     if enemy_exist:
#         enemy = Turtle(shape="circle")
#         plus_or_minus = choice([-1, 1])
#         x = randint(width/2) * plus_or_minus
#         y = randint(height/2) * plus_or_minus
#         enemy.setpos(x, y)

screen.listen()
screen.exitonclick()