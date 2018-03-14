class Heap(object):
    """
    A list implementation for binary heap. 
    List element can be object and tuple, comparator can be specified
    by the key argument at construction.
    """
    __slots__ = ('_data', '_key')
    def __init__(self, data=[], key=lambda x : x, inplace=False):
        """
        Create binary heap with a given initial data interable. The input
        data is not muted, unless inplace parameter is specified to True.
        """
        if inplace:
            self._data = data
        else:
            self._data = data.copy()

        self._key = key
        self._heapfy()

    def _swim(self, k):
        """
        When a new value is insert at the bottum of the tree,
        swim method is used to keep the tree heapfied
        """
        d, key = self._data, self._key
        p = (k-1)//2
        while (k > 0 and key(d[p]) < key(d[k])):
            d[k], d[p] = d[p], d[k]
            k, p = p, (p-1)//2

    def _sink(self, k):
        """
        When a value is poped out from the top of the tree, for simplicity
        move the last element in the heap to the top, then sink method is 
        used to keep the tree heapfied
        """
        d, key = self._data, self._key
        j = 2*k+1

        while (j < len(d)):
            if j+1 < len(d) and key(d[j]) < key(d[j+1]): 
                j += 1
            if key(d[j]) < key(d[k]):  
                break
            
            d[k], d[j] = d[j], d[k]
            k, j = j, 2*k+1

    def _heapfy(self):
        """
        Use Floyd's method to heapfy the initial array
        """
        k = (len(self._data)-1)//2
        for i in range(k, -1, -1):
            self._sink(i)

    def insert(self, v):
        """
        After the insertion, the data array is kept to be heapfied
        """
        self._data.append(v)
        self._swim(len(self) - 1)

    def pop(self):
        """
        Pop out the the maximum value in the tree and keep the tree heapfied
        """
        d = self._data
        if len(self) > 1:
            mx, d[0] = d[0], d.pop()
            self._sink(0)
        else:
            mx = d.pop()

        return mx

    def replace(self, v):
        """
        Pop out the maximum value and replace with a new value.
        This method is faster than pop out and then insert
        """
        d = self._data
        mx, d[0] = d[0], v
        self._sink(0)

        return mx

    def __str__(self):
        return self._data.__str__()
    
    def __repr__(self):
        return self._data.__repr__()

    def __iter__(self):
        return self._data.__iter__()

    def __len__(self):
        return len(self._data)
    
    def __nonzero__(self):
        return len(self._data) > 0