
def pretty_print(grid):
  grid_repr = []
  grid_repr.append(pp_horizontal_line(grid.width))
  for row_index in xrange(grid.height - 1, -1, -1):
    grid_repr.append(pp_row(grid, grid.rows[row_index]))
    grid_repr.append(pp_horizontal_line(grid.width))
  print("\n".join(grid_repr))

def pp_horizontal_line(width):
  plusses = ["+" for _ in xrange(width + 1)]
  return "-".join(plusses)

def pp_row(grid, row):
  starts = []
  ends = []
  for block in row:
    starts.append(block.start)
    ends.append(block.start + block.length)
  row_repr = [" " for _ in xrange(2 * grid.width + 1)]
  for start in starts:
    row_repr[2*start] = "|"
  for end in ends:
    row_repr[2*end] = "|"
  return "".join(row_repr)