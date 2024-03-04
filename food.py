from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('hotpink')
        self.respawn()

    def respawn(self):
        x = randint(-250, 250)
        y = randint(-250, 250)
        self.goto(x, y)