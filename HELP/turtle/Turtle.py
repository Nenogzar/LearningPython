import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

for i in range(3):
    my_turtle.left(30)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)

    my_turtle.left(-30)
    my_turtle.penup()
    my_turtle.backward(50)
    my_turtle.pendown()
    my_turtle.backward(100)
    my_turtle.penup()
    my_turtle.forward(150)
    my_turtle.pendown()

turtle.done()
turtle.mainloop()
