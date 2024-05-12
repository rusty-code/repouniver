# Reccur3. Написать рекурсивный алгоритм определения
# произведения цифр целого числа N.

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
        except ValueError:
            print(invalid_txt)


def powNumbers(n):
    if n < 10:
        return n
    
    return n % 10 * powNumbers(n//10)

print(powNumbers(int(input("Input"))))