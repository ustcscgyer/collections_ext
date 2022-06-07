class QuickSelect(object):
    __slots__ = ('data')
    
    def __init__(self, data):
        self.data = data
        
    def select(self, k):
        self._sort(k, self.data, 0, len(self.data)-1)
        return self.data[k-1]
    
    def selects(self, k):
        self._sort(k, self.data, 0, len(self.data)-1)
        return self.data[:k]
    
    def _sort(self, k, data, lo, hi):
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
        
        if k <= lt:
            self._sort(k, data, lo, lt-1)
        elif k > gt + 1:
            self._sort(k, data, gt+1, hi)
        else:
            return
