from functools import reduce


def func_comp(prev_el, el):
    return prev_el * el


work_list = reduce(func_comp, [i for i in range(100, 1001) if i % 2 == 0])
print(work_list)

# Тест корректной работы функции
print(reduce(func_comp, [2, 4, 2]))
