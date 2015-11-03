import math
import unittest

def IsPythTriple(a, b, c):
    if (a < b < c):
        if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
            return True
    else:
        return False

def GenCandidateTriples(maxSum):
    for i in xrange(1, maxSum):
        for j in xrange(i + 1, maxSum):
            for k in xrange(j + 1, maxSum):
                yield i, j, k
#print("ANSWER", FindPrime(10001))

def Find(maxSum):
    for triple in GenCandidateTriples(maxSum):
        if sum(triple) == maxSum:
            if IsPythTriple(*triple):
                yield triple

print([triple for triple in Find(1000)])  # Answer is 200 * 275 * 425 = 31875000

class MyTests(unittest.TestCase):

    def test_isPythTripleTrue(self):
        self.assertTrue(IsPythTriple(3, 4, 5))

    def test_GenCandidateTriples(self):
        self.assertEqual(
            [t for t in GenCandidateTriples(5)], [
                (1, 2, 3),
                (1, 2, 4),
                (1, 3, 4),
                (2, 3, 4)
            ]
        )

if __name__ == '__main__':
    unittest.main()
