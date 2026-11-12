# Lab_2_oop_magnus_akerman
## UML - Diagram

 -- see "UML_graphs" --
## Description of Classes
### class Translate - superclass
     The Translate class allows for the representation of a point in three-dimensional space using x, y, and z coordinates.

     If Translate() is leaved blank with no entered numbers it will it will assume Translate(x=0, y=0, z=0)

     - properties: [_x, _y, _z]

### class Circle - subclass
     Inherits from Translate class: 
      - composition Translate()
      - properties: [_x, _y, _z] 
      - attribute: _translate
      - methods: move()  

     Represents the 2d shape of a circle with "radius" (entered first) followed by inherited "Translate()" consisting of 0 to max 3 numbers. Use comma "," between the numbers entered. 

     move() enter 0 to max 3 numbers the new 3d position can be read by _translate attribute and one compsant by _x, _y _z.
        Examples: c1 = Circle(radius, Translate(x,y,z))
                  c1.move(x,y,z)
                  c1._tranlate  -> gives the new center coordinate in 3D.
                  c1._translate._x   -> gives only x-coordinate of the new position.
                  c1._x   -> gives the initial x-coordinate.
      Other read only properties:
        - circumference: c1.circumference
        - circle_center: c1.circle_center
        - area: c1.area
      Other methods:
        - check unity circle (radius=1): c1.check_unity()
      
      Dunder methods: Equality, >, <, >=, =<, Repr

### class Rectangle - Subclass
      Inherits from Translate class: 
      - composition Translate()
      - properties: [_x, _y, _z] 
      - attribute: _translate
      - methods: move()  

     Represents the 2d shape of a rectangle with "base" and "height" (entered first) followed by inherited "Translate()" consisting of 0 to max 3 numbers. Use comma "," between the numbers entered. 

     move() enter 0 to max 3 numbers the new 3d position can be read by _translate attribute and one compsant by _x, _y _z.
        Examples: r1 = Rectangle(base, height, Translate(x,y,z))
                  r1.move(x,y,z)
                  r1._tranlate  -> gives the new coordintates of bottom left corner in 3D.
                  r1._translate._x   -> gives only x-coordinate of the new bottom left corner.
                  r1._x   -> gives the initial bottom left corner x-coordinate.
          
      Other read only properties:
        - perimeter: r1.perimiter
        - rectangle center: r1.rectangle_center
        - area: r1.area

      Other methods:
        - check square: r1.check_square()
      
      Dunder methods: Equality, >, <, >=, =<, Repr

### class Sphere
   Sphere:
     Represents a sphere in 3D space.
     The Sphere class allows for the representation of a sphere in three-dimensional space using a radius and a center point represented by a Translate object. It provides methods to calculate the volume and surface area of the sphere, as well as to compare two Sphere objects for equality.

   Attributes:
     _radius (float): The radius of the sphere.
     _translate (Translate): A Translate object representing the center point of the sphere.

   Methods:
     volume: Calculates the volume of the sphere.
     surface_area: Calculates the surface area of the sphere.
     sphere_center: Returns the center point of the sphere as a Translate object.
     check_unity: Checks if the radius of the sphere is equal to 1.0
     __eq__(other): Compares two Sphere objects for equality based on their radius and center point.
     __repr__(): Returns a string representation of the Sphere object.
### class Cube

### class Plt2d - Plotting 2D
### class Plt3d - Plotting 3D
## Unit testning

 
