
# from turtle import *

# # Create a turtle instance
# t = Turtle()



# # Set up the turtle window
# wn = Screen()
# wn.bgcolor("black")



# # Customize turtle appearance
# t.shape("turtle")
# t.color("yellow", "green")



# # Draw the middle finger
# t.left(90)
# t.forward(40)
# t.right(90)
# t.circle(40, 90)
# t.forward(80)
# t.circle(20, 180)
# t.right(180)
# t.circle(20, 180)
# t.right(180)
# t.forward(80)
# t.circle(20, 180)
# t.forward(80)
# t.right(180)
# t.circle(20, 180)
# t.forward(80)
# t.right(180)

# t.penup( )
# t.forward(40)
# t.pendown()

# t.circle(20, 180)
# t.left(50)
# t.forward(50)
# t.right(50)
# t.circle(40, 90)
# t.right(90)
# t.forward(40)
# t.left(90)
# t.forward(80)



# # Finish drawing
# done()

# #.....draw letter P with python turtle........!
# import turtle
# t=turtle.Turtle()
# t.penup()
# t.goto(-30,50) #centering in the screen
# t.pendown()
# t.pensize(10)
# t.pencolor("red")
# t.right(90)
# t.forward(150)
# t.goto(-30,50)
# t.circle(50,None,100)







# #import turtle
# import turtle


# #import turtle as t
# t=turtle.Turtle()
# scr=turtle.getscreen()
# scr.bgcolor("SkyBlue1")

# #create the body of house
# t.penup()
# t.pensize(3)
# t.color("black","yellow")
# t.begin_fill()
# t.goto(-200,-150)
# t.pendown()
# t.forward(400)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(400)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.end_fill()

# #create partiton
# t.forward(100)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(100)
# t.end_fill()

# #create roof
# t.color("black","brown")
# t.begin_fill()
# t.right(120)
# t.forward(100)
# t.right(120)
# t.forward(100)
# t.end_fill()
# t.begin_fill()
# t.backward(100)
# t.left(60)
# t.forward(300)
# t.right(60)
# t.forward(100)
# t.end_fill()

# #create door
# t.penup()
# t.goto(-200,-150)
# t.setheading(0)
# t.pendown()
# t.color("black","pink")
# t.forward(230)
# t.left(90)
# t.begin_fill()
# t.forward(90)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(90)
# t.end_fill()
# t.penup()

# #create left window1
# t.goto(-60,-50)
# t.pendown()
# t.color("black","pink")
# t.begin_fill()
# t.backward(50)
# t.left(90)
# t.forward(60)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(60)
# t.right(90)
# t.forward(25)
# t.right(90)
# t.forward(60)
# t.backward(30)
# t.right(90)
# t.forward(25)
# t.backward(50)
# t.end_fill()


# #creqte right window
# t.penup()
# t.setheading(270)
# t.goto(100,-50)
# t.pendown()
# t.color("black","pink")
# t.begin_fill()
# t.backward(50)
# t.left(90)
# t.forward(60)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(60)
# t.right(90)
# t.forward(25)
# t.right(90)
# t.forward(60)
# t.backward(30)
# t.right(90)
# t.forward(25)
# t.backward(50)
# t.end_fill()
# t.penup()

# #grass
# t.color("black","green")
# t.goto(-650,-150)
# t.left(90)
# t.pendown()
# t.begin_fill()
# t.forward(1300)
# t.right(90)
# t.forward(180)
# t.right(90)
# t.forward(1300)
# t.right(90)
# t.forward(180)
# t.end_fill()
# t.penup()

# #create circle of sun
# t.goto(-500,150)
# t.pendown()
# t.color("yellow","yellow")
# t.begin_fill()
# t.circle(45)
# t.end_fill()
# t.goto(-545,150)

# #create sunrays
# t.pensize(5)
# for i in range(12):
#         t.forward(80)
#         t.backward(80)
#         t.left(30)
# t.penup()

# #create clouds
# t.goto(500,160)
# t.pendown()
# t.color("white","white")
# t.setheading(90)
# t.begin_fill()
# t.circle(60,180)
# t.end_fill()
# t.goto(440,160)
# t.setheading(90)
# t.begin_fill()
# t.circle(80,180)
# t.end_fill()

#  uychizish tugashi turtle.done()



# from turtle import *


# # Doraemon with Python Turtle
# def ankle(x, y):
#     penup()
#     goto(x, y)
#     pendown()


# def eyes():
#     fillcolor("#ffffff")
#     begin_fill()

#     tracer(False)
#     a = 2.5
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a -= 0.05
#             lt(3)
#             fd(a)
#         else:
#             a += 0.05
#             lt(3)
#             fd(a)
#     tracer(True)
#     end_fill()


# def daari():
#     ankle(-32, 135)
#     seth(165)
#     fd(60)

#     ankle(-32, 125)
#     seth(180)
#     fd(60)

#     ankle(-32, 115)
#     seth(193)
#     fd(60)

#     ankle(37, 135)
#     seth(15)
#     fd(60)

#     ankle(37, 125)
#     seth(0)
#     fd(60)

#     ankle(37, 115)
#     seth(-13)
#     fd(60)


# def mukh():
#     ankle(5, 148)
#     seth(270)
#     fd(100)
#     seth(0)
#     circle(120, 50)
#     seth(230)
#     circle(-120, 100)


