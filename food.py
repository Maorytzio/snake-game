from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")

        x_pox, y_pos = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x_pox, y_pos)

    def refresh(self):
        x_pox, y_pos = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x_pox, y_pos)
