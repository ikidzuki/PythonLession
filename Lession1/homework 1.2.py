time = int(input("Введите время(в секундах):"))

hours = int(time / 60 // 60 % 24)
min = time // 60 % 60
sec = time % 60
print(f"{hours:02}:{min:02}:{sec:02} ", sep=':')
