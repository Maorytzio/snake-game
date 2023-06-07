import time

from turtle import Screen

from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game = True
while is_game:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        print("collision occurred!")
        score_board.increment()
        food.refresh()
        snake.extend()

    # detect collision with Wall
    if snake.snake_head.xcor() > 282 or snake.snake_head.xcor() < -282 or \
            snake.snake_head.ycor() > 282 or snake.snake_head.ycor() < -282:
        score_board.reset_game()
        snake.reset()

    # detect collision with segments
    for seg in snake.segments[1:]:  # dont check head
        if snake.snake_head.distance(seg) < 10:
            score_board.reset_game()
            snake.reset()
            
screen.exitonclick()
