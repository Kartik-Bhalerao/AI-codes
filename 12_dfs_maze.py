# Practical: DFS for Maze Solving
# 0 = Free path, 1 = Obstacle/Wall
maze = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)


def dfs():
  # Stack stores: (current_position, path_list)
  stack = [(start, [start])]
  visited = set()

  # Possible movements: Left, Up, Right, Down
  moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]

  while stack:
    position, path = stack.pop()

    # Check if goal is reached
    if position == goal:
      print("Path Found!")
      print("Coordinates Path:", path)
      print("Total Steps:", len(path) - 1)
      return

    if position in visited:
      continue
    visited.add(position)

    row, col = position

    for dr, dc in moves:
      r = row + dr
      c = col + dc

      # Check grid boundaries, open path (0), and visited set
      if (
          0 <= r < 5
          and 0 <= c < 5
          and maze[r][c] == 0
          and (r, c) not in visited
      ):
        stack.append(((r, c), path + [(r, c)]))

  print("No Path Found")


# Run the DFS maze solver
dfs()