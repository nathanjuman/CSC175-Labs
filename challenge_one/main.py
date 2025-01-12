#------------------------------------------------------------------------------------
#Nathan Juman, CSC-175-01
#Challenge One: Draws 5 Red 8-Pointed Stars, all with yellow circles centered inside.
#------------------------------------------------------------------------------------
import turtle

def centerStar(s, c):
    s.fillcolor("red")
    s.begin_fill()

    for i in range(8) : 
        s.right(45)
        s.forward(50)
        s.left(135)
        s.forward(50)
        s.right(45)
    s.end_fill()
        
    c.fillcolor("yellow")
    c.penup()
    c.left(90)
    c.forward(10)
    c.right(90)
    c.pendown()
    c.begin_fill()
    c.circle(40)
    c.end_fill()
    
def topStar(ts,tc):
    ts.fillcolor("red")
    ts.penup()
    ts.goto(0,171)
    ts.pendown
    ts.begin_fill()

    for i in range(8) : 
        ts.right(45)
        ts.forward(50)
        ts.left(135)
        ts.forward(50)
        ts.right(45)
    ts.end_fill()
        
    tc.fillcolor("yellow")
    tc.penup()
    tc.goto(0,171)
    tc.left(90)
    tc.forward(10)
    tc.right(90)
    tc.pendown()
    tc.begin_fill()
    tc.circle(40)
    tc.end_fill()

def bottomStar(bs,bc):
    bs.fillcolor("red")
    bs.penup()
    bs.goto(0,-171)
    bs.pendown()
    bs.begin_fill()

    for i in range(8) : 
        bs.right(45)
        bs.forward(50)
        bs.left(135)
        bs.forward(50)
        bs.right(45)
    bs.end_fill()
        
    bc.fillcolor("yellow")
    bc.penup()
    bc.goto(0,-171)
    bc.left(90)
    bc.forward(10)
    bc.right(90)
    bc.pendown()
    bc.begin_fill()
    bc.circle(40)
    bc.end_fill()

def leftStar(ls,lc):
    ls.fillcolor("red")
    ls.penup()
    ls.goto(-171,0)
    ls.pendown()
    ls.begin_fill()

    for i in range(8) : 
        ls.right(45)
        ls.forward(50)
        ls.left(135)
        ls.forward(50)
        ls.right(45)
    ls.end_fill()
        
    lc.fillcolor("yellow")
    lc.penup()
    lc.goto(-171,0)
    lc.left(90)
    lc.forward(10)
    lc.right(90)
    lc.pendown()
    lc.begin_fill()
    lc.circle(40)
    lc.end_fill()

def rightStar(rs,rc):
    rs.fillcolor("red")
    rs.penup()
    rs.goto(171,0)
    rs.pendown()
    rs.begin_fill()

    for i in range(8) : 
        rs.right(45)
        rs.forward(50)
        rs.left(135)
        rs.forward(50)
        rs.right(45)
    rs.end_fill()
        
    rc.fillcolor("yellow")
    rc.penup()
    rc.goto(171,0)
    rc.left(90)
    rc.forward(10)
    rc.right(90)
    rc.pendown()
    rc.begin_fill()
    rc.circle(40)
    rc.end_fill()

def main():
    wn = turtle.Screen()
    wn.bgcolor("navy blue")
    s = turtle.Turtle()
    c = turtle.Turtle()
    centerStar(s,c)
    topStar(s,c)
    rightStar(s,c)
    bottomStar(s,c)
    leftStar(s,c)

    wn.exitonclick()
main()