import turtle
import math

# Создаем экран
screen = turtle.Screen()
screen.bgcolor("white")  # Белый фон

# Настройка черепахи
tri = turtle.Turtle()
tri.shape("turtle")
tri.speed(1)  # Устанавливаем максимальную скорость, чтобы рисование было мгновенным

# Убираем контур, устанавливаем цвет пера и заливки
tri.pensize(0)  # Убираем толщину пера
tri.pencolor("white")  # Убираем черный контур, устанавливаем цвет пера в белый

# Длины сторон
hypotenuse = 100
cathetus = 50 * (2 ** 0.5)
side_1 = (50 * (2 ** 0.5)) / 2
side_2 = 50
#----------------------------------------------------------------------------------------------
tri.right(45)
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

tri.left(45)
tri.forward(cathetus)
tri.left(135)
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

tri.right(60)
tri.forward(side_2)
tri.left(135)

def triangle4():
    # Устанавливаем цвет заливки
    tri.fillcolor("DarkGoldenrod1")
    tri.begin_fill()
    tri.forward(cathetus)
    tri.left(135)
    tri.forward(side_2)
    tri.left(90)
    tri.forward(side_2)
    tri.end_fill()
triangle4()

tri.right(180)
tri.forward(side_2)
tri.left(15)
tri.forward(hypotenuse)
tri.right(140)

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

tri.right(130)
tri.forward(hypotenuse-cathetus)
tri.left(135)
tri.forward(cathetus)
tri.right(135)
tri.forward(side_2)
tri.right(180)

def triangle5():
    # Устанавливаем цвет заливки
    tri.fillcolor("DarkOrange")
    tri.begin_fill()
    tri.forward(side_2)
    tri.left(135)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.end_fill()
triangle5()

tri.right(180)


def square():
    tri.fillcolor("brown1")
    tri.begin_fill()
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.left(90)
    tri.forward(side_1)
    tri.end_fill()
square()

tri.right(180)
tri.forward(side_1)
tri.right(90)
tri.forward(side_1*2)
tri.left(90)
tri.forward(side_1)
tri.right(180)

def parallelogram():
    # Устанавливаем цвет заливки
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
