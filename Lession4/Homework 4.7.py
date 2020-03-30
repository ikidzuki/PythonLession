def factorial(x):
    a = 1
    for i in range(1, x + 1):
        a *= i + 1
        if len(str(a)) > 15:
            result = str(a)[:15] + "..."
        else:
            result = a
        yield result


generator = factorial(19)

for el in generator:
    print(el)
