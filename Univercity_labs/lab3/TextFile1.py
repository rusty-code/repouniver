file = open("textfile1.txt", "w")

invalid_txt = "Некорректный ввод. Повторите попытку..."

def valid_inpt(txt):
    while True:
        try:
            tmp = input(txt)
            if tmp[0] == "-":
                print(invalid_txt)
            else:
                return int(tmp)
        except ValueError:
            print(invalid_txt)

print("Поиск чисел Фибоначчи на заданном отрезке:")
print()

bg = valid_inpt("Введите начало отрезка целым числом: ")
end = valid_inpt("Введите конец отрезка целым числом: ")

# prevalid
if bg == 0:
    file.write(str(0) + '\n')

a = 0
b = 1
c = 0
for it in range(bg, end+1):
    if bg <= a+b <= end:
        file.write(str(a+b) + '\n')
    c = a
    a = b
    b += c

file.close()