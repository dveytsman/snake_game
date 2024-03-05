from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self

    def increase_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0
    
    def show_score(self):
        self.clear()
        display = f"Score: {self.score}"
        self.write(display, False, "center", ("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align="center", font=("Courier", 26, "normal"))
        self.goto(0, 280)