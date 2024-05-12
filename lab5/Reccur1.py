# Кол-во цифр в числе рекурсивной ф-цией

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
        except ValueError:
            print(invalid_txt)

def countnumb(n):
    if (n < 0): n *= -1 # если отриц., то приведение к положительным
    if n < 10: # базовый случай
        return 1
    else:
        return 1 + countnumb(n//10)

print(countnumb(valid_inpt("Введите целое число N: ")))    
    