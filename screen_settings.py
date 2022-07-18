from turtle import Screen, Turtle

WIDTH = 800
HEIGHT = 600
LEFT_UPPER_CORNER = (-WIDTH/2, HEIGHT/2)
RIGHT_UPPER_CORNER = (WIDTH/2, HEIGHT/2)
LEFT_BOTTOM_CORNER = (-WIDTH/2, -HEIGHT/2)
RIGHT_BOTTOM_CORNER = (WIDTH/2, -HEIGHT/2)
FONT = ('Times New Roman', 30, 'normal')


class Scenario:

    def __init__(self):
        super().__init__()
        Screen().bgcolor('black')
        Screen().setup(width=WIDTH, height=HEIGHT)
        Screen().title('Pong')
        Screen().tracer(0)
        Screen().listen()
        self.wall_box = Turtle()
        self.collision_line = Turtle()
        self.scored_line = Turtle()
        self.score_board = Turtle()
        self.waiting_text = Turtle()
        self.create_wallbox()
        self.create_wall_collision_line()
        self.create_scored_line()
        self.create_score_board()
        self.waiting_message()
        print('screen criada')

    def create_wallbox(self):
        self.wall_box.hideturtle()
        self.wall_box.pencolor('white')
        self.wall_box.penup()
        self.wall_box.goto(x=0, y=HEIGHT/2)
        self.wall_box.setheading(270)
        for step in range(15):
            self.wall_box.pendown()
            self.wall_box.forward(20)
            self.wall_box.penup()
            self.wall_box.forward(20)
        self.wall_box.goto(LEFT_UPPER_CORNER)
        self.wall_box.pendown()
        self.wall_box.goto(RIGHT_UPPER_CORNER)
        self.wall_box.goto(RIGHT_BOTTOM_CORNER)
        self.wall_box.goto(LEFT_BOTTOM_CORNER)
        self.wall_box.goto(LEFT_UPPER_CORNER)

    def create_wall_collision_line(self):
        self.collision_line.shape('square')
        self.collision_line.penup()
        self.collision_line.color('blue')
        self.collision_line.setheading(90)
        self.collision_line.shapesize(stretch_wid=40, stretch_len=0.1)
        self.collision_line.hideturtle()

    def create_scored_line(self):
        self.scored_line.shape('circle')
        self.scored_line.penup()
        self.scored_line.color('red')
        self.scored_line.setheading(180)
        #self.scored_line.shapesize(stretch_wid=30, stretch_len=0.1)
        self.scored_line.hideturtle()

    def create_score_board(self):
        self.score_board.hideturtle()
        self.score_board.color('white')
        self.score_board.penup()
        self.score_board.goto(x=0, y=250)

    def show_collision_line(self, position):
        if position > 0:
            self.collision_line.goto(x=0, y=HEIGHT / 2)
        else:
            self.collision_line.goto(x=0, y=-HEIGHT / 2)
        self.collision_line.showturtle()

    def show_scored_line(self, x, y):
        self.scored_line.goto(x=x, y=y)
        self.scored_line.showturtle()

    def show_score_board(self, paddle_left_score, paddle_right_score):
        self.score_board.clear()
        self.score_board.write(f"{paddle_left_score}   {paddle_right_score}", font=FONT, align='center')

    def waiting_message(self):
        self.waiting_text.hideturtle()
        self.waiting_text.color('white')
        self.waiting_text.penup()
        self.waiting_text.goto(x=0, y=100)
        self.waiting_text.clear()
        self.waiting_text.write(f"Press SPACE to roll the ball.", font=FONT, align='center')

    def end_game(self, winner, points):
        self.waiting_text.clear()
        self.waiting_text.goto(x=0, y=0)
        self.waiting_text.write(f"Winner: {winner} with {points} points", font=FONT, align='center')