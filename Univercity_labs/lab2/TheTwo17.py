

while 1:
    n = float(input("Введите целое число: "))
    n = abs(n)
    a = set()
    if n*10%10 == 0:
        while n > 0:
            a.add(n%10)
            n//=10
        mx = 0
        break
    else:
        print("Некорректный ввод. Повторите попытку...")
