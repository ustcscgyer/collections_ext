class TstNode:
    __slots__ = ('val', 'c','left', 'right', 'mid')
    def __init__(self, c=None, val=None):
        self.val = val
        self.c = c
        self.left = self.mid = self.right = None
    
    def __repr__(self):
        return (self.c, self.val).__repr__()

class TST:
    __slots__ = ('size', 'root')

    def __init__(self, key_vals=[]):
        self.size = 0
        self.root = None

        for k, v in key_vals:
            self.put(k, v)

    def put(self, key, val=0):
        self.root = self._put(self.root, key, val)

        return self

    def _put(self, node, key, val, d=0):
        if node is None:
            node = TstNode(key[d])

        if key[d] < node.c:
            node.left = self._put(node.left, key, val, d)
        elif key[d] > node.c:
            node.right = self._put(node.right, key, val, d)
        elif d < len(key) - 1:
            node.mid = self._put(node.mid, key, val, d+1)
        else:
            if node.val is None: self.size += 1
            node.val = val
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

        return self

    def _delete(self, node, key, d=0):
        if node is None:
            return None
        elif key[d] < node.c:
            node.left = self._delete(node.left, key, d)
        elif key[d] > node.c:
            node.right = self._delete(node.right, key, d)
        elif d == len(key) - 1:
            self.size -= 1
            node.val = None
        else:
            node.mid = self._delete(node.mid, key, d+1)

        if node.val is not None:
            return node

        for n in [node.left, node.right, node.mid]:
            if n is not None:
                return node

        return None

    def prefix(self, pre):
        node = self._search(self.root, pre) 

        if node is None:
            return []
        elif node.val is None:
            return self._collect(node.mid, pre)
        else:
            return [pre] + self._collect(node.mid, pre)

    def _collect(self, node, pre):
        if node is None:
            return []
        elif node.val is not None:
            result = [pre + node.c]
        else:
            result = []

        if node.mid is not None:
            result = result + \
                    self._collect(node.mid, pre + node.c) +\
                    self._collect(node.left, pre) +\
                    self._collect(node.right, pre)

        return result

    def keys(self):
        return self._collect(self.root, '')

    def __iter__(self):
        return self.keys().__iter__()
        
    def contains(self, key):
        return self.get(key) != None

    def isEmpty(self):
        return self.size == 0

    def get(self, key):
        node = self._search(self.root, key)

        if node is None:
            return None
        else:
            return node.val

    def _search(self, node, key, d=0):
        if node is None:
            return None
        elif key[d] < node.c:
            return self._search(node.left, key, d)
        elif key[d] > node.c:
            return self._search(node.right, key, d)
        elif d < len(key) - 1:
            return self._search(node.mid, key, d+1)
        else:
            return node

    def items(self):
        raise NotImplementedError