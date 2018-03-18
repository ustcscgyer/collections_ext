class QuickUnion(object):
    def __init__(self, n, connections=[]):
        self.parent = list(range(n))
        self.size = [1] * n

        for conn in connections:
            self.union(conn[0], conn[1])

    def _root(self, k):
        p = self.parent
        while k != p[k]:
            p[k] = p[p[k]]
            k = p[k]
        
        return k

    def union(self, a, b):
        """
        Make connection between a and b
        """
        roota = self._root(a)
        rootb = self._root(b)

        if roota != rootb:
            if self.size[roota] < self.size[rootb]:
                self.parent[roota] = rootb
                self.size[rootb] += self.size[roota]
            else:
                self.parent[rootb] = roota
                self.size[roota] += self.size[rootb]

    def connected(self, a, b):
        """
        Whether a and be are connected
        """
        return self._root(a) == self._root(b)
