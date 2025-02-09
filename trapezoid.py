import turtle

turtle.shape("turtle")

def square(x, y, a, b, c):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.color("silver")
    turtle.begin_fill()
    
    turtle.forward(a)
    turtle.left(120)

    turtle.forward(b)
    turtle.left(60)
    
    turtle.forward(c)
    turtle.left(60)

    turtle.forward(b)
    turtle.left(120)
    
    turtle.end_fill()
    
def main():
    square(0, 0, 200, 100, 100)
    turtle.done()

main()