time = int(input("Введите время(в секундах):"))

hours = time / 60 // 60 % 24
min = time // 60 % 60
sec = time % 60
print('{:02}'.format(int(hours)), '{:02}'.format(int(min)), '{:02}'.format(int(sec)), sep=':')