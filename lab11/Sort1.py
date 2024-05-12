
# Дан массив размерности N.
# Создать алгоритм сортировки
# Отсортированные числа должны быть в начале массива
# Между отстортированной частью и не отстортированной ставить символ "|"
# После каждой итерации выводить промежуточный результат сортировки
# Протокол алгоритма вывести в файл

import random

file = open("input_sort1.txt", "r").readlines() # input data
output_data = open("output_sort1.txt", 'w+') # file for output protocol


###################################FUNC`S####################################################################################

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
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
            continue
        tmpLst.append(tmpNum)
    return tmpLst


def write_toFile(wrt : str): # append a string 
    output_data.write(wrt + '\n')


def print_divList(lst : list, posit : int): # output list with different of sort part forom not sort with "|" word 
    tmp = '' # store for write to protokol file
    for it in range(0, len(lst)):
        print(lst[it], end = ' ')
        tmp = tmp + f"{lst[it]} "
        if it == posit:
            print('|', end= ' ')
            tmp = tmp + "| "
    write_toFile(tmp)
    print()
        
            
def sort_this(array : list): # procedur for sort array
    current = 0

    print_divList(array, -1)
    for it in range(0, len(array)):
        for it1 in range(it+1, len(array)):
            if array[it] > array[it1]:
                current = array[it]
                array[it] = array[it1]
                array[it1] = current
        print_divList(array, it)


###################################MAIN####################################################################################


cspis = [] # clean and convert data from file

for it in range(0, len(file)): # clear and convert 
    cspis.append(convert_strMtrx(file[it].split()))
    
rand_lst = [] # additionally test case
for it in range(0, random.randint(5, 9)):
    rand_lst.append(round(random.uniform(-5, 10), 2))

cspis.append(rand_lst)

# iteration of testcases
num_it = 1
for sortlist in cspis:
    write_toFile(f"Сортировка массива #{num_it}")
    sort_this(sortlist)
    write_toFile('\n')
    num_it += 1

output_data.close()