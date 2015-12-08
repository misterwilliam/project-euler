# 12/7 10:36 - 10:49
import collections
import unittest

class Node(object):

    def __init__(self, data, children=None):
        self.data = data
        if children is not None:
            self.children = children
        else:
            self.children = []


def DFS(root, onNode):
    onNode(root)
    if root.children:
        for child in root.children:
            DFS(child, onNode)

def BFS(root, onNode):
    todo = collections.deque([root])
    seen = set([root])
    while todo:
        current = todo.pop(0)
        onNode(current)
        for child in current.children:
            if child not in seen:
                todo.append(child)
                seen.add(child)


class MyTests(unittest.TestCase):

    def test_TriangleBFS(self):
        c = Node("c")
        b = Node("b", children=[c])
        a = Node("a", children=[b])
        c.children.append(a)

        log = []
        def LogNodes(node):
            log.append(node.data)
        BFS(a, LogNodes)
        self.assertEqual(log, ["a", "b", "c"])

    def test_SimpleDFS(self):
        a = Node("a", children=[
                Node("b", children=[
                    Node("d"),
                    Node("e")
                ]),
                Node("c")
            ])

        log = []
        def LogNodes(node):
            log.append(node.data)
        DFS(a, LogNodes)
        self.assertEqual(log, ["a", "b", "d", "e", "c"])

    def test_SimpleBFS(self):
        a = Node("a", children=[
                Node("b", children=[
                    Node("d"),
                    Node("e")
                ]),
                Node("c")
            ])

        log = []
        def LogNodes(node):
            log.append(node.data)
        BFS(a, LogNodes)
        self.assertEqual(log, ["a", "b", "c", "d", "e"])

if __name__ == "__main__":
  unittest.main()