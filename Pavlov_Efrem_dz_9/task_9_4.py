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
    simple_car = Car('Audi', 'Red')
    t_car = TownCar('Эвакуатор', 'White')
    sport = Car('Ferrari', 'Yellow')
    w_car = WorkCar('Трактор', 'Blue')
    police = Car('Полицейский Ford', 'Red')
    objects = [simple_car, t_car, sport, w_car, police]
    for car_obj in objects:
        car_obj.go()
        car_obj.stop()
        car_obj.turn('направо')
        car_obj.speed = 100
        car_obj.show_speed()
        print('#' * 70)

