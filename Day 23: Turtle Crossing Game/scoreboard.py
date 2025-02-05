from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=-230,y=270)
        self.level=1
        self.hideturtle()
    def generate_new_board(self):
        self.write(f'Level : {self.level}', align='center',font=FONT)
    def increase_level(self):
        self.level+=1
        self.clear()
        self.generate_new_board()
