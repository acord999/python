class Car:
    speed: float
    color: str
    name: str
    is_police: bool = False

    def __init__(self, name: str, color: str, is_police: bool = False) -> None:
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} едет')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость машины {self.name} {self.speed} км/ч')
        return self.speed


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self) -> float:
        spd = super().show_speed()

        if spd > 60:
            print("Превышен лимит скорости 60 км/ч !!!")

        return spd


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(self, name, color)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self) -> float:
        spd = super().show_speed()

        if spd > 40:
            print("Превышен лимит скорости 40 км/ч !!!")

        return spd


class PoliceCar(Car):

    def __init__(self, colour, name) -> None:
        super().__init__(colour, name)
        self._is_police = True


if __name__ == '__main__':
    # Тест класса Car
    simple_car = Car('Audi', 'Red')
    simple_car.go()
    simple_car.stop()
    simple_car.turn('направо')
    simple_car.speed = 100
    simple_car.show_speed()
    print('#' * 70)
    # Тест класса TownCar
    t_car = TownCar('Эвакуатор', 'White')
    t_car.go()
    t_car.stop()
    t_car.turn('направо')
    t_car.speed = 75
    t_car.show_speed()
    print('#' * 70)
    # Тест класса Car
    sport = Car('Ferrari', 'Yellow')
    sport.go()
    sport.stop()
    sport.turn('направо')
    sport.speed = 175
    sport.show_speed()
    print('#' * 70)
    # Тест класса WorkCar
    w_car = TownCar('Трактор', 'Blue')
    w_car.go()
    w_car.stop()
    w_car.turn('направо')
    w_car.speed = 50
    w_car.show_speed()
    print('#' * 70)
    police = Car('Полицейский Ford', 'Red')
    police.go()
    police.stop()
    police.turn('направо')
    police.speed = 60
    police.show_speed()
