from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
WIDTH = 800
HEIGHT = 600
BORDER = HEIGHT/2 - 30

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("PIN PONG")
screen.tracer(0)
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision to the wall
    # if (ball.ycor() > BORDER and ball.xcor() > 0) or \
    #         (ball.ycor() < -BORDER and ball.xcor() < 0):
    #     new_direction = ball.heading() + 270
    #     ball.setheading(new_direction)
    # elif (ball.ycor() < -BORDER and ball.xcor() > 0) or \
    #         (ball.ycor() > BORDER and ball.xcor() < 0):
    #     new_direction = ball.heading() + 90
    #     ball.setheading(new_direction)
    if ball.ycor() > BORDER or ball.ycor() < -BORDER:
        ball.bounce_y()

    if ball.xcor() > WIDTH/2:
        ball.bounce_x()
        # ball.refresh()

    # Detect collision to the right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or \
        (ball.distance(l_paddle) < 50 and ball.xcor() > -370):
            ball.bounce_x()


print(1)
screen.exitonclick()
