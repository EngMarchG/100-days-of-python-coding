from tkinter import *
from turtle import width

from pyparsing import col

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

window = Tk()
window.minsize(500,300)
window.maxsize(900,600)

my_label = Label(text="I am label", font=("Times new roman", 24,"normal"))
my_label.config(text="New text")
my_label.grid(column=0, row=0)

button_new = Button(text="I am new")
button_new.grid(column=0, row=3)

button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)

input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()