# def scarf():
#     fillcolor('#e70010')
#     begin_fill()
#     seth(0)
#     fd(200)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     fd(207)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     end_fill()


# def nose():
#     ankle(-10, 158)
#     seth(315)
#     fillcolor('#e70010')
#     begin_fill()
#     circle(20)
#     end_fill()


# def black_eyes():
#     seth(0)
#     ankle(-20, 195)
#     fillcolor('#000000')
#     begin_fill()
#     circle(13)
#     end_fill()

#     pensize(6)
#     ankle(20, 205)
#     seth(75)
#     circle(-10, 150)
#     pensize(3)

#     ankle(-17, 200)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(5)
#     end_fill()
#     ankle(0, 0)


# def face():
#     fd(183)
#     lt(45)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(120, 100)
#     seth(180)
#     # print(pos())
#     fd(121)
#     pendown()
#     seth(215)
#     circle(120, 100)
#     end_fill()
#     ankle(63.56, 218.24)
#     seth(90)
#     eyes()
#     seth(180)
#     penup()
#     fd(60)
#     pendown()
#     seth(90)
#     eyes()
#     penup()
#     seth(180)
#     fd(64)


# def taauko():
#     penup()
#     circle(150, 40)
#     pendown()
#     fillcolor('#00a0de')
#     begin_fill()
#     circle(150, 280)
#     end_fill()


# def Doraemon():
#     taauko()

#     scarf()

#     face()

#     nose()

#     mukh()

#     daari()

#     ankle(0, 0)

#     seth(0)
#     penup()
#     circle(150, 50)
#     pendown()
#     seth(30)
#     fd(40)
#     seth(70)
#     circle(-30, 270)

#     fillcolor('#00a0de')
#     begin_fill()

#     seth(230)
#     fd(80)
#     seth(90)
#     circle(1000, 1)
#     seth(-89)
#     circle(-1000, 10)

#     # print(pos())

#     seth(180)
#     fd(70)
#     seth(90)
#     circle(30, 180)
#     seth(180)
#     fd(70)

#     # print(pos())
#     seth(100)
#     circle(-1000, 9)

#     seth(-86)
#     circle(1000, 2)
#     seth(230)
#     fd(40)

#     # print(pos())

#     circle(-30, 230)
#     seth(45)
#     fd(81)
#     seth(0)
#     fd(203)
#     circle(5, 90)
#     fd(10)
#     circle(5, 90)
#     fd(7)
#     seth(40)
#     circle(150, 10)
#     seth(30)
#     fd(40)
#     end_fill()

#     seth(70)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(-30)
#     end_fill()

#     ankle(103.74, -182.59)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(-15, 180)
#     fd(90)
#     circle(-15, 180)
#     fd(10)
#     end_fill()

#     ankle(-96.26, -182.59)
#     seth(180)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(15, 180)
#     fd(90)
#     circle(15, 180)
#     fd(10)
#     end_fill()

#     ankle(-133.97, -91.81)
#     seth(50)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(30)
#     end_fill()
#     # Doraemon with Python Turtle

#     ankle(-103.42, 15.09)
#     seth(0)
#     fd(38)
#     seth(230)
#     begin_fill()
#     circle(90, 260)
#     end_fill()

#     ankle(5, -40)
#     seth(0)
#     fd(70)
#     seth(-90)
#     circle(-70, 180)
#     seth(0)
#     fd(70)

#     ankle(-103.42, 15.09)
#     fd(90)
#     seth(70)
#     fillcolor('#ffd200')
#     # print(pos())
#     begin_fill()
#     circle(-20)
#     end_fill()
#     seth(170)
#     fillcolor('#ffd200')
#     begin_fill()
#     circle(-2, 180)
#     seth(10)
#     circle(-100, 22)
#     circle(-2, 180)
#     seth(180 - 10)
#     circle(100, 22)
#     end_fill()
#     goto(-13.42, 15.09)
#     seth(250)
#     circle(20, 110)
#     seth(90)
#     fd(15)
#     dot(10)
#     ankle(0, -150)

#     black_eyes()


# if __name__ == '__main__':
#     screensize(800, 600, "#f0f0f0")
#     pensize(3)
#     speed(9)
#     Doraemon()
#     ankle(100, -300)
#     mainloop()
    



import turtle
from turtle import *

turtle.title("rainbow spiral")
speed(20)
bgcolor("black")
r,g,b=255,0,0

for i in range(255*5):
    colormode(255)
    if i<255//3:
        g+=3
    elif i<255*2//3:
        r-=3
    elif i<255:
        b+=3
    elif i<255*4//3:
        g-=3
    elif i<255*5//3:
        r+=3
    else:
        b-=3
    fd(50+i)
    rt(91)
    pencolor(r,g,b)

done()




# import turtle
import colorsys

def draw_one_color_arc(x,y,r,pensize,color):
    turtle.up()
    turtle.goto(x+r,y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(pensize)
    turtle.pencolor(color)
    turtle.circle(r,180)


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor('light blue')
turtle.title('Rainbow In Python Turtle')
turtle.setup(1000,1000)
num_colors = 49

radius = 300
penwidth = 50*8/num_colors
hue = 0

for i in range(num_colors):
    (r,g,b) = colorsys.hsv_to_rgb(hue,1,1)
    draw_one_color_arc(0,-100,radius,penwidth,(r,g,b))
    radius -= (penwidth-1)
    hue += 0.2/num_colors

turtle.done()