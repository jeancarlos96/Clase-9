import turtle
import os
 
 
win=turtle.Screen()
win.bgcolor("blue")
t = turtle.Pen()
t.reset()
t.color(1,0,0)
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(30)
t.right(90)
t.forward(30)
t.left(90)
t.forward(150)
t.right(90)
t.forward(75)
t.right(90)
t.forward(30)
t.right(90)
t.forward(40)
t.left(90)
t.forward(120)
t.left(30)
t.forward(30)
t.left(90)
t.forward(30)
t.end_fill()
 
t.color(0,0,0)
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
 
 
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
 
#t.begin_fill()
#t.down()
#t.circle(10)
#t.end_fill()
 
turtle.getscreen()._root.mainloop()