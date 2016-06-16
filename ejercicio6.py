import turtle 
t=turtle.Pen()

def micuadrado(size, num):
	grad=360/num
	for x in range(0,num):
		t.forward(size)
		t.left(grad)
		
x=int(input("ingrese tamaño de un lado (en un rango de 50 - 200): "))
ld=int (input("Ingrese numero de lados "))


fig=micuadrado(x, ld)
turtle.getscreen()._root.mainloop()
