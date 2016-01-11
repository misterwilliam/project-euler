import unittest

def memeoize(f):
  cache = {}
  def helper(arg):
    if arg in cache:
      return cache[arg]
    else:
      result = f(arg)
      cache[arg] = result
      return result
  return helper

def next(n):
  assert n > 0
  if n % 2 == 0:
    return n / 2
  else:
    return 3 * n + 1

@memeoize
def get_sequence(n):
  if n == 1:
    return []
  n = next(n)
  return [n] + get_sequence(n)

# ANSWER -----------------------

max_length = 0, -1
for i in xrange(1, 1000000):
  sequence = get_sequence(i)
  max_length = max(max_length, (len(sequence), i))

print max_length


# TESTS ------------------------

class MyTests(unittest.TestCase):

  def test_next(self):
    self.assertEqual(40, next(13))
    self.assertEqual(20, next(40))

  def test_get_sequence(self):
    self.assertEqual([40, 20, 10, 5, 16, 8, 4, 2, 1],
      get_sequence(13))


if __name__ == '__main__':
    unittest.main()