from turtle import *
from freegames import floor, vector

food = vector(0,0)
snake = [vector(100,0)]
direction = vector(0, -100)

def inside(point):
    "Return True if x, y in axes coordinates and within separation."
    return -200 < point.x < 200 and -200 < point.y < 200 and point.x!= 0 and point.y!= 0

def change(x, y):
    "Move snake with x and y as direction."
    direction.x += x
    direction.y += y

def move():
    "Move snake to the new location chosen."
    food.x += direction.x
    food.y += direction.y

    head = snake[-1].copy()
    head.move(direction)

    if inside(food) and head == snake[-1]:
        print("A perfect world beforo!")
        food.x -= direction.x
        food.y -= direction.y
        snake.append(head)
    elif head in snake:
        print("You lost!")
        return

    clear()

    for body in snake:
        penup()
        forward(body.x)
        left(90)
        forward(body.y)
        right(90)

    penup()
    forward(head.x)
    right(90)
    forward(head.y)
    right(90)
    draw_line(head.x, head.y, food.x, food.y, 10)

    # wait for a mouse click
    ontimer(move, 50)

setup(420, 420, 370, 200)
hideturtle()
up()
tracer(False)
onscreenclick(move)
move()
done()
