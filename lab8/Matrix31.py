# Дана матрица размера M × N. Найти номера строки и столбца для элемента матрицы,
# наиболее близкого к среднему значению всех ее элементов.

DEBUG = False
def info_log(s : str, endstr = '\n'):
    if DEBUG: 
        print(f"#DEBUG: ({s})", end= endstr)
    return DEBUG
file = open('testcase_matrix31.txt', 'r').readlines()


# convert all elements from str matrix to float
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

        
cspis = [] # for convert spis


for it in range(0, len(file)):
    cspis.append(convert_strMtrx(file[it].split()))

if info_log("File: ", ' '): print(file)
if info_log("List: ", ' '): 
    print('\n', end='')
    for string in cspis:
        for it in string:
            print(it, end=' ')
        print('\n', end='')

# search sum of elements matrix
sum_elements = 0
count = 0
for string in cspis:
    for element in string:
        sum_elements += element
        count += 1

if info_log("Sum e-ts: ", ' '): print(sum_elements)
if info_log("Count: ", ' '): print(count)

midvar = sum_elements/count # среднее значение
thisnum = cspis[0][0] # так как ищем наибольший в матрице, то берём элемент из её же множества
mindiff = round(midvar - thisnum, 5) # initilize var for answer
# iteration all elements 
for string in cspis:
    for element in string:
        if abs(midvar - element) < mindiff:
            thisnum = element
            mindiff = round(midvar - element, 5)
mindiff = round(mindiff, 5) # избавляемся от хвоста


if info_log("Midvar: ", ' '): print(midvar)
if info_log("Mindiff: ", ' '): print(mindiff)
if info_log("Thisnum: ", ' '): print(thisnum)

for lev0 in range(0, len(cspis)):
    for lev1 in range(0, len(cspis[0])):
        if cspis[lev0][lev1] == thisnum:
            print(f"Позиция этого элемента в матрице:\n строка - {lev0}\nстолбец - {lev1}")
        
