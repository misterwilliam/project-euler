import unittest

import trees


class NodeTests(unittest.TestCase):

    def test_strOfOneNodeTree(self):
        root = trees.Node(data="data")
        self.assertEqual(str(root), "data")

    def test_strOfThreeNodeTree(self):
        a = trees.Node(data="a")
        b = trees.Node(data="b")
        c = trees.Node(left=a, right=b, data="c")
        self.assertEqual(str(c), "(c: a b)")

    def test_strOfMultilevelTree(self):
        a = trees.Node(data="a")
        b = trees.Node(data="b")
        c = trees.Node(left=a, right=b, data="c")
        e = trees.Node(data="e")
        d = trees.Node(left=c, right=e, data="d")
        self.assertEqual(str(d), "(d: (c: a b) e)")


class DFSTests(unittest.TestCase):

    def test_onNodeTraversalOrder(self):
        d = trees.Node(data="d",
                       right=trees.Node(data="e"),
                       left=trees.Node(data="c",
                                       right=trees.Node(data="b"),
                                       left=trees.Node(data="a")))

        path = []
        def recordPath(node):
            path.append(node.data)

        trees.DFS(d, onNode=recordPath)

        self.assertEqual(path, ["d", "c", "a", "b", "e"])

    def test_willExitNodeTraversalOrder(self):
        d = trees.Node(data="d",
                       right=trees.Node(data="e"),
                       left=trees.Node(data="c",
                                       right=trees.Node(data="b"),
                                       left=trees.Node(data="a")))

        path = []
        def recordPath(node):
            path.append(node.data)

        trees.DFS(d, willExitNode=recordPath)

        self.assertEqual(path, ["a", "b", "c", "e", "d"])


class BFSTests(unittest.TestCase):

    def test_onNodeTraversalOrder(self):
        d = trees.Node(data="d",
                       right=trees.Node(data="e"),
                       left=trees.Node(data="c",
                                       right=trees.Node(data="b"),
                                       left=trees.Node(data="a")))

        path = []
        def recordPath(node):
            path.append(node.data)

        trees.BFS(d, onNode=recordPath)

        self.assertEqual(path, ["d", "c", "e", "a", "b"])


if __name__ == '__main__':
    unittest.main()
