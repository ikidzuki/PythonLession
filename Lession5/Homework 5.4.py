import os

numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('text_4.txt', 'r') as txt:
    list_num = [i for i in txt]

    for i in range(len(list_num)):
        for key in numbers:
            list_num[i] = list_num[i].replace(key, numbers[key])

with open("new_text_4.txt", 'w', encoding="utf-8") as new_txt:
    new_txt.writelines(list_num)
