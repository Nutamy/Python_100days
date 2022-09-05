import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

cars = []

screen.listen()
screen.onkey(player.step, "Up")

speed = 5
traffic_jum = 0
frequency = 6
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Start traffic
    traffic_jum += 1
    if traffic_jum % frequency == 0:
        car = CarManager()
        cars.append(car)

    # Detect collision to cars
    for auto in cars:
        if auto.distance(player) < 30 and abs(auto.ycor() - player.ycor()) <= 20:
            scoreboard.game_over()
            player.foot = 0
            time.sleep(3)
            game_is_on = False
            for one in cars:
                one.drive_speed = 0
        else:
            auto.drive(speed)

    # Detect finish
    if player.ycor() > 300:
        player.start()
        scoreboard.level_up()
        speed += 3
        if scoreboard.level % 3 == 0:
            frequency -= 1
        for auto in cars:
            auto.new_level()



