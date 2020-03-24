# 1 Вариант
degree = lambda x, y: x ** y
print(degree(2, -2))


# 2 Вариант
def degree2(x, y):
    deg_el = 1
    for i in range(abs(y)):
        deg_el *= x;
    return 1 / deg_el


print(degree2(2, -2))
