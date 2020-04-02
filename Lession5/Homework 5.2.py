import os

# Вывод всех строк в список. Приводим в порядок, удаляем лишние \n
with open("text_2.txt", "r", encoding="utf-8") as txt:
    all_text = txt.readlines()
    all_text = [i.rstrip() for i in all_text]

# Количество слов
for i in range(len(all_text)):
    sum_s = 0
    sum_s += len(all_text[i].split())
    # количество букв
    max_s = 0
    for j in all_text[i].split():
        max_s += len(j)
    print(all_text[i])
    print(f'{i+1} строка имеет {sum_s} слов(а) и {max_s} букв(символов)')
