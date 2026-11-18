# Practical: DFS for Missionaries and Cannibals Problem


def missionaries_and_cannibals():
  # State representation: (m_left, c_left, boat)
  # boat: 1 = left bank, 0 = right bank
  start = (3, 3, 1)
  goal = (0, 0, 0)

  # Stack stores: (current_state, path_list)
  stack = [(start, [start])]
  visited = set()

  # Possible boat moves: (missionaries, cannibals)
  moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

  while stack:
    state, path = stack.pop()
    m, c, boat = state

    if state == goal:
      print("Solution Found!")
      print(f"Total Steps: {len(path) - 1}\n")
      for i, step in enumerate(path):
        side = "Left" if step[2] == 1 else "Right"
        print(
            f"Step {i}: Left Bank (M:{step[0]}, C:{step[1]}), Boat is on"
            f" {side} bank"
        )
      return path

    if state in visited:
      continue
    visited.add(state)

    for dm, dc in moves:
      if boat == 1:
        # Move from left bank to right bank
        new_m = m - dm
        new_c = c - dc
        new_boat = 0
      else:
        # Move from right bank to left bank
        new_m = m + dm
        new_c = c + dc
        new_boat = 1

      # Check if counts are within valid bounds (0 to 3)
      if 0 <= new_m <= 3 and 0 <= new_c <= 3:
        right_m = 3 - new_m
        right_c = 3 - new_c

        # Safety condition: Missionaries cannot be outnumbered by cannibals on either bank
        left_safe = new_m == 0 or new_m >= new_c
        right_safe = right_m == 0 or right_m >= right_c

        if left_safe and right_safe:
          new_state = (new_m, new_c, new_boat)
          if new_state not in visited:
            stack.append((new_state, path + [new_state]))

  print("No solution found")


# Run the DFS algorithm
missionaries_and_cannibals()