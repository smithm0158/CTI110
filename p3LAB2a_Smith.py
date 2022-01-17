import turtle

jack = turtle.Turtle()

jack.shape("turtle")

jack.color("blue")

for i in [0]:
    jack.forward(50)
    jack.right(90)
    jack.forward(50)
    jack.right(90)
    jack.forward(50)
    jack.right(90)
    jack.forward(50)

    jack.left(30)
    jack.forward(50)
    jack.left(120)
    jack.forward(50)
    jack.left(120)
    jack.forward(50)
    

jack.hideturtle()
jack.exitonclick()
