reven = float(input("Введите сумму выручки компании: "))
costs = float(input("Введите сумму издержек компании: "))

if reven > costs:
    print("Поздравляем, вы вышли в прибыль!")
    rent = reven - costs
    print("Рентабельность выручки равна", reven - costs)
    empl = int(input("Введите количество сотрудников: "))
    print("Прибыль на 1 сотрудника равна", rent/empl)
elif reven < costs:
    print("Увы, вы потерпели убытки!")
    print("Выши убытки -", costs - reven)
else:
    print("Вы вышли в 0!")
