from itertools import cycle, count

# Задание а
min_c = int(input("С какого числа начать отсчет? "))
max_c = int(input("До какого числа вести отсчет? "))
for i in count(min_c):
    if i == max_c:
        print(i)
        break
    else:
        print(i, end=", ")

# Задание б
test_list = [5, 6, True, "city", 21]

step = 0
for i in cycle(test_list):
    if step == 10:
        break
    else:
        print(i)
        step += 1
