

from rectangle import Rectangle
from circle import Circle
from cube import Cube
from sphere import Sphere
from space_3d import Translate
from plot_2d_3d import Plt2d
from plot_2d_3d import Plt3d

""" 
______________________________________________________________________________________

Use this file to make nice plotting with one or more objects use .add(shape, "color") 
to add more objects in the same diagram
_______________________________________________________________________________________

run this file to view some exampes:"""

r1= Rectangle(10, 10, Translate())
c1= Circle(15,Translate())       
r2= Rectangle(6, 5, Translate(1, 2))
s1=Sphere(7,Translate())
k1=Cube(5,Translate(10,10,10))

pl = Plt2d()
pl.add(r1, "red")
pl.add(r1, "green")
pl.add(r2, "orange")
pl.add(c1,"red")  
pl.plot()

pl3=Plt3d()
pl3.add(s1, "green")
pl3.add(k1,"b")
pl3.plot()

"""____________________________________________________________________________________________
"""