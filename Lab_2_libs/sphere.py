import numpy as np
from space_3d import Translate
class Sphere(Translate):

    def __init__(self, radius: float, translate: Translate) -> tuple:
        
        """Initializes a Sphere object with a specified radius and center coordinates."""

        Translate.__init__(self, *translate)
        
        self._radius = radius
        self._translate = translate
        
       


        if not isinstance(self._radius, (int, float)):
            raise TypeError(f"Radius must be an int or float, got {type(self._radius).__name__}")
        if self._radius <= 0:
            raise ValueError("Radius must be a positive number")

         
    @property
    def volume(self) -> float:
        return (4/3) * np.pi * self._radius**3

    @property
    def surface_area(self) -> float:
        return 4 * np.pi * self._radius**2
    @property
    def sphere_center(self) -> Translate:
        return self._translate
    @property
    def check_unity(self) -> bool:
        return self._radius == 1.0
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Sphere):
            return NotImplemented
        return self._radius < other._radius

    def __gt__(self, other) -> bool:
        if not isinstance(other, Sphere):
            return NotImplemented
        return self._radius > other._radius

    def __le__(self, other) -> bool:
        if not isinstance(other, Sphere):
            return NotImplemented
        return self._radius <= other._radius

    def __ge__(self, other) -> bool:
        if not isinstance(other, Sphere):
            return NotImplemented
        return self._radius >= other._radius

    def __eq__(self, other):        
        if not isinstance(other, Sphere):
            return NotImplemented
        return self._radius == other._radius and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Sphere(radius={self._radius}, center_coordinates:{self._translate})"

if __name__ == "__main__":
    s1= Sphere(5, Translate())
    
    print(s1._x)
    s1.move(1, 2, 3)
    print(s1._translate)
    
    print(type(s1.sphere_center))
    print(type(s1._translate._x))
    print(s1._translate._x + s1._translate._y + s1._translate._z)
    s2= Sphere(3, Translate()) 
    print(s2)
    print(s2._translate._x, s2._translate._y, s2._translate._z)
    print(type(s2._translate))
    
    
    



