from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
#screen.onkey(player.go_up, "Up")    #allows 1 click at a time only
screen.onkeypress(player.go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    #Create cars by chance and move them
    car_manager.create_car()
    car_manager.move_cars()
    
    #Game over when collision with cars occurs
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    
    #Resets turtle position and speed cars up (new level)
    if player.ycor() >= 300:
        player.at_finish()
        car_manager.speed_up()
        scoreboard.lvl_up()

screen.exitonclick()