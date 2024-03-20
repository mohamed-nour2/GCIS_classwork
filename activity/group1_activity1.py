from turtle import Screen,Turtle
"""

Group: 1
   Author1:Abebe Endalamie
   Part: Contributed with the "pattern" function and the "main" 
   function and also added "to_east" function to 
   make the pattern function more better. And helped with comments

   Author2 : Mohame Nour
   Part: contibuted with the "square" function and the "setPos" function, 
   also the comments for the 2 functions.

   Author3: Quasim Mabrouk  
   Part:Contributed with the hexagon and circle. Also helped with the comments. 

   Manifesto: This is a program is written to draw a hexagon,
  circle and square in a pattern in a row; and repeat the pattern two more times at different positions

    
    """

def hexagon(turta, hexagon_color, border_color):
    """ Draws hexagon with a given side_lengh and a given border_color
      and fills it with a given hex_color."""
    
    turta.pencolor(border_color)
    turta.fillcolor(hexagon_color)
    turta.begin_fill()
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.left(60)
    turta.forward(50)
    turta.end_fill()

   
def square(turta, square_color, border_color):
    """
    Draws square with a give side_length and a given border_color
    and fills it with a given square_color
    """
    turta.pencolor(border_color) # i set the pencolor to its border color
    turta.fillcolor(square_color) # setting the fillcolor to the square color
    turta.begin_fill()
    
    turta.forward(90)# move forward 90
    turta.left(90)# turn left 90 degrees
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.left(90)
    turta.forward(90)
    turta.end_fill()#ending filling the square
    
   
def circle(turta, circle_color, border_color):
    """
    Draws a circle with a given radius and a given border_color and 
    fills it with a given circle_color
    """
    turta.pencolor(border_color)
    turta.fillcolor(circle_color)
    turta.begin_fill()
    turta.circle(45)
    turta.end_fill()

def setPos(turta, x, y):
    """
    Sets the turtle to the given x and y coordinate value without any trace.
    
    """
    # using x,y coordinates to set the turtle to
    turta.penup()
    turta.setheading(0)# set its heading to 0 facing east direction
    turta.goto(x, y)# turtle will be set to spacific coordinates
    turta.pendown()

def to_east(turta, magnitude):
    """
    Takes the turtle 'distance' units to the east without any trace
    """
    turta.setheading(0)
    turta.penup()
    turta.forward(magnitude)

   


 
def pattern(turta, hex_color, squ_color, cir_color, border_color):
    """
    
    Draws a hexagon filled with  hexa_color color first followed by a circle filled with circle_color
    then followed by a square filled with square_color.
    
    """
    
    hexagon(turta, hex_color,  border_color)
    to_east(turta, 160)

    circle(turta, cir_color, border_color)
    to_east(turta, 85)
    
    square(turta, squ_color, border_color)

   



def main():
    """
    is used to call the pattern function three times.
    """
    hexagon_color = input("enter the color of hexagon: ")
    circle_color = input("enter the color of circle: ")
    square_color = input("enter the color of square: ")
    border_color = input("enter the color of border: ")
    win = Screen()
    turta = Turtle()
    win.title("ACTIVITY_1")
    win.bgcolor("#3a1f61")
    turta.speed(10)

    setPos(turta, -300, 200)
    pattern(turta, hexagon_color, square_color,circle_color, border_color)
    setPos(turta, -200, 60)
    pattern(turta, hexagon_color, square_color,circle_color, border_color)
    setPos(turta, -100, -80)
    pattern(turta, hexagon_color, square_color,circle_color, border_color)

    win.exitonclick()
   
  

main()
    




