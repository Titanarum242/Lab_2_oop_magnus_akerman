
from space_3d import Translate


class Cube:
    
    def __init__(self, side_length: float, Translate: Translate) -> tuple:
        self._side_length = side_length
        self._translate = Translate

        if not isinstance(self._side_length, (int, float)):
            raise TypeError(f"Expected int or float, got {type(self._side_length).__name__}")
        if self._side_length <= 0:
            raise ValueError("Side length must be a positive number")

    @property
    def volume(self) -> float:
        return self._side_length ** 3

    @property
    def surface_area(self) -> float:
        return 6 * self._side_length ** 2
    
    @property
    def cube_center(self) -> Translate:
        center_x = self._translate[0] + self._side_length / 2
        center_y = self._translate[1] + self._side_length / 2
        center_z = self._translate[2] + self._side_length / 2
        return Translate(center_x, center_y, center_z)

    @property
    def check_unity(self) -> bool:
        return self._side_length == 1.0

    def __eq__(self, other):
        if not isinstance(other, Cube):
            return NotImplemented
        return self._side_length == other._side_length and self._translate == other._translate

    def __repr__(self) -> str:
        return f"Cube(side_length={self._side_length}, center_coordinates:{self.cube_center})"