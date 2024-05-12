# Reccur8. Написать рекурсивную функцию для вычисления суммы: 
# S = 1 + 2 + 6 + 24 + 120 + ... , содержащей N первых членов 
# (N - натуральное число, N < 15, S - вещественное).


invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
        except ValueError:
            print(invalid_txt)


def reccurSum(s, n, p):
    if n < 1:
        return s
    print(s)
    return s + reccurSum(s*p, n-1, p+1)

print(reccurSum(1, int(input("Input: ")), 2))
