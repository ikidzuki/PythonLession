a = int(input("Введите расстояние на первый день: "))
b = int(input("Введите итоговое расстояние: "))
day = 1
while a < b:
    day = day+1
    a += (a * 0.1)
print(day)
