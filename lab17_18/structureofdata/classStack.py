
import strucureofdata.classNode as cnd


class Stack:
    """The Container-class realized LIFO"""

    def __init__(self, node = cnd.Node):
        self._size = 1
        self._head = node # indicates to the "last in" element

    def is_empty(self):
        if (self._head is None):
            return True
        return False
    
    def push(self, data):
        if (self._head.get_data() is None):
            self._head = cnd.Node(data)
        else:
            new_node = cnd.Node(data=data, next=self._head)
            self._head = new_node

    def pop(self):
        if (self.is_empty()):
            return None
        else:
            poppednode = self._head
            poppednode.update_next(None)

            self._head = self._head.get_next() 

            return poppednode.get_data()
            # clearing poppednode

    def peek(self):
        if (self.is_empty()):
            return None
        return self._head.get_data()
        
    def get_node(self):
        return self._head
    
