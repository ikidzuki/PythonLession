"""""
1. Находим 1ое максимальное значение через список
2. Удаляем этот элемент из списка
3. Находим максимальное значение нового списка
"""

def sum_max(arg1, arg2, arg3):
    list_arg = [arg1, arg2, arg3]
    max1 = max(list_arg)
    list_arg.remove(max1)
    max2 = max(list_arg)
    return max1 + max2


print(sum_max(5, 6, 11))
