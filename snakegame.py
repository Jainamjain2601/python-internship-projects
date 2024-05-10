import turtle
import time
import random

DELAY = 0.1
SCORE_FONT = ("Courier", 24, "normal")

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake eyes
eye_left = turtle.Turtle()
eye_left.speed(0)
eye_left.shape("square")
eye_left.color("white")
eye_left.penup()
eye_left.goto(-4, 0)

eye_right = turtle.Turtle()
eye_right.speed(0)
eye_right.shape("square")
eye_right.color("white")
eye_right.penup()
eye_right.goto(4, 0)

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
score = 0

# Scoreboard
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0", align="center", font=SCORE_FONT)

# Game over message
game_over = turtle.Turtle()
game_over.speed(0)
game_over.color("white")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)

# Functions
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
        eye_left.sety(4)
        eye_right.sety(4)
        if head.ycor() > 290:
            head.sety(-290)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        eye_left.sety(-4)
        eye_right.sety(-4)
        if head.ycor() < -290:
            head.sety(290)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        eye_left.setx(-8)
        eye_right.setx(-8)
        if head.xcor() < -290:
            head.setx(290)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        eye_left.setx(8)
        eye_right.setx(8)
        if head.xcor() > 290:
            head.setx(-290)

def check_collision():
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        global score
        score += 10
        scoreboard.clear()
        scoreboard.write("Score: {}".format(score), align="center", font=SCORE_FONT)

def check_self_collision():
    for segment in segments:
        if head.distance(segment) < 20:
            return True
    return False

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for collisions
    if check_self_collision():
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        scoreboard.clear()
        scoreboard.write("Score: {}".format(score), align="center", font=SCORE_FONT)
        game_over.write("Game Over\nPress 'R' to play again\nPress 'Q' to quit", align="center", font=SCORE_FONT)
        game_over.showturtle()
        break

    check_collision()

    # Move the segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(DELAY)

def play_again():
    game_over.clear()
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()
    score = 0
    scoreboard.clear()
    scoreboard.write("Score: {}".format(score), align="center", font=SCORE_FONT)

    # Restart the game
    main()

def quit_game():
    wn.bye()

def main():
    # Main game loop
    while True:
        wn.update()

        # Check for collisions
        if check_self_collision():
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            scoreboard.clear()
            scoreboard.write("Score: {}".format(score), align="center", font=SCORE_FONT)
            game_over.write("Game Over\nPress 'R' to play again\nPress 'Q' to quit", align="center", font=SCORE_FONT)
            game_over.showturtle()
            break

        check_collision()

        # Move the segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        time.sleep(DELAY)

# Bindings for play again and quit
wn.listen()
wn.onkeypress(play_again, "r")
wn.onkeypress(quit_game, "q")

wn.mainloop()
