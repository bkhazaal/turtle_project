import turtle

class Shell:
    def __init__(self, color):
        self.color = color

    def draw(self):
        my_pen.begin_fill()
        my_pen.color(self.color)
        my_pen.forward(150)
        my_pen.left(45)
        my_pen.forward(45)
        my_pen.left(45)
        my_pen.forward(45)
        my_pen.left(45)
        my_pen.forward(45)
        my_pen.left(45)
        my_pen.forward(150)
        my_pen.left(45)
        my_pen.forward(45)
        my_pen.left(45)
        my_pen.forward(45)
        my_pen.left(45)
        my_pen.forward(45)
        my_pen.end_fill()

class Leg_1:
    def __init__(self, color):
        self.color = color

    def draw(self):
        my_pen.begin_fill()
        my_pen.color(self.color)
        my_pen.right(45)
        my_pen.forward(35)
        my_pen.left(90)
        my_pen.forward(20)
        my_pen.left(90)
        my_pen.forward(35)
        my_pen.left(90)
        my_pen.forward(20)
        my_pen.end_fill()

class Leg_2:
    def __init__(self, color):
        self.color = color

    def draw(self, position):
        my_pen.penup()
        my_pen.goto(position)
        my_pen.pendown()
        my_pen.begin_fill()
        my_pen.color(self.color)
        my_pen.left(90)
        my_pen.forward(35)
        my_pen.left(90)
        my_pen.forward(20)
        my_pen.left(90)
        my_pen.forward(35)
        my_pen.left(90)
        my_pen.forward(20)
        my_pen.end_fill()

class Neck:
    def __init__(self, color):
        self.color = color

    def draw(self, position):
        my_pen.penup()
        my_pen.goto(position)
        my_pen.pendown()
        my_pen.begin_fill()
        my_pen.color(self.color)
        my_pen.left(45)
        my_pen.forward(150)
        my_pen.left(90)
        my_pen.forward(20)
        my_pen.left(90)
        my_pen.forward(150)
        my_pen.left(90)
        my_pen.forward(20)
        my_pen.end_fill()

class Head:
    def __init__(self, color):
        self.color = color
    
    def draw(self, position):
        my_pen.penup()
        my_pen.goto(position)
        my_pen.pendown()
        my_pen.begin_fill()
        my_pen.color(self.color)
        my_pen.circle(-30)
        my_pen.end_fill()

my_window = turtle.Screen()
my_window.bgcolor("white")
my_pen = turtle.Turtle()

turtle_shell = Shell("green")
turtle_leg_1 = Leg_1("yellow")
turtle_leg_2 = Leg_2("yellow")
turtle_neck = Neck("green")
turtle_head = Head("green")

draw_functions = [
    turtle_shell.draw,
    turtle_leg_1.draw,
    lambda: turtle_leg_2.draw((130, 0)),
    lambda: turtle_neck.draw((200, 150)),
    lambda: turtle_head.draw((200, 130))
]

for draw_function in draw_functions:
    draw_function()

turtle.done()
turtle.exitonclick()
