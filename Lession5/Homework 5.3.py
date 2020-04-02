import os

with open('text_3.txt', 'r', encoding='utf-8') as txt:
    empl = [i.rstrip().split() for i in txt]
    empl = dict(empl) # Преобразуем список в словарь
    print(empl)
    sum_salary = 0
    sum_empl = 0
    # Преобразуем сумм из str в int и печатаем список сотрудников < 20 000
    print("Список сотрудников, получающих меньше 20 000 руб.:")
    for key in empl:
        empl[key] = float(empl[key])
        if empl[key] < 20000.0:
            print(key)
        sum_salary += empl[key]
        sum_empl += 1
    print(f"\nСредняя заработная плата равна {sum_salary / sum_empl}")