import turtle

turtle.color("green")

def draw_shapes(*args):

    turtle.pencolor("green")
    for shape in args:
        if shape == "square":
            draw_square()
        elif shape == "circle":
            draw_circle()
        elif shape == "triangle":
            draw_triangle()


turtle.color("green")
def draw_square():
    turtle.color("green")
    square_turtle = turtle.Turtle()
    for _ in range(4):
        square_turtle.forward(100)
        square_turtle.right(90)


def draw_circle():
    turtle.color("green")
    circle_turtle = turtle.Turtle()
    circle_turtle.circle(50)

def draw_triangle():
    turtle.color("green")
    triangle_turtle = turtle.Turtle()
    for _ in range(3):
        triangle_turtle.forward(100)
        triangle_turtle.left(120)

# Create a turtle screen
screen = turtle.Screen()

# Call the draw_shapes function with variable-length arguments
draw_shapes("square", "circle", "triangle")

# Close the turtle graphics window
turtle.done()
