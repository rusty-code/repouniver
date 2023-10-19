f = open("textfile5.txt", "r")

iter = 0
ans = 0

for it in f:
    try: # если не натуральное число, то пропуск
        if it[0] == "0" or int(it)<=0:
            print(f"expt {it}")
            continue
        ans += int(it)
    except ValueError: # обработка не int
        print(f"Find a not int number {it}")
    else: # всё ОК
        print(it)
        iter += 1

print(iter, ans/iter)

f.close()
