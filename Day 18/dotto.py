import colorgram as cg
import turtle as t
import random

tim = t.Turtle()
#Note that the path is relative!
colors = cg.extract("100 days of python\\Day 18\\images.jpg", 84)
rgb = []
t.colormode(255)
tim.penup()
tim.hideturtle()

#initial positioning
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

def timmy_reset_line(n, space):
    """Puts the turtle on to the next column"""
    tim.backward(dot_spacing*n)
    tim.left(90)
    tim.forward(dot_spacing)
    tim.right(90)

for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    color_pallet = (r, g, b)
    rgb.append(color_pallet)


i = 0
n = 6   #can be input for the dots in the row
dot_size = 30
dot_spacing = dot_size*2.5

tim.dot(dot_size, rgb[random.randint(0,33)])

#given rgb length which is 34 instead of 84 since module cant take it & tim.dot was according to index which is why i kept while as len of rgb
while i <= len(rgb):
    tim.dot(dot_size, rgb[random.randint(0,33)])
    tim.forward(dot_spacing)
    i += 1
    if i % n == 0:
        timmy_reset_line(n, dot_spacing)


screen = t.Screen()
screen.exitonclick()