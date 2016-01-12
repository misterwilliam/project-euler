import blocks
import grids

def randomly_fill_row(grid, row_index, col_start):
  if row_index == grid.width:
    return
  for col in xrange(col_start, grid.width):
    for length in xrange(1, grid.width - col + 1):
      block = blocks.Block(col, length)
      grid_clone = grid.clone()
      grid_clone.maybe_add_block(block, row_index)
      for filled_grid in randomly_fill_row(grid_clone,
                                           row_index,
                                           block.start + block.length + 1):
        yield filled_grid


grid = grids.Grid(4, 3)
assert grid.maybe_add_block(blocks.Block(0, 3), 0)
grids.pretty_print(grid)
