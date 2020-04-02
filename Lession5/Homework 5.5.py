import os

with open('text_5.txt', 'w', encoding='utf-8') as txt:
    n = [i for i in range(1, 10)]
    print(*n, f"\nСумма чисел = {sum(n)}", file=txt)
