import os

while True:
    with open('test.txt', 'a') as hm:
        st = input("Введите строку: ") + "\n"
        if st == "\n":
            break
        hm.write(st)
