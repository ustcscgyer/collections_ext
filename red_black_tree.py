BLACK = True
RED = False

class Node:
    __slots__ = ('key', 'value', 'color', 'size')
    
    def __init__(self, key, value, color, size):
        self.key = key
        self.value = value
        self.color = color
        self.size = size
        
class RedBlackTree:
    __slots__ = ('root')
    
    def __init__(self):
        self.root = None
        
        
    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)
        self.root.color = BLACK
        
        return self

    def _insert(self, node, key, value):
        pass
    
    def search(self, key):
        pass
    
    def _search(self, node, key):
        pass
    
    
    
    
