

while 1:
    n = int(input("Введите количество вещественнвх чисел целым числом >0: "))
    if n > 0:
        a = [0.0] * n

        print("Ввод вещественных чисел:")
        for it in range(0, n):
            print("Число №", it+1, ": ")
            a[it] = float(input())

        print("Сумма чисел", sum(a))

        tt = 1.0
        for it in a:
            tt *= it
        print("Произведение чесел", tt)

        break
    else:
        print("Некорректный ввод. Повторите попытку...")