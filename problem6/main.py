import math
import unittest

def SumOfSquares(n):
    return sum(math.pow(i, 2) for i in xrange(1, n + 1))


def SquareOfSums(n):
    return math.pow(sum(i for i in xrange(1, n + 1)), 2)

print(SquareOfSums(100) - SumOfSquares(100))

class TestSumOfSquares(unittest.TestCase):

    def test_3(self):
        self.assertEqual(SumOfSquares(3), 1 + 4 + 9)

    def test_10(self):
        self.assertEqual(SumOfSquares(10), 385)


class TestSquareOfSums(unittest.TestCase):

    def test_3(self):
        self.assertEqual(SquareOfSums(3), 36)

    def test_10(self):
        self.assertEqual(SquareOfSums(10), 3025)

if __name__ == '__main__':
    unittest.main()
