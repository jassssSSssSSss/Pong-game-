from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
#rmb no () for paddle.move_up bc it will get called immediately and wont work!!!
#TODO: ask why shouldnt have () inside the function!!!
screen.onkey(fun = r_paddle.move_up, key = "Up")
screen.onkey(fun = r_paddle.move_down, key = "Down")
screen.onkey(fun = l_paddle.move_up, key = "w")
screen.onkey(fun = l_paddle.move_down, key = "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    #delays loop by 0.1
    screen.update()
    ball.move()

    #detect collision w wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #de3tect r paddle miss ball lol 
    if ball.xcor() > 370:
        ball.reset()
        scoreboard.l_point()

    #detect l paddle miss ball 
    elif ball.xcor() < -350:
        ball.reset()
        scoreboard.r_point()




screen.exitonclick()