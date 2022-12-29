from turtle import Turtle

FONT = ("Courier", 30, "normal")
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('#97D8B2')
        self.hideturtle()
        self.goto(520, 330)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, -100)
        self.write(f"GAME OVER\nTry Again?\n   Y/N", move=False, align=ALIGN, font=FONT)
