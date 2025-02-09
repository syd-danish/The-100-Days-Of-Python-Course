donatello.pensize(width=15)
for i in range(0,300):
    donatello.color(random_color())
    donatello.forward(40)
    donatello.setheading(random.choice(directions))




my_screen=t.Screen()
my_screen.canvheight=3000
my_screen.canvwidth=3000

my_screen.exitonclick()
