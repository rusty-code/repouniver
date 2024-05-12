# Создать ф-цию генератор
# Ф-ция-генератор должна принимать список чисел
# Ф-ция-генератор должна возвращать список минимумов



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


# Convert an elements from str to float
def convert_strMtrx(lst : list) -> list:
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = float(it)
        except ValueError:
            tmpNum = 0
        tmpLst.append(tmpNum)
    return tmpLst


def _gnrt_func_read_array():
    try:
        with open("testcases/tst_sg1.txt", 'r') as file:
            spis = file.readlines() # list of strings

            for arr in range(0, len(spis)):
                yield (convert_strMtrx(spis[arr].split()))

    except FileNotFoundError: 
        if info_log(endstr=' '): print("File not found...")
    except:
        if info_log(endstr=' '): print("Runtime error...")


def _gnrt_func_find_mins(array : list):
    # default cases: valid of ends
    if   array[0] < array[1]:     
        yield array[0]
    if array[-1] < array[-2]:   
        yield array[-1]
    
    # find mins inside array
    for ind in range(1, len(array)-1):
        if array[ind] < array[ind-1] and \
           array[ind] < array[ind+1]:
                yield array[ind]


def main():
    cspis = [] # list of testcases-arrays

    for arr in _gnrt_func_read_array():
        cspis.append(arr)

    num_tst = 0
    for arr in cspis:
        print(f"testcase-{num_tst} : {arr}")
        print("Min`s: ", end=' ')
        for melem in _gnrt_func_find_mins(arr):
            print(melem, end=' ')
        num_tst+=1
        print()


if __name__ == "__main__":
    main()