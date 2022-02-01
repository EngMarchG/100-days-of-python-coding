import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")
tim.pensize(3)
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randomcol = (r, g, b)
    return randomcol

# def draw_spirograph(gap):
#     for _ in range(int(360 / gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + gap)

# draw_spirograph(5)


#Below is a bad method since can't control gap range goes randomly
#But it works 

gap = range(361)
for i in gap:
    print(tim.heading())
    tim.color(random_color())
    tim.circle(100)
    tim.left(i)


#Makes the screen sleep for 10 sec (needs time module)
#time.sleep(10)

#Freezes screen 
screen = t.Screen()
screen.exitonclick()
