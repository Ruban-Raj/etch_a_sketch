from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forward():
    tim.forward(20)
    
def move_backward():
    tim.backward(20)

def move_right():
    tim.right(15)
    
def move_left():
    tim.left(15)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.listen()
my_screen.onkey(key="w", fun=move_forward)
my_screen.onkey(key="s", fun=move_backward)
my_screen.onkey(key="a", fun=move_left)
my_screen.onkey(key="d", fun=move_right)
my_screen.onkey(key="c", fun=clear_screen)

my_screen.exitonclick()