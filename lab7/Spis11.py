# Дан произвольный список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет - не выводите ничего. 
# Если таких пар соседей несколько – выведите первую пару

# 0 - положителен!!!

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

flag = True
for it in range(0, len(cspis)-1):
    if cspis[it] >= 0 and cspis[it + 1] >= 0 and flag:
        print("Первая пара чисел с одним знаком: ", cspis[it], cspis[it + 1])
        flag = False
    elif cspis[it] < 0 and cspis[it + 1] < 0 and flag:
        print("Первая пара чисел с одним знаком: ", cspis[it], cspis[it + 1])
        flag = False
        

