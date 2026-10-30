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
         
    def __eq__(self, other):
        if not isinstance(other, Translate):
            return NotImplemented
        return self._numbers == other._numbers
    
    def __getitem__(self, index: int) -> float:
        return self._numbers[index]

    def __repr__(self) -> str:
        return f"Translate(x={self._numbers[0]}, y={self._numbers[1]}, z={self._numbers[2]})"