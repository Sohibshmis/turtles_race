import random
from turtle import Turtle, Screen


colors = ["blue", "red", "yellow", "orange", "green", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter a color: ")

all_turtles = []
y_position = -100

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    new_turtle.color(color)
    y_position += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won, the {winning_color} turtle made it.")
                is_race_on = False
            else:
                print(f"You've lost, the {winning_color} turtle made it.")
                is_race_on = False
        random_distance = random.randint(1, 10)
        turtle.forward(random_distance)


screen.exitonclick()