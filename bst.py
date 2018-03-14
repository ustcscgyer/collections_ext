class Node:
    __slots__ = ['value', 'right', 'left']
    def __init__(self, value):
        self.value=value
        self.left = None
        self.right = None
        
class BST:
    __slots__ = ['size', 'head', '_key']
    
    def __init__(self, key=lambda x : x):
        self.size = 0
        self.head = None
        self._key = key
        
    def insert(self, value):
        self.size += 1
        self.head = self._insert(self.head, value)
        
        return self
    
    @staticmethod
    def _insert(node, value):
        if node is None:
            return Node(value)
        elif value > node.value:
            node.right = BST._insert(node.right, value)
            return node
        else:
            node.left = BST._insert(node.left, value)
            return node

    def search(self, value):
        return self._search(self.head, value)
    
    @staticmethod
    def _search(node, value):
        if node is None:
            return None
        elif node.value == value:
            return node
        elif value > node.value:
            return BST._search(node.right, value)
        else:
            return BST._search(node.left, value)
        
    def floor(self, value):
        return self._floor(self.head, value)
    
    @staticmethod
    def _floor(node, value, cur=float('-inf')):
        if node is None:
            return cur
        elif value < node.value:
            return BST._floor(node.left, value, cur)
        else:
            return BST._floor(node.right, value, node.value)
        
    def ceil(self, value):
        return self._ceil(self.head, value)
    
    @staticmethod
    def _ceil(node, value, cur=float('inf')):
        if node is None:
            return cur
        elif value < node.value:
            return BST._ceil(node.left, value, node.value)
        else:
            return BST._ceil(node.right, value, cur)
        
    def floor_and_ceil(self, value):
        return self._floor_and_ceil(self.head, value)
    
    @staticmethod
    def _floor_and_ceil(node, value, cur=(float('-inf'), float('inf'))):
        if node is None:
            return cur
        elif value < node.value:
            return BST._floor_and_ceil(node.left, value, (cur[0], node.value))
        else:
            return BST._floor_and_ceil(node.right, value, (node.value, cur[1]))
        
    def range_search(self, low, high):
        return self._range_search(self.head, low, high)
    
    @staticmethod
    def _range_search(node, low, high):
        if node is None:
            return []
        elif low <= node.value <= high:
            return ([node] 
                    + BST._range_search(node.left, low, node.value) 
                    + BST._range_search(node.right, node.value, high))
        elif node.value > high:
            return BST._range_search(node.left, low, high)
        else:
            return BST._range_search(node.right, low, high)
