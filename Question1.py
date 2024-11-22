import turtle

# Setting up the screen and turtle
screen = turtle.Screen()
screen.bgcolor("white")

flower = turtle.Turtle()
flower.speed(10)
flower.color("red")

# Function to draw a petal
def draw_petal():
    for _ in range(2):
        flower.circle(100, 60)
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)

# Drawing the flower
flower.penup()
flower.goto(0, -100)
flower.pendown()
for _ in range(6):
    draw_petal()
    flower.right(60)

# Drawing the center of the flower
flower.color("yellow")
flower.penup()
flower.goto(0, 0)
flower.pendown()
flower.circle(100)

# Hiding the turtle
flower.hideturtle()

# Keeping the window open
turtle.done()
