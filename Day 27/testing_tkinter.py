import tkinter
from turtle import width

window = tkinter.Tk()
window.minsize(500,300)
window.maxsize(900,600)

my_label = tkinter.Label(text="I am label", font=("Times new roman", 24,"normal"))
my_label.pack()

my_label["text"] = "You expected I am label but it is I dio!"


def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text = "Click me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=50)
input.pack()


window.mainloop()