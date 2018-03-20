class QuickUnion(object):
<<<<<<< HEAD
    __slots__ = ('_parent', '_size')

    def __init__(self, n, connections=None):
        self._parent = list(range(n))
        self._size = [1] * n
=======
    def __init__(self, n, connections=[]):
        self.parent = list(range(n))
        self.size = [1] * n
>>>>>>> 1e1729fd9866636da7eb6bb88cea9ab91ce8a375

        for conn in connections:
            self.union(conn[0], conn[1])

    def _root(self, k):
        p = self._parent
        while k != p[k]:
            p[k] = p[p[k]]  # This simple trick enhances the performance
            k = p[k]
        
        return k

    def union(self, a, b):
        """
        Make connection between a and b
        """
        roota = self._root(a)
        rootb = self._root(b)

        if roota != rootb:
            if self._size[roota] < self._size[rootb]:
                self._parent[roota] = rootb
                self._size[rootb] += self._size[roota]
            else:
                self._parent[rootb] = roota
                self._size[roota] += self._size[rootb]

    def connected(self, a, b):
        """
        Whether a and be are connected
        """
        return self._root(a) == self._root(b)
