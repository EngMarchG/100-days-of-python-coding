from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.setheading(0)
    tim.forward(10)
def move_upwards():
    tim.setheading(90)
    tim.forward(10)
def move_downwards():
    tim.setheading(270)
    tim.forward(10)
def move_backwards():
    tim.setheading(180)
    tim.forward(10)
def clearo():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="Up", fun=move_upwards)
screen.onkey(key="Down", fun=move_downwards)
screen.onkey(key="Left", fun=move_backwards)
screen.onkey(key="Right", fun=move_forward)
screen.onkey(key="c", fun=clearo)
screen.exitonclick()