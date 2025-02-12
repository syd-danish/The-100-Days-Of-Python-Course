from turtle import Turtle

class Snake:
    def __init__(self):
        self.segment_1 = Turtle()
        self.segment_2 = Turtle()
        self.segment_3 = Turtle()
        self.Turt_Array = [self.segment_1, self.segment_2, self.segment_3]
        h=0
        for i in self.Turt_Array:
            i.goto(x=h,y=0)
            h-=20
        self.create_snake()
    def create_snake(self):
        for i in self.Turt_Array:
            i.shape('square')
            i.speed('fastest')
            i.penup()
            if i == self.segment_1:
                i.color('red')
            else:
                i.color('white')
    def increase_length(self):
        new_turt=Turtle()
        self.Turt_Array.append(new_turt)
        self.create_snake()
    def move(self):
        for seg in range(len(self.Turt_Array) - 1, 0, -1):
            new_x = self.Turt_Array[seg - 1].xcor()
            new_y = self.Turt_Array[seg - 1].ycor()
            self.Turt_Array[seg].goto(x=new_x, y=new_y)
        self.Turt_Array[0].forward(20)
    def up(self):
        if self.segment_1.heading()!=270:
           self.segment_1.setheading(90)
    def down(self):
        if self.segment_1.heading()!=90:
            self.segment_1.setheading(270)
    def right(self):
        if self.segment_1.heading() != 180:
            self.segment_1.setheading(0)
    def left(self):
        if self.segment_1.heading() != 0:
            self.segment_1.setheading(180)
