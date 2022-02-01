import turtle as t
import random

tim = t.Turtle()
t.colormode(255)    #changes turtle to accept rgb

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomcol = (r, g, b)
    return randomcol

#colors = ["DarkOrchid", "Crimson", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "SlateGray"]
angles = [0, 90, 180, 270]
tim.speed("fastest")
tim.pensize(10)

for ka in range(300):
    #tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30)
    tim.right(random.choice(angles))