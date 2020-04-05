class Auto:

    car_name = "Lexus"

    def on_stop(self):
        print("Стоп")

    def on_start(self):
        print("Поехали")

car1 = Auto()
print(car1.car_name)
car1.on_start()