#over-your-head
from graphics import *
win=GraphWin("OverHead",300,300)
win.setBackground("white")

#dude
#Head
head=Circle(Point(150,200),30)
head.setWidth(2)
head.draw(win)
#body
body=Line(Point(150,230),Point(150,299))
body.setWidth(2)
body.draw(win)
#eyes
left=Line(Point(140,195),Point(142,195))
left.setWidth(2)
left.draw(win)
right=Line(Point(167,195),Point(169,195))
right.setWidth(2)
right.draw(win)

#arrow
#line
start=Line(Point(299,190),Point(250,190))
start.setWidth(2)
start.draw(win)
#overhead1
over0=Line(Point(250,190),Point(200,100))
over0.setWidth(2)
over0.draw(win)
over1=Line(Point(200,100),Point(155,75))
over1.setWidth(2)
over1.draw(win)
over_=Line(Point(155,75),Point(110,72))
over_.setWidth(2)
over_.draw(win)
#overhead2
over2=Line(Point(110,72),Point(75,120))
over2.setWidth(2)
over2.draw(win)
over_2=Line(Point(75,120),Point(60,160))
over_2.setWidth(2)
over_2.draw(win)
#arrowhead
arrow=Polygon(Point(50,160),Point(70,160),Point(60,175))
arrow.setWidth(2)
arrow.draw(win)

#text
#theJoke
joke=Text(Point(150,62),"The Joke")
joke.draw(win)
#you
you=Text(Point(230,240),"You")
you.draw(win)
#you2=Entry(Point(230,240),5)
#you2.draw(win)
#arrow
y_L=Line(Point(215,240),Point(190,230))
y_L.setWidth(2)
y_L.draw(win)
y_P=Polygon(Point(195,225),Point(182,235),Point(177,220))
y_P.setWidth(2)
y_P.draw(win)



win.getMouse()
win.close()

