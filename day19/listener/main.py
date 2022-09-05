from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)
def back_move():
    tim.backward(10)
def right():
    tim.right(10)
def left():
    tim.left(10)
def clear():
    tim.reset()


screen = Screen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=back_move, key="s")
screen.onkey(fun=right, key="d")
screen.onkey(fun=left, key="a")
screen.onkey(fun=clear, key="c")
screen.listen()
screen.exitonclick()
