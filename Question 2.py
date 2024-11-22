import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
star = turtle.Turtle()
star.color("black")

# Define a function to draw a star
def draw_star(turtle, size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

# Set the speed of the turtle
star.speed(2)

# Draw the star
draw_star(star, 100)

# Hide the turtle and display the window
star.hideturtle()
turtle.done()
