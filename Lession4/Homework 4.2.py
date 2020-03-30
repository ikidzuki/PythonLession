test_list = [5, 2, 1, 4, 9, 9, 5, 6, 1, 2]
print([test_list[i] for i in range (1, len(test_list)) if test_list[i] > test_list[i - 1]])