import turtle


def moveforward():
    turtle.forward(10)
    with open('textul.txt', 'a') as fisier:
        fisier.write("w")


def movebackwards():
    turtle.backward(10)
    with open('textul.txt', 'a') as fisier:
        fisier.write("s")


def right():
    turtle.right(45)
    with open('textul.txt', 'a') as fisier:
        fisier.write("d")


def left():
    turtle.left(45)
    with open('textul.txt', 'a') as fisier:
        fisier.write("a")


def upwards():
    turtle.up()
    with open('textul.txt', 'a') as fisier:
        fisier.write("f")


def downwards():
    turtle.down()
    with open('textul.txt', 'a') as fisier:
        fisier.write("g")


def clear_screen():
    turtle.clear()
    with open('textul.txt', 'a') as fisier:
        fisier.write("c")


def deseneaza_din_taste():
    turtle.home()
    turtle.clear()
    turtle.onkey(moveforward, 'w')
    turtle.onkey(movebackwards, 's')
    turtle.onkey(right, 'd')
    turtle.onkey(left, 'a')
    turtle.onkey(upwards, 'f')
    turtle.onkey(downwards, 'g')
    turtle.onkey(exit, 'Return')
    turtle.onkey(clear_screen, 'c')
    turtle.listen()
    turtle.done()
