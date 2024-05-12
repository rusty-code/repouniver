# Даны целые пложительные числа M, N. Сформировать матрицу MxN
# Все элементы i-строки == i*10 (i == 1, .. , N)

invalid_txt = "Ошибка ввода. Повторите попытку..."
def valid_input(txt: str): # valid: an elem -> number
    while True:
        try:
            tmp = int(input(txt))
            if tmp >= 0:
                return tmp
            else:
                print(invalid_txt)
        except ValueError:
            print(invalid_txt)


M = valid_input("Введите кол-во элементов в строке матрицы (целое, положительное число): ")
N = valid_input("Введите кол-во строк матрицы (целое, положительное число): ")

#matrix = [ [0] * M ] * N # 
matrix1 = []

mut = 1
# for lev0 in range(0, len(matrix)):
#     for lev1 in range(0, len(matrix[lev0])):
#         matrix[lev0][lev1] = mut * 10
#     mut += 1


for string in range(0, N):
    tmp = []
    for coumn in range(0, M):
        tmp.append(mut * 10)
    mut += 1
    matrix1.append(tmp)



# Print matrix
for lev0 in range(0, N):
    for lev1 in range(0, M):
        print(matrix1[lev0][lev1], end = ' ')
    print()



