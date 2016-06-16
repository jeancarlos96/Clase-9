import turtle 
t=turtle.Pen()

#for x in range (1,9):
	#t.forward(100)
	#t.left(225)

##t.reset()


#turtle.getscreen()._root.mainloop()

## dibujar ingresando el numero de lados

x=int(input("ingrese un numero: "))
grado =360/x

for x in range (0, x):
	t.forward(100)
	t.left(grado)

turtle.getscreen()._root.mainloop()