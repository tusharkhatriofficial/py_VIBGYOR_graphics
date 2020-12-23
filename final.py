import turtle

def loop(colour, radius):
    art=turtle.Turtle()
    art.begin_fill()
    art.color(colour)
    art.circle(radius)
    art.end_fill()
    
loop("violet", 150)
loop("indigo", 130)
loop("blue", 110)
loop("green", 90)
loop("yellow", 70)
loop("orange", 50)
loop("red", 30)


