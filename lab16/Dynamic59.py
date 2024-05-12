# Даны ссылки на первый, последний и текущий элементы
# Дано число N>0, кол-во целых чисел
# Добавить в конец списка набор N чисел
# При помощи метода Put класса PT обёрнутых в процедуру Put (без параметров) 
# вывести первый, последний и текущий элементы 

import structureofdata.classDoublyLinkedList as soddl
from structureofdata.valid_input import valid_inpt as vinput, invalid_txt

class PT:

    def __init__(self, dll : soddl.DoublyLinkedList):
        self.dll = dll

    def Put(self):
        print("Элементы списка:")
        print(f"    Первый элемент {self.dll.get_first().get_data()}")
        print(f"    Последний элемент {self.dll.get_last().get_data()}")
        print(f"    Текущий элемент {self.dll.get_current().get_data()}")

pt = PT(soddl.DoublyLinkedList())

def Put():
    global pt
    pt.Put()

def main():
    global pt
    
    beg = 1
    end = 6

    dll = soddl.DoublyLinkedList()
    for it in range(beg, end):
        dll.insert(it)
    dll.print_list()

    for it in range(100, 100+vinput("Введите кол-во целых чисел: ", int)):
        dll.insert(it)
    dll.print_list()

    dll.insert(vinput("Введите число целое число D: ", int))
    
    pt = PT(dll)

    Put()


if __name__ == "__main__":
    main()