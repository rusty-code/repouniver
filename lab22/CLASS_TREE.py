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
    
    def end_bypass(self, node:Node) -> list:
    
        if node is None:
            pass
        elif node.get_left() is None and node.get_right() is None:
            # self.end_bypass(node=node.get_left())
            print(node)
        elif not node.get_left() is None and node.get_right() is None:
            self.end_bypass(node=node.get_left())
            print(node)
        elif node.get_left() is None and not node.get_right() is None:
            self.end_bypass(node=node.get_right())
            print(node)
        else:
            self.end_bypass(node=node.get_left())
            self.end_bypass(node=node.get_right())
            print(node)
    
    def format(self, node : Node):
        if node is None: 
            return ''

        if node.get_left() is None and node.get_right() is None:
            return f'{node.get_data()}'

        if not node.get_left is None and node.get_right() is None:
            return f"({self.format(node.get_left())}){node.get_data()}"

        if not node.get_right() is None and node.get_left() is None:
            return f"{node.get_data()}({self.format(node.get_right())})"
        
        return f"({self.format(node.get_left())}){node.get_data()}({self.format(node.get_right())})"
    