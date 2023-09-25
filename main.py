import turtle

t = turtle.Turtle()


def zbiorCantor(dl, wytnij, n):
  if n == 0:
    t.pd()
    t.forward(dl)
    t.pu()
  else:
    nowa_dl = dl * (1 - wytnij) / 2
    zbiorCantor(nowa_dl, wytnij, n - 1)
    t.forward(dl * wytnij)
    zbiorCantor(nowa_dl, wytnij, n - 1)


myWin = turtle.Screen()
t.speed(1000)
szerokosc = 800
wysokosc = 300

n = 6
t.pu()
t.back(szerokosc / 2)
t.lt(90)
t.forward(wysokosc / 2)

for i in range(n):
  t.rt(90)
  zbiorCantor(szerokosc, 1 / 3, i)
  t.back(szerokosc)
  t.lt(90)
  t.back(wysokosc / (n - 1))

myWin.exitonclick()
