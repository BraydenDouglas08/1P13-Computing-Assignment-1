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

## Start of your code
def Start_Screen():
    turtle.bgcolor("#4CBE00")
    t.up()
    t.goto(0, 100)
    t.write("Try and Find the Hidden Target!",align="center", font=("Arial", 24, "bold"))
    t.goto(0,0)
    t.write("Player 1 will set the coordinates on where to hide",align="center", font=("Arial", 16))
    t.goto(0,-50)
    t.write("Player 2 will have 4 guesses to find the hidden turtle.",align="center", font=("Arial", 16))
    # time.sleep(5)

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
    t.up()
    t.goto(x,y)
    t.write(f"You are {calc_distance(x,y):.2f} away!", align="center", font=("Arial", 8))
    t.goto(x,y-15)
    t.write(f"You got {calc_score(x,y):.2f} points!", align="center", font=("Arial", 8))

def draw_cloud(x, y, radius):
    pass

def create_map():
    turtle.clearscreen()
    turtle.bgcolor("#3F87E6")

def final_summary(total_score, total_distance, best_guess):
    turtle.clearscreen()
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
    

Start_Screen()
x_hide = int(screen.numinput("X-Location","Player 1, choose the X location on where to hide, (0,0 is in center)"))
y_hide = int(screen.numinput("Y-Location","Now choose the Y location on where to hide"))
create_map()

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

# print(total_score)
final_summary(total_score, total_distance, best_guess)

screen.exitonclick()

