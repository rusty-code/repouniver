# Дано число D и вершина A1 непустого стека
# Добавить D в стек и вывести ссылку на вершину А2

import structreofdata.classStack as sods
from structreofdata.valid_input import valid_inpt as vinput

def main():

    stack = sods.Stack(sods.cnd.Node(1.0))

    print("Верхний элемент стека:")
    print(" 1. Данные: ", stack.peek())
    
    stack.push(vinput("Введите вещественное число: ", "float"))
    print("Верхний элемент стека:")
    print(" 1. Данные: ", stack.peek())
    print(" 2. Ссылка на вершину: id", id(stack.get_node()))



if (__name__ == "__main__"):
    main()