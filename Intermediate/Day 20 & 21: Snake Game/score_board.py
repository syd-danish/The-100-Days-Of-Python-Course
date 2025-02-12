from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center", font=('Arial',24,'normal'))
        self.hideturtle()
    def game_score(self):
        self.score+=1
        self.clear()
        self.score_update()
    def score_update(self):
        self.write(f"Score: {self.score}", align="center", font=('Arial', 24, 'normal'))
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!",align='center',font=('Arial',24,'normal'))
