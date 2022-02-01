from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.faster = 0     #speed up cars every clear
    
    def create_car(self):
        check_create = random.randint(1, 6)
        if check_create == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)
    
    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE + self.faster)
    
    def speed_up(self):
        self.faster += 2

