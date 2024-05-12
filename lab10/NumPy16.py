# Дана матрица n*n
# Заполнить её по столбцам числами от [1, 10] (не включая границы)
# Запрость у пользователя номера столбцов, которые нужно поменять местами

import numpy as np

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  data_type = 'float'): # Verefed input
    while True:
        try:

            tmp = input(txt)
            if data_type == 'int':
                if int(tmp) > 0: return int(tmp)
            elif data_type == 'float':
                if float(tmp) > 0: return float(tmp)
            else:
                return str(tmp)
        except ValueError:
            print(invalid_txt)


def output_mtrx(matrix : np.array): # print array
    for it in matrix:
        print('| ', end = ' ')
        for elem in it:
            print(elem, end=' ')
        print(' |')

while True:
    n = valid_inpt("Для создания 2-мерного массива введите его размерность натуральным нечётным числом >1: ", 'int')
    if n > 1:
        break
    print("Зачем вам 2-мерный массив из одного единственного элемента(-_-)?")

matrix = np.array([[0]*n]*n)

plusNum = 1
for stringMtrx in range(0, n):
    for columnMtrx in range(0, n):
        if plusNum > 10: plusNum = 1
        if columnMtrx != 0 and columnMtrx != n-1:
            matrix[stringMtrx][columnMtrx] = plusNum
            plusNum += 1
    plusNum = 1

output_mtrx(matrix)

while True:
    i = valid_inpt("Введите номер первого столбца натуральным нечётным числом: ", 'int') - 1
    if 0<=i<n:
        break
    print("Такого номера столбца не существует. Повтрите попытку...")

while True:
    j = valid_inpt("Введите номер второго столбца натуральным нечётным числом: ", 'int') - 1
    if 0<=j<n:
        break
    print("Такого номера столбца не существует. Повтрите попытку...")


# switch i-column and j-column
tmp = 0

for stringMtrx in range(0, n):
    tmp = matrix[stringMtrx][i]
    matrix[stringMtrx][i] = matrix[stringMtrx][j]
    matrix[stringMtrx][j] = tmp

output_mtrx(matrix)