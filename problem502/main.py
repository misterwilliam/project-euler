import blocks
import grids

def randomly_fill_row(grid, row_index, col_start):
  if col_start >= grid.width:
    raise StopIteration
  for col in xrange(col_start, grid.width + 1):
    for length in xrange(1, grid.width - col + 1):
      block = blocks.Block(col, length)
      grid_clone = grid.clone()
      grid_clone.maybe_add_block(block, row_index)
      for filled_grid in randomly_fill_row(grid_clone,
                                           row_index,
                                           block.start + block.length + 1):
        yield filled_grid
      else:
        yield grid_clone

def build_castles(width, height):
  grid = grids.Grid(width, height)
  grid.maybe_add_block(blocks.Block(0, width), 0)
  candidates = set([grid])
  for row_index in xrange(1, height):
    new_candidates = set()
    for grid in candidates:
      for filled_grid in randomly_fill_row(grid, row_index, 0):
        new_candidates.add(filled_grid)
    candidates = new_candidates
  castles = set()
  for candidate in candidates:
    if candidate.is_castle() is True:
      castles.add(candidate)
  return castles


grid = grids.Grid(4, 3)
assert grid.maybe_add_block(blocks.Block(0, 3), 0)
grids.pretty_print(grid)
