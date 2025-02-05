from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.right(random.randint(0,360))
        self.penup()
        self.x_move=2
        self.y_move=2
        self.movement=0.01
    def move(self):
        new_x= self.xcor() + self.x_move
        new_y= self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def change_y_angle(self):
        self.y_move*=-1
    def change_x_angle(self):
        self.x_move*=-1
    def ball_speed_increase(self):
        self.movement*=0.8
    def ball_speed_restore(self):
        self.movement=0.01
