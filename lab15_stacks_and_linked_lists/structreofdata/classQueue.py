
import structreofdata.classNode as cnd
from structreofdata.valid_input import debug_print as dprint

class Queue:
    """The Container-class realized FIFO """
    
    def __init__(self, node = None):
        self._first = node 
        self._last = self._first # while in queue one element
        self._size = 1

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
    
    def first_is_last(self):
        if (self._first is self._last):
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

    def attach(self, queue): # attach queue to end self.queue
        while (not queue.is_empty()):
            self.push(queue.pop())

    def extract(self):
        node = self._first
        self._first = self._first.get_next()
        node.update_next(None)

        return node
        # clearing of extract node

    def get(self):
        return self._first


def merge(queue_main : Queue, queue : Queue) -> Queue: # first is _first, second parameter._frist and etc..
    # check queue`s for empty
    if (queue_main.is_empty()):
        if (not queue.is_empty):
            return queue
    elif (queue.is_empty()):
        if (not queue_main.is_empty()):
            return queue_main
        else:
            dprint("'merge' queue`s is empty")
            return Queue
    dprint(1)
    new_queue = Queue()
    while (
            not(queue_main.is_empty()) \
                  and \
            not(queue.is_empty())
        ):
            new_queue.push(queue_main.pop())
            new_queue.push(queue.pop())
            dprint(f"m\n{queue_main}")
            dprint(f"q\n{queue}")
            dprint(f"n\n{new_queue}")
    dprint(2)
    if (queue_main.is_empty()):
        if (queue.is_empty()):
            return new_queue
        else:
            new_queue.attach(queue)
    else:
        if ( not queue.is_empty() ):
            new_queue.attach(queue_main)
        else:
            dprint("'merge' return incomplete queue")
            return new_queue
        
        