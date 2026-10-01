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
t.hideturtle()
screen.tracer(0)
t.speed(0)

## Start of your code
def start_screen():
    turtle.bgcolor("#4CBE00")
    t.up()
    t.goto(0, 100)
    t.write("Try and Find the Hidden Target!",align="center", font=("Arial", 24, "bold"))
    t.goto(0,0)
    t.write("Player 1 will set the coordinates on where to hide",align="center", font=("Arial", 16))
    t.goto(0,-50)
    t.write("Player 2 will have 4 guesses to find the hidden turtle.",align="center", font=("Arial", 16))

def calc_distance(x, y):
    x_dist = x_hide - x
    y_dist = y_hide - y
    distance = ((x_dist ** 2) + (y_dist **2)) ** 0.5
    return distance
    
def calc_score(x, y):
    distance = calc_distance(x,y)
    distance_difference = 200 - distance
    score = (max(0,distance_difference) ** 2) / 4000
    return score

def guess_info(x,y):
    t.pencolor("red")
    t.up()
    t.goto(x,y)
    t.down()
    t.dot(8)
    t.dot(8)
    t.pencolor("black")
    t.up()
    t.goto(x, y - 30)
    t.write(f"You are {calc_distance(x,y):.0f} away!", align="center", font=("Arial", 10))
    t.goto(x,y-45)
    t.write(f"You got {calc_score(x,y):.2f} points!", align="center", font=("Arial", 10))
    screen.update()

def draw_cloud():
    x = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
    y = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2)
    radius = random.randint(20,40)

    t.fillcolor("#f3f2f0")
    t.pencolor("black")

    t.up()
    t.begin_fill()
    t.goto(x-(radius//2),y)
    t.circle(radius*0.8)
    t.end_fill()
    t.begin_fill()
    t.goto(x+(radius//2),y)
    t.circle(radius*0.8)
    t.end_fill()
    t.goto(x, y)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_plane():
    x = random.randint(-SCREEN_WIDTH//2,SCREEN_WIDTH//2)
    y = random.randint(-SCREEN_HEIGHT//2,SCREEN_HEIGHT//2)
    size = random.randint(30,70)

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
    t.left(90) # Sets heading back to default
    
    # Draw black border around plane
    t.pencolor("black")
    t.pensize(1)
    t.up()
    t.goto(x + size, y + size//4)
    t.down()
    t.goto(x + (size - size//2), y)
    t.goto(x, y)
    t.goto(x - (size // 1.5), y - (size // 3))
    t.goto(x, y - (size // 3))
    t.goto(x + size//3, y - (size // 3))
    t.goto((x + size//10) + (size//1.2), (y - size//5) - (size//3))
    t.goto((x + size//10) + (size//1.2), y - size//3)
    t.goto(x + size, y - size//3)
    t.goto(x + size, y - (size // 3))
    t.goto(x + size, y)
    t.goto(x + size, y + size//4)

def create_map():
    t.clear()
    for _ in range (25):
        draw_cloud()
    for _ in range(10):
        draw_plane()
    turtle.bgcolor("#3F87E6")





def final_summary(total_score, total_distance, best_guess):
    t.clear()
    turtle.bgcolor("#4CBE00")
    t.up()
    t.goto(0, 100)
    t.write("Thank you for playing!",align="center", font=("Arial", 24, "bold"))
    t.goto(0,0)
    t.write(f"Your total score is:{total_score:.2f}",align="center", font=("Arial", 16))
    t.goto(0,-50)
    t.write(f"The total distance away of all your guesses is {total_distance:.0f} pixels",align="center", font=("Arial", 16))
    t.goto(0,-100)
    t.write(f"Your closest guess was {best_guess:.0f} pixels away.",align="center", font=("Arial", 16))

def show_location():
    t.pencolor("green")
    t.up()
    t.goto(x_hide,y_hide)
    t.down()
    t.dot(8)
    t.dot(8)
    t.pencolor("black")
    t.up()
    t.goto(x_hide, y_hide - 30)
    t.write(f"The hidden coordinates were ({x_hide}, {y_hide}).", align="center", font=("Arial", 14))

start_screen()
screen.update()
time.sleep(3)

create_map()
screen.update()
time.sleep(1.5)

x_hide = int(screen.numinput("X-Location","Player 1, choose the X location on where to hide, (0,0 is in center)"))
y_hide = int(screen.numinput("Y-Location","Now choose the Y location on where to hide"))


total_score = 0
total_distance = 0
best_guess = 9999 # High value placeholder as using min function to compare with itself for lowest distance, 0 placeholder would always be selected if used


for _ in range(4):
    x_find = int(screen.numinput("X-Location","Player 2, choose the X location for your guess"))
    y_find = int(screen.numinput("Y-Location","Now choose the Y location for your guess"))
    total_score += calc_score(x_find, y_find)
    total_distance += calc_distance(x_find, y_find)
    best_guess = min(best_guess, calc_distance(x_find, y_find))
    guess_info(x_find, y_find)


show_location()
screen.update()
time.sleep(3)


final_summary(total_score, total_distance, best_guess)

screen.exitonclick()

