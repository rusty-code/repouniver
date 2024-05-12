# Описать ф-цию Exp1, находящую приближенное значение exp(a)

import math

def exp(x, e):
    sum = 0
    for it in range(1, int(e)+100):
        a = (x**it)/(math.factorial(it))
        if a > e:
            sum += a
    return sum

def Exp1(num, e):
    return round(exp(num, e), 5)

invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return float(tmp)
        except ValueError:
            print(invalid_txt)

print("Нахождение приближенного значения ф-ции exp(x)")
x = valid_inpt("Введите заначение вещественного числа х: ")
e = 0
iter = 0
while iter < 4:
    e = valid_inpt(f"Введите занчение экспоненты >0 #{iter+1}: ")
    if e > 0:
        try:
            print("Значение округленного exp(x): ", Exp1(x, e))
            iter += 1
        except OverflowError:
            print("Ошибка переполнения. Введите число меньшее число...")
    else:
        print(invalid_txt)
