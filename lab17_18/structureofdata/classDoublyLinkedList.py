

import structureofdata.classNode as cnd

class DoublyLinkedList:
    """An Class-container realized a doubly linked list"""

    def __init__(self):
        self._current = self._last = self._first = None
        self._size = 0


    def __str__(self):
        return f"1. Current : {self._current}\n2. First : {self._first}\n3. Last : {self._last}"


    def get_current(self): return self._current
    def get_first(self): return self._first
    def get_last(self): return self._last
    def get_size(self): return self._size


    def insert(self, data, pos = None):
        """default is insert to back"""
        
        if (self._first is None):
            # list is empty
            self._first = cnd.Node(data=data)
            self._last = self._current = self._first

        elif (pos is None):
            # default 
            tmpnode = self._last
            tmpnode.update_next( \
                        cnd.Node(\
                                data=data, 
                                next=None, 
                                prev=tmpnode
                                )
                            )
            self._last = tmpnode.get_next()
            self._current = self._last
        
        elif (pos == 0):
            tmpnode = self._first
            tmpnode.update_prev( \
                        cnd.Node(\
                                data=data, 
                                next=tmpnode, 
                                prev=None
                                )
                            )
            self._first = tmpnode.get_prev()
            self._current = self._last
        else:
            node = self.get_node(pos)
            
            node.get_prev().update_next( \
                                cnd.Node(\
                                        data=data, 
                                        next=node, 
                                        prev=node.get_prev()
                                        )
                                    )
            self._current = node.get_prev()
            
        self._size += 1

        return self
    

    def update_current(self, pos : int):
        self._current = self.get_node(pos)
        return self


    def switch(self, posbefore : int, posafter : int):
        nodebefore = self.get_node(posbefore) # moved node
        nodeafter = None # to moved node

        # simple switch data of nods
        if (posafter >= self._size):
            tmp = self._last
            
            self._last.update_data(nodebefore.get_data())
            nodebefore.update_data(tmp.get_data())

        else:
            nodeafter = self.get_node(posafter)
            tmp = nodebefore.get_data()

            nodebefore.update_data(nodeafter.get_data())
            nodeafter.update_data(tmp)


    def get_node(self, pos : int):
        # pos - thr position of node in List
        if (pos < 0 or pos >= self._size): 
            if pos < 0:
                pos = self._size + pos
            else:
                pos = pos - self._size
        elif (pos == 0): 
            return self._first
        elif (pos == self._size - 1): 
            return self._last
        
        # searh the node inside list
        node = self._first.get_next()
        p = 1
        while p < pos:
            node = node.get_next()
            p += 1

        # if ( (self._size - pos) >= pos ):
        #     # pos near for begin
        #     p = 1
        #     node = self._first.get_next()
        #     while (p != pos):
        #         node = node.get_next()
        #         p += 1
        # else:
        #     # pos near for end
        #     p = self._size - 1
        #     node = self._last.get_prev()
        #     while (p != pos):
        #         node = node.get_prev()
        #         p -= 1

        return node        


    def remove(self, pos : int):

        if (pos == 0):
            # save data
            data = self._first.get_data()

            # disconnect and redefine _first
            self._first = self._first.get_next()
            self._first.update_prev(None)

            # resize
            self._size -= 1

            return data
        
        if (pos == self._size - 1):
            # save data
            data = self._last.get_data()

            # disconnect and redefine _last
            self._last = self._last.get_prev()
            self._last.update_next(None)

            # resize
            self._size -= 1

            return data
        
        node = self.get_node(pos)
        
        # connect node.next and node.prev
        node.get_prev().update_next(node.get_next())
        node.get_next().update_prev(node.get_prev())

        # disconect node
        node.update_next(None)
        node.update_prev(None)

        self._size -= 1

        return node.get_data()
        # node has been cleared


    def print_list(self): 
        # output from begin list
        num_element = 0
        node = self._first
        while ( not (node is None) ):
            print(f"Node #{num_element}:")
            node.print_node()
            node = node.get_next()
            num_element += 1


    def print_reverselist(self): # output from end list (for test prev)
        num_element = self._size - 1 
        node = self._last
        while ( not (node is None) ):
            print(f"Node #{num_element}:")
            node.print_node()
            node = node.get_prev()
            num_element -= 1


