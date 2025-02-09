import turtle

turtle.shape("turtle")

def square(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.color("green")
    turtle.begin_fill()

    turtle.left(90)
    turtle.forward(a)

    turtle.left(90)
    turtle.forward(b)

    turtle.left(90)
    turtle.forward(a)

    
    turtle.left(90)
    turtle.forward(b)


    turtle.end_fill()
    

def main():
    square(0, 0, 200, 100)
    turtle.done()

main()