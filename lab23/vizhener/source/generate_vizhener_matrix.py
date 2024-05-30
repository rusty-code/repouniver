
from IOFILESTREEM import FileInstance


def cycle_shift(shift : int, arr : list) -> list:
    tmp = []
    for wd in range(-1, -shift-1, -1): # get end
        tmp.append(arr[wd])
    tmp.reverse()
    for wd in range(0, len(arr)-shift):
        tmp.append(arr[wd])

    return tmp
    

def open_close_keys_matrix(lat):
    
    matrix = [[]]*len(lat)
    for wd in lat:
        matrix[0].append(wd)
    
    for line in range(1, len(matrix)):
        matrix[line] = cycle_shift(
                                shift=line,
                                arr=lat
                            )

    for line in matrix:
        print(line)

    return matrix



def proc(act : str):

    print('GENERATE CODE MATRIX\n')

    lat = "abcdefghijklmnopqrstuvwxyz"
    
    # alphabet mtrx
    matrix = open_close_keys_matrix(lat)

    
    file = FileInstance(
        path='vizhener/source/files/code_matrix.txt'
    )

    for line in matrix:
        file.write(line, endstr=' ')
        file.write(['\n'], endstr='')
        
    

