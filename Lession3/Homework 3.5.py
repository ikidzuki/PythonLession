def sum_list():
    qt = None
    sum_num = 0
    while qt != "Q":
        input_list = []
        for i in input("Для выхода введите 'Q'.Введите числа через пробел: ").split():
            if i.upper() == "Q":
                qt = "Q"
                break  # Позволяет не включать в сумму цифры после "Q"
            else:
                input_list.append(int(i))
        sum_num += sum(input_list)
        print(sum_num)


sum_list()
