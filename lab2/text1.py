print("Процесс моделирования подбрасывания монеты...")

orel = 0
reshka = 0

from random import *

for it in range(0, 20):
    if randint(0, 1) == 1:
        reshka += 1
        print("Подбрасывание #", it+1, ": РЕШКА")
    else:
        orel += 1
        print("Подбрасывание #", it+1, ": ОРЁЛ")

print("Кол-во ОРЛОВ: ", orel)
print("Кол-во РЕШЕК: ", reshka)