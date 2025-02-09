import turtle

turtle.shape("turtle")

def square(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.color("indigo")
    turtle.begin_fill()

    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

        turtle.forward(a)
        turtle.right(90)
    
        turtle.forward(b)
        turtle.left(90)

    turtle.end_fill()
    

def main():
    square(0, -200, 200, 100)
    turtle.done()

main()