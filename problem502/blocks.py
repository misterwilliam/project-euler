class Block(object):

  def __init__(self, start, length):
    self.start = start
    self.length = length

  def __str__(self):
    return "Block { start: %i length: %i }" % (self.start, self.length)

  def range(self):
    for i in xrange(self.start, self.start + self.length + 1):
      yield i

def separation(block_a, block_b):
  return abs(block_b.start - (block_a.start + block_a.length))