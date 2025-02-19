
from tkinter import *
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT=("Arial", 40 ,"italic")
WORD_FONT=("Arial",60,"bold")


language_file=pd.read_csv("./data/french_words.csv")
language_dict=language_file.to_dict(orient="records")
def flashcard():
    def empty():
        pass
    def correct_button_function():
        del language_dict[word_index]
        flashcard()
    def wrong_button_function():
        global wrong_answers_dataframe
        new_entry = pd.DataFrame([{
            "French": language_dict[word_index]["French"],
            "English": language_dict[word_index]["English"]
        }])
        wrong_answers_dataframe = pd.concat([wrong_answers_dataframe, new_entry], ignore_index=True)
        wrong_answers_dataframe.to_csv("words_you_missed.csv",index=False)
        flashcard()
    def english_reveal():
        canvas.itemconfig(card_image, image=back_card)
        canvas.itemconfig(language_word, text="English",fill="white")
        canvas.itemconfig(flash_card_word, text=f"{language_dict[word_index]["English"]}",fill="white")
        correct_button.config(command=correct_button_function)
        wrong_button.config(command=wrong_button_function)

    word_index=random.randint(0,len(language_dict)-1)
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(language_word, text="French",fill="black")
    canvas.itemconfig(flash_card_word, text=f"{language_dict[word_index]["French"]}",fill="black")
    correct_button.config(command=empty)
    wrong_button.config(command=empty)
    window.after(5000,english_reveal)



window=Tk()
window.title("Flashcard Capstone Project")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
front_card=PhotoImage(file="./images/card_front.png")
back_card=PhotoImage(file="./images/card_back.png")
correct_card=PhotoImage(file="./images/right.png")
wrong_card=PhotoImage(file="./images/wrong.png")
correct_button=Button(image=correct_card,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,)
wrong_button=Button(image=wrong_card,highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
canvas=Canvas(width=800,height=526,highlightthickness=0,bd=0,highlightbackground=BACKGROUND_COLOR)
card_image=canvas.create_image(400,263,image=front_card)
language_word = canvas.create_text(400, 150, text=f"French", font=LANGUAGE_FONT, fill="black")
flash_card_word = canvas.create_text(400, 263, text=f"", font=WORD_FONT,fill="black")
canvas.grid(columnspan=2)
correct_button.grid(row=1,column=1)
wrong_button.grid(row=1)
wrong_answers={}
wrong_answers_dataframe = pd.DataFrame(wrong_answers)
wrong_answers_dataframe.to_csv("words_you_missed.csv",index=False)
flashcard()
window.mainloop()

