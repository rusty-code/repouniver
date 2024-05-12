file = open('textfile9.txt', 'w+')
invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_ans(val, num):
    # откалывание последней цифры и сравнение с искомой
    while val > 0:
        if val % 10 == num:
            return True
        val //= 10
    return False

def valid_inpt(txt): # отсечение строк-чисел, нач с 0
    while True:
        try: # если строка-число содержит не цифру, то повторный ввод 
            tmp = input(txt)

            if tmp[0] == '-':
                if tmp[1] == '0':
                    print(invalid_txt)
                else:
                    return int(tmp)
            elif tmp[0] == '0':
                    print(invalid_txt)
            else:
                return int(tmp)
        except ValueError:
                print(invalid_txt)

while True:
    try:
        a = valid_inpt("Введите начало отрезка целым числом: ")
        b = valid_inpt("Введите конец отрезка целым числом: ")
        n = valid_inpt("Введите искомую цифру числа: ")
        
        # цифра прин. [0, 9]
        if n > 9 or n < 0:
            print(invalid_txt)
            continue            
        
        # начало отрезка всегда меньше конца
        if a < b:
            for it in range(a, b+1):
                if valid_ans(it, n):
                    file.write(str(it) + '\n')
            break
        else:
            continue
    except ValueError:
        print(invalid_txt)
    else:
        break


file.close()