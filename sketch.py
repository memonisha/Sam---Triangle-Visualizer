from p5 import *


def setup():
    createCanvas(windowWidth,windowHeight)
    global a, b, c
    a=createMovableCircle(200,250,20)
    b=createMovableCircle(150,200,20)
    c=createMovableCircle(250,200,20)

def draw():
    global a,b,c
    background("black")
    drawTickAxes()
    fill("teal")
    a.draw()
    fill("lime")
    b.draw()
    fill("purple")
    c.draw()
