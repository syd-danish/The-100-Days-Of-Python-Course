from turtle import Turtle,Screen



leonardo=Turtle()

#draw a square
for i in range(0,4):
    for j in range(0,5):
        leonardo.forward(20)
        leonardo.penup()
        leonardo.forward(20)
        leonardo.pendown()
    leonardo.right(90)

#draw a triangle
for i in range(0,3):
    for j in range(0,5):
        leonardo.forward(20)
        leonardo.penup()
        leonardo.forward(20)
        leonardo.pendown()
    leonardo.left(120)

#draw a hexagon
for i in range(0,6):
    for j in range(0,10):
        leonardo.back(10)
        leonardo.penup()
        leonardo.back(10)
        leonardo.pendown()

    leonardo.right(60)




screen= Screen()
screen.exitonclick()
