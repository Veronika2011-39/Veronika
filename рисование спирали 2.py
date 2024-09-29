# рисование круглой спирали
import turtle
t = turtle.Pen()
# можно задать от 2 до 6 граней
sides = eval(input("введите количество сторон от 2 до 6:"))
turtle.bgcolor ("black")
colors=["red","yellow","blue","green","orange","purple"]
for x in range (360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
 
input ()
    
