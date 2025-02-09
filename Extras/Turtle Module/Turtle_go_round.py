import random
from turtle import Turtle, Screen


raphael=Turtle()
raphael.color("chocolate4")
colors=["AliceBlue","bisque3","DarkKhaki","DarkMagenta","DarkSeaGreen","CadetBlue","cornsilk","AntiqueWhite2","DarkOliveGreen","DarkGrey","black","BlanchedAlmond","DarkSlateBlue","DarkSlateGray"]


n=3
angle=120
while n<=10:
    for i in range(0,n):
        raphael.forward(100)
        raphael.right(angle)
    n+=1
    angle=360/n
    raphael.color(random.choice(colors))





screen = Screen()
screen.exitonclick()
