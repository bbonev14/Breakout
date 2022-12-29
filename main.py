import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from squares import Squares
from scoreboard import Scoreboard


# Helpers
def restart():
    screen.clear()
    setup()


def quit_game():
    screen.bye()


def setup():
    # Initial setup
    global screen
    screen = Screen()
    screen.setup(width=1280, height=800)
    screen.bgcolor('#170312')
    screen.title("Breakout")
    screen.tracer(0)

    board = Paddle((0, -330))
    ball = Ball()
    points = Scoreboard()
    squares = Squares()
    squares.create_objects()

    screen.listen()
    screen.onkey(board.move_right, "d")
    screen.onkey(board.move_left, "a")

    game_is_on = True
    while game_is_on:

        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Ball and wall collision
        if ball.ycor() < -380:
            game_is_on = False
            points.game_over()
            screen.onkey(restart, "y")
            screen.onkey(quit_game, "n")

        if ball.ycor() > 380:
            ball.bounce_y()

        if ball.xcor() > 630 or ball.xcor() < -630:
            ball.bounce_x()

        # Paddle and ball collision
        if ball.ycor() < -305 and ball.ycor() < -315 and (board.xcor() + 50 > ball.xcor() > board.xcor() - 50):
            ball.bounce_y()

        # Ball and squares collision
        for v in squares.list_squares:
            if v.distance(ball) < 40:
                points.add_score()
                ball.bounce_y()
                v.goto(1500, 1500)

    screen.exitonclick()


# Start game
setup()
