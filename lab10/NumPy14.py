# Даны вектора: a, b, c размерности 3.
# Найти вектор d = 2a + (a + b - c)

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
    num = 1
    for it in matrix:
        print(f"{num}. |", end = "   ")
        for elem in it:
            print(f"{elem}", end="   ")
        num += 1
        print("|")

# Convert an elements from str to float
def convert_strMtrx(lst : list):
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = float(it)
        except ValueError:
            tmpNum = 0
        tmpLst.append(tmpNum)
    return tmpLst

def sum_vectors(vec1 : list, vec2 : list): # vector1 + vector2
    return [round(vec1[num] + vec2[num], 2) for num in range(0, min(len(vec1), len(vec2))) ]

def diff_vectors(vec1 : list, vec2 : list): # vector1 - vector2
    return [round(vec1[num] - vec2[num], 2) for num in range(0, len(vec1)) ]

def mod_vector( md_num : float, vec : list):# mod * vector
    return [round(vec[num] * md_num, 2) for num in range(0, len(vec)) ]
    

file = open('testcase1_NumPy14.txt', 'r').readlines()

cspis = []
# clear string to int
for it in range(0, len(file)):
    cspis.append(convert_strMtrx(file[it].split()))

# three vectors to matrix
matrix_vecs = np.array([cspis[0], cspis[1], cspis[2]])

print("Матрица векторов:")
output_mtrx(matrix_vecs)

apb = sum_vectors(matrix_vecs[0], matrix_vecs[1]) # a + b
print("a+b=", apb)
apbmc = diff_vectors(apb, matrix_vecs[2]) # a + b - c
print("a+b-c=", apbmc)
aa = mod_vector(2, matrix_vecs[0]) # 2*a
print("2*a=", aa)
aa_p_apbmc = sum_vectors(aa, apbmc) # 2 * a + (a + b - c)

print(f"Вектор d = 2a + (a + b - c) = {aa_p_apbmc}") # result