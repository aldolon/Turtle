import turtle

turtle.shape("turtle")

def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.color("orange")
    turtle.begin_fill()
    
    turtle.left(30)
    turtle.forward(a)
    
    turtle.left(120)
    turtle.forward(a)
    
    turtle.left(120)
    turtle.forward(a)

    turtle.left(90)
    
    turtle.end_fill()
    

def main():
    square(0, 0, 200)
    turtle.done()

main()