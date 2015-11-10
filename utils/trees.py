import collections

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


def DFS(root, onNode=None, willExitNode=None):
    if onNode is not None:
        onNode(root)
    if root.left is not None:
        DFS(root.left, onNode, willExitNode)
    if root.right is not None:
        DFS(root.right, onNode, willExitNode)
    if willExitNode is not None:
        willExitNode(root)


def BFS(root, onNode=None):
    todo = collections.deque()
    todo.append(root)
    while todo:
        node = todo.popleft()
        if onNode is not None:
            onNode(node)
        if node.left is not None:
            todo.append(node.left)
        if node.right is not None:
            todo.append(node.right)
