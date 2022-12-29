import random
from turtle import Turtle

COLORS = ["#F48668", "#F4A698", "#73A580", '#A0ACAD']


class Squares:

    def __init__(self):
        self.list_squares = []
        self.index_x = -690
        self.index_y = 300

    def create_objects(self):
        for _ in range(5):
            for _ in range(11):
                new_obj = Turtle()
                new_obj.shape('square')
                new_obj.turtlesize(stretch_wid=2, stretch_len=5)
                new_obj.color(random.choice(COLORS))
                new_obj.penup()
                self.index_x += 115
                new_obj.goto(self.index_x, self.index_y)
                self.list_squares.append(new_obj)
            self.index_x = -690
            self.index_y -= 50
