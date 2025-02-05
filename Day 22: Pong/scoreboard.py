from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.l_score=0
        self.r_score=0
    def create_scoreboard(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score,align='center',font=('Courier',80,'normal'))
        self.goto(x=100, y=200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))
    def point_for_r(self):
        self.r_score+=1
        self.clear()
        self.create_scoreboard()
    def point_for_l(self):
        self.l_score+=1
        self.clear()
        self.create_scoreboard()
