import colorgram as cg
import random
import turtle as t

t.colormode(255)

raphael=t.Turtle()
rgb_array=[]
colors=cg.extract('img.png',100)
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    if r>225 and g>225 and b>225:
        continue
    new_color= (r,g,b)
    rgb_array.append(new_color)

raphael.hideturtle()
raphael.penup()
raphael.setheading(225)
raphael.forward(300)
raphael.setheading(0)
def reset():
    raphael.speed("fastest")
    raphael.left(90)
    raphael.forward(50)
    raphael.left(90)
    raphael.forward(500)
    raphael.left(180)
    raphael.speed("normal")
def ten_pattern():
    for i in range(10):
        raphael.dot(20, random.choice(rgb_array))
        raphael.forward(50)
for i in range(10):
    ten_pattern()
    reset()



screen=t.Screen()
screen.exitonclick()
