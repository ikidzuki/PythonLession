user_num = int(input("Введите число: "))
my_list = [3, 5, 6, 7, 7, 8]
for i in range(len(my_list)):
    if user_num < my_list[i]:
        my_list.insert(i, user_num)
        break;
    if my_list[-1] <= user_num:
        my_list.insert((len(my_list)) + 1, user_num)
        break
print(my_list)
