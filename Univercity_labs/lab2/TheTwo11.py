
while 1:
    n = float(input("Введите натуральное число: "))
    if n > 0 and (n*10%10) == 0: # проверка на натуральность число
        n = int(n)
        res = 0
        for it in range(1, n+1):
            pw = it
            for it1 in range(1, it):
                pw *= it1
            print(it, pw)
            res += pw // it
            print("Результат: ", float(res))
        break
    else:
        print("Некорректный ввод. Повторите попытку...")