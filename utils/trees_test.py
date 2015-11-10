import unittest

import trees

root = trees.Node()


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

if __name__ == '__main__':
    unittest.main()
