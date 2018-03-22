class QuickSort(object):
    """ 3-way quick sort (https://algs4.cs.princeton.edu/23quicksort/)
    """
    __slots__ = ('data')
    
    def __init__(self, data):
        self.data = data
        
    def sort(self):
        self._sort(self.data, 0, len(self.data)-1)
        
        return self.data
    
    def _sort(self, data, lo, hi):
        if (hi <= lo):
            return 

        lt, gt, i = lo, hi, lo + 1
        while i <= gt:
            if data[i] < data[lt]:
                data[i], data[lt] = data[lt], data[i]
                lt += 1; i += 1
            elif data[i] > data[lt]:
                data[i], data[gt] = data[gt], data[i]
                gt -= 1
            else:
                i += 1
                
        self._sort(data, lo, lt-1)
        self._sort(data, gt+1, hi)