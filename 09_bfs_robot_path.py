# Practical: BFS for Robot Path Planning
from collections import deque

# Grid environment: 0 = Free path, 1 = Obstacle
grid = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]

start = (0, 0)
goal = (3, 3)


def bfs():
  # Queue stores: (current_position, path_list)
  queue = deque([(start, [start])])
  visited = {start}

  # Possible movements: Right, Left, Down, Up
  moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

  while queue:
    position, path = queue.popleft()

    # Check if goal position is reached
    if position == goal:
      print("Path Found!")
      print("Coordinates Path:", path)
      print("Total Steps:", len(path) - 1)
      return

    row, col = position

    for dr, dc in moves:
      r = row + dr
      c = col + dc

      # Check grid boundaries, obstacles (0), and visited set
      if 0 <= r < 4 and 0 <= c < 4 and grid[r][c] == 0 and (r, c) not in visited:
        visited.add((r, c))
        queue.append(((r, c), path + [(r, c)]))

  print("No Path Found")


# Run the BFS robot path planning
bfs()