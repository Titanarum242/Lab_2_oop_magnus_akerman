import numpy as np
from space_3d import Translate

class Rectangle:

    def __init__(self, base: float, height: float, Translate: Translate) -> tuple:
        self._base = base
        self._height = height
        self._translate = Translate

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

    @property
    def rectangle_center(self) -> Translate:
        center_x = self._translate[0] + self._base / 2
        center_y = self._translate[1] + self._height / 2
        return Translate(center_x, center_y)

    @property
    def check_square(self) -> bool:
        return self._base == self._height

    @property
    def check_unity(self) -> bool:
        return self._base == 1.0 and self._height == 1.0

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self._height == other._height and self._base == other._base and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Rectangle(base={self._base}, height={self._height}, center_coordinates:{self.rectangle_center})"