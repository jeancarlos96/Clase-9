from tkinter import* 
tk=Tk()
canvas= Canvas(tk, width=500, height=500)
canvas.pack()

my_image= PhotoImage(file="ball.gif")
canvas.create_image(100,100, ancho=NW, image=my_image)

canvas.create_image(100,300, ancho=NW, image=my_image)

canvas.create_image(200,50, ancho=NW, image=my_image)

canvas.create_image(10,150, ancho=NW, image=my_image)
tk.mainloop()