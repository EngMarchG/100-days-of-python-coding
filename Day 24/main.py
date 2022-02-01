from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("March Snake")
screen.tracer(0)

snake = Snake()
food = Food()
increase_score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Collision detection of food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        increase_score.score_change()

    #Wall collision.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        increase_score.reset()
        snake.reset()
    
    for segment in snake.snake_length[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            increase_score.reset()
            snake.reset()


screen.exitonclick()