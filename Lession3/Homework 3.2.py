def data_user1(name="Радищев", second_name="Антон", years="12.12.1912", city="Новоябрьск"):
    print(f"Имя: {name}, Фамилия: {second_name}, Год рождения: {years}, Город: {city}")


data_user1()


# 2 вариант
def data_user1(**kwargs):
    print(kwargs)


data_user1(
    name=input("Введите имя:").title(),
    second_name=input("Введите фамилию:").title(),
    years=input("Введите дату рождения:"),
    city=input("Введите город проживания:").title()
)
