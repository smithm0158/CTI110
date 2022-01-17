import turtle
import random

risu = turtle.Turtle()
risu.speed(15)

#list of colors
sfcolor = ["white", "blue", "orange", "magenta"]

#function for actual snowflake
def snowflake (size):
    #move the pen into starting position
    risu.penup()
    risu.forward(10*size)
    risu.left(45)
    risu.pendown()
    risu.color(random.choice(sfcolor))

    for i in range(8):
        branch(size)
        risu.left(45)
        
def branch(size):
    for i in range(3):
        for i in range(3):
            risu.forward(10.0*size/3)
            risu.backward(10.0*size/3)
            risu.right(45)
        risu.left(90)
        risu.backward(10.0*size/3)
        risu.left(45)
    risu.right(90)
    risu.forward(10.0*size)

#creates many different snowflakes
for i in range(20):
    x=random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    risu.penup()
    risu.goto(x,y)
    risu.pendown()
    snowflake(sf_size)
