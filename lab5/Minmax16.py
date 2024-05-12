
# Minmax16. Дано целое число N и набор из N целых чисел. 
# Найти количество элементов, расположенных перед первым минимальным элементом


invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt): # Проверка ввода
    while True:
        try:
            tmp = input(txt)
            return int(tmp)
        except ValueError:
            print(invalid_txt)

def splitting(arrRight, arrLeft):
    if len(arrRight) > 1:
        return splitting(arrRight[0:(len(arrRight))])


#=========
while True:
    n = valid_inpt("Введите кол-во целых чисел целым числом >0: ")
    if n > 0:
        break
nums = [0] * n
for n in range(0, n):
    nums[n] = valid_inpt(f"Ввод {n+1} целого числа: ")

# для поиска максимального из них берем однго число из этого набора
mx = nums[0]
lenght = 0 # для нахождения кол-ва после последнего максимального
ln = n # дополнительный итератор для цикла
for lev in range(n):
    if nums[lev] >= mx:
        mx = nums[lev]
        lenght = ln
    ln -= 1

print(*nums)
print("Последнее максимальное число из этого списка: ", mx)
print("Кол-во чисел после него: ", lenght)
