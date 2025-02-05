from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)
r_paddle=Paddle(og_x=350,og_y=0)
l_paddle=Paddle(og_x=-350, og_y=0)
ball=Ball()
scoreboard=Scoreboard()
scoreboard.create_scoreboard()
screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")
game_run=True
while game_run:
    time.sleep(ball.movement)
    screen.update()
    ball.move()
    if ball.ycor()>290 or ball.ycor()<-280:
        ball.change_y_angle()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.change_x_angle()
        ball.ball_speed_increase()
    if ball.xcor()>410 or ball.xcor()<-410:
        ball.ball_speed_restore()
        if ball.xcor()>410:
            scoreboard.point_for_l()
            r_paddle.reset()
        elif ball.xcor()<410:
            scoreboard.point_for_r()
            l_paddle.reset()
        time.sleep(1)
        ball.goto(0,0)



screen.exitonclick()
