from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("Day 30\data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("Day 30\data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("Day 30\data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            messagebox.showinfo(title="Success", message=f"Your account at {website} has been added to the data store.")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pass():
    website = website_entry.get()
    try:
        with open("Day 30\data.json") as data_file:
            data = json.load(data_file)
    
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Beep boop baap \nNo Data File Found.")
    
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else: 
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 75, pady = 50)

canvas = Canvas(height=300, width=300)
logo_pic = PhotoImage(file="Day 30\download.png")
canvas.create_image(120, 120, image = logo_pic)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website", font=(FONT_NAME, 15,"normal"))
website.grid(column=0, row=1)
username = Label(text="Email/Username", font=(FONT_NAME, 15, "normal"))
username.grid(column=0, row=2)
user_pass = Label(text="Password", font=(FONT_NAME, 15, "normal"))
user_pass.grid(column=0, row=3)

#Buttons
add_button = Button(text="Add", width=48, command=save)
add_button.grid(column=1, row=4, columnspan=2)
gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3, sticky=W)
search_button = Button(text="Search", command=find_pass)
search_button.grid(column=2, row=1, sticky=W)

#Entries
website_entry = Entry(width=29)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=48)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "kaiz@gmail.com")
password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

window.mainloop()


