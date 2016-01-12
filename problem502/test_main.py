import unittest

import blocks
import grids

from main import *

class MyTests(unittest.TestCase):

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