from turtle import Turtle, Screen
import random

winning_color = ""
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt= "Pick the turtle you think would win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for l in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[l])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_position[l])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)


screen.exitonclick()