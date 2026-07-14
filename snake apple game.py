import turtle
import time
import random

# Game settings
DELAY = 0.1
SCORE = 0
HIGH_SCORE = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off automatic screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Apple (Food)
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0, 100)

# Snake body segments list
segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "normal"))

# Functions to change directions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def reset_game():
    global SCORE, DELAY
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
     
    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    
    SCORE = 0
    DELAY = 0.1
    update_score()

def update_score():
    pen.clear()
    pen.write(f"Score: {SCORE}  High Score: {HIGH_SCORE}", align="center", font=("Arial", 24, "normal"))

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main Game Loop
while True:
    screen.update()

    # Check for wall collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset_game()

    # Check for apple collision
    if head.distance(apple) < 20:
        # Move apple to a random spot
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        # Add a body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("dark blue")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay to make game faster
        DELAY -= 0.003

        # Increase score
        SCORE += 10
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
        update_score()

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for body collisions
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(DELAY)

screen.mainloop()
