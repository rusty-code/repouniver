
invalid_txt = "Некорректный ввод. Повторите попытку..."
def valid_inpt(txt,  data_type = 'float'): # Verefed input
    while True:
        try:

            tmp = input(txt)
            if data_type == 'int':
                return int(tmp)
            elif data_type == 'float':
                return float(tmp)
            else:
                return str(tmp)
        except ValueError:
            print(invalid_txt)

class Node:

    def __init__(self, data=None, left=None, right=None) -> None:
        # content
        self._data = data

        # descedants
        self._left = left
        self._right = right

    def __str__(self):
        out = f"head {self._data}"
        return out

    def __lt__(self, right_ins): # var: right_ins is Node
        return self._data < right_ins._data
    
    def __gt__(self, right_ins): # var: right_ins is Node
        return self._data > right_ins._data
    
    def __eq__(self, right_ins): # var: right_ins is Node
        return self._data == right_ins._data
    
    def is_end(self) -> bool:
        if not self._left is None and\
           not self._right is None:
                return False
        return True

    # getters
    def get_data(self):
        return self._data 
    
    def get_left(self):
        return self._left
    
    def get_right(self):
        return self._right

    # setters
    def set_data(self, data):
        self._data = data

    def set_left(self, node):
        if isinstance(node, Node):
            self._left = node
        else:
            raise TypeError(f"(ERROR) append to left not Node instance")
        
    def set_right(self, node):
        if isinstance(node, Node):
            self._right = node
        else:
            raise TypeError(f"(ERROR) append to right not Node instance")
    

class BinaryTree:

    def __init__(self, node=None):
        self._head = node
        self._nodes = []

    def find_for_insert(self, data, node:Node) -> Node:
        if data <= node.get_data():
            if node.get_left() is None:
                return node
            else:
                return self.find_for_insert(data, node.get_left())
        else:
            if node.get_right() is None:
                return node
            else:
                return self.find_for_insert(data, node.get_right())
        
    def append(self, data=None):
        if self._head is None:
            self._head = Node(data=data)
        else:
            node = self.find_for_insert(data=data, node=self._head)
            if data <= node.get_data():
                node.set_left(Node(data=data))
            else:
                node.set_right(Node(data=data))
    
    def _init_end_bypass(self, node:Node, nodes:list) -> list:
    
        # defence
        if node is None: return []
        
        # default - is end node
        elif node.get_left() is None and \
                       node.get_right() is None:
            # print(node)

            self._nodes.append(node.get_data())
        
        # to left node
        elif not node.get_left() is None and \
                        node.get_right() is None:
            
            self._init_end_bypass(
                                    node=node.get_left(), 
                                    nodes=nodes
                                )
            # print(node)

            self._nodes.append(node.get_data())
            

        # to right node
        elif node.get_left() is None and \
                        not node.get_right() is None: 

            self._init_end_bypass(
                                    node=node.get_right(), 
                                    nodes=nodes
                                )
            # print(node)

            self._nodes.append(node.get_data())
            

        # to rigth after left
        else:
            self._init_end_bypass(
                                    node=node.get_left(), 
                                    nodes=nodes
                                )
            self._init_end_bypass(
                                    node=node.get_right(), 
                                    nodes=nodes
                                )
            # print(node)

            self._nodes.append(node.get_data())
            
    
    # start find
    def end_bypass(self) -> list:
        self._init_end_bypass(self._head, [])
        return self._nodes


def main():
    tst = [ 0, 2, 1, 14, 2, 5, 6, 4, 3]
    tree = BinaryTree()
    for it in tst:
        tree.append(it)

    
    print(sorted(tree.end_bypass())[1])
   


def test():
    tree = BinaryTree()

    for it in [2, 4, 1, 3, 11, 12, -1, 0]:
        tree.append(float(it))
    print("Бинарное дерево:\n")
    tree.end_bypass()

    var = valid_inpt("Введите вещественное число для вставки в дерево\n(Ввод)> ")
    tree.append(var)
    print("Бинарное дерево:\n")
    tree.end_bypass()


if __name__ == "__main__":
    main()
    # test()