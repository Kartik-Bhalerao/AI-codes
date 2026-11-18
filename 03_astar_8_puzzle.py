import heapq

# Goal state
goal = (1, 2, 3, 8, 0, 4, 7, 6, 5)

# Guaranteed solvable start state (1 move away from goal)
start = (1, 2, 3, 0, 8, 4, 7, 6, 5)


def heuristic(state):
  distance = 0
  for i in range(9):
    if state[i] != 0:
      goal_index = goal.index(state[i])
      x1, y1 = divmod(i, 3)
      x2, y2 = divmod(goal_index, 3)
      distance += abs(x1 - x2) + abs(y1 - y2)
  return distance


def get_neighbors(state):
  neighbors = []
  zero = state.index(0)
  row, col = divmod(zero, 3)
  moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  for dr, dc in moves:
    r, c = row + dr, col + dc
    if 0 <= r < 3 and 0 <= c < 3:
      new_pos = r * 3 + c
      new_state = list(state)
      new_state[zero], new_state[new_pos] = new_state[new_pos], new_state[zero]
      neighbors.append(tuple(new_state))
  return neighbors


def astar():
  pq = [(heuristic(start), 0, start)]
  visited = set()
  parent = {}

  while pq:
    f, g, state = heapq.heappop(pq)

    if state == goal:
      print("Goal Reached!")
      print("Steps:", g)
      path = []
      while state in parent:
        path.append(state)
        state = parent[state]
      path.append(start)
      for s in reversed(path):
        for i in range(0, 9, 3):
          print(s[i : i + 3])
        print()
      return

    if state in visited:
      continue
    visited.add(state)

    for neighbor in get_neighbors(state):
      if neighbor not in visited:
        parent[neighbor] = state
        new_g = g + 1
        heapq.heappush(pq, (new_g + heuristic(neighbor), new_g, neighbor))

  print("No solution found")


astar()