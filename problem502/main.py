import blocks
import grids
import grid_utils

grid = grids.Grid(4, 3)
assert grid.maybe_add_block(blocks.Block(0, 3), 0)
grid_utils.pretty_print(grid)
