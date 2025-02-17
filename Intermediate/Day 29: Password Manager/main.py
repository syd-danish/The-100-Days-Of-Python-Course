from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    symbols = ['=', '+', '-', '#', '$', ':', ';', '*', '%', '[', ']', '!', '{', '}']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    all_symbols = [letters, symbols, numbers]
    password = "".join(random.choice(random.choice(all_symbols)) for i in range(13))
    if password!="":
        password_entry.delete(0,END)
    password_entry.insert(string=password,index=0)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_function():
    if website_entry.get()=="" or email_username_entry.get()=="":
        messagebox.showerror("Error","Your Email/Username or Website field has been left empty!\n"
       "Please fill both fields to continue")
    elif password_entry.get()=="":
        messagebox.showerror("Error","The Password field is left empty!\n Please Enter it to continue")
    else:

        with open("./data.txt",'w') as data_file:
            data_string=f"{website_entry.get()} | {email_username_entry.get()} | {password_entry.get()}"
            data_file.write(data_string)
        website_entry.delete(0,END)
        email_username_entry.delete(0,END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("PassWord Manager")
website_head=Label(text="Website:")
email_username_head=Label(text="Email/Username:")
password_head=Label(text="Password:")
website_entry=Entry(width=35)
email_username_entry=Entry(width=35)
password_entry=Entry(width=18)
logo=PhotoImage(file="./logo.png")
logo_canvas=Canvas(width=150,height=180)
logo_canvas.create_image(95,105,image=logo)
generate_password_button=Button(text="Generate Password",command=password_generator)
add_button=Button(text="Add",width=30,command=add_button_function)
logo_canvas.grid(row=0,column=1,pady=20,padx=10,sticky="w")
website_head.grid(row=1)
email_username_head.grid(row=2)
password_head.grid(row=3)
website_entry.grid(column=1,row=1,padx=10)
email_username_entry.grid(column=1,row=2,padx=10)
generate_password_button.grid(column=1,row=3,sticky="e",padx=10)
password_entry.grid(column=1,row=3,sticky="w",padx=10) #sticky is used for alignment, "w" is for west
add_button.grid(row=4,column=1,pady=15)
window.minsize(width=400,height=500)
window.mainloop()
