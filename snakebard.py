import turtle
import random

# Initialize the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")

# Create the snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.speed(0)

# Set the initial position of the snake
snake.penup()
snake.goto(-200, 0)

# Create the food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(200, 0)

# Create a variable to track the score
score = 0

# Define a function to move the snake
def move_snake(direction):
    if direction == "up":
        snake.setheading(90)
    elif direction == "down":
        snake.setheading(270)
    elif direction == "left":
        snake.setheading(180)
    elif direction == "right":
        snake.setheading(0)

# Define a function to check if the snake has eaten the food
def check_collision(snake, food):
    if snake.distance(food) < 20:
        # If the snake has eaten the food, increase the score and create a new food
        score += 1
        food.goto(random.randint(-200, 200), random.randint(-200, 200))
        snake.shapesize(snake.shapesize()[0] + 0.1)

# Define a function to check if the snake has hit the wall or itself
def check_game_over(snake):
    if snake.xcor() > 200 or snake.xcor() < -200 or snake.ycor() > 200 or snake.ycor() < -200:
        # If the snake has hit the wall, the game is over
        print("Game Over!")
        screen.bye()

    # Check if the snake has hit itself
    for i in range(len(snake) - 1):
        if snake.distance(snake[i]) < 20:
            print("Game Over!")
            screen.bye()

# Create a keyboard listener
turtle.listen()
turtle.onkey(lambda: move_snake("up"), "Up")
turtle.onkey(lambda: move_snake("down"), "Down")
turtle.onkey(lambda: move_snake("left"), "Left")
turtle.onkey(lambda: move_snake("right"), "Right")

# Start the main game loop
while True:
    # Move the snake
    snake.forward(20)

    # Check for collisions
    check_collision(snake, food)
    check_game_over(snake)

    # Update the screen
    screen.update()
