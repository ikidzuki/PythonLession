class Worker:
    def __init__(self, surname, name, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"Сотрудник: {self.surname} {self.name}")

    def get_total_income(self):
        print(f"Доход: {self._income['wage'] + self._income['bonus']}")


kassir = Position('Ковена', 'Анна', 'Кассир', 15000, 6500)
kassir.get_full_name()
kassir.get_total_income()
print('')
manager = Position('Бодров>', 'Андрей', 'Менеджер', 20000, 5000)
manager.get_full_name()
manager.get_total_income()
print('')
administrator = Position('Курлов', 'Борис', 'Администратор', 32500, 8750)
administrator.get_full_name()
administrator.get_total_income()
