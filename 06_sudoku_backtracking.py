# Practical: Sudoku Solver
grid = [
    [8, 0, 2, 0, 0, 3, 5, 1, 0],
    [0, 6, 0, 0, 9, 1, 0, 0, 3],
    [7, 0, 1, 0, 0, 0, 8, 9, 4],
    [6, 0, 8, 0, 0, 4, 0, 2, 1],
    [0, 0, 0, 2, 5, 8, 0, 6, 0],
    [9, 2, 0, 3, 1, 0, 4, 0, 0],
    [0, 0, 0, 4, 0, 0, 7, 8, 0],
    [0, 0, 5, 0, 8, 9, 0, 0, 0],
    [2, 0, 0, 0, 0, 7, 1, 0, 0],
]


def is_valid(row, col, num):
  for i in range(9):
    if grid[row][i] == num:
      return False
    if grid[i][col] == num:
      return False
  start_row = (row // 3) * 3
  start_col = (col // 3) * 3
  for i in range(3):
    for j in range(3):
      if grid[start_row + i][start_col + j] == num:
        return False
  return True


def solve():
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        for num in range(1, 10):
          if is_valid(row, col, num):
            grid[row][col] = num
            if solve():
              return True
            grid[row][col] = 0
        return False
  return True


if solve():
  print("Sudoku Solution:")
  for row in grid:
    print(row)
else:
  print("No solution exists")