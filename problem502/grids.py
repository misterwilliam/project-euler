import itertools

import blocks
from grid_utils import pretty_print

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

  def is_too_close_on_left(self, block, insertion_point, row):
    # If there is a block on left
    if insertion_point != 0:
      # Make sure at least 1 away from it
      if blocks.separation(row[insertion_point - 1], block) < 1:
        return True
    return False

  def is_too_close_on_right(self, block, insertion_point, row):
    # If there is a block on right
    if insertion_point < len(row) - 1:
      # Make sure at least 1 away from it
      if blocks.separation(block, row[insertion_point]) < 1:
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