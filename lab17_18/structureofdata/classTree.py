
class Node:
    """Modificate node for tree"""

    def __init__(
            self, 
            child_num : int, 
            data = None, 
            prev = None, 
            childs = None
            ) -> None:
        
        self._data = data
        self._prev = prev
        self._num_childs = child_num
        self._childs = None

        # define a childs
        if not childs is None:
            if len(childs) != child_num:
                print(f"(ERROR) invalid creating childs -> child_num({child_num}) != len(childs)({len(childs)})")
            else:
                self._childs = childs
        else:
            self._childs = [None] * child_num
    
    def __str__(self):
        return self.str_node()

    def get_data(self): return self._data
    def get_prev(self): return self._prev
    def get_num_childs(self): return self._num_childs
    def get_childs(self) -> list: return self._childs
    def get_prev(self): return self._prev

    def get_child(self, index):
        if self._childs is None: 
            return None 

        if 0 <= index < self._num_childs:
            return self._childs[index]
        
        print(f"(ERROR) invalid index")
        return None

    def str_node(self):
        childs = ''
        for it in range(0, self._num_childs):
            if self._childs[it] is None:
                childs = childs + f"    Child {it} : {None}\n"
            else:
                childs = childs + f"    Child {it} : {self._childs[it].get_data()}\n"

        return f"HEAD : {self._data}\n" + childs

    def print_node(self): print(self.str_node())


    def update_data(self, data): self._data = data
    def update_prev(self, prev): self._prev = prev

    def update_child(self, index, child):
        if 0 <= index < self._num_childs:
            self._childs[index] = child
        else:
            print(f"(ERROR) invalid index")

    def update_childs(self, childs):
        pass

class Tree:

    """ The class for create ABSTRACT TREE.

        - A number of children for vertex define 
        whith creting the instance of class.
        - Power by double linked list
        - A Default number childs of childs == num childs of head """
    
    def __init__(self, child_num : int, data):
        self._head = Node(data=data, child_num=child_num)
        self._current = None

    def push(self, data, child_num = None): # cyclic uniform filling
        
        current = self._head.get_childs() # start level
        this_node = None

        while this_node is None:
            _search_None(current)

        # recure find empty node
        def _search_None(current : list):
            index = 0
            for it in range(0, len(current)):
                if current[it] is None:
                    if this_node is None:
                        this_node = Node(data=data, child_num=self._head.get_num_childs())
                        
