user_words = input("Введите несколько слов: ").split()
print(user_words)
for i in range (len(user_words)):
    if len(user_words[i]) > 10:
        print(f"{i+1} строка - {user_words[i][:10]}...")
    else:
        print(f"{i + 1} строка - {user_words[i]}")