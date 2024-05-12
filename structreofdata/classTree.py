
# After experimetnting with an arbitrary number of node descedants,
# it turned out that is was impossible to create a noramal logic for append 
# a new descedant. 

# Possible ligic: balance append for node with defined count descedants.
# And other specific logic

from classDoublyLinkedList import DoublyLinkedList as DLL

DEBUG = True
def log(msg='', code=None, debug_data=dict):
    global DEBUG

    if DEBUG == True:
        if code is None:
            print(f"(DEBUG) {msg}")
        elif code == 0:
            print(f"(ERROR) {msg}")
        elif code == 1:
            print(f"(WARNING) {msg}")
        elif code == 2:
            print(f"(UNDEF) {msg}")
        
        if debug_data != {}:
            print("VARS:")
            num = 0
            for key in debug_data.keys():
                print(f"    {num}. {key} : {debug_data.get(key)}")
    
    # REALESE MOD
    else:
        print(msg)


class TreeNode:
    """
    Class realized node of Tree structure data.
        - Doesnt have funcs for traversing child and parents elemets
        - Have getters for acesses next array chields elements
        - Have setters for acesses prev element
        - Have func for self remove
        - Have funcs for removes
    """

    def __init__(self, data=None, next=None, prev=None) -> None:
        self._data = data
        
        """if is None -> instance is root node """
        self._prev = prev # TreeNode instance 

        self._next = DLL() # DLL instance
        self._next.insert(next) # append children element

    def _is_root(self):
        if self._prev is None:
            return True
        return False

    def __out_of_range(self, pos:int) -> bool:
        if 0 <= pos <= self._next.get_size():
            return False
        return True

    # setters
    def set_next(self, next=None): # return all childrens
        self._next = next
    
    def set_prev(self, prev):
        if self._is_root():
            log('node is root', 1) # warning
        else: 
            self._prev = prev
    
    def set_data(self, data=None):
        self._data = data

    def set_node_to_next(self, data=None, pos=int):
        if self.__out_of_range(pos):
            log(f'pos {pos} out of range', 0)
        else:
            self._next.get_node(pos).update_data(data)

    # getters
    def get_data(self):
        return self._data
    
    def get_all_childs(self) -> DLL:
        return self._next

    def get_chield(self, pos:int):
        if not self.__out_of_range(pos):
            return self._next.get_node(pos)
        log(f'pos {pos} out of range', 0)

    def get_prev(self) -> DLL:
        if self._is_root():
            log('node is root', 1) # warning
            return None
        return self._prev

    # removes
    def remove_self_linked(self):
        if self._is_root():
            log('node is root.\n for full clear TREE call method clear', 0)


class BaseTree:
    """
    Class realized tree 
        - Optional number chields for node
        - Uniform distrubutation of node append
    """

    def __init__(self, init=None) -> None:
        self._head = TreeNode(data=init)
        self._treedepth = 0 # if 0 -> tree have only root node

    def __out_of_depth(self, depth):
        if 0 <= depth <= self._treedepth:
            return False
        return True

    def append_to(self, depth:int):
        if self.__out_of_depth(depth):
            log(f'invalid depth: {depth}', 0)
        
        diving = 0
        while (diving < depth):
            pass

        
