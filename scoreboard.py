from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center",
                   font=("Times New Roman", 30, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align="center",
                   font=("Times New Roman", 30, "normal"))
