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

# Устанавливаем цвет заливки
tri.fillcolor("DarkCyan")
tri.begin_fill()

# Длины сторон
hypotenuse = 100  # Катет
cathetus = 50 * (2 ** 0.5)  # Гипотенуза (основание)

# Разворачиваем на 90 градусов вправо
tri.right(90)

# Рисуем треугольник
tri.forward(hypotenuse)  
tri.left(135)  
tri.forward(cathetus)  
tri.left(90)
tri.forward(cathetus)  
tri.left(135)


tri.end_fill()
tri.left(90)
#------------------------------------------------------------------
# Устанавливаем цвет заливки
tri.fillcolor("CornflowerBlue")
tri.begin_fill()

# Рисуем треугольник
tri.right(45)
tri.forward(cathetus)  
tri.left(90)  
tri.forward(cathetus)  
tri.left(135)
tri.forward(hypotenuse)  
tri.left(135)

tri.end_fill()
tri.forward(cathetus) 
#------------------------------------------------------------------
# Устанавливаем цвет заливки
tri.fillcolor("coral1")
tri.begin_fill()

# Длины сторон
side_1= (50 * (2 ** 0.5))/2

# Рисуем квадрат
tri.forward(side_1)
tri.left(90)  
tri.forward(side_1)
tri.left(90)
tri.forward(side_1)
tri.left(90)
tri.forward(side_1)

tri.end_fill()
#------------------------------------------------------------------
# Устанавливаем цвет заливки
tri.fillcolor("DarkOrange")
tri.begin_fill()

# Длины сторон
side_2 = 50
# Рисуем треугольник
tri.forward(side_1)
tri.left(135)
tri.forward(side_2)
tri.left(135)
tri.forward(side_1)

tri.end_fill()
tri.left(90)
tri.forward(side_1)
#------------------------------------------------------------------
# Устанавливаем цвет заливки
tri.fillcolor("CadetBlue3")
tri.begin_fill()

# Рисуем параллелограмм
tri.forward(side_1)
tri.left(135)
tri.forward(side_2)
tri.left(45)
tri.forward(side_1)
tri.left(135)
tri.forward(side_2)

tri.end_fill()
tri.right(135)
tri.forward(2*side_1)
tri.right(90)
#------------------------------------------------------------------
# Устанавливаем цвет заливки
tri.fillcolor("DarkOliveGreen4")
tri.begin_fill()

# Рисуем треугольник
tri.forward(side_1)
tri.left(135)
tri.forward(side_2)
tri.left(135)
tri.forward(side_1)

tri.end_fill()
tri.left(90)
tri.forward(side_1)
tri.right(90)
#------------------------------------------------------------------
# Устанавливаем цвет заливки
tri.fillcolor("burlywood4")
tri.begin_fill()

# Рисуем треугольник
tri.forward(cathetus)
tri.left(135)
tri.forward(side_2)
tri.left(90)
tri.forward(side_2)

tri.end_fill()
tri.right(90)

# Скрываем черепаху
tri.hideturtle()

# Ожидаем, пока пользователь не закроет окно
screen.mainloop()
