
from structureofdata.valid_input import debug_print as dprint
import structureofdata.classNode as cnd

class Queue:
    """The Container-class realized FIFO """
    
    def __init__(self, node = None):
        self._first = node 
        self._last = self._first # while in queue one element
        self._size = 0
        if not node is None: # if node not default
            self._size += 1 

    def __str__(self):
        node = self._first
        num = 1
        ret_str = ''
        while ( not(node is None) ):
            ret_str = ret_str + f"{num} : {node.get_data()}\n"
            
            node = node.get_next()
            num += 1
        
        return ret_str

    def is_empty(self):
        if (self._first is None):
            return True
        return False
    
    def push(self, data = None):
        if (self.is_empty()):
            dprint("'push' is empty")
            self._first = cnd.Node(data)
            self._last = self._first

        elif (self._first == self._last): # if num of elem == 1
            dprint("'push' last is first")
            self._last = cnd.Node(data=data)
            self._first.update_next(self._last)

        else:
            dprint("'push' else")
            last_node = self._last
            self._last = cnd.Node(data)
            last_node.update_next(self._last)

        self._size += 1

    def pop(self):
        poppped = self._first
        if (poppped is None):
            return None
        self._first = poppped.get_next()
        poppped.update_next(None)

        return poppped.get_data()
        # clearing of popped node

    def extract(self):
        node = self._first
        self._first = self._first.get_next()
        node.update_next(None)

        return node
        # clearing of extract node

    def peek(self): 
        return self._first


        