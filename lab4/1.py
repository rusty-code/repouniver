# Доказать теорему Гольдбаха (четное число == сумма двух простых)

invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = int(input(txt))
            if tmp <= 2 or tmp % 2 != 0:
                print(invalid_txt)
                continue
            return tmp
        except ValueError:
            print(invalid_txt)

def is_prost(n):
    for it in range(2, n):
        if n % it == 0:
            return False
    return True

def goldbah(n):
    for it in range(1, n):
            if is_prost(it):
                for it1 in range(1, n - it + 1):
                    if is_prost(it1):
                        print("nums:", it, it1 )
                        if (it + it1 == n):    
                            return True
    return False
                

print(goldbah(valid_inpt("Введите чётное число >2: ")))
