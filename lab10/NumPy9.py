# Дано число n.
# Создать массив размерностью n*n
# Заполнить его случайными числами
# Отсортировать кажду строку по возрастанию


import numpy as np
import random


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
    n = valid_inpt("Для создания 2-мерного массива введите его размерность натуральным числом: ", 'int')
    if n > 1:
        break
    print(invalid_txt)


# creating 2 dem-l array
matrix = np.array([[0.0]*n]*n)

# filling the matrix a random float nums
for stringMtrx in range(0, n):
    for columnMtrx in range(0, n):
        matrix[stringMtrx][columnMtrx] = round(random.uniform(-1000, 1000), 3)#get_randfloat()

print("Исходый массив:")
output_mtrx(matrix)
print()

print("Исходный массив, отсортированный построчно в порядке возрастания:")
for stringMtrx in range(len(matrix)):
    matrix[stringMtrx] = sorted(matrix[stringMtrx])

output_mtrx(matrix)