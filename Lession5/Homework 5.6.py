import os


def srez(y, x):
    if ls_less[i][y] != '-':
        ls_less[i][y] = int(ls_less[i][y][:x])


with open('text_6.txt', 'r', encoding='utf-8') as txt:
    ls_less = [i.rstrip().split() for i in txt]

# Делаем срез и приводим значения к int
for i in range(len(ls_less)):
    ls_less[i][0] = ls_less[i][0][:-1]  # Не применяем функцию, так как нельзя привести к int
    srez(1, -3)
    srez(2, -4)
    srez(3, -5)

# Очищаем список от "-". Невозможно выполнить в предыдущем цикле, так как ломает ему range
for i in range(len(ls_less)):
    mark_del = ls_less[i].count('-')
    for mark_del in range(mark_del):
        ls_less[i].remove('-')

# Создаем словарь. Суммируем числа
result = {}
for i in range(len(ls_less)):
    key = ls_less[i][0]
    result[key] = sum(ls_less[i][1:])

print(result)
