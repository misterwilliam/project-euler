import unittest

import blocks
import grids

from main import *

class RandomlyFillRowTests(unittest.TestCase):

  def test_randomly_fill_row_width_4(self):
    grid = grids.Grid(4, 2)
    randomly_filled_grids = [
      grid for grid in randomly_fill_row(grid, 0, 0)
    ]
    self.assertEqual(15, len(set(randomly_filled_grids)))

  def test_randomly_fill_row_width_1(self):
    grid = grids.Grid(1, 2)
    randomly_filled_grids = [
      grid for grid in randomly_fill_row(grid, 0, 0)
    ]
    self.assertEqual(1, len(randomly_filled_grids))

  def test_randomly_fill_row_width_2(self):
    grid = grids.Grid(2, 2)
    randomly_filled_grids = [
      grid for grid in randomly_fill_row(grid, 0, 0)
    ]
    self.assertEqual(3, len(randomly_filled_grids))

  def test_randomly_fill_row_width_3(self):
    grid = grids.Grid(3, 2)
    randomly_filled_grids = [
      grid for grid in randomly_fill_row(grid, 0, 0)
    ]
    self.assertEqual(7, len(randomly_filled_grids))

class BuildCastlesTest(unittest.TestCase):

  def test_4_1(self):
    castles = build_castles(4, 1)
    self.assertEqual(0, len(castles))

  def test_1_2(self):
    castles = build_castles(1, 2)
    self.assertEqual(1, len(castles))

  def test_2_2(self):
    castles = build_castles(2, 2)
    self.assertEqual(3, len(castles))

  def test_4_2(self):
    castles = build_castles(4, 2)
    self.assertEqual(10, len(castles))
