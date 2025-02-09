import turtle

turtle.shape("turtle")

def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.color("red")
    turtle.begin_fill()
    for i in range(6):
        turtle.left(60)
        turtle.forward(a)

    turtle.end_fill()
    

def main():
    square(0, 0, 200)
    turtle.done()

main()