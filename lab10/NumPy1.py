# Дано нечётное n. Создать 2-мерный массив n*n и заполнить его "."
# Заполнить средние столбец и строку симв. "*"
# Вывевести полученныйц массив, разделяя элементы пробелом 

import numpy as np

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  data_type = 'float'): # Verefed input
    while True:
        try:

            tmp = input(txt)
            if data_type == 'int':
                return int(tmp)
            elif data_type == 'float':
                return float(tmp)
            else:
                return str(tmp)
        except ValueError:
            print(invalid_txt)


def output_mtrx(matrix : np.array): # print array
    for it in matrix:
        for elem in it:
            print(elem, end=' ')
        print()


while True: # verefied input
    n = valid_inpt("Для создания 2-мерного массива введите его размерность натуральным нечётным числом: ", 'int')
    if n > 1 and n % 2 != 0:
        break
    print(invalid_txt)


# creating 2 dem-l array
matrix = np.array([['.']*n]*n)

print("Исходный 2-х мерный массив:")
output_mtrx(matrix)

print() # <-- this is a identation

print(f"Исходный 2-х мерный массив с изменёнными средними строкой и столбцом:")
# change the middle str
for theElement in range(0, n):
    matrix[n//2][theElement] = '*'
    matrix[theElement][n//2] = '*'

output_mtrx(matrix)
