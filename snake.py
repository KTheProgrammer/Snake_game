from turtle import Turtle

SNAKE_CORD = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.make_snake()

    def make_snake(self):
        for snakes in SNAKE_CORD:
            self.add_snake(snakes)

    def add_snake(self, snakes):
        snake1 = Turtle(shape="square")
        snake1.penup()
        snake1.goto(snakes)
        self.snake_list.append(snake1)

    def extend(self):
        # add new snake length
        self.add_snake(self.snake_list[-1].position())

    def move(self):
        for snake_num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake_num - 1].xcor()
            new_y = self.snake_list[snake_num - 1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.snake_list[0].forward(MOVEMENT)

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)
