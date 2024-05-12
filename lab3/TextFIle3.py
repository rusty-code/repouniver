file = open("textfile3.txt", "+w")
invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            #if tmp[0] == "-":
             #   print(invalid_txt)
            #else:
            return int(tmp)
        except ValueError:
            print(invalid_txt)

print("Поиск чисел Фибоначчи на заданном отрезке:")
print()

while True:
    N = valid_inpt("Введите целое число: ")
    K = valid_inpt("Введите кол-во чисел фибоначчи целым числом: ")

    if K >= 0:
        # алгоритм поиска чисел фибоначчи
        a = 0
        b = 1
        c = 0
        if N < 0: # препроверка на 0
            file.write(str(0) + '\n')
            file.write(str(1) + '\n')
            K -= 3
        count = 0
        while count <= K:
            if a+b >= N and (a+b)%2==1: # проверка на условие
                file.write(str(a+b) + '\n')
                count += 1
            c = a
            a = b
            b += c
        break
    else:
        print(invalid_txt)


file.close()