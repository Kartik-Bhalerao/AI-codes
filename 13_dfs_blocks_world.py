# Practical: DFS for Blocks World Problem
# Goal: Reorganize blocks from initial tower state to goal tower state


def dfs():
  # States represented as tuples of tuples of blocks on towers
  start = (("B", "C", "D", "A"),)
  goal = (("A", "B", "C", "D"),)

  # Stack stores: (current_state, path_list)
  stack = [(start, [])]
  visited = set()

  while stack:
    state, path = stack.pop()

    if state == goal:
      print("Goal State Reached!")
      for step in path:
        print(step)
      print(goal)
      return

    if state in visited:
      continue
    visited.add(state)

    for i, tower in enumerate(state):
      if not tower:
        continue
      block = tower[-1]  # Get top block of the tower
      remaining = [list(s) for j, s in enumerate(state) if j != i]
      if len(tower) > 1:
        remaining.append(list(tower[:-1]))

      # Move block onto another tower
      for j in range(len(remaining)):
        new_state = [s[:] for s in remaining]
        new_state[j].append(block)
        new_state = tuple(sorted(tuple(s) for s in new_state))
        if new_state not in visited:
          stack.append((new_state, path + [new_state]))

      # Move block onto the table (new tower stack)
      new_state = tuple(sorted(tuple(s) for s in remaining + [[block]]))
      if new_state not in visited:
        stack.append((new_state, path + [new_state]))

  print("No solution found")


# Run the DFS blocks world algorithm
dfs()