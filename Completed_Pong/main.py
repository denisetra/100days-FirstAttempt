from turtle import Screen
from frame import outside_frame
from my_paddles import Paddles
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My_Pong_2021")
screen.tracer(0)
outside_frame() #remove this when I get more of screen setup.

right_paddle = Paddles((350, 0))
left_paddle = Paddles((-360, 0))

ball = Ball()
score = Scoreboard()


screen.listen() # Listen for keystokes

screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down,"x")
slp = .1

game_is_on = True
while game_is_on:
    if ball.xcor() ==0 and ball.ycor() == 0:
        slp=.1
    time.sleep(slp)
    screen.update()
    ball.move()
    print (f"Sleeping for: {slp}wwwwsssswwwwwwxxxxx")

    ## Detect collison with the top and bottom wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        slp -= .001

    ## Detect collision with right-paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 310 or ball.distance(left_paddle) < 50 and ball.xcor() < -310:
        ball.bounce_x()
        slp -= .01

    ## If right paddle misses the ball:
    if ball.xcor() > 350:
        ball.reset_position()
        score.left_point()

    ## If left paddle misses the ball:
    if ball.xcor() < -350:
        ball.reset_position()
        score.right_point()





screen.exitonclick()


