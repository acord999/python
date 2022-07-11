class WareHouse:
    def __init__(self):
        self._data = {}

    def add_to(self, equipment):
        """Adding equipment object"""
        self._data.setdefault(f'{equipment.name}{equipment.model}', equipment) + equipment

    def extract(self, name, quantity):
        """Extract equipment to destination company"""
        if self._data.get(name) and isinstance(quantity, int):
            for i in range(quantity):
                self._data[name].qnt = self._data[name].qnt - 1
        else:
            raise ValueError('Wrong name or current quantity of objects(s)')


class Equipment:
    def __init__(self, name, qnt, model):
        self.name = name
        self.qnt = qnt
        self.model = model

    def __add__(self, other):
        self.qnt += other.qnt


class Printer(Equipment):
    def __init__(self, series, name, qnt, model):
        super().__init__(name, qnt, model)
        self.series = series

    @staticmethod
    def action():
        return 'Printing'


class Scaner(Equipment):
    def __init__(self, name, qnt, model):
        super().__init__(name, qnt, model)

    @staticmethod
    def action():
        return 'Scnaning'


class MFU(Equipment):
    def __init__(self, name, qnt, model):
        super().__init__(name, qnt, model)

    @staticmethod
    def action():
        return 'Copying'


if __name__ == '__main__':
    sklad = WareHouse()
    scaner = Scaner('hp', 321, '90')
    sklad.add_to(scaner)
    scaner = Scaner('hp', 311, '97')
    sklad.add_to(scaner)
    scaner = Scaner('hp', 330, '99')
    sklad.add_to(scaner)
    print(sklad._data['hp90'].qnt)
    sklad.extract('hp90', 3)
    print(sklad._data['hp90'].qnt)

