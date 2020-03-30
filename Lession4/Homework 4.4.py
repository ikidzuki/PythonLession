test_list = [4, 4, 9, 1, 8, 9, 5, 7, 7, 6]
print([test_list[i] for i in range (len(test_list)) if test_list.count(test_list[i]) == 1])