import turtle
import math

# Создаем экран
screen = turtle.Screen()
screen.bgcolor("white")  # Белый фон

# Настройка черепахи
tri = turtle.Turtle()

tri.speed(0)  # Устанавливаем максимальную скорость, чтобы рисование было мгновенным

# Убираем контур, устанавливаем цвет пера и заливки
tri.pensize(0)  # Убираем толщину пера
tri.pencolor("white")  # Убираем черный контур, устанавливаем цвет пера в белый

# Задаем длины сторон
hypotenuse = 100
cathetus = 50 * (2 ** 0.5)
side_1 = (50 * (2 ** 0.5)) / 2
side_2 = 50


# Рисуем параллелограм 
def parallelogram():
    # Устанавливаем цвет заливки
    tri.fillcolor("DarkCyan")
    tri.begin_fill()
    tri.forward(side_1)
    tri.left(45)
    tri.forward(side_2)
    tri.left(135)
    tri.forward(side_1)
    tri.left(45)
    tri.forward(side_2)
    tri.end_fill()
parallelogram()

tri.left(135)
tri.forward(side_1)
tri.left(45)
tri.forward(side_2)
tri.left(135)

#Рисуем квадрат
def square():
    tri.fillcolor("brown1")
    tri.begin_fill()
    tri.left(45)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.left(90)
    tri.end_fill()
square()
tri.left(90)
tri.forward(side_1)
tri.left(270)

# Рисуем Треугольник (1)

def triangle1():

    tri.fillcolor("BlueViolet")
    tri.begin_fill()
    tri.forward(hypotenuse)
    tri.left(135)
    tri.forward(cathetus)
    tri.left(90)
    tri.forward(cathetus)
    tri.end_fill()
triangle1()

tri.left(135)
tri.forward(hypotenuse)
tri.left(45)
tri.forward(cathetus)
tri.left(135)

# Рисуем треугольник (2)
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
#Рисуем Треугольник (4)

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

tri.left(180)
tri.forward(side_2)
tri.left(315)
tri.forward(side_1)
tri.left(180)

#Рисуем треугольник (3)
def triangle3():

    tri.fillcolor("chartreuse3")
    tri.begin_fill()
    tri.forward(side_1)
    tri.left(135)
    tri.forward(side_2)
    tri.left(135)
    tri.forward(side_1)
    tri.end_fill()
triangle3()

tri.left(225)

#Рисуем Треугольник (5)
def triangle5():

    tri.fillcolor("DarkOrange")
    tri.begin_fill()
    tri.forward(side_2)
    tri.left(135*(-1))
    tri.forward(side_1)
    tri.left(90*(-1))
    tri.forward(side_1)
    tri.end_fill()
    
    tri.left(270)
triangle5()
turtle.getscreen()._root.mainloop()
screen.mainloop