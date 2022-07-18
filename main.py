from screen_settings import Scenario, Screen
from paddle import Paddle
from ball import Ball
import time
import sound_effect

waiting = True
game_running = True
current_round = 0

def stop_wait():
    global waiting
    waiting = False


def start_wait():
    global waiting
    waiting = True


screen = Scenario()
paddle_right = Paddle('left')
paddle_left = Paddle('right')
ball = Ball()
Screen().update()

rounds_limit = Screen().numinput("Rounds Limit", "How much rounds will stop the game?", minval=2, maxval=100)
paddle_right.player_name = Screen().textinput("Player 1 - Right Paddle", "Player 1 name (RIGHT PADDLE)" )
paddle_left.player_name = Screen().textinput("Player 2 - Left Paddle", "Player 2 name (LEFT PADDLE)")
Screen().listen()


# BUTTONS AND GAME CONTROLLERS (orientar isso a objetos)
Screen().onkeypress(paddle_right.go_up, 'Up')
Screen().onkeypress(paddle_right.go_down, 'Down')
Screen().onkeypress(paddle_left.go_up, 'w')
Screen().onkeypress(paddle_left.go_down, 's')
Screen().onkey(stop_wait, 'space')
Screen().onkey(start_wait, 'p')

while game_running and current_round < rounds_limit:
    current_round = paddle_right.score + paddle_left.score
    screen.show_score_board(paddle_left.score, paddle_right.score)
    Screen().update()
    time.sleep(0.01)
    if not waiting:
        screen.waiting_text.clear()
        ball.move()
        # Approximation to the wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            screen.show_collision_line(ball.ycor())
            sound_effect.ball_bouncing()
        else:
            screen.collision_line.hideturtle()

        # Collision with the wall
        if ball.ycor() > 290 or ball.ycor() < -290:
            ball.wall_bouncing()

        # Collision with the paddle
        if ball.distance(paddle_right) < 60 and ball.xcor() > 325 or ball.distance(paddle_left) < 60 and ball.xcor() < -325:
            sound_effect.ball_bouncing()
            ball.paddle_bouncing()

        # Collision with the right wall
        if ball.xcor() > 360:
            sound_effect.game_over()
            paddle_left.score += 1
            screen.show_scored_line(x=ball.xcor(), y=ball.ycor())
            ball.reset_ball()
            Screen().update()
            waiting = True

        elif ball.xcor() < -360:
            sound_effect.game_over()
            paddle_right.score += 1
            screen.show_scored_line(x=ball.xcor(), y=ball.ycor())
            ball.reset_ball()
            Screen().update()
            waiting = True

        else:
            screen.scored_line.hideturtle()
    else:
        screen.waiting_message()

Screen().clear()
Screen().bgcolor('black')
if paddle_right.score == paddle_left.score:
    screen.end_game(f'{paddle_right.player_name} & {paddle_left.player_name} each', paddle_right.score)
elif paddle_right.score > paddle_left.score:
    screen.end_game(paddle_right.player_name, paddle_right.score)
else:
    screen.end_game(paddle_left.player_name, paddle_left.score)

Screen().exitonclick()
