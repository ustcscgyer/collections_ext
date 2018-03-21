def partial(W):
    """
    An efficient implementation of partial matching table
    """
    T = [-1] * len(W)
    k = 0
        
    for pos in range(1, len(W)):
        while k >= 1 and W[pos-1] != W[k-1]:
            k = T[k]
        
        if W[pos] == W[k]:
            T[pos] = T[k]
        else:
            T[pos] = k
            
        k = k  + 1
        
    return T

def partial_ez(W):
    """
    Partial table created by this function is a working table but suboptimal,
    however the implementation is easier and straightforward.
    """
    T = [-1] * len(W)
    k = 0
    
    for pos in range(1, len(W)):
        while k >= 1 and W[pos-1] != W[k-1]:
            k = T[k]
            
        T[pos] = k
        k = k + 1
        
    return T
    
class KMP(object):
    __slots__ = ('W', 'T')
    
    def __init__(self, pat):
        self.W = pat
        self.T = partial(pat)
        
    def search(self, S):
        m, i = 0, 0
        c = 0
        
        while i < len(self.W) and m+i < len(S):
            if S[m+i] == self.W[i]:
                i += 1
            else:
                m = m + i - self.T[i]
                i = max(self.T[i], 0)
            
        print(c)
        if i == len(self.W):
            return m
        else: 
            return -1
