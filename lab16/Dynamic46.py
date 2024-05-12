# Дано число К > 0 и ссылка А0 на один из элементов списка
# Сдвинуть А0 на К позиций вперёд
# Если элементов перед А0 < К, то переместить А0 в конец списка

import structureofdata.classDoublyLinkedList as soddl
from structureofdata.valid_input import valid_inpt as vinput, invalid_txt


def main():
    beg = 1
    end = 11

    # create list
    dll = soddl.DoublyLinkedList()
    for it in range(1, 11):
        dll.insert(it)
    dll.print_list()

    # choose A0 element
    position = vinput(f"Ввод позиции элемента от {beg} до {end-1}: ", int) - 1
    while (position < beg and position >= end):
        print(invalid_txt)
        position = vinput(f"Ввод позиции элемента от {beg} до {end-1}: ", int) - 1

    A0 = dll.update_current(position).get_current()
    print(f"\nNode {position}:")
    A0.print_node()

    K = vinput("Введите число К, на которое сдвинуть элемент: ", int)
    if (position+K >= dll.get_size()):
        dll.remove(position)
        dll.insert(A0.get_data())
    else:
        dll.remove(position)
        if (position+K >= dll.get_size()):
            dll.insert(A0.get_data())
        else:
            dll.insert(data=A0.get_data(), pos=position+K)
    
    dll.print_list()


def test():
    dll = soddl.DoublyLinkedList()
    for it in range(1, 11):
        dll.push_back(it)
    dll.print_list()
    print("####################################################")
    dll.remove(0)
    dll.remove(dll.get_size() - 1)
    dll.remove(3)
    dll.print_list()
    print(dll.get_size())
    print("####################################################")
    dll.insert(data=1, pos=0)
    dll.insert(10)
    dll.insert(data=100, pos=3)
    dll.print_list()
    print(dll.get_size())


if __name__ == "__main__":
    main()
    # test()