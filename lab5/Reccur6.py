# Кол

invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
        except ValueError:
            print(invalid_txt)

def reccursum(s, n):
    if n <= 1: # Базовый случай
        return s
    
    return s + reccursum(s*s, n-1)


while True:
    inp = valid_inpt("Введите кол-во членов ряда целым неотриц. числом <8: ")
    if inp < 0 or inp >= 8: # Допроверка корректности вводимых данных
        print(invalid_txt)
        continue
    
    print(f"Сумма первых {inp} элементов: ", reccursum(2, inp))
    break