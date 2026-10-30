import numpy as np
from space_3d import Translate

class Circle:
    def __init__(self, radius: float, Translate: Translate) -> tuple:
        self._radius = radius
        self._translate = Translate

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
    @property
    def check_unity(self) -> bool:
        return self._radius == 1.0
        
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self._radius == other._radius and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius}, center_coordinates:{self._translate})"



    
