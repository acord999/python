class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        return Cell(self.amount - other.amount)

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __floordiv__(self, other):
        return Cell(self.amount // other.amount)

    def __truediv__(self, other):
        return Cell(self.amount / other.amount)

    def __str__(self):
        return f'{self.amount} cells'

    def make_order(self, count):
        x = self.amount
        while x > 0:
            for k in range(1, count + 1):
                print('*', end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')
