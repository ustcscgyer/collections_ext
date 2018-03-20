BLACK = True
RED = False

class Node:
    __slots__ = ('key', 'value', 'color', 'size')
    
    def __init__(self, key, value, color, size=0):
        self.key = key
        self.value = value
        self.color = color
        self.size = size

def isRed(node):
    return node is not None and node.color == RED
        
class RedBlackTree:
    __slots__ = ('root', 'size')
    
    def __init__(self):
        self.root = None
        self.size = 0
        
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        self.root.color = BLACK
        
        return self

    def _put(self, node, key, value):
        if node is None:
            return Node(key, value, RED)    
        if key < node.key:
            node.left = self._put(node.left, key, value)
        elif key > node.key:
            node.right = self._put(node.right, key, value)
        else:
            node.value = value

        if not isRed(node.left) and isRed(node.right):
            node = self._rotateLeft(node)
        if isRed(node.left) and isRed(node.left.left):
            node = self._rotateRight(node)
        if isRed(node.left) and isRed((node.right)):
            node = self._flipColor(node)

        return node


    def search(self, key):
        node = self._search(self.head, key)
        if node is not None:
            return 
    
    def _search(self, node, key):
        if node is None:
            return None


    def _rotateLeft(self, node):
        x = node.right
        x.color = node.color
        node.color = RED
        node.right = x.left
        x.left = node

        return x

    def _rotateRight(self, node):
        x = node.left
        x.color = node.color
        node.color = RED
        node.left = x.right
        x.right = node

        return x

    def _flipColor(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

        return node

    
    
    
    
