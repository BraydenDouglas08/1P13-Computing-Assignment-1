import turtle
import random
import time
import math

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "Code and Seek!"

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)


t = turtle.Turtle()


t.down()
t.pencolor("black")

def draw_plane():
    x = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
    y = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2)
    size = random.randint(50,100)

    # Main Body
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.forward(size)
    t.right(90)
    t.forward(size//3)
    t.right(90)
    t.forward(size)
    t.right(90)
    t.forward(size//3)
    t.right(90)
    t.end_fill()

    # Head
    t.begin_fill()
    t.goto(x-(size//1.5), y-(size//3))
    t.goto(x, y-size//3)
    t.goto(x,y)
    t.end_fill()

    # Back Top Wing
    t.up()
    t.goto(x + size, y)
    t.down()
    t.begin_fill()
    t.goto(x + size, y + size//4)
    t.goto(x + (size - size//2), y)
    t.goto(x + size, y)
    t.end_fill()

    # Main Wing
    t.up()
    t.goto(x + size//10, y - size//5)
    t.down()
    t.begin_fill()
    t.forward(size//1.2)
    t.right(90)
    t.forward(size//3)
    t.goto(x + size//10, y - size//5)
    t.end_fill()

    # Windows
    t.fillcolor("#222222")
    t.pencolor("#222222")
    for i in range(5):
        t.up()
        t.goto(x + (size // 15) + ((size // 10) * i), y - size // 9)
        t.down()
        t.begin_fill()
        t.circle(size // 25)
        t.end_fill()
    t.left(90)  # Returns the turtle to its default heading.

    # Border
    t.pencolor("black")
    t.pensize(1)
    t.up()
    t.goto(x + size, y + size // 4)
    t.down()
    t.goto(x + (size - size // 2), y)
    t.goto(x, y)
    t.goto(x - (size // 1.5), y - (size // 3))
    t.goto(x, y - (size // 3))
    t.goto(x + size // 3, y - (size // 3))
    t.goto((x + size // 10) + (size // 1.2),
    t.goto(y - size // 5) - (size // 3))
    t.goto((x + size // 10) + (size // 1.2), y - size // 3)
    t.goto(x + size, y - size // 3)
    t.goto(x + size, y - (size // 3))
    t.goto(x + size, y)
    t.goto(x + size, y + size // 4)

draw_plane()
screen.exitonclick()
