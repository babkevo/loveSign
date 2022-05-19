from turtle import *
import turtle
tur = turtle.Screen()
tur.bgcolor("black")
tur.title("JamesN Love")

color("red")
begin_fill()
left(50)
forward(100)
circle(40, 180)
left(260)
circle(40, 180)
forward(100)
end_fill()

loadWindow = turtle.Screen()
turtle.speed(2)

for i in range(100):
    turtle.circle(5 * i)
    turtle.circle(-5 * i)
    turtle.left(i)

turtle.exitonclick()

done()