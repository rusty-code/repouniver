# В файле (input_sort13.txt) записан набор целых чисел по возрастанию
# Дано целое число Х
# Найти число вхождений числа Х

# Для генерации набора целых числе исп. generateInputData_sort13.py


file = open("input_sort13.txt", "r")
s = file.readline().split(' ')

# Convert an elements from str to float
def convert_str(lst : list):
    tmpLst = []
    tmpNum = 0
    for it in lst:
        try: 
            tmpNum = int(it)
        except ValueError:
            continue
        tmpLst.append(tmpNum)
    return tmpLst


nums = convert_str(s)

nums = [-1, -1, -1, 0, 0, 0, 0, 1, 2, 2, 3, 5, 5] # for test cases

# recursive binary search 
def bin_find(array : list, this_val : int, left : int, right : int):
    if (right - left == 1): return -1
    
    mid_index = (right + left) // 2
    
    if (array[mid_index] == this_val):
        return mid_index
    elif (array[mid_index] > this_val):
        return bin_find(array, this_val, left, mid_index)
    elif (array[mid_index] < this_val):
        return bin_find(array, this_val, mid_index, right)
    else:
        return -1


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




print("Список элементов: ")
print(*nums)
var = valid_inpt("Введите искомый элемент, чтобы найти его кол-во в массиве: ", "int")

ind = bin_find(nums, var, 0, len(nums) - 1)

if (ind != -1):
    # find left index
    ind1 = ind
    while (ind1 >= 0 and nums[ind1] == var):
        ind1 -= 1
    ind1 += 1
    
    #find right index
    ind2 = ind
    while (ind2 < len(nums) and nums[ind2] == var):
        ind2 += 1
    ind1 -= 1

    print(f"Кол-во элеметов {var} в массиве = {ind2 - ind1 - 1}")
else:
    print("Этот элемент в массиве отсутствует")


file.close()