

class Node:
    """An any node at a double linked list"""

    def __init__(self, data = None, next = None, prev = None):
        self._data = data
        self._next = next
        self._prev = prev
    
    def get_data(self): return self._data
    def get_next(self): return self._next # return a instance of Node
    def get_prev(self): return self._prev # return a instance of Node
    def get_str(self) : return f"1. Data : {self._data}\n2. Next : {self._next}\n3. Prev : {self._prev}\n"

    def update_data(self, data): self._data = data
    def update_next(self, next): self._next = next
    def update_prev(self, prev): self._prev = prev

    def print_node(self):
        print(f"    1. Data : {self._data}")
        print(f"    2. Next : {self._next}")
        print(f"    3. Prev : {self._prev}")

    