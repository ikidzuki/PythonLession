import os
import json

with open('text_7.txt', 'r', encoding='utf-8') as txt:
    ls_org = [i.rstrip().split() for i in txt] # Сразу выходим из with, чтобы не занимать файл

org_dict = {i[0] : (int(i[2]) - int(i[3]))for i in ls_org} # Создаем словарь организаций

# Ищем среднюю прибыль
counter = 0 # Счетчик количества орг-ий с плюсовой выручкой
earn_sum = 0 #Счетчик обющей прибыли
for key in org_dict:
    if org_dict[key] > 0:
        counter += 1
        earn_sum += org_dict[key]
result_dict = [org_dict, {'middle_earnings': (earn_sum / counter)}]

# Сохраняем список в json-файл
with open('text_7.json', 'w', encoding='utf-8') as n_jsn:
    json.dump(result_dict, n_jsn, indent=4)

