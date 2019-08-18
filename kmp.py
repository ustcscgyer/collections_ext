def partial(w):
    nexts = [0] * len(w)

    for pos in range(1, len(w)):
        k = nexts[pos - 1]
        while k > 0 and w[k] != w[pos]:
            k = nexts[k - 1]
            
        nexts[pos] = k + 1 if w[k] == w[pos] else k

    return nexts


class KMP(object):

    def __init__(self, w):
        self.w = w
        self.nexts = partial(w)
        print(self.nexts)

    def search(self, s):
        m, i = 0, 0

        while i < len(self.w) and m+i < len(s):
            if s[m+i] == self.w[i]:
                i += 1
            else:
                print(m, i, self.nexts[i-1])
                if i == 0:
                    m += 1
                else:
                    m += i - self.nexts[i-1]
                    i = self.nexts[i-1]
                
        if i == len(self.w):
            return m
        else:
            return -1
