class Translate:

    def __init__(self, *numbers: float|int):
        for number in numbers:
            if not isinstance(number, (int, float)):
                raise TypeError(f"Expected int or float, got {type(number).__name__}")
        
        
        if len(numbers) > 3:
            raise ValueError("At most three numbers are allowed")

        
        self._numbers=tuple(float(number) for number in numbers)

        if len(self._numbers) ==0:
            self._numbers = (0.0, 0.0, 0.0)
        if len(self._numbers) ==1:
            self._numbers = (self._numbers[0],0.0, 0.0)
        if len(self._numbers) ==2:
            self._numbers = (self._numbers[0], self._numbers[1], 0.0)
        if len(self._numbers) ==3:
            self._numbers = (self._numbers[0], self._numbers[1], self._numbers[2])
    @property
    def _x(self) -> float:
        return self._numbers[0] 
    @property
    def _y(self) -> float:
        return self._numbers[1]
    @property
    def _z(self) -> float:
        return self._numbers[2]
    
    def move(self, *coords: float|int):

        for coord in coords:
            if not isinstance(coord, (int, float)):
                raise TypeError(f"Expected int or float, got {type(coord).__name__}")
        
        if len(coords) > 3:
            raise ValueError("At most three numbers are allowed")
        
        if len(coords) ==0:
            self._coords = (0.0, 0.0, 0.0)
        if len(coords) ==1:
            self._coords = (coords[0],0.0, 0.0)
        if len(coords) ==2:
            self._coords = (coords[0], coords[1], 0.0)
        if len(coords) ==3:
            self._coords = (coords[0], coords[1], coords[2])

        
        self._translate = Translate(self._x+self._coords[0],self._y+self._coords[1],self._z+self._coords[2])
        

            

    def __eq__(self, other):
        if not isinstance(other, Translate):
            return NotImplemented
        return self._numbers == other._numbers
    
    def __getitem__(self, index: int) -> float:
        return self._numbers[index]

    def __repr__(self) -> str:
        return f"(x={self._x}, y={self._y}, z={self._z})"

if __name__ == "__main__":
    print(Translate(1, 2, 3))
    t1=Translate()
    t1.move(1, 2, 3)
    print(t1)
