class Road:
    _length: float
    _width: float

    def __init__(self, length: float = 0, width: float = 0) -> None:
        self._length = length
        self._width = width

    def total_weight(self, weight: float, thickness: float) -> float:
        return self._width * self._length * weight * thickness


if __name__ == '__main__':
    r = Road(5000, 20)
    print(r.total_weight(25, 5))
