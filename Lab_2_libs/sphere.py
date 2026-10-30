import numpy as np
from space_3d import Translate
class Sphere:
    
    def __init__(self, radius: float, Translate: Translate) -> tuple:
        self._radius = radius
        self._translate = Translate

        if not isinstance(self._radius, (int, float)):
            raise TypeError(f"Expected int or float, got {type(self._radius).__name__}")
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
    
    

    def __eq__(self, other):
        if not isinstance(other, Sphere):
            return NotImplemented
        return self._radius == other._radius and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Sphere(radius={self._radius}, center_coordinates:{self._translate})"

