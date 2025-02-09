import turtle

turtle.shape("turtle")

def square(x, y, a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    turtle.color("blue")
    turtle.begin_fill()
    
    turtle.circle(a)

    turtle.end_fill()
    

def main():
    square(0, 0, 200)
    turtle.done()
    

main()