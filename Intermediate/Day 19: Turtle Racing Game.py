from turtle import Turtle,Screen
import random
leo= Turtle()
raph=Turtle()
mikey=Turtle()
donnie=Turtle()
screen = Screen()
screen.title('Turtle Racing Game')
finish_line=Turtle()
screen.setup(3000,3000)
screen.listen()

finish_line.speed("fastest")
finish_line.setposition(x=0,y=1000)
finish_line.setposition(x=0,y=-1000)

race_turts=[leo,raph,donnie,mikey]
Turtle_Color={leo: "blue",raph:"red",mikey:"orange",donnie:"purple"}
def random_move(turtle):
    step=random.randint(5,30)
    turtle.forward(step)
h=-100
for i,j in Turtle_Color.items():
    i.shape("turtle")
    i.color(j)
    i.penup()
    i.goto(x=-600,y=h)
    h+=100
bet=screen.textinput(title="Make Your Bet!", prompt="Which Turtle will win the race? (red,blue,orange,purple)")
is_race_on=True
while is_race_on:
    for i in race_turts:
        if i.xcor()>0:
            winning_color=i.pencolor()
            is_race_on=False
            if winning_color==bet:
                print(f"Congratulations! your {winning_color} turtle has won the race!")
            else:
                print(f"Oh No! Looks like you've lost the bet! The {winning_color} turtle has won!")
        random_move(i)


screen.exitonclick()
