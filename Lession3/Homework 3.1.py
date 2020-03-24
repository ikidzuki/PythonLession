def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Деление на ноль запрещено")
    else:
        print(f'{x}/{y} = {result}')


try:
    division(int(input("Введит первое число: ")), (int(input("ведит второе число: "))))
except ValueError:
    print("Использование символов и букв запрещено")
