from ctypes.wintypes import PLONG
from turtle import Screen
from pong import Pong
from score import Score
import time
from ball import Ball


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping pong")
screen.tracer(0)

l_paddle = Pong((-350, 0))
r_paddle = Pong((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    
    #Collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()
    
    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()




screen.exitonclick()