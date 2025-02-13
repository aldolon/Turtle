import turtle
import math

# Создаем экранн
screen = turtle.Screen()
screen.bgcolor("white")  # Белый фон

# Настройка черепахи
tri = turtle.Turtle()
tri.shape("turtle")
tri.speed(0)  # Устанавливаем максимальную скорость, чтобы рисование было мгновенным

# Убираем контур, устанавливаем цвет пера и заливки
tri.pensize(0)  # Убираем толщину пера
tri.pencolor("white")  # Убираем черный контур, устанавливаем цвет пера в белый


# Длины сторон
hypotenuse = 100
cathetus = 50 * (2 ** 0.5)
side_1 = (50 * (2 ** 0.5)) / 2
side_2 = 50

tri.right(45)

def square():
    tri.fillcolor("brown1")
    tri.begin_fill()
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.end_fill()
square()

def triangle1():
    tri.fillcolor("BlueViolet")
    tri.begin_fill()
    tri.forward(cathetus)
    tri.right(135)
    tri.forward(hypotenuse)
    tri.right(135)
    tri.forward(cathetus)
    tri.right(90)
    tri.end_fill()
triangle1()

tri.forward(cathetus)

tri.right(135)

def triangle2():
    tri.fillcolor("CornflowerBlue")
    tri.begin_fill()
    tri.forward(hypotenuse)
    tri.left(135)
    tri.forward(cathetus)
    tri.left(90)
    tri.forward(cathetus)
    tri.end_fill()
triangle2()

tri.left(90)
tri.forward(30)
tri.right(155)

def triangle4():
    tri.fillcolor("DarkGoldenrod1")
    tri.begin_fill()
    tri.forward(cathetus)
    tri.left(135)
    tri.forward(side_2)
    tri.left(90)
    tri.forward(side_2)
    tri.end_fill()
triangle4()

tri.left(115)
tri.forward(30)
tri.right(90)
tri.forward(30)
tri.left(45)

def triangle3():
    tri.fillcolor("chartreuse3")
    tri.begin_fill()
    tri.forward(side_2)
    tri.left(135)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.end_fill()
triangle3()

tri.left(90)
tri.forward(cathetus-28)
tri.right(90)
tri.forward(cathetus-28)
tri.left(135)

def triangle3():
    tri.fillcolor("DarkOrange")
    tri.begin_fill()
    tri.forward(side_2)
    tri.right(135)
    tri.forward(side_1)
    tri.right(90)
    tri.forward(side_1)
    tri.end_fill()
triangle3()

tri.up()
tri.left(90)
tri.forward(30)
tri.right(90)
tri.forward(30)
tri.left(70)
tri.down()
 
tri.forward(side_2)
tri.left(45)

def parallelogram():
    tri.fillcolor("DarkCyan")
    tri.begin_fill()
    tri.forward(side_1)
    tri.left(135)
    tri.forward(side_2)
    tri.left(45)
    tri.forward(side_1)
    tri.left(135)
    tri.forward(side_2)
    tri.end_fill()
parallelogram()

tri.hideturtle()
screen.mainloop()
