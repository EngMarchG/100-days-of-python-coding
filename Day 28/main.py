
# ---------------------------- CONSTANTS ------------------------------- #
from tkinter import Canvas, PhotoImage, Label, Button
from tkinter.tix import Tk

from matplotlib.pyplot import text


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reseter():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_marks.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter(long_break_sec)
        my_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        counter(short_break_sec)
        my_label.config(text="Break", fg = PINK)
    else:
        counter(work_sec)
        my_label.config(text="Work", fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, counter, count - 1)
    else:
        start_timer()
        marks = ""
        work_session =  reps//2
        for any in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Technique application")
window.config(padx=100, pady=50, bg=GREEN)


canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0.1)
tomato_img = PhotoImage(file="100 days of python\\Day 28\\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


my_label = Label(text="Timer", font=(FONT_NAME, 50,"normal"), bg=GREEN, fg=YELLOW)
# my_label.config(text="New text")
my_label.grid(column=1, row=0)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", highlightthickness=0, command=reseter)
button_reset.grid(column=3, row=2)

check_marks = Label(text="", fg=YELLOW, bg=GREEN)
check_marks.grid(column=1, row=3)


window.mainloop()