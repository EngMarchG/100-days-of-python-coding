from tkinter import *
from matplotlib.pyplot import text

from sqlalchemy import column

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Convert Miles to Kilometer")

miles_input = Entry()
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grind(column=1, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grind(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grind(column=1, row=1)

kilometer_label = Label(text="ka")
kilometer_label.grind(column=2, row=1)

converting_button = Label(text="Calculate")
converting_button.grind(column=1, row=2)
