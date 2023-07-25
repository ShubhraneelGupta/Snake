from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("orange")
        self.shapesize(0.5)
        self.refresh()

    def refresh(self):
        new_x = random.randint(-250, 200)
        new_y = random.randint(-250, 200)
        self.goto(new_x, new_y)
