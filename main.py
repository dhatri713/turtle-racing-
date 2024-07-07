from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=600)

red = Turtle()
green = Turtle()
yellow = Turtle()
blue = Turtle()
orange = Turtle()
indigo = Turtle()
violet = Turtle()

turtles = [red, green, yellow, blue, orange, indigo, violet]
turtle_colors = ["red", "green", "yellow", "blue", "orange", "indigo", "violet"]

for n in range(0, len(turtles)):
    turtles[n].color(turtle_colors[n])

for turtle in turtles:
    turtle.shape("turtle")

start_x = -290
start_y = -150

for turtle in turtles:
    turtle.penup()
    turtle.setpos(start_x, start_y)
    start_y += 50

user_bet = screen.textinput(title="Turtle racing", prompt="Which color of VIBGYOR do you think will win?")

race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 260:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race.")
            else:
                print(f"You lost. The {winning_color} turtle won the race.")
        random_distance = random.randint(10, 20)
        turtle.forward(random_distance)

screen.exitonclick()
