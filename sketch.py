from p5 import *


def setup():
    createCanvas(windowWidth,windowHeight)
    global a, b, c
    a=createMovableCircle(200,250,20)
    b=createMovableCircle(150,200,20)
    c=createMovableCircle(250,200,20)

def draw():
    global a,b,c,yellow,blue,red, A,B,C
    background("black")
    drawTickAxes()
    
    noStroke()
    fill("teal")
    a.draw()
    fill("lime")
    b.draw()
    fill("purple")
    c.draw()

    #displaying the coordinates
    displayDotposition(a,100,450,"teal")
    displayDotposition(b,100,425,"lime")
    displayDotposition(c,100,400,"purple")

    
    maketriangle(a,b,c)

    #finding and dispplaying distances
    yellow = findDistance(a,b)
    displayDistance(a,b,yellow,"yellow")
    
    blue = findDistance(b,c)
    displayDistance(b,c,blue,"blue")
    
    red = findDistance(a,c)
    displayDistance(a,c,red,"red")
    
    triangleType()
    displayAngle()
    
    fill("purple")
    stroke("white")
    strokeWeight(2)
    textSize(10)
    text(A,c.x,c.y)
    
    fill("teal")
    stroke("white")
    strokeWeight(2)
    textSize(10)
    text(B,a.x,a.y)
    
    fill("lime")
    stroke("black")
    strokeWeight(2)
    textSize(10)
    text(C,b.x,b.y)
    
    

def maketriangle(a,b,c): #functions with parameters
    strokeWeight(3)
    stroke("yellow")
    line(a.x,a.y,b.x,b.y)
    stroke("blue")
    line(b.x,b.y,c.x,c.y)
    stroke("red")
    line(c.x,c.y,a.x,a.y)


    
def findDistance(a,b): #this function has a return statement
    # a and b here are local variables
    dist = int(sqrt((a.x - b.x)**2 + (a.y - b.y)**2))
    return dist
    # we can also do  #type casting-changing the datatype

def displayDistance(a,b,dis,color):
    midx = (a.x+b.x)/2
    midy = (a.y+b.y)/2
    noStroke()
    fill("black")
    rect(midx,midy-5,15,15)
    fill(color)
    textSize(10)
    text(dis,midx,midy)
    
def displayDotposition(a,p,q,color):
    fill(color)
    textSize(20)
    text(f"({a.x},{a.y})",p,q)


# if all three same-1st
#  if R

def triangleType():
    global yellow,blue,red
 
    if yellow == blue and yellow == red and blue == red:
        triangleside = "equilateral"

    elif yellow != blue and blue != red and red != yellow:
        triangleside = "scalene"
    else:
        triangleside = "isosceles"
    textSize(30)
    fill("pink")
    text(f"Triangle is {triangleside}",100,650)

def displayAngle():
    global yellow, blue, red,A,B,C
    a=yellow
    b=blue
    c=red
    a2=a**2
    b2=b**2
    c2=c**2
    #Python's Exception handling 
    try:
        A = round(acos((b2+c2-a2)/(2*b*c)))
        B = round(acos((a2+c2-b2)/(2*a*c)))
        C = 180 - A - B
        print(A, B, C)
        #B- teal one
        #C-lime one
        #A -purple one
        if A == 90 or B == 90 or C == 90:
            angle = "right"
        elif A >90 or B > 90 or C > 90:
            angle = "obtuse"
        else:
            angle = "acute"
        textSize(30)
        fill("orange")
        text(f"Triangle is {angle} angled",100,600)
    except:
        fill("white")
        textSize(40)
        text("NOT A TRIANGLE ANYMORE",50,500)

    
    