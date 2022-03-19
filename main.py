from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

still_playing = True
while still_playing:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # Detect collision with wall
    if snake.snake_list[0].xcor() > 280 or snake.snake_list[0].xcor() < -280 or snake.snake_list[0].ycor() > 280 or \
            snake.snake_list[0].ycor() < -280:
        still_playing = False
        scoreboard.game_over()

    # Detect collision with tail
    for tail in snake.snake_list[1:]:
        if snake.snake_list[0].distance(tail) < 10:
            still_playing = False
            scoreboard.game_over()

screen.exitonclick()
