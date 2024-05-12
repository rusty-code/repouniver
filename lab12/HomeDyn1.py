
# Дана квадратная доска NxN из целых неотриц. чисел
# По доске возможно сделать ход только на одну клетку вниз или вправо
# Методом "жадного алгоритма" определить максимальную сумму, которою возможно получить 
# начав в левом верхнем углу и закончив в правом нижнем

###################################FUNC`S####################################################################################


def convert_str(lst : list): # convert elem`s lst from str to int
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = int(it)
        except ValueError:
            continue
        tmpLst.append(tmpNum)
    return tmpLst


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


###################################MAIN####################################################################################

testcases = open("testcase1_HomeDyn1.txt", "r")

data = testcases.readlines() # read data from file
cspis = [] # clean and convert data from file


