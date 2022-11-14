from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle(type='right')
l_paddle = Paddle(type='left')
ball = Ball()
screen.listen()

scoreboard = ScoreBoard()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"s")
screen.onkey(l_paddle.go_down,"x")


game_is_on = True
while game_is_on:
    scoreboard.update_score()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -200:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320 :
        ball.bounce_x()

    #Detect ball going past paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_score()


screen.exitonclick()













