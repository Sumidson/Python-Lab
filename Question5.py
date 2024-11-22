import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pattern_turtle = turtle.Turtle()
pattern_turtle.speed(0)  # Fastest speed

# Function to create a custom pattern
def draw_spiral():
    colors = ["red", "blue", "green", "purple", "orange", "yellow"]
    for i in range(360):
        pattern_turtle.pencolor(random.choice(colors))
        pattern_turtle.forward(i * 3 / 2)
        pattern_turtle.right(45)

# Draw the pattern
draw_spiral()

# Hide the turtle and display the window
pattern_turtle.hideturtle()
turtle.done()
