#Sailboat animation
from graphics import *
win=GraphWin("Sailboat2",300,300)
win.setBackground("white")

#daggerboard
DB=Oval(Point(130,190),Point(145,220),)
DB.draw(win)

#spin
spin=Polygon(Point(65,144),Point(72,120),Point(80,100),Point(90,85),Point(123,60),Point(128,151), Point(100,155),Point(75,151))
spin.setOutline("cyan")
spin.setFill("cyan")
spin.draw(win)

#hull
hull=Polygon(Point(75,175),Point(125,173),Point(200,175),Point(200,197),Point(125,200),Point(100,197),Point(85,190))
hull.setFill("white")
hull.draw(win)

#rudderbox
rudbox=Rectangle(Point(200,171),Point(210,180))
rudbox.setFill("black")
rudbox.draw(win)
#rudderblade
rudblade=Oval(Point(200,175),Point(210,210))
rudblade.draw(win)

#tiller
tiller=Rectangle(Point(200,171),Point(178,171))
tiller.setFill("Black")
tiller.draw(win)
#extension
ext=Line(Point(178,171),Point(168,160))
ext.setWidth(2)
ext.draw(win)

#mast
mast=Rectangle(Point(123,173),Point(128,60))
mast.setFill("grey")
mast.setOutline("grey")
mast.draw(win)
#boom
boom=Rectangle(Point(128,155),Point(195,151))
boom.setOutline("grey")
boom.setFill("grey")
boom.draw(win)

#forestay
stay=Line(Point(75,175),Point(123,80))
stay.setFill("grey")
stay.draw(win)
#Boomvang
vang=Line(Point(128,170),Point(140,155))
vang.setWidth(3)
vang.setFill("green")
vang.draw(win)
#mainblock
block=Oval(Point(165,174),Point(157,155))
block.setOutline("red")
block.draw(win)
block2=Oval(Point(162,168),Point(159,155))
block2.setOutline("red")
block2.draw(win)

#mainsail
main=Polygon(Point(128,60),Point(150,75),Point(195,151),Point(155,150),Point(129,151))
main.setWidth(3)
main.setOutline("orange")
main.draw(win)
#jib
jib=Polygon(Point(123,81),Point(79,170),Point(100,168),Point(118,170))
jib.setWidth(2)
jib.setOutline("orange")
jib.draw(win)

#spinpole
pole=Line(Point(123,147),Point(65,144))
pole.setWidth(3)
pole.setFill("grey")
pole.setOutline("grey")
pole.draw(win)

#water=Polygon(Point(0,195),Point(10,185),Point(25,180),Point(30,185),Point(50,193),Point(60,195),Point(75,200),Point(80,195),Point(100,187),Point(110,185),Point(125,180),Point(130,185),Point(150,193),Point(160,195),Point(175,200),Point(180,195),Point(200,187),Point(210,185),Point(225, 180),Point(230,185),Point(250,193),Point(260,195),Point(275,200),Point(280,195),Point(299,190),Point(299,299),Point(0,299))
#water.setFill("blue")
#water.setOutline("blue")
#water.draw(win)
#water2=Polygon(Point(0,190),Point(15,187),Point(30,185),Point(65,188),Point(90,194),Point(100,195),Point(110,194),Point(135,187),Point(170,185),Point(205,188),Point(230,194),Point(240,195),Point(250,194),Point(275,188),Point(299,190),Point(299,299),Point(0,299))
#water2.setFill("blue")
#water2.setOutline("blue")
#water2.draw(win)



#extra waves
extra=Polygon(Point(70,250),Point(75,245),Point(90,240),Point(100,247),Point(115,250),Point(100,247),Point(90,240),Point(75,245),Point(70,250))
extra.setFill("black")
extra.setWidth(3)
extra.draw(win)
extra2=Polygon(Point(170,260),Point(175,255),Point(190,250),Point(200,257),Point(215,260),Point(200,257),Point(190,250),Point(175,255),Point(170,260))
extra2.setFill("black")
extra2.setWidth(3)
extra2.draw(win)
extra3=Polygon(Point(250,230),Point(255,225),Point(270,220),Point(280,227),Point(295,230),Point(280,227),Point(270,220),Point(255,225),Point(250,230))
extra3.setFill("black")
extra3.setWidth(3)
extra3.draw(win)

#bird
bird=Polygon(Point(15,15),Point(23,10),Point(30,20),Point(37,10),Point(45,15),Point(37,10),Point(30,20),Point(23,10),Point(15,15))
bird.setWidth(2)
bird.move(10,20)
bird.draw(win)
#bird position 2
bird2=Polygon(Point(15,5),Point(23,10),Point(30,20),Point(37,10),Point(45,5),Point(37,10),Point(30,20),Point(23,10),Point(15,5))
bird2.setWidth(2)
bird2.move(10,22)
#bird2.draw(win)

#birdalt
birdalt=Polygon(Point(15,15),Point(23,10),Point(30,20),Point(37,10),Point(45,15),Point(37,10),Point(30,20),Point(23,10),Point(15,15))
birdalt.setWidth(2)
birdalt.move(200,30)
#birdalt.draw(win)
#bird position 2
bird2alt=Polygon(Point(15,5),Point(23,10),Point(30,20),Point(37,10),Point(45,5),Point(37,10),Point(30,20),Point(23,10),Point(15,5))
bird2alt.setWidth(2)
bird2alt.move(200,32)
bird2alt.draw(win)

