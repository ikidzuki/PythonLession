class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")
        print(f"Отрисованное сообщение: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашом")
        print(f"Отрисованное сообщение: {self.title}")


class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")
        print(f"Отрисованное сообщение: {self.title}")


hello1 = Pen('Привет мир!')
hello1.draw()

print('')

hello2 = Pencil('Hello world!')
hello2.draw()

print('')

hello3 = Handle('Konnichiwa warudo!')
hello3.draw()
