from turtle import Turtle , Screen
hexa_color = input("Enter the color for Haxagone: ")
cir_color = input("Enter the color for Circle: ")
squ_color = input("Enter the color for Square: ")
T=Turtle
def setpos(T , x , y):
    T.penup()
    T.setheading(0)
    T.goto(x,y)
    T.pendown()
   

def hexagon(T,hexa_color,border_color):
    T.fillcolor(hexa_color)
    T.begin_fill()
    T.forward(50)
    T.right(60)
    T.forward(50)
    T.right(60)
    T.forward(50)
    T.right(60)
    T.forward(50)
    T.right(60)
    T.forward(50)
    T.end_fill()
    T.color(border_color)
    T.penup()
    T.penup()
    T.goto(-200, 0)
    T.pendown()
    T.forward(50)
    T.right(90)
    T.forward(100)
    T.backward(50)
    T.left(90)
    T.backward(50)
    T.penup()
    T.goto(-150, 50)
    T.pendown()
    T.left(90)
    T.forward(100)

   
def circle(T,cir_color,border_color):
    T.fillcolor(cir_color)
    T.begin_fill()
    T.circle(45)
    T.end_fill()
    T.color(border_color)
   
def square(T,squ_color,border_color):
    T.fillcolor(squ_color)
    T.begin_fill()
    T.forward(90)
    T.left(90)
    T.forward(90)
    T.left(90)
    T.forward(90)
    T.left(90)
    T.forward(90)
    T.color(border_color)

def pattern(turta, hex_color, squ_color,cir_color, border_color):
    """
    
    """
    
    setpos(turta, -300, 300)
    hexagon(turta, hex_color,  border_color)
    setpos(turta, -140, 210)
    circle(turta, cir_color, border_color)
    setpos(turta, -55, 210)
    square(turta, squ_color, border_color)

    setpos(turta, -260, 170)
    hexagon(turta, hex_color,  border_color)
    setpos(turta, -100, 80)
    circle(turta, cir_color, border_color)
    setpos(turta, -15, 80)
    square(turta, squ_color, border_color)

    setpos(turta, -220, 40)
    hexagon(turta, hex_color,  border_color)
    setpos(turta, -60, -50)
    circle(turta, cir_color, border_color)
    setpos(turta, 25, -50)
    square(turta, squ_color, border_color)





def main ():
    t = Turtle ()
    t.speed(10)
    win = Screen()
    win.title("Group 1 Act.1")
    win.bgcolor("light blue")
    border_color = "yellow"
    
    pattern(border_color,t,hexa_color,squ_color,cir_color)
    win.exitonclick()

main ()