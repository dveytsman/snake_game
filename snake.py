from turtle import Turtle
from icecream import ic

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self, segments=[]):
        self.segments = segments
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

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

    def grow(self):
        self.add_segment(self.segments[-1].position())