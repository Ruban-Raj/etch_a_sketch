from turtle import Turtle, Screen
import random

is_game = True
my_screen = Screen()
my_screen.setup(width=500, height= 400)
user_bet = my_screen.textinput(title="your bet?", prompt="which color turtle is gonna win? R,Y,B,V,G,O: ").lower()
colors = ["red", "yellow", "blue", "purple", "green", "orange"]
all_turtle = []

y = -160
for turt in range(0, 6):
    new_turt = Turtle(shape="turtle")
    new_turt.color(colors[turt])
    new_turt.penup()
    new_turt.goto(-230, y=y)
    all_turtle.append(new_turt)
    y += 60

while is_game:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won, and the winning color is {winning_color}")
            else:
                print(f"You've lost, the winning color is {winning_color}")
            is_game = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

my_screen.exitonclick()