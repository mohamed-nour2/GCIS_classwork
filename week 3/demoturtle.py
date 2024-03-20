from  turtle import Screen, Turtle

wind = Screen ()
wind.title("turtle demo")
wind.bgcolor("red")

t = Turtle

t.pencolor("green")
t.pensize(10)
t.pendown()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.fillcolor("purple")
t.end_fill()

wind.exitonclick()

