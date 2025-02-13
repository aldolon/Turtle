import turtle
import math

# Создаем экран
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

def triangle1():
    tri.fillcolor("BlueViolet")
    tri.begin_fill()
    tri.forward(cathetus)
    tri.left(90)
    tri.forward(cathetus)
    tri.left(135)
    tri.forward(hypotenuse)
    tri.end_fill()
triangle1()

tri.left(180)
tri.forward(hypotenuse)
tri.left(90)

def triangle2():
    tri.fillcolor("CornflowerBlue")
    tri.begin_fill()
    tri.forward(cathetus)
    tri.left(135)
    tri.forward(hypotenuse)
    tri.left(135)
    tri.forward(cathetus)
    tri.end_fill()
triangle2()

tri.left(180)
tri.forward(cathetus)
tri.right(135)
tri.forward(30)

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

tri.left(90)
tri.forward(hypotenuse-50)
tri.left(90)

def square():
    tri.fillcolor("brown1")
    tri.begin_fill()
    tri.forward(side_1)
    tri.right(90)
    tri.forward(side_1)
    tri.right(90)
    tri.forward(side_1)
    tri.right(90)
    tri.forward(side_1)
    tri.end_fill()
square()

tri.left(180)
tri.forward(side_1)

def parallelogram():
    # Устанавливаем цвет заливки
    tri.fillcolor("DarkCyan")
    tri.begin_fill()
    tri.forward(side_2)
    tri.left(45)
    tri.forward(side_1)
    tri.left(135)
    tri.forward(side_2)
    tri.left(45)
    tri.forward(side_1)
    tri.end_fill()
parallelogram()

tri.left(225)

def triangle4():
    # Устанавливаем цвет заливки
    tri.fillcolor("DarkGoldenrod1")
    tri.begin_fill()
    tri.forward(side_2)
    tri.right(90)
    tri.forward(side_2)
    tri.right(135)
    tri.forward(cathetus)
    tri.end_fill()
triangle4()

tri.right(45)
tri.forward(side_1-(hypotenuse - 30 - 50))
tri.left(45)
tri.forward(cathetus)
tri.right(45)
tri.forward(10)

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

tri.right(135)

tri.hideturtle()
screen.mainloop()