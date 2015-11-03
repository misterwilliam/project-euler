import unittest

def FindPrime(n):
    knownPrimes = []
    i = 2
    while i <= n:
        for prime in knownPrimes:
            if i % prime == 0:
                break
        else:
            knownPrimes.append(i)
        i += 1
    return knownPrimes

def FindNextTrue(candidates, start):
    i = start
    while i < len(candidates) and candidates[i] != True:
        i += 1
    return i

def SieveFindPrime(n):
    knownPrimes = []
    candidates = [True for i in xrange(1, n)]
    i = 1
    while i < len(candidates):
        largestKnownPrime = i + 1
        knownPrimes.append(largestKnownPrime)

        for j in xrange(largestKnownPrime * 2 - 1, len(candidates), largestKnownPrime):
            candidates[j] = False
        i = FindNextTrue(candidates, i + 1)
    return knownPrimes

print("ANSWER", sum(SieveFindPrime(2000000)))

class TestFindPrime(unittest.TestCase):

    def test_3(self):
        self.assertEqual(SieveFindPrime(3), [2])

    def test_6(self):
        self.assertEqual(SieveFindPrime(6), [2, 3, 5])


if __name__ == '__main__':
    unittest.main()
