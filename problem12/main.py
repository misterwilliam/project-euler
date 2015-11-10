import itertools
import functools
import unittest


def memoize(f):
    cache = {}
    @functools.wraps(f)
    def wrapped(*args):
        if args in cache:
            return cache[args]
        else:
            retVal = f(*args)
            cache[args] = retVal
            return retVal
    return wrapped


@memoize
def GetTriangleNumber(n):
    return sum(i for i in xrange(1, n + 1))


@memoize
def Factor(n):
    factors = set([1, n])
    for i in xrange(2, n):
        if n % i == 0:
            recursiveFactors = Factor(n / i)
            return factors | set([i, n]) | recursiveFactors | \
                set([i * e for e in recursiveFactors])
    return factors


def GetFirstWithNumDivisors(n):
    i = 0
    while True:
        triangle_num = GetTriangleNumber(i)
        if len(Factor(triangle_num)) > n:
            return triangle_num
        i += 1


print GetFirstWithNumDivisors(500)


class GetTriangleNumberTests(unittest.TestCase):

    def test_FirstFiveNumbers(self):
        self.assertEqual(GetTriangleNumber(1), 1)
        self.assertEqual(GetTriangleNumber(2), 3)
        self.assertEqual(GetTriangleNumber(3), 6)
        self.assertEqual(GetTriangleNumber(4), 10)
        self.assertEqual(GetTriangleNumber(5), 15)


class FactorTests(unittest.TestCase):

    def test_Ten(self):
        self.assertEqual(Factor(10), set([1, 2, 5, 10]))

    def test_TwentyEight(self):
        self.assertEqual(Factor(28), set([1, 2, 4, 7, 14, 28]))


class GetFirstWithNumDivisorsTests(unittest.TestCase):

    def test_Five(self):
        self.assertEqual(GetFirstWithNumDivisors(5), 28)


if __name__ == '__main__':
    unittest.main()
