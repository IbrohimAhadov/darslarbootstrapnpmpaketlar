
from turtle import *

# Create a turtle instance
t = Turtle()



# Set up the turtle window
wn = Screen()
wn.bgcolor("black")



# Customize turtle appearance
t.shape("turtle")
t.color("yellow", "green")



# Draw the middle finger
t.left(90)
t.forward(40)
t.right(90)
t.circle(40, 90)
t.forward(80)
t.circle(20, 180)
t.right(180)
t.circle(20, 180)
t.right(180)
t.forward(80)
t.circle(20, 180)
t.forward(80)
t.right(180)
t.circle(20, 180)
t.forward(80)
t.right(180)

t.penup()
t.forward(40)
t.pendown()

t.circle(20, 180)
t.left(50)
t.forward(50)
t.right(50)
t.circle(40, 90)
t.right(90)
t.forward(40)
t.left(90)
t.forward(80)



# Finish drawing
done()
