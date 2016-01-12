import blocks
import grids

grid = grids.Grid(4, 3)
assert grid.maybe_add_block(blocks.Block(0, 3), 0)
grids.pretty_print(grid)
