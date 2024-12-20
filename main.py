import turtle

def getXLines(x, y, cubewidth):
    xlines = []
    i = -(x/2)

    while i <= x/2:
        xlines.append(int(i))
        i += cubewidth
    return xlines

def getYLines(x, y, cubewidth):
    ylines =[]
    i = (y/2)

    while i >= -(y/2):
        ylines.append(int(i))
        i -= cubewidth

    return ylines

def drawGrid(t, x, y):
    CUBEWIDTH = 100
    
    t.penup()
    t.goto(-(x/2), (y/2))

    xlines = getXLines(x, y, CUBEWIDTH)
    ylines = getYLines(x, y, CUBEWIDTH)


    # draw each line on y axis
    t.right(90)

    for i in xlines:
        t.goto(i, (y/2))

        t.pendown()
        t.forward(y)
        t.penup()

    # draw each line on y axis
    t.left(90)
    
    for i in ylines:
        t.goto(-(x/2), i)

        t.pendown()
        t.forward(x)
        t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(500 + 4, 500 + 8)
    
    john = turtle.Turtle()
    john.speed(696969)

    drawGrid(john, 500, 500)


if __name__ == "__main__":
    main()
