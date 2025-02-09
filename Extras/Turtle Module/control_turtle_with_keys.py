from turtle import Turtle,Screen
import random
raph=Turtle()
screen=Screen()
screen.listen()
def forward_move():
    raph.forward(100)
def right_move():
    raph.right(30)
def left_move():
    raph.left(30)
def backward_move():
    raph.backward(100)
def clear():
    raph.clear()
    raph.penup()
    raph.home()
    raph.pendown()


screen.onkey(key='W', fun=forward_move)
screen.onkey(key='A', fun=left_move)
screen.onkey(key='S', fun=backward_move)
screen.onkey(key='D', fun=right_move)
screen.onkey(key='C', fun=clear)



screen.exitonclick()
