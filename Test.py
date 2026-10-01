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
turtle.bgcolor("#3F87E6")

def draw_plane():
    x = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
    y = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2)
    size = random.randint(50,100)

    # Main Body
    t.up()
    t.goto(x,y)
    t.down()
    t.fillcolor("#FFFFFF")
    t.pencolor("#FFFFFF")
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
    t.fillcolor("#FF3333")
    t.pencolor("#FF3333")
    t.begin_fill()
    t.goto(x + size, y + size//4)
    t.goto(x + (size - size//2), y)
    t.goto(x + size, y)
    t.end_fill()

    # Main Wing
    t.up()
    t.goto(x + size//10, y - size//5)
    t.down()
    t.fillcolor("#E6E6E6")
    t.pencolor("#E6E6E6")
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
        t.goto(x + (size // 15) + ((size//10) * i), y - size//9)
        t.down()
        t.begin_fill()
        t.circle(size//25)
        t.end_fill()
    t.left(90)

# --- Single Unified Outer Border Outline ---
    t.pencolor("black")
    t.pensize(2)
    
    # 1. Start precisely at the top tip of the tail fin
    t.up()
    t.goto(x + size, y + size//4)
    t.down()
    
    # 2. Trace down the back edge of the tail to the body top
    t.goto(x + (size - size//2), y)
    
    # 3. Trace along the top of the body to the base of the nose
    t.goto(x, y)
    
    # 4. Trace out to the nose tip
    t.goto(x - (size // 1.5), y - (size // 3))
    
    # 5. Trace back along the bottom of the nose/head to the body bottom-left
    t.goto(x, y - (size // 3))
    
    # 6. Trace across the bottom of the body right to the exact start of the main wing root (x + size//10)
    t.goto(x + size//3, y - (size // 3))
    
    # 7. Trace along the bottom edge of the main wing to its lowest tip
    t.goto((x + size//10) + (size//1.2), (y - size//5) - (size//3))
    
    # 8. Trace back up to the outer tip of the main wing
    t.goto((x + size//10) + (size//1.2), y - size//3)
    
    # 9. Trace back from the wing tip into the body right side
    t.goto(x + size, y - size//3)
    
    # 10. Trace down the rest of the rear body to the bottom-right corner
    t.goto(x + size, y - (size // 3))
    
    # 11. Trace back up the back edge of the body to the tail base
    t.goto(x + size, y)
    
    # 12. Trace up the back slant of the tail fin back to the starting point
    t.goto(x + size, y + size//4)

draw_plane()
screen.exitonclick()
