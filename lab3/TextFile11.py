file = open("textfile11.txt", "+w")
invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            if tmp[0] == "-":
                print(invalid_txt)
            else:
                return int(tmp)
        except ValueError:
            print(invalid_txt)

def sum_nums(num): # нахождение суммы цифр
    sum = 0
    while num > 0:
        sum += num%10
        num //= 10
    return sum

while True:
    N = valid_inpt("Введите целое число: ")
    K = valid_inpt("Введите искомую сумму цифр числа: ")

    if K >= 0:
        summa = 0
        for theNum in range(0, N): 
            if sum_nums(theNum) == K and sum_nums(theNum) > 0: # если сумма цифр == К, то записать в файл
                file.write(str(theNum)+'\n')
        break
    else:
        print(invalid_txt)


file.close()