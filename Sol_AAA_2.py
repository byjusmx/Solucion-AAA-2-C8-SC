import turtle

def draw_star(size,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(5):
        turtle.fd(size)
        turtle.right(144)
        
draw_star(10,30,10)
draw_star(30,60,20)
draw_star(100,120,40)
