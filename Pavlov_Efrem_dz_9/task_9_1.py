class TrafficLight:
    __color = ''

    def running(self):
        from time import sleep
        self.__color = 'Красный'
        print(self.__color)
        sleep(7)
        self.__color = 'Желтый'
        print(self.__color)
        sleep(2)
        self.__color = 'Зеленый'
        print(self.__color)
        sleep(5)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
