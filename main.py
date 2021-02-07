from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

screen.listen()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_is_running = True
while game_is_running:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect a goal
    if ball.distance(r_paddle) > 50 and ball.xcor() > 380 or ball.distance(l_paddle) > 50 and ball.xcor() < -380:
        ball.reset_position()
        ball.reverse_move()

screen.exitonclick()
