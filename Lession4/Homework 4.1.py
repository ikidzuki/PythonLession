import sys
try:
    hours = int(sys.argv[1])
    rate = int(sys.argv[2])
except ValueError:
    print("Введите числовые значеня!")
except IndexError:
    print("Введите два числовых значеня(рабочие часы и ставка сотрудника) через пробел!")
else:
    print(f"Заработная плата сотрудника: {rate * hours}")