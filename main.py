from turtle import Turtle, Screen
from icecream import ic
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("The Original Snake Game")
my_screen.tracer(0)
game_on = True

snake = Snake()
def end():
    return False

my_screen.onkey(snake.go_left, 'a')
my_screen.onkey(snake.go_down, 's')
my_screen.onkey(snake.go_right, 'd')
my_screen.onkey(snake.go_up, 'w')
my_screen.onkey(end, 'p')
my_screen.listen()

food = Food()
score = ScoreBoard()
score.show_score()
 
while game_on:
    my_screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        score.increase_score()
        score.show_score()
        food.respawn()
        snake.grow()

    # Detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()


    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

    





my_screen.exitonclick()