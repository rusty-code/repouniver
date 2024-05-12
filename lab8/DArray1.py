# Дана матрица. Найти сумму элементов в заданном диапазоне: от строки s1 до s2 и со столбца st1 до st2

DEBUG = True
def info_log(s = '', endstr = '\n'): 
    if DEBUG: 
        print(f"#DEBUG: ({s})", end= endstr)
    return DEBUG

def print_matrix(mtrx): # Out a matrix like up to down
    for string in mtrx:
        for element in string:
            print(element, end=' ')
        print('\n', end='')

invalid_txt = "Ошибка ввода. Повторите попытку..."
def valid_input(txt : str): # valid: an elem -> number
    while True:
        try:
            tmp = int(input(txt))
            if tmp >= 0:
                return tmp
            else:
                print(invalid_txt)
        except ValueError:
            print(invalid_txt)

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



file = open('testcase_darray1.txt', 'r').readlines()

cspis = []

for it in range(0, len(file)):
    cspis.append(convert_strMtrx(file[it].split()))

if info_log(): print_matrix(cspis)

s1 = valid_input("Введите номер строки матрицы - начало диапазона подсчёта (целое, неотрицательное число): ") - 1
s2 = valid_input("Введите номер строки матрицы - конец диапазона подсчёта (целое, неотрицательное число): ") - 1

st1 = valid_input("Введите номер столбца матрицы - начало диапазона подсчёта (целое, неотрицательное число): ") - 1
st2 = valid_input("Введите номер столбца матрицы - конец диапазона подсчёта (целое, неотрицательное число): ") - 1

sum_elems = 0
for string in range(0, len(cspis)):
    for element in range(0, len(cspis[string])):
        # проверка, что элемнет попадает под искомый дтапазон
        if s1 <= string <= s2:
            if st1 <= element <= st2:
                sum_elems += cspis[string][element]
                if info_log(f"{cspis[string][element]}", ' '): print()
    print()
print(sum_elems)
