from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 30, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 30, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Times New Roman", 30, "normal"))
