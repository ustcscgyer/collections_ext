class Node:
    # Constructor to create a new node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)


class MorrisTraverser:
    def __init__(self, root):
        self.root = root

    def transform(self):
        curr, self.root, tail = self.root, None, None

        while curr:
            if curr.left is None:
                print("out", curr)
                if self.root is None:
                    self.root = curr
                    tail = curr
                else:
                    tail.right, tail = curr, curr
                curr = curr.right
            else:
                prev = curr.left
                while prev.right: prev = prev.right

                prev.right = curr
                curr.left, curr = None, curr.left

        return self.root


