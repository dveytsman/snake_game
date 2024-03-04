from turtle import Turtle
from icecream import ic

class Snake:
    def __init__(self, segments=[]):
        self.segments = segments
        x = 0
        for _ in range(0, 3):
            snake = Turtle()
            snake.penup()
            self.segments.append(snake)
            snake.color("white")
            snake.shape("square")
            snake.goto(x, 0)
            x -= 20
        self.head = self.segments[0]

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            lastx = self.segments[index-1].xcor()
            lasty = self.segments[index-1].ycor()
            self.segments[index].goto(lastx, lasty)
        self.head.forward(20)
    
    def go_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def go_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)