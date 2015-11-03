import unittest

def FindPrime(n):
    knownPrimes = []
    i = 2
    while n > len(knownPrimes):
        for prime in knownPrimes:
            if i % prime == 0:
                break
        else:
            knownPrimes.append(i)
        i += 1
    return knownPrimes[-1]


print("ANSWER", FindPrime(10001))

class TestFindPrime(unittest.TestCase):

    def test_3(self):
        self.assertEqual(FindPrime(3), 5)

    def test_6(self):
        self.assertEqual(FindPrime(6), 13)


if __name__ == '__main__':
    unittest.main()
