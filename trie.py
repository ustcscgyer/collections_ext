R = 256 
class TrieNode:
    __slots__ = ('val', 'next')
    def __init__(self, val=None):
        self.val = val
        self.next = [None] * R

class Trie:
    __slots__ = ('root', 'size')

    def __init__(self, key_vals=[]):
        self.root = None
        self.size = 0

        for k, v in key_vals:
            self.put(k, v)

    def put(self, key, val=0):
        self.root =  self._put(self.root, key, val)

        return self

    def _put(self, TrieNode, key, val, d=0):
        if TrieNode is None:
            TrieNode = TrieNode()
        if d == len(key):
            if TrieNode.val is None: self.size += 1
            TrieNode.val = val
        else:
            c = ord(key[d])
            TrieNode.next[c] = self._put(TrieNode.next[c], key, val, d+1)

        return TrieNode

    def isEmpty(self):
        return self.size == 0

    def contains(self, key):
        return self.get(key) != None

    def get(self, key):
        TrieNode = self._search(self.root, key)

        if TrieNode is None:
            return None
        else:
            return  TrieNode.val

    def _search(self, TrieNode, key, d=0):
        if TrieNode is None:
            return None
        elif d == len(key):
            return TrieNode
        else:
            c = ord(key[d])
            return self._search(TrieNode.next[c], key, d+1)

    def delete(self, key):
        self.root = self._delete(self.root, key)

        return self

    def _delete(self, TrieNode, key, d=0):
        if TrieNode is None:
            return None
        elif d == len(key) and TrieNode.val is not None:
            TrieNode.val = None
            self.size -= 1
        else:
            c = ord(key[d])
            TrieNode.next[c] = self._delete(TrieNode.next[c], key, d+1)

        if TrieNode.val is not None:
            return TrieNode

        for n in TrieNode.next:
            if n is not None:
                return TrieNode

        return None

    def prefix(self, pre):
        TrieNode = self._search(self.root, pre)

        return self._collect(TrieNode, pre)


    def _collect(self, TrieNode, pre):
        if TrieNode is None:
            return []
        elif TrieNode.val is not None:
            result = [pre]
        else:
            result = []

        for i in range(len(TrieNode.next)):
            result += [s for s in self._collect(TrieNode.next[i], pre + chr(i))]

        return result

    def keys(self):
        return self.prefix('')

    def __iter__(self):
        return self.keys().__iter__()

    def items(self):
        raise NotImplementedError