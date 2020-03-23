nomenclature = []
number = int(input("Введите количество товаров: "))

for i in range (1, number+1):
    buy_dict = {"название": input("Наименование товара: "), "цена": input("Цена товара: "), "количество": input("Количество: "),"ед": input("Единицы измерения: ")}
    buy_list= (i, buy_dict)
    nomenclature.append((i, buy_dict))

print("Номенклатура товаров:")
for i in nomenclature:
    print(i)


named_value = []
print("Список наименований:")
for i in range (len(nomenclature)):
    named_value.append(nomenclature[i][1].get("название"))
named = {"Наименование": named_value}
print(named)
