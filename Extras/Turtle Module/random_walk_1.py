import turtle as t
import random

colors=["AliceBlue","bisque3","DarkKhaki","DarkMagenta","DarkSeaGreen","CadetBlue","cornsilk","AntiqueWhite2","DarkOliveGreen","DarkGrey","black","BlanchedAlmond","DarkSlateBlue","DarkSlateGray"]
directions=[0,90,180,270]

michaelangelo=t.Turtle()
michaelangelo.speed("fastest")
t.colormode(255)


def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

michaelangelo.pensize(width=15)
for i in range(0,300):
    michaelangelo.color(random.choice(colors))
    michaelangelo.forward(40)
    michaelangelo.setheading(random.choice(directions))


my_screen=t.Screen()
my_screen.canvheight=3000
my_screen.canvwidth=3000

my_screen.exitonclick()
