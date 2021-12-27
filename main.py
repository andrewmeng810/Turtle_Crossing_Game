import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create tutle player
player = Player()

screen.listen()
screen.onkey(player.move, 'Up')

# Create cars
cars = CarManager()

# Create scoreboard

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_car()  # to crate the new car
    cars.move_car()  # get the cars moving

    # Detect if player collides with a car
    for car in cars.car_list:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.is_reach_finish_line():
        player.reset_position()
        cars.level_up()  # increase car move speed
        scoreboard.increase_level()  # update the scoreboard

    screen.update()

screen.exitonclick()
