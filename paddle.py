from turtle import Turtle

X_POS = 350
Y_POS = 0


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.side = side
        self.player_name = None
        self.score = 0
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=0.6)
        if self.side == 'left':
            self.goto(X_POS, Y_POS)
        else:
            self.goto(-X_POS, Y_POS)

    def go_up(self):
        if not self.ycor() > 230:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if not self.ycor() < -230:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
