# Дан односвязный линейный список и ссылка на его head
# Вставить занчение M после каждого второго элемента списка
# Вывести ссылку на послдений элемент полученного списка 

import structreofdata.classList as sodl
import structreofdata.classNode as cnd
from structreofdata.valid_input import valid_inpt as vinput



def main():

    lst = sodl.List()
    # fill list
    n = 11 # num of elements
    for it in range(0, n):
        lst.pushend(float(it))
    print("Связный список:\n", lst)

    M = vinput("Введите вещественное число для вставки в список: ")
    k = 0
    for it in range(2, n, 2):
        lst.insert(M, it + k)
        k += 1

    
    print("Связный список:\n", lst)


if __name__ == "__main__":
    main()