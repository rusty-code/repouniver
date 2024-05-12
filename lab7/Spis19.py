
# Дан произвольный список, содержащий неcколько нулей.
# Требуется переместить все нулевые элементы в правый конец,
# сдвинув при этом все элементы влево сохраняя их порядок

def valid_convert(num): # проверка, чтобы эелемент был числом
    try:
        return float(num)
    except ValueError:
        print(f'Из ввода было исключено: {num}') # если не число, то возврат 'None'


spis = list(input("Введите список элементов через пробел: ").split()) # Создание списка под элнменты ввода 

cspis = list() # Список для очищенного ввода 
for it in range(0, len(spis)):
    conv = valid_convert(spis[it])
    if conv != None: # если элемент число, то зансение его в список
        cspis.append(valid_convert(spis[it]))

print("Очищенный список: ", cspis)

def func(arr, var):
    for go in range(0, var):
        for it in range(0, len(arr)):
            if arr[it] == 0:
                for it1 in range(it+1, len(arr)):
                    arr[it1-1] = arr[it1]
                    arr[it1] = 0
    return arr

itszero = 0
for zero in cspis:
    if zero == 0:
        itszero += 1

cspis = func(cspis, itszero//2+1)

print(cspis)