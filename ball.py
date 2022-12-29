from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color('#97D8B2')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        # self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        # self.move_speed *= 0.9

    def reset(self):
        self.setposition(0, 0)
        self.move_speed = 0.1
        self.move()
