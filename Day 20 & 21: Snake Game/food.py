from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('brown')
        self.speed('fastest')
        self.refresh()
    def refresh(self):
        foodpos_x=random.randint(a=-275,b=275)
        foodpos_y=random.randint(a=-275,b=275)
        self.goto(foodpos_x,foodpos_y)
