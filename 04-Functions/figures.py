import turtle 
import draw_figures

# Draws each of the figures (square, triangle, rectangle) twice,
# in different location

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   


## Draw figures
draw_figures.draw_square(50)
draw_figures.draw_square(50)
draw_figures.draw_triangle(50)
draw_figures.draw_triangle(50)
draw_figures.draw_rectangle(50,40)
draw_figures.draw_rectangle(50,40)


window.mainloop()