class Node:

    def __init__(self, left = None, right = None, data = None):
        self.left = left
        self.right = right
        self.data = data

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        if self.isLeaf():
            return str(self.data)
        else:
            return "(%s: %s %s)" % (self.data, self.left, self.right)

