import tkinter

window = tkinter.Tk()
window.minsize(500,300)
window.maxsize(900,600)

my_label = tkinter.Label(text="I am label", font=("Times new roman", 24,"normal"))
my_label.pack()







window.mainloop()