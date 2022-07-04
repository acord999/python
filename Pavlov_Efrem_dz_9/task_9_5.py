class Stationery:
    title = 'Название'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки Pencil')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Handle')


if __name__ == '__main__':
    a = Stationery()
    b = Pen()
    c = Pencil()
    d = Handle()
    for some_obj in [a, b, c, d]:
        some_obj.draw()
