
# Дан произвольный список чисел. Определите количество элементов, которые больше
# обоих своих соседей, и выведите количество таких элементов.

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

res = 0
for it in range(1, len(cspis)-1):
    if cspis[it-1] < cspis[it] and cspis[it+1] < cspis[it]:
        print(cspis[it])
        res += 1

print("Количество чисел, больше своих сосдей равно: ", res)
