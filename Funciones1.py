import turtle

def cuadrado(t, longitud):
    for i in range(4):
       t.forward(longitud)
       t.left(90)        

def espiral(t,longitud):
    for i in range(5):
        cuadrado(t,longitud)
        t.left(90)
        t.forward(longitud)
        longitud=longitud/2
        
turtle.setup(800,800)
wn = turtle.Screen() 
wn.bgcolor("white")
wn.title("Espiral")

miTortuga = turtle.Turtle()
miTortuga.color("blue")
espiral(miTortuga, 200)

turtle.mainloop()
turtle.done()
turtle.bye()