#water_add
water2=Polygon(Point(0,190),Point(15,187),Point(30,185),Point(65,188),Point(90,194),Point(100,195),Point(110,194),Point(135,187),Point(170,185),Point(205,188),Point(230,194),Point(240,195),Point(250,194),Point(275,187),Point(299,185),Point(299,299),Point(0,299))
water2.setFill("blue")
water2.setOutline("blue")
water2.draw(win)
#water2.move(-120,0)

water_add_1=Polygon(Point(269,190),Point(289,194),Point(299,195),Point(299,299),Point(269,299))
water_add_1.setFill("blue")
water_add_1.setOutline("blue")
#water_add_1.draw(win2)
#water_add_1.move(-60,0)

water_add_2=Polygon(Point(269,195),Point(279,194),Point(299,190),Point(299,299),Point(269,299))
water_add_2.setFill("blue")
water_add_2.setOutline("blue")
#water_add_2.draw(win2)
#water_add_2.move(-30,0)

water_add_3=Polygon(Point(269,190),Point(284,187),Point(299,185),Point(299,299),Point(269,299))
water_add_3.setOutline("blue")
water_add_3.setFill("blue")
#water_add_3.draw(win2)

water_add_int=Polygon(Point(179,185),Point(204,188),Point(209,190),Point(209,299),Point(179,299))
water_add_int.setOutline("blue")
water_add_int.setFill("blue")
#water_add_int.draw(win2)
water_add_int.move(90,0)


#animations
#use  win.update(<time>) instead of click
#main() is useless
#def main():
    #for i in range(10):
        #win.getMouse()
        #bird.undraw()
        #bird2.draw(win)
        #bird2alt.undraw()
        #birdalt.draw(win)
        #win.getMouse()
        #bird2.undraw()
        #bird.draw(win)
        #birdalt.undraw()
        #bird2alt.draw(win)
#main()
def bird_1():
    bird.undraw()
    bird2.draw(win)
    bird2alt.undraw()
    birdalt.draw(win)

def bird_2():
    bird2.undraw()
    bird.draw(win)
    birdalt.undraw()
    bird2alt.draw(win)
    
#move boat down 5
def boat_1():
    DB.move(0,5)
    spin.move(0,5)
    hull.move(0,5)
    rudbox.move(0,5)
    rudblade.move(0,5)
    tiller.move(0,5)
    ext.move(0,5)
    mast.move(0,5)
    boom.move(0,5)
    stay.move(0,5)
    vang.move(0,5)
    block.move(0,5)
    block2.move(0,5)
    main.move(0,5)
    jib.move(0,5)
    pole.move(0,5)

#move boat up 5
def boat_2():
    DB.move(0,-5)
    spin.move(0,-5)
    hull.move(0,-5)
    rudbox.move(0,-5)
    rudblade.move(0,-5)
    tiller.move(0,-5)
    ext.move(0,-5)
    mast.move(0,-5)
    boom.move(0,-5)
    stay.move(0,-5)
    vang.move(0,-5)
    block.move(0,-5)
    block2.move(0,-5)
    main.move(0,-5)
    jib.move(0,-5)
    pole.move(0,-5)

#move boat up 5
def boat_3():
    DB.move(0,-5)
    spin.move(0,-5)
    hull.move(0,-5)
    rudbox.move(0,-5)
    rudblade.move(0,-5)
    tiller.move(0,-5)
    ext.move(0,-5)
    mast.move(0,-5)
    boom.move(0,-5)
    stay.move(0,-5)
    vang.move(0,-5)
    block.move(0,-5)
    block2.move(0,-5)
    main.move(0,-5)
    jib.move(0,-5)
    pole.move(0,-5)

#move boat down 5
def boat_4():
    DB.move(0,5)
    spin.move(0,5)
    hull.move(0,5)
    rudbox.move(0,5)
    rudblade.move(0,5)
    tiller.move(0,5)
    ext.move(0,5)
    mast.move(0,5)
    boom.move(0,5)
    stay.move(0,5)
    vang.move(0,5)
    block.move(0,5)
    block2.move(0,5)
    main.move(0,5)
    jib.move(0,5)
    pole.move(0,5)

#move wave right by one position, add more wave left
def wave_1():
    water2.move(-30,0)
    water_add_int.draw(win)

def wave_2():
    water2.move(-30,0)
    water_add_int.move(-30,0)
    water_add_1.draw(win)
    
def wave_3():
    water2.move(-30,0)
    water_add_int.move(-30,0)
    water_add_1.move(-30,0)
    water_add_2.draw(win)
    
def wave_4():
    water2.move(-30,0)
    water_add_int.move(-30,0)
    water_add_1.move(-30,0)
    water_add_2.move(-30,0)
    water_add_3.draw(win)
    
def wave_5():
    water2.move(120,0)
    water2.undraw()
    water2.draw(win)
    water_add_int.move(90,0)
    water_add_int.undraw()
    water_add_1.move(60,0)
    water_add_1.undraw()
    water_add_2.move(30,0)
    water_add_2.undraw()
    water_add_3.undraw()
    
#move waves across, boat up/down
def animate():
    for i in range(20):
        bird_1()
        boat_1()
        wave_1()
        
        update(6)
        bird_2()
        boat_4()
        wave_2()
        
        update(6)
        bird_1()
        boat_3()
        wave_3()
        
        update(6)
        bird_2()
        boat_2()
        wave_4()
        
        update(6)
        wave_5()
animate()
#to fix this:
    #make waves longer(copy from water2 then change x position)
    #maybe use undraw and just make the Polygon bigger
    #change move(30) to move(35)
    #make the waves loop back(put the updates in reverse order)

close=input("Press Enter to Quit: ")
#win.getMouse()
win.close()
