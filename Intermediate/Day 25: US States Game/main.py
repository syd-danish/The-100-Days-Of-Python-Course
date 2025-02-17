import pandas as pd
import turtle

screen=turtle.Screen()
screen.title("U.S States Game")

screen.addshape("/Users/yasindanish13/PycharmProjects/100DaysOfCode/Day 25: CSV and The Pandas Library/day-25-us-states-game-start/blank_states_img.gif")
turtle.shape("/Users/yasindanish13/PycharmProjects/100DaysOfCode/Day 25: CSV and The Pandas Library/day-25-us-states-game-start/blank_states_img.gif")


state_turt=turtle.Turtle()
state_turt.penup()
state_turt.hideturtle()
state_turt.speed('fastest')

all_state_file=pd.read_csv("./50_states.csv")

state_list=all_state_file.state.to_list()


guess=0
while True:
    qna=screen.textinput(title=f"Your Current Score: {guess}/50", prompt="Name A State")
    if guess==50:
        state_turt.write(f"Congratulations! You have guessed all 50 states!",align="center",
                         font=("Arial", 50, "normal"))
        break
    elif qna=="Exit":
        screen.tracer(0)
        for i in all_state_file["state"]:
            state_data = all_state_file[all_state_file.state == i]
            x, y = state_data.x.item(), state_data.y.item()
            state_turt.goto(x, y)
            state_turt.write(i, align="center", font=("Arial", 12, "normal"))
        screen.update()
        state_turt.color("blue")
        state_turt.goto(0,0)
        state_turt.write(f"GAME-OVER!\n", align="center", font=("Courier", 40, "normal") )
        state_turt.goto(0, -40)
        state_turt.write(f"YOUR FINAL SCORE IS {guess}/50\n", align="center", font=("Courier", 40, "normal"))
        break
    for i in state_list:
        if qna.upper().lower().title()==i:
            state_list.remove(i)
            guess+=1
            state_data=all_state_file[all_state_file.state==qna.title()]
            x, y = state_data.x.item(), state_data.y.item()
            state_turt.goto(x, y)
            state_turt.write(qna.title(), align="center", font=("Arial", 12, "normal"))

state_frame=pd.Series(state_list)
state_frame.to_csv("States you missed.csv")




turtle.mainloop()
