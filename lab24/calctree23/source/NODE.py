

class Node:
    """An any node at the list"""

    def __init__(self, data = None, next = None):
        self._next = next
        self._data = data

    def __str__(self):
        return f"1. data: {self.get_data()}\n2. hasnext next: {not self.is_empty()}" 

    def is_empty(self):
        if (self._data is None):
            return True
        return False

    def get_next(self): 
        return self._next

    def get_data(self):
        return self._data

    def update_data(self, data):
        self._data = data
    
    def update_next(self, next):
        self._next = next
