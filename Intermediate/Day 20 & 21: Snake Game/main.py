from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time
screen=Screen()
screen.title("Snake Game")
screen.listen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
snake=Snake()
foo=Food()
score=ScoreBoard()
screen.tracer(0)
screen.onkey(fun=snake.up,key='w')
screen.onkey(fun=snake.down,key='s')
screen.onkey(fun=snake.right,key='d')
screen.onkey(fun=snake.left,key='a')
game_mode=True
while game_mode:
    screen.update()
    time.sleep(0.075)
    snake.move()
    if snake.segment_1.distance(foo)<15:
        foo.refresh()
        score.game_score()
        snake.increase_length()
    for seg in (1,len(snake.Turt_Array)-1):
        if snake.segment_1.distance(snake.Turt_Array[seg])<=10:
            score.game_over()
            game_mode=False
    if snake.segment_1.xcor()>295 or snake.segment_1.xcor()<-295 or snake.segment_1.ycor()>295 or snake.segment_1.ycor()<-295:
        score.game_over()
        game_mode=False

screen.exitonclick()
