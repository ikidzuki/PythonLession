class Cell():

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if other.amount >= self.amount:
            return 'Нельзя вычесть. Значение превышает(или равно) исходное количество клеток.'
        else:
            return self.amount - other.amount

    def __mul__(self, other):
        return self.amount * other.amount

    def __truediv__(self, other):
        try:
            return self.amount // other.amount
        except ZeroDivisionError:
            print("Попытка деления на 0")

    def make_order(self, row):
        return ''.join(['* ' if i % row != 0 else '*\n' for i in range(1, self.amount + 1)])


cell_1 = Cell(13)
cell_2 = Cell(5)
cell_3 = Cell(25)  # тест предупреждения
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 - cell_3)  # тест предупреждения
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print('')
print(cell_1.make_order(5))
