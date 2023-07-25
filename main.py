from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard


WIDTH = 600
HEIGHT = 600


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)


mySnake = Snake()
food = Food()
sb = Scoreboard(HEIGHT)
screen.listen()
screen.onkey(mySnake.up, "Up")
screen.onkey(mySnake.right, "Right")
screen.onkey(mySnake.left, "Left")
screen.onkey(mySnake.down, "Down")


def move():
    x = mySnake.head.xcor()
    y = mySnake.head.ycor()
    tail_collision = False
    for segment in mySnake.segments[1:]:
        if mySnake.head.distance(segment) < 10:
            tail_collision = True
    if x > 263 or x < -263:
        sb.game_over()
    elif y > 200 or y < -263:
        sb.game_over()
    elif tail_collision:
        sb.game_over()
    else:
        mySnake.move()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    move()

    if mySnake.head.distance(food) < 20:
        food.refresh()
        sb.update()
        mySnake.add_segment()

screen.exitonclick()