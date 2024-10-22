import turtle
# Create the turtle
pen = turtle.Turtle()

def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)
    pen.penup()
    pen.forward(100)
    pen.pendown()


def draw_rectangle(a,b):
    # Draw a square
    for i in range(4):
        if i%2 ==0:
            pen.forward(a)
            pen.right(90)
        else:
            pen.forward(b)
            pen.right(90)
    pen.penup()
    pen.backward(300)
    pen.pendown()
    

def draw_triangle(length):
    for i in range(3):
        pen.forward(length)
        pen.right(120)
    pen.penup()
    pen.forward(100)
    pen.pendown()

