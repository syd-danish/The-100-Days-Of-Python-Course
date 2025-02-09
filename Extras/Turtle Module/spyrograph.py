import turtle as t
import random

tom=t.Turtle()

t.colormode(255)
tom.speed("fastest")

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color


def spyrosaurus(angular_gap,direction):
    no_of_rotations=360/angular_gap
    for i in range(0, round(no_of_rotations)):
        tom.color(random_color())
        tom.circle(100)
        if direction=="r":
            tom.right(angular_gap)
        if direction=="l":
            tom.left(angular_gap)


spyrosaurus(3,"l")


my_screen=t.Screen()
my_screen.exitonclick()
