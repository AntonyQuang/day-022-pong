import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Let's Play Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
sleep_time = 0.1
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()


    if ball.xcor() > 380:
        time.sleep(0.4)
        scoreboard.l_point()
        ball.reset_position()


    if ball.xcor() < -380:
        time.sleep(0.4)
        scoreboard.r_point()
        ball.reset_position()


    ball.move()

screen.exitonclick()
