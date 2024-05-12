
# Дан односвязный линейный список и ссылка на его head
# Вставить занчение M после каждого K элемента списка
# Вывести ссылку на послдений элемент полученного списка 

import structreofdata.classList as sodl
import structreofdata.classNode as cnd
from structreofdata.valid_input import valid_inpt as vinput



def main():

    lst = sodl.List()
    # fill list
    n = 10 # num of elements
    for it in range(0, n):
        lst.pushend(float(it))
    print("Связный список:\n", lst)

    M = vinput("Введите вещественное число для вставки в список: ", "float")
    K = vinput("Ввелите параметр вставки целым числом: ", "int")
    if (K < n):
        k = 1
        for it in range(2, n, K):
            lst.insert(M, it + k)
            k += 1
    else:
        print("Выход за пределы списка....")
    
    print("Связный список:\n", lst)


if __name__ == "__main__":
    main()