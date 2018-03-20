class Node(object):
    __slots__ = ['value', 'next']
    
    def __init__(self, value=None):
        self.value = value
        self.next = [None] * 256
        
    def __repr__(self):
        return ('TrieNode:', self.value).__repr__()
        
class Trie(object):
    __slots__ = ['root', 'size']
    
    def __init__(self):
        self.root = Node()
        self.size = 0
        
    def get(self, key):
        """
        get gets the value of the node,
        search gets the node
        """
        node = self.search(key)
        if node is None: 
            return None
        else:
            return node.value

    def search(self, key):
        return self._search(self.root, key, 0)
        
    def _search(self, node, key, d):
        if node is None:
            return None
        
        if d == len(key):
            return node
        else:
            c = ord(key[d])
            return self._search(node.next[c], key, d+1)

    def insert(self, key, value=0):
        self.root = self._insert(self.root, key, value, 0)
        
        return self
        
    def _insert(self, node, key, value, d):
        if node is None:  node = Node()
        if d == len(key):
            if node.value is None:
                self.size += 1
            node.value = value
        else:
            c = ord(key[d])
            node.next[c] = self._insert(node.next[c], key, value, d+1)
        
        return node
