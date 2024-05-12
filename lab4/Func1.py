

def Sign(num):
    if (num < 0): return -1
    elif (num == 0): return 0
    elif (num > 0): return 1

invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return float(tmp)
        except ValueError:
            print(invalid_txt)

print("___Sign(A) + Sign(B)___")
while True:
    a = valid_inpt("Введите вещественное число A для выражения Sign(A) + Sign(B): ")
    b = valid_inpt("Введите вещественное число B для выражения Sign(A) + Sign(B): ")

    print("Значение выражения Sign(A) + Sign(B) = ", a + b)
        
    break