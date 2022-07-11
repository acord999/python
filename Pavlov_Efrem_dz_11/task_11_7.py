class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a - (self.b * other.b), self.b * other.a)

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


if __name__ == '__main__':
    z_1 = ComplexNumber(1, -2)
    z_2 = ComplexNumber(3, 4)
    print(z_1)
    print(z_1 + z_2)
    print(z_1 * z_2)