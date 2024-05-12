# Дана сслыка на один из элементов списка
# Вывести кол-во элементов и ссылки на первый и последний элементы списка


import structureofdata.classDoublyLinkedList as soddl
from structureofdata.valid_input import valid_inpt as vinput, invalid_txt

def main():
    beg = 1
    end = 11
    dll = soddl.DoublyLinkedList()
    for it in range(beg, end):
        dll.insert(it)
    dll.print_list()

    # refer to an any element from list
    position = vinput(f"Ввод позиции элемента от {beg} до {end-1}: ", int) - 1
    while (position < beg and position >= end):
        print(invalid_txt)
        position = vinput(f"Ввод позиции элемента от {beg} до {end-1}: ", int) - 1

    A0 = dll.update_current(position-1).get_current()
    print(f"\nNode {position+1}:")
    A0.print_node()

    print(f"Кол-во элементов в списке : {dll.get_size()}")
    print(f"Первый элемент списка: {dll.get_first().get_data()}")
    print(f"Последний элемент списка: {dll.get_last().get_data()}")


if __name__ == "__main__":
    main()