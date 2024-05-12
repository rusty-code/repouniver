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

def unique_read_matrix() # geting string with div 