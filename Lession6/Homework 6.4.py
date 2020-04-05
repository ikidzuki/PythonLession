class Car:
    def __init__(self, name, color, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        is_police = is_police

    def go(self, speed):
        self.speed = speed
        if self.speed == 0:
            print('Машина поехала!')
        else:
            print('Машина продолжает движение вперед!')
    def stop(self):
        self.speed = 0
        print('Машина остановилась!')

    def turn(self, speed, side):
        self.speed = speed
        if self.speed == 0:
            print(f'Машина не может повернуть, так как скорость автомобиля = {self.speed}')
        else:
            if side.lower() in ('вправо', 'влево', 'назад', 'направо', 'налево'):
                print(f'Машина повернула {side.lower()}!')
            else:
                print('Направление поворота указано неверно. Машина продолжила движение вперед')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed > 60:
            print('Вы нарушили скоростной режим!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')
        if self.speed > 40:
            print('Вы нарушили скоростной режим!')


class PoliceCar(Car):
    pass


avto1 = WorkCar('BMW', 'Black')
avto1.show_speed()
avto1.go(65)
avto1.show_speed()
avto1.stop()
avto1.show_speed()
avto1.turn(0, 'направо')
avto1.turn(10, 'налево')
avto1.turn(50, 'наискосок')

print('')

avto2 = PoliceCar('Audio', 'White', 0, True)
avto2.go(0)
avto2.go(100)
avto2.show_speed()
avto2.turn(100, 'назад')
avto2.stop()

