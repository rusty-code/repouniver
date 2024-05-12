

def PowerA3(num):
    res = 1
    for i in range(0, 3):
        res *= num
    return res

invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return float(tmp)
        except ValueError:
            print(invalid_txt)

print("Нахождение 3ей степени числа: ")
while True:
    for it in range(0, 5):
        #num = valid_inpt("Введите вещественное число: ")
        print("3я степень этого числа = ", round(PowerA3(num = valid_inpt("Введите вещественное число: ")), 3))
    break