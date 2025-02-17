from tkinter import *
window=Tk()
window.title("Miles to Km Converter")
window.minsize(width=350,height=200)
window.config(padx=20,pady=10)
label1=Label(text="Miles",font=("Arial",25))
label2=Label(text="is equal to", font=("Arial",25))
label3=Label(text="Km", font=("Arial",25))
def calculate():
    int_op=round(float(inp.get())*1.6,2)
    op.config(text=f"{int_op}")
    op.grid(row=4,column=2)
button=Button(text="Convert to KMs",command=calculate)
inp=Entry(width=10)
op=Label(text="",font=("Arial",25))
label1.grid(row=1,column=4)
label2.grid(row=4,column=0)
label3.grid(row=4,column=4)
inp.grid(row=1,column=2)
op.grid(row=4,column=2)
button.grid(column=2,row=6)








window.mainloop()
