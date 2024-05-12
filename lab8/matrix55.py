# Дана матрица. Поменять верхнюю и нижнюю половины местами

DEBUG = True
def info_log(s : str, endstr = '\n'):
    if DEBUG: 
        print(f"#DEBUG: ({s})", end= endstr)
    return DEBUG
file = open('testcase_matrix55.txt', 'r').readlines()

def print_matrix(mtrx):
    for string in mtrx:
        for element in string:
            print(element, end=' ')
        print('\n', end='')

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



def switchString_matrix(fullarr, party_check):
    begTailup = 0 # начальная строка верхней части
    endTailup = cnt_strgs//2 # конечная  верней части
    tailOftailup = [] # список под верхнюю часть

    begTaildown = cnt_strgs//2 + party_check # party_check - избежание захвата ценьральной строки 
    endTaildown = cnt_strgs
    tailOftaildown = []

    while (begTailup < endTailup) and (begTaildown < endTaildown):
        
        # закидываем строки матрицы для смены
        tailOftailup = fullarr[begTailup] 
        tailOftaildown = fullarr[begTaildown]

        # свитчуем их
        fullarr[begTailup] = tailOftaildown
        fullarr[begTaildown] = tailOftailup

        # переходи к след. строкам
        begTailup += 1
        begTaildown += 1

    return fullarr    



cspis = []

# забиваем массив значениями из файла
for it in range(0, len(file)):
    cspis.append(convert_strMtrx(file[it].split()))

print_matrix(cspis)

cnt_strgs = len(cspis)

print()
print_matrix(switchString_matrix(cspis, cnt_strgs%2))