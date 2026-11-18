# Practical: 8-Queens Problem Using Backtracking
N = 8
board = [-1] * N  # board[row] stores the column position of the queen in that row


def is_safe(row, col):
  for i in range(row):
    # Check if same column or same diagonal
    if board[i] == col or abs(board[i] - col) == abs(i - row):
      return False
  return True


def solve(row):
  if row == N:
    return True

  for col in range(N):
    if is_safe(row, col):
      board[row] = col  # Place queen
      if solve(row + 1):  # Recurse for next row
        return True
      board[row] = -1  # Backtrack if placement leads to no solution

  return False


# Execute and print the chessboard
if solve(0):
  print("Solution Found:\n")
  for row in range(N):
    for col in range(N):
      if board[row] == col:
        print("Q", end=" ")
      else:
        print(".", end=" ")
    print()
else:
  print("No Solution Found")