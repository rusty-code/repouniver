
# Дан односвязный линейный список и указатель на его head
# Необходимо вывести указатель на второй элемент списка
# (Спсисок сотоит минимум из 2 элементов)

import structreofdata.classList as sodl

def main():
    
    lst = sodl.List()
    # fill list
    for it in range(0, 10):
        lst.pushend(it)
    print("Связный список:\n", lst)

    head = lst.get_first()
    # print("Первый элемент списка: \n", head)
    print("Второй элемент списка: \n", head.get_next())

    

if __name__ == "__main__":
    main()