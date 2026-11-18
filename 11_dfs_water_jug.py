# Practical: DFS for Water Jug Problem
# Problem: Fill 5-gal jug and empty 2-gal jug, target goal states


def dfs():
  # Stack stores: (small_jug, big_jug, path_list)
  stack = [(0, 0, [])]
  visited = set()

  while stack:
    small, big, path = stack.pop()

    # Target condition (e.g., reaching goal state)
    if (small, big) == (0, 1):
      print("Solution Found:")
      for step in path + [(small, big)]:
        print(step)
      return

    if (small, big) in visited:
      continue
    visited.add((small, big))

    # Possible state transitions for a 2-gal and 5-gal jug
    states = [
        (small, 5),  # Fill big jug to max (5)
        (2, big),  # Fill small jug to max (2)
        (small, 0),  # Empty big jug
        (0, big),  # Empty small jug
        # Pour small jug into big jug
        (max(0, small - (5 - big)), min(5, big + small)),
        # Pour big jug into small jug
        (min(2, small + big), max(0, big - (2 - small))),
    ]

    for new_state in states:
      if new_state not in visited:
        stack.append((new_state[0], new_state[1], path + [(small, big)]))

  print("No solution found")


# Run the DFS water jug algorithm
dfs()