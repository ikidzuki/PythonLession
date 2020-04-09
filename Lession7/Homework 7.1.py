class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        return '\n'.join([' '.join(str(j) for j in i) for i in self.matr])

    def __add__(self, other):
        return '\n'.join([' '.join(str(self.matr[i][j] + other.matr[i][j]) for j in range(len(self.matr[i]))) for i in
                          range(len(self.matr))])


matrix_1 = Matrix([  # начало матрицы
    [6, 9, 3],
    [0, 2, 9],
    [1, 0, 5],
])  # конец матрица

matrix_2 = Matrix([  # начало матрицы
    [3, 0, 6],
    [2, 5, 1],
    [7, 3, 3],
])  # конец матрица

print(f'Первая матрица:\n{matrix_1}')
print('')
print(f'Вторая матрица:\n{matrix_2}')
print('')
print(f'Сумма матриц:\n{matrix_1 + matrix_2}')
