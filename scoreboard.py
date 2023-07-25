from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, height):
        super().__init__()
        self.score = 0
        self.height = height
        self.color("white")
        self.make_border()
        self.penup()
        self.write_score()

    def make_border(self):
        self.penup()
        self.goto(-263, 233)
        self.pendown()
        self.fd(526)

    def write_score(self):
        self.hideturtle()
        self.goto(0, (self.height - 100) / 2)
        self.write("Score : " + str(self.score), font=("ariel", 30, "bold"), align="center")

    def update(self):
        self.clear()
        self.penup()
        self.score += 1
        self.write_score()
        self.make_border()

    def game_over(self):
        self.penup()
        self.goto(0, -22)
        self.write("GAME OVER!!", font=("ariel", 55, "bold"), align="center")