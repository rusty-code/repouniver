file = open("textfile16.txt", "r")
invlid_text = "Некорректный ввод. Повторите попытку..."

flag = True
pw = 0
num = 0
for it in file:
    try:
        pw += int(it)
        num += abs(int(it))
    except ValueError:
        print("find error word: ", it)

if pw != num:
    flag = False

print(flag)


file.close()