
# ---------------------------- MODULES ------------------------------- #

from tkinter import *
import time
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
TIMER=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer_button():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_in_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps % 8 == 0:
        timer_title.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_title.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_in_sec)
        timer_title.config(text="WORK-TIME", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global TIMER
        TIMER=window.after(1000, count_down,count-1)
    else:
        start_timer()
        mark=""
        for i in range(math.floor(reps/2)):
            mark+="✔"
            check_mark.config(text=mark)





# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro App")
timer_title=Label(text="Timer",font=(FONT_NAME,35), bg=YELLOW, fg=GREEN)
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="./tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130, text=f"00:00", font=(FONT_NAME,35,"bold"))
start_button=Button(text="start", bg=YELLOW,highlightbackground=YELLOW,command=start_timer)
reset_button=Button(text="reset", bg=YELLOW,highlightbackground=YELLOW,command=reset_timer_button)
check_mark=Label(text="",bg=YELLOW,fg=GREEN)
check_mark.grid(row=3, column=1)
timer_title.grid(row=0,column=1)
canvas.grid(row=1,column=1)
start_button.grid(row=2,column=0)
reset_button.grid(row=2,column=2)



window.mainloop()
