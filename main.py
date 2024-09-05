import random
import turtle
from turtle import Screen, Turtle
is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="make a bet", prompt="which turtle will win the race?Pick a color: ")
color =["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.pu()
    new_turtle.goto(x= -230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("you win!")
            else:
                print("you lose")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()