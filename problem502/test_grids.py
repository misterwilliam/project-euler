import unittest

from grids import *

class MyTests(unittest.TestCase):

  def test_missing_block_in_top_row(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 0))
    self.assertFalse(grid.is_castle())

  def test_missing_odd_blocks(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 1))
    self.assertFalse(grid.is_castle())

  def test_not_1_block_away(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual((False, "Too close left"),
                     grid.maybe_add_block(blocks.Block(1, 1), 0))

  def test_not_overlapping(self):
    grid = Grid(4, 2)
    self.assertEqual((False, "Not completely supported"),
                     grid.maybe_add_block(blocks.Block(3, 1), 1))

  def test_make_a_castle(self):
    grid = Grid(4, 2)
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 0))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(0, 1), 1))
    self.assertEqual(True, grid.maybe_add_block(blocks.Block(3, 1), 1))
    self.assertTrue(grid.is_castle())
