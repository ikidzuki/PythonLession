a = input('Введите список: ').split()
for i in range (len(a)):
    if i > 0 and i % 2 == 1:
        a[i], a[i-1] = a[i-1], a[i]
print(a)
