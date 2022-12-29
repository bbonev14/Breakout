from turtle import Turtle

MOVE_DISTANCE = 45


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.shape('square')
        self.color('#97D8B2')
        self.turtlesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(position)

    def move_right(self):
        if self.xcor() < 520:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def move_left(self):
        if self.xcor() > -520:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())
