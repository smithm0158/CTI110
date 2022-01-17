import turtle

john = turtle.Turtle()

john.shape("turtle")
john.color("orange")
john.pensize(5)

john.penup()
john.left(180)
john.forward(300)

john.pendown()
john.right(120)
john.forward(100)
john.right(120)
john.forward(50)
john.left(120)
john.forward(50)
john.right(120)
john.forward(100)

john.penup()
john.left(60)
john.forward(100)
john.pendown()

for i in range(8):
    john.left(20)
    john.forward(10)
john.right(20)
for i in range(8):
    john.right(20)
    john.forward(10)
    
