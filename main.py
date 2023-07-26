import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user = screen.textinput(title= "Make your bet", prompt ="Which turtle will win the race? enter a color: ")
print(user)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race = False
if user in colors:
    user_bet = True

n = 0
j = 0
turtles = []
for i in colors:
    new_turtle = Turtle()
    new_turtle.color(colors[j])
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(-230, -100 + n)
    turtles.append(new_turtle)
    n += 50
    j += 1


if user_bet ==True:
    is_race =True

while is_race:
    for tur in turtles:
        if tur.xcor() > 230:
            is_race = False
            win_turtle = tur.pencolor()
            if win_turtle == user:
                print(f"You win! the {win_turtle} turtle is the winner!")
            else:
                print(f"You lost the {win_turtle} turtle is the winner!")

        random_dis = random.randint(0,10)
        tur.forward(random_dis)



screen.exitonclick()