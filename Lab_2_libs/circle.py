import numpy as np
from space_3d import Translate

""" Circle subclass inherits composition from Translate superclass """
class Circle(Translate):
    def __init__(self, radius: float, translate: Translate) -> tuple:
        Translate.__init__(self, *translate)
        self._radius = radius
        self._translate = translate

        if not isinstance(self._radius, (int, float)):
                raise TypeError(f"Expected int or float, got {type(self._radius).__name__}")
        if self._radius <= 0:
                raise ValueError("Radius must be a positive number")

    @property
    def area(self) -> float:
        return np.pi * self._radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * np.pi * self._radius
    @property
    def circle_center(self) -> Translate:
        return self._translate
    
    def check_unity(self) -> bool:
        return self._radius == 1.0
        
    def __lt__ (self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius < other._radius
    
    def __gt__(self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius > other._radius
            
    def __le__ (self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius <= other._radius

    def __ge__ (self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius >= other._radius
    
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius}, center_coordinates:{self._translate})"


if __name__ == "__main__":
    
    c1=Circle(5, Translate())
    print(c1)
    c1.move(7, 4, 5)
    print(c1.circle_center._x)
    print(c1._x)
    c3=Circle(3, Translate(1, 2, 3))
    print(c3<c1)
    print(c3>c1)
    print(c3<=c1)
    print(c3>=c1)

    


   
    
