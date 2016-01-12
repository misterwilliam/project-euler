import unittest

from blocks import *

class BlocksTests(unittest.TestCase):

  def test_eq(self):
    self.assertEqual(Block(0, 1), Block(0, 1))
    self.assertNotEqual(Block(0, 1), Block(0, 2))

  def test_hash(self):
    self.assertEqual(hash(Block(0, 1)), hash(Block(0, 1)))
    self.assertNotEqual(hash(Block(0, 1)), hash(Block(0, 2)))
