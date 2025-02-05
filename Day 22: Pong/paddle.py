from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,og_x,og_y):
        super().__init__()
        self.og_x=og_x
        self.og_y=og_y
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(x = og_x,y = og_y)
    def up(self):
        new_y=self.ycor() + 30
        self.goto(self.xcor(), new_y)
    def down(self):
        new_y=self.ycor() - 30
        self.goto(self.xcor(),new_y)
    def reset(self):
        self.goto(self.og_x,self.og_y)
