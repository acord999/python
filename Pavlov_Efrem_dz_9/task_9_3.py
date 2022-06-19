class Worker:
    name: str
    surname: str
    position: str
    income: dict = {'wage': 0.0, 'bonus': 1.0}

    def __init__(self, name: str, surname: str, position: str, income: dict = {'wage': 0, 'bonus': 1.0}) -> None:
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str, income: dict = {'wage': 0, 'bonus': 1.0}) -> None:
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    worker_1 = Position('Efrem', 'Pavlov', 'Python developer', {'wage': 3000, 'bonus': 500})
    print(worker_1.get_full_name())
    print(f'Total: {worker_1.get_total_income()} $')
