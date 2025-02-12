from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_cars(self):
        r=random.randint(0,3)
        if r==0:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            car_y_position = random.randint(-250, 250)
            new_car.goto(300, car_y_position)
            self.all_cars.append(new_car)
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def increase_speed(self):
        self.car_speed+=STARTING_MOVE_DISTANCE
        self.move()
    def collision(self):
        game_over=Turtle()
        game_over.hideturtle()
        game_over.write('GAME OVER!', align='center', font= ("Courier", 100, "normal") )
