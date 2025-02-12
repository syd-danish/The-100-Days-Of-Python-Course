import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player_turtle=Player()
car_load=CarManager()
level=Scoreboard()
level.generate_new_board()
screen.onkey(fun=player_turtle.go_up,key='w')
screen.onkey(fun=player_turtle.go_back, key='s')
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_load.create_cars()
    car_load.move()
    for cars in car_load.all_cars:
        if cars.distance(player_turtle)<20:
            car_load.collision()
            game_is_on=False

    if player_turtle.finish_line():
        player_turtle.go_to_start()
        level.increase_level()
        car_load.increase_speed()

screen.exitonclick()
