import turtle

def draw_clock():
    screen = turtle.Screen()
    t = turtle.Turtle()
    screen.setup(600,600)
    screen.bgcolor('back')
    t.pensize(2)
    t.shape('arrow')
    t.penup()
    t.pencolor('white')

    num=0
    for i in range(12):
        num +=1
        t.penup()
        t.setheading(-30 * i + 60)
        t.forward(134)
        t.pendum()
        t.forward(24)
        t.penup()
        t.forward(35)
        t.write(str(num), font=("Arial", 14, "bold"), alian="center")
        if num == 12:
            num = 0
        t.home()
    t.home()
    t.setpos(0, -250)
    t.pendown()
    t.pensize(7)
    t.pencolor('white')
    t.circle(250)
    t.penup()
    t.setpos(150, -290)
    t.pendown()
    t.hideturtle()
draw_clock()
turtle.done()

