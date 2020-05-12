#Sailboat Picture
from graphics import *
win=GraphWin("Sailboat")

#note:after testing, the order vertically is order back to front on window

#background
back=Rectangle(Point(0,0),Point(199,199))
back.setFill("white")
back.draw(win)
#water
water=Rectangle(Point(0,130),Point(199,199))
water.setFill("blue")
water.draw(win)
#water splash
#splash=Oval(Point(25,30),Point(80,150))

#hull base
hull=Rectangle(Point(75,125),Point(150,150))
    #hull.setFill("white")
hull.draw(win)
#hull patch to cover line
patch=Line(Point(75,126),Point(75,130))
patch.setFill("white")
patch.draw(win)
patch2=Line(Point(75,130),Point(75,150))
patch2.setFill("blue")
patch2.draw(win)
#hull front
edge=Line(Point(75,150),Point(25,125))
edge.draw(win)
top=Line(Point(75,125),Point(25,125))
top.draw(win)
#mast
mast=Rectangle(Point(77,125),Point(80,25))
mast.setFill("black")
mast.draw(win)
#boom
boom=Rectangle(Point(80,103),Point(140,100))
boom.setFill("black")
boom.draw(win)
#Daggerboard
DB=Oval(Point(90,140),Point(105,175))
    #DB.setFill("white")
DB.draw(win)
#Daggerboard Patch
patchD=Rectangle(Point(90,149),Point(105,130))
patchD.setFill("blue")
patchD.setOutline("blue")
patchD.draw(win)
#rudderbox
rudbox=Rectangle(Point(150,120),Point(160,135))
rudbox.setFill("black")
rudbox.draw(win)
#rudderblade
rudblade=Oval(Point(150,120),Point(160,165))
    #rudblade.setFill("white")
rudblade.draw(win)
#tiller
tiller=Rectangle(Point(150,120),Point(130,122))
tiller.setFill("black")
tiller.draw(win)
#tiller extension
ext=Line(Point(130,120),Point(120,108))
ext.setWidth(2)
ext.draw(win)
#mainsail
#Domain: 80-140 Range: 25-75
main=Line(Point(80,25),Point(140,100))
main.setWidth(3)
main.draw(win)
#forestay
stay=Line(Point(77,35),Point(25,125))
stay.setWidth(2)
stay.draw(win)
#jib
jib=Line(Point(31,115),Point(70,115))
jib.setWidth(2)
jib.draw(win)
jtack=Line(Point(31,115),Point(77,35))
jtack.setWidth(3)
jtack.draw(win)
jleech=Line(Point(70,115),Point(77,35))
jleech.setWidth(3)
jleech.draw(win)
#spin pole
    #pole=Line(Point(77,80),Point(20,80))
    #pole.setWidth(3)
    #pole.draw(win)
#spin

#boomvang
vang=Line(Point(80,118),Point(100,103))
vang.setWidth(3)
vang.draw(win)
#main block
block1=Oval(Point(110,125),Point(117,103))
block1.draw(win)
block2=Oval(Point(112,118),Point(115,103))
block2.draw(win)
#sail number
num=Text(Point(95,65),"#69")
num.draw(win)

win.getMouse()
win.close()
#draw to have right layering
    #DB and rudblade need to be at back
    #hull patch needs to be over hull
        #spin is at back, spin pole at front

