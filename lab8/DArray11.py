# Дана матрица. Найти значение первого максимального элемента матрицы и его индексы

DEBUG = False
def info_log(s = '', endstr = ' '): 
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



file = open('testcase_darray11.txt', 'r').readlines()

cspis = []

if info_log("Матрица была взята из файла: testcase_darray11.txt"): print_matrix(cspis)

for it in range(0, len(file)):
    cspis.append(convert_strMtrx(file[it].split()))

#if info_log(): print_matrix(cspis)

# Find max element
max_element = cspis[0][0]
for string in cspis:
    for element in string:
        if max_element < element:
            max_element = element

if info_log('Max element', ' '): print(max_element)

# Find position of first max element
position = { 'столбец' : None, 'строка' : None }
for string in range(0, len(cspis)):
    for element in range(0, len(cspis[string])):
        if position['столбец'] == None and position['строка'] == None:
            if cspis[string][element] == max_element:
                # +1 because list begin with 0
                position['столбец'] = element + 1
                position['строка'] = string + 1

print(f"Максимальный элемент: {max_element}")
print(f"Позция элемента: строка - {position['строка']}, столбец  - {position['столбец']}")













