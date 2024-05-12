
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


def main():
    file = open("testcases/tstcase_backtrack7.txt", 'r')
    
    instr = file.readlines()
    cspis = []

    for it in range(0, len(file)):
        cspis.append(convert_strMtrx(instr[it].split()))

    if info_log(): print_matrix(cspis)

    file.close()



def test():
    pass



if __name__ == "__main__":
    # main()
    test()