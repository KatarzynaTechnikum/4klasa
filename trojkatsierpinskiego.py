#nie dziala
import turtle
t=turtle.Turtle()

def rysujTrojkat(punkty):
    t.fillcolor("white")
    t.up()
    t.goto(punkty[0][0], punkty[0][1])
    t.down()
    t.goto(punkty[1][0], punkty[1][1])
    t.goto(punkty[2][0], punkty[2][1])
    t.goto(punkty[0][0], punkty[0][1])

def polowa(p1,p2):
  return(p1[0]+p2[0]/2, p1[1]+p2[1]/2)

def sierpinski(punkty, liczbaPoziomow):
    rysujTrojkat(punkty)
    if liczbaPoziomow>0:
      sierpinski([punkty[0],polowa(punkty[0], punkty[1]), polowa(punkty[0],punkty[2]) ],liczbaPoziomow-1)
      sierpinski([punkty[1],polowa(punkty[0], punkty[1]), polowa(punkty[1],punkty[2]) ],liczbaPoziomow-1)
      sierpinski([punkty[2],polowa(punkty[2], punkty[1]), polowa(punkty[0],punkty[2]) ],liczbaPoziomow-1)


myWin= turtle.Screen()
mojepunkty=[[-200,-100],[00,200],[200,-100]]
sierpinski(mojepunkty,3)
myWin.exitonclick()