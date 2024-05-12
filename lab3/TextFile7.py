file = open("textfile7.txt", 'r')


id = 1
sum = 0
for it in file:
    try:
        if id%2==1:
            sum += int(it)
        id += 1
    except ValueError:
        id += 1

print("Сумма нечетных элементов: ", sum)

file.close()