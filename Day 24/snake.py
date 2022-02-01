from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_length = []
        self.create_snake()
        self.head = self.snake_length[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        make_snake = Turtle("square")
        make_snake.color("white")
        make_snake.penup()
        make_snake.goto(position)
        self.snake_length.append(make_snake)

    def extend(self):
        self.add_segment(self.snake_length[-1].position())

    def reset(self):
        for parto in self.snake_length:
            parto.goto(1000, 1000)
        self.snake_length.clear()
        self.create_snake()
        self.head = self.snake_length[0]
    
    def move(self):
        for snake_part in range(len(self.snake_length)-1,0,-1):
            new_x = self.snake_length[snake_part-1].xcor()
            new_y = self.snake_length[snake_part-1].ycor()
            self.snake_length[snake_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
