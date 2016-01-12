import unittest

from grids import *

class GridTests(unittest.TestCase):

  def test_missing_block_in_top_row(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 0))
    self.assertEqual((False, "Too short"), grid.is_castle())

  def test_missing_odd_blocks(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 1))
    self.assertEqual((False, "Not even number blocks"), grid.is_castle())

  def test_not_1_block_away(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual((False, "Too close left"),
                     grid.maybe_add_block(blocks.Block(1, 1), 0))

  def test_not_overlapping(self):
    grid = Grid(4, 2)
    self.assertEqual((False, "Not completely supported"),
                     grid.maybe_add_block(blocks.Block(3, 1), 1))

  def test_not_single_foundation(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 1))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 1))
    self.assertEqual((False, "Not single complete foundation"), grid.is_castle())

  def test_make_a_castle(self):
    grid = Grid(4, 3)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 4), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 1))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 1))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 2))
    self.assertEqual(True, grid.is_castle())

  def test_eq(self):
    grid_a = Grid(4, 3)
    grid_b = Grid(4, 3)

    assert grid_a.maybe_add_block(blocks.Block(0, 4), 0)
    assert grid_b.maybe_add_block(blocks.Block(0, 4), 0)

    assert grid_a.maybe_add_block(blocks.Block(0, 1), 1)
    assert grid_b.maybe_add_block(blocks.Block(0, 1), 1)

    self.assertEqual(grid_a, grid_b)

  def test_hash(self):
    grid_a = Grid(4, 3)
    grid_b = Grid(4, 3)

    assert grid_a.maybe_add_block(blocks.Block(0, 4), 0)
    assert grid_b.maybe_add_block(blocks.Block(0, 4), 0)

    assert grid_a.maybe_add_block(blocks.Block(0, 1), 1)
    assert grid_b.maybe_add_block(blocks.Block(0, 1), 1)

    self.assertEqual(hash(grid_a), hash(grid_b))

