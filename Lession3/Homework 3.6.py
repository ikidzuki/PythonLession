def int_func(word):
    return word.title()


def many_func(words):
    words = words.split()
    words_up = []
    for i in words:
        words_up.append(int_func(i))
    return words_up


print(int_func("слово"))
print(*many_func("несколько слов написанных через пробел"))
