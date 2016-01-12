import itertools
import unittest

class Block(object):

  def __init__(self, start, length):
    self.start = start
    self.length = length

  def __str__(self):
    return "Block { start: %i length: %i }" % (self.start, self.length)

  def range(self):
    for i in xrange(self.start, self.start + self.length + 1):
      yield i

def find_index_of_first(sequence, predicate):
  for i, element in enumerate(sequence):
    if predicate(element):
      return i
  return None

class Grid(object):
  """
  Rules for a valid castle:
  1. Blocks can be placed on top of other blocks as long as nothing sticks out past the edges or hangs out over open space.
  2. All blocks are aligned/snapped to the grid.
  3. Any two neighboring blocks on the same row have at least one unit of space between them.
  4. The bottom row is occupied by a block of length w.
  5. The maximum achieved height of the entire castle is exactly h.
  6. The castle is made from an even number of blocks.

  Enforcement:
  1. Enforced during maybe_add_block().
  2. Adding block to grid naturally enforces this.
  3. Enforced during maybe_add_block().
  4.
  5. Enforced by is_castle().
  6. Enforced by is_castle().
  """

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.rows = [[] for _ in xrange(self.height)]
    self.num_blocks = 0

  def pretty_print(self):
    grid_repr = []
    grid_repr.append(self.pp_horizontal_line(self.width))
    for row_index in xrange(self.height - 1, -1, -1):
      grid_repr.append(self.pp_row(self.rows[row_index]))
      grid_repr.append(self.pp_horizontal_line(self.width))
    print("\n".join(grid_repr))

  def maybe_add_block(self, new_block, row_index):
    row = self.rows[row_index]
    return self._maybe_add_block_to_row(row_index, row, new_block)

  def _maybe_add_block_to_row(self, row_index, row, new_block):
    insertion_point = len([block for block in
      itertools.takewhile(
        lambda block: block.start < new_block.start,
        row)])
    if not self.is_block_within_grid(new_block):
      return False, "Outside"
    if self.is_too_close_on_left(new_block, insertion_point, row):
      return False, "Too close left"
    if self.is_too_close_on_right(new_block, insertion_point, row):
      return False, "Too close right"
    if not self.is_completely_supported(new_block, row_index):
      return False, "Not completely supported"

    row.insert(insertion_point, new_block)
    self.num_blocks += 1
    return True

  def is_completely_supported(self, block, row_index):
    if row_index >= 1:
      supporting_row = self.rows[row_index - 1]
      supports = self.get_filled_cols(supporting_row)
      for col in block.range():
        if col not in supports:
          return False
    return True

  def get_filled_cols(self, row):
    filled_cols = set()
    for block in row:
      for col in block.range():
        filled_cols.add(col)
    return filled_cols

  def is_block_within_grid(self, block):
    if block.start < 0:
      return False
    if block.start + block.length > self.width:
      return False
    return True

  def get_block_separation(self, block_a, block_b):
    return block_b.start - (block_a.start + block_a.length)

  def is_too_close_on_left(self, block, insertion_point, row):
    # If there is a block on left
    if insertion_point != 0:
      # Make sure at least 1 away from it
      if self.get_block_separation(row[insertion_point - 1], block) < 1:
        return True
    return False

  def is_too_close_on_right(self, block, insertion_point, row):
    # If there is a block on right
    if insertion_point < len(row) - 1:
      # Make sure at least 1 away from it
      if self.get_block_separation(block, row[insertion_point]) < 1:
        return True
    return False

  def is_castle(self):
    if self.num_blocks % 2 == 1:
      return False
    elif len(self.rows[self.height - 1]) == 0:
      # Castles must have blocks in top row
      return False
    else:
      return True

  def pp_horizontal_line(self, width):
    plusses = ["+" for _ in xrange(width + 1)]
    return "-".join(plusses)

  def pp_row(self, row):
    starts = []
    ends = []
    for block in row:
      starts.append(block.start)
      ends.append(block.start + block.length)
    row_repr = [" " for _ in xrange(2 * self.width + 1)]
    for start in starts:
      row_repr[2*start] = "|"
    for end in ends:
      row_repr[2*end] = "|"
    return "".join(row_repr)

# ANSWER -----------------------

grid = Grid(4, 3)
assert grid.maybe_add_block(Block(0, 3), 0)


# TESTS ------------------------

class MyTests(unittest.TestCase):

  def test_missing_block_in_top_row(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(Block(3, 1), 0))
    self.assertFalse(grid.is_castle())

  def test_missing_odd_blocks(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(Block(3, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(Block(3, 1), 1))
    self.assertFalse(grid.is_castle())

  def test_not_1_block_away(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(Block(0, 1), 0))
    self.assertEqual((False, "Too close left"),
                     grid.maybe_add_block(Block(1, 1), 0))

  def test_not_overlapping(self):
    grid = Grid(4, 2)
    self.assertEqual((False, "Not completely supported"),
                     grid.maybe_add_block(Block(3, 1), 1))

  def test_make_a_castle(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(Block(3, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(Block(0, 1), 1))
    self.assertEqual(True, grid.maybe_add_block(Block(3, 1), 1))
    grid.pretty_print()
    self.assertTrue(grid.is_castle())


if __name__ == '__main__':
    unittest.main()