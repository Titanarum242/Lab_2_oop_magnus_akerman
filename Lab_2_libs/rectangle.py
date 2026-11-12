import numpy as np
from space_3d import Translate

"""Rectangle subclass inherits composition from Translate superclass"""

class Rectangle(Translate):

    def __init__(self, base: float, height: float, translate: Translate) -> tuple:
        Translate.__init__(self, *translate)
        self._base = base
        self._height = height
        self._translate = translate
        
        if not isinstance(self._base and self._height, (int, float)):
            raise TypeError(f"Expected int or float, got {type(self._base).__name__}")
        if self._base <= 0 or self._height <= 0:
            raise ValueError("Base and height must be positive numbers")
        
        
    @property
    def area(self) -> float:
        return self._base * self._height

    @property
    def perimeter(self) -> float:
        return 2 * (self._base + self._height)

    """ center ccordinate of the rectangle in 2D"""
    @property
    def rectangle_center(self) -> Translate:  
        center_x = self._translate._x + self._base / 2
        center_y = self._translate._y + self._height / 2
        
        return Translate(center_x, center_y)
    

    """ method for checking if the rectangle is a square"""
    def check_square(self) -> bool:
        return self._base == self._height

    
    def __lt__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        
        return self._base < other._base and self._height < other._height

    def __gt__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        
        return self._base > other._base and self._height > other._height    
    
    def __le__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        
        return self._base <= other._base and self._height <= other._height
    
    def __ge__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return NotImplemented
        
        return self._base >= other._base and self._height >= other._height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self._height == other._height and self._base == other._base and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Rectangle(base={self._base}, height={self._height}, center_coordinates:{self.rectangle_center})"

if __name__ == "__main__":
    r1= Rectangle(4, 3, Translate(1, 2))
    r2= Rectangle(6, 5, Translate(1, 2))
    print(r1)
    r1.move(3, 4)
    print(r1)
    r3=Rectangle(5,7, Translate(1,6,))
    print(r3)
    r3.move(2,3)
    print(r3)
    print(r1.check_square())
    print(r1<r2)
    print(r1>r2)
    print(r1<=r2)
    print(r1>=r2)
    print(r1.area>r2.area)

    
