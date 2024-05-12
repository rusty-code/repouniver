# Найти целые числа из промежутка, квадрат числа которых полиндромичен


invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
        except ValueError:
            print(invalid_txt)

def polindr(num):
    ln = len(num)
    mun = ''
    # переворачивание входной строки
    for it in range(len(num) - 1, 0, -1):
        mun += num[it]

    flag = 0
    for it in range(0, ln//2):
        if num[it] == mun[it]: flag = 1
        else: flag = 0
    
    if flag == 1:
        return "Полиндромен"
    else:
        return "Неполиндромен"
    
while True:
    inp = valid_inpt("Введите целое число - начало отрезка : ")
    inp1 = valid_inpt("Введите целое число - конец отрезка : ")
    
    if inp >= inp1: # если начало больше конца, то возврат к вводу
        print(invalid_txt)
        continue
    for oi in range(inp, inp1+1):
        print(f"Квадрат числа {oi} = {oi*oi}... ", polindr(str(oi*oi)))
    break