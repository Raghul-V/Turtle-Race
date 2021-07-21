import turtle
import random
import time
import sys
from turtle import Turtle


WIDTH = 800
HEIGHT = 600

COLORS = ["purple", "blue", "orange", "red", "brown", "green", "pink", "yellow", "cyan", "black"]
random.shuffle(COLORS)

TRACK_HEIGHT = HEIGHT - 200


def get_num_of_racers(mini, maxi):
    try:
        num_of_racers = int(turtle.numinput(
            title="No.of racers", 
            prompt=f"How many racers would you like to race ({mini}-{maxi})?"
        ))
    except:
        return None
    if mini <= num_of_racers <= maxi:
        return num_of_racers
    return get_num_of_racers(mini, maxi)


def draw_line(start, end, width=1):
    pen = Turtle(visible=False)
    pen.width(width)
    pen.speed(0)

    pen.penup()
    pen.goto(*start)
    pen.pendown()
    pen.goto(*end)


def draw_track(start, end, length, width=1):
    pen = Turtle(visible=False)
    pen.width(width)
    pen.speed(0)

    xcor = start[0]
    for ycor in range(start[1], end[1], length):
        pen.penup()
        pen.goto(xcor, ycor)
        pen.pendown()
        pen.goto(xcor, ycor + length/2)


def init_race(racer_speed=0, racer_width=1):
    num_of_racers = get_num_of_racers(2, len(COLORS))
    if num_of_racers is None:
        sys.exit()

    track_width = 50 * (num_of_racers + 1)
    start_x = -track_width // 2
    start_y = -TRACK_HEIGHT // 2
    dist_betw_racers = track_width / (num_of_racers - 1)

    half_line_width = abs(start_x - dist_betw_racers/2)
    draw_line((-half_line_width, start_y + 10), (half_line_width, start_y + 10), 3)
    draw_line((-half_line_width, start_y + TRACK_HEIGHT), (half_line_width, start_y + TRACK_HEIGHT), 3)

    xcor = -(track_width + dist_betw_racers) / 2

    for i in range(num_of_racers+1):
        draw_track((xcor, start_y-35), (xcor, start_y+TRACK_HEIGHT+25), 25, 1.5)
        xcor += dist_betw_racers
    
    for i in range(num_of_racers):
        pen = Turtle(visible=False)
        pen.penup()
        pen.goto(start_x + (i * dist_betw_racers) - 5, start_y - 50)
        pen.write(i + 1, font=("Arial", 16, "normal"))

    racers = []

    for i in range(num_of_racers):
        racer = Turtle(shape="turtle")
        racer.width(racer_width)
        racer.speed(racer_speed)
        racer.color(COLORS[i % len(COLORS)])

        racer.penup()
        racer.goto(start_x + (i * dist_betw_racers), start_y)
        racer.left(90)
        racer.pendown()

        racers.append(racer)

    return racers


def race(speed=1):
    if speed < 1:
        speed = 1

    racers = init_race()
    num_of_racers = len(racers)
    finish_y = racers[0].ycor() + TRACK_HEIGHT

    while True:
        for i in range(num_of_racers):
            new_ycor = racers[i].ycor() + (random.randint(0, 10) * speed)
            racers[i].goto(racers[i].xcor(), new_ycor)
            # if not won the race
            if new_ycor < finish_y:
                continue
            # if won the race
            time.sleep(0.75)
            turtle.clearscreen()
            
            pen = Turtle(visible=False)
            color = COLORS[i % len(COLORS)]
            pen.color(color)
            pen.penup()
            pen.goto(-250, 0)
            pen.write(f"Turtle at position {i + 1} won the race", font=("Arial", 26, "normal"))
            
            time.sleep(3)
            return i


screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)

turtle.title("Turtle Race")

winner_index = race(speed=2)
print(f"Turtle at position {winner_index+1} won the race")


