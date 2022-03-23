

from cslgraphics import *
from time import *

paper = Canvas()
rectanglePoint= Point(100,100)
rectangle = Rectangle(40,20,rectanglePoint)
rectangle.setFillColor('black')
paper.add(rectangle)

x=0
while x < 8:
	rectangle.rotate(45)
	sleep(0.1)
	x = x+1

