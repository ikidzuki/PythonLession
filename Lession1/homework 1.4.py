num = int(input('Введите число: '))
result = 0
while num > 0:
    elem = num%10
    num = num//10
    if elem > result:
        result = elem
print(result)
