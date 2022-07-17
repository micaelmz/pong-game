from screen_settings import Scenario, Screen
from paddle import Paddle
from ball import Ball
import time
import sound_effect

waiting = True
game_running = True

#resposta = screen.textinput(title='Determine o fim da partida', prompt='Digite quantas rodadas encerram o jogo')


def stop_wait():
    global waiting
    waiting = False

screen = Scenario()
paddle_right = Paddle('left')
paddle_left = Paddle('right')
ball = Ball()



# BUTTONS AND GAME CONTROLLERS (orientar isso a objetos)
Screen().onkeypress(paddle_right.go_up, 'Up')
Screen().onkeypress(paddle_right.go_down, 'Down')
Screen().onkeypress(paddle_left.go_up, 'w')
Screen().onkeypress(paddle_left.go_down, 's')
Screen().onkeypress(stop_wait, 'space')


while game_running:
    screen.show_score_board(paddle_left.score, paddle_right.score)
    time.sleep(0.01)
    Screen().update()
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
        if ball.distance(paddle_right) < 50 and ball.xcor() > 330 or ball.distance(paddle_left) < 50 and ball.xcor() < -330:
            sound_effect.ball_bouncing()
            ball.paddle_bouncing()

        # Collision with the right wall
        if ball.xcor() > 360:
            sound_effect.game_over()
            paddle_left.score += 1
            screen.show_scored_line(position=ball.xcor())
            ball.reset_ball()
            Screen().update()
            waiting = True

        if ball.xcor() < -360:
            sound_effect.game_over()
            paddle_right.score += 1
            screen.show_scored_line(position=ball.xcor())
            ball.reset_ball()
            Screen().update()
            waiting = True

        else:
            screen.scored_line.hideturtle()
    else:
        screen.waiting_message()

Screen().exitonclick()
