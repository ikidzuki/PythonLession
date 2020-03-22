number_moth = int(input("Введите номер месяца: "))
if number_moth in (3,4,5):
    print("Это месяц пробуждающейся весны")
elif number_moth in (6,7,8):
    print("Это месяц палящего лета")
elif number_moth in (9,10,11):
    print("Это месяц депрессивной осени")
elif number_moth in (12,1,2):
    print("Это месяц леденящей зимы")
else:
    print("Не обманывай меня, это не номер месяца!")
