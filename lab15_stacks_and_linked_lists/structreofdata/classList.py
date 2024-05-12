

from structreofdata.valid_input import debug_print as dprint
import structreofdata.classNode as cnd


class List:
    """The Container-class realized linked list"""

    def __init__(self, node = None):
        self._head = node
        self._size = 0

    def __str__(self):
        node = self._head
        num = 1
        ret_str = ''
        while ( not(node is None) ):
            ret_str = ret_str + f"{num} : {node.get_data()}\n"
            
            node = node.get_next()
            num += 1
        
        return ret_str


    def is_empty(self):
        if (self._head is None):
            return True
        return False

    def pushbegin(self, node : cnd.Node) -> cnd.Node:
        if (self._head is None):
            self._head = node
        else:
            # insert to head
            tmp = self._head
            self._head = node
            self._head.update_next(tmp)
        self._size += 1

    def pushend(self, data):
        if (self._head is None):
            self._head = cnd.Node(data=data)
        else:
            # insert to end
            mainNode = self._head
            while (not mainNode.get_next() is None):
                mainNode = mainNode.get_next()
            mainNode.update_next(cnd.Node(data=data))
        self._size += 1

    def pop(self):
        if (self.is_empty()):
            return None
        else:
            poppednode = self._head
            self._head = self._head.get_next() 
            poppednode.update_next(None)

            return poppednode.get_data()
            # clearing poppednode
    
    def get_first(self):
        return self._head
    
    def insert(self, data, position):
        pos = 0
        node = self._head
        while (pos < position-1):
            node = node.get_next()
            pos += 1
        
        nextNode = node.get_next()
        node.update_next(cnd.Node(data=data, next=nextNode))


            
