# 12/7 10:54
import collections
import unittest

class Node(object):

    def __init__(self, data, children=None):
        self.data = data
        if children:
            self.children = children
        else:
            self.children = []

def DFS(root, onNode):
    onNode(root)
    for child in root.children:
        DFS(child, onNode)

def BFS(root, onNode):
    todo = collections.deque([root])
    seen = set([root])
    while todo:
        current = todo.popleft()
        onNode(current)
        for child in current.children:
            if child not in seen:
                todo.append(child)
                seen.add(child)


class MyTests(unittest.TestCase):

    def test_SimpleDFS(self):
        root = Node("a", children=[
                    Node("b", children=[
                        Node("c"),
                        Node("d")
                    ]),
                    Node("e")
               ])
        log = []
        def LogVisits(node):
            log.append(node.data)
        DFS(root, LogVisits)
        self.assertEqual(log, ["a", "b", "c", "d", "e"])

    def test_SimpleBFS(self):
        root = Node("a", children=[
                    Node("b", children=[
                        Node("c"),
                        Node("d")
                    ]),
                    Node("e")
               ])
        log = []
        def LogVisits(node):
            log.append(node.data)
        BFS(root, LogVisits)
        self.assertEqual(log, ["a", "b", "e", "c", "d"])


if __name__ == "__main__":
    unittest.main()