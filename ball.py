from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.speed('slowest')
        self.penup()
        self.x_move = 2
        self.y_move = 2
        self.random_direction()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bouncing(self):
        self.y_move *= -1

    def paddle_bouncing(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = 2
        self.y_move = 2
        self.random_direction()

    def random_direction(self):
        pick_a_number = randint(0, 1)
        if pick_a_number == 1:
            self.paddle_bouncing()

    def increase_speed(self):
        if self.x_move > 0:
            self.x_move += 0.15
        else:
            self.x_move -= 0.15
        if self.y_move > 0:
            self.y_move += 0.15
        else:
            self.y_move -= 0.